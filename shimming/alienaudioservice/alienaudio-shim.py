#!/usr/bin/python

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from enum import IntEnum, IntFlag
import logging
from typing import Any, Callable, Coroutine, Optional

from sdbus import (
    DbusInterfaceCommonAsync,
    dbus_method_async,
    dbus_signal_async,
    get_current_message,
    sd_bus_open_system,
)

import pulsectl
import pulsectl_asyncio


# Resource policy manager D-BUS parameters
POLICY_DBUS_SERVICE = "org.maemo.resource.manager"
POLICY_DBUS_PATH = "/org/maemo/resource/manager"
POLICY_DBUS_INTERFACE = "org.maemo.resource.manager"

CLIENT_DBUS_INTERFACE = "org.maemo.resource.client"

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)


class Client(DbusInterfaceCommonAsync, interface_name=CLIENT_DBUS_INTERFACE):
    @dbus_method_async("iuuu", method_name="advice")
    async def advice(self, type: int, id: int, reqno: int, resources: int) -> None:
        raise NotImplementedError

    @dbus_method_async("iuuu", method_name="grant")
    async def grant(self, type: int, id: int, reqno: int, resources: int) -> None:
        raise NotImplementedError


@dataclass
class Resource:
    mandatory: int
    optional: int
    dbus: Client
    is_alien_call: bool = False


class DummyPolicyDaemon(DbusInterfaceCommonAsync, interface_name=POLICY_DBUS_INTERFACE):
    def __init__(self, routeManager: RouteManagerShim) -> None:
        super().__init__()

        self.route_manager = routeManager
        self.background_tasks: set[asyncio.Task[None]] = set()
        self.granted = True
        self.clients: dict[str, dict[str, Resource]] = {}

    def path(self, id: int) -> str:
        return f"/org/maemo/resource/client{id}"

    async def advice(self, sender: str, id: int, reqno: int, resources: int) -> None:
        type = 6

        print("")
        print("ADVICE")
        print("type:     ", str(type))
        print("id:       ", str(id))
        print("reqno:    ", str(reqno))
        print("resources:", str(resources))

        path = self.path(id)

        if sender in self.clients:
            if path in self.clients[sender]:
                resource = self.clients[sender][path]
                try:
                    await resource.dbus.advice(type, id, reqno, resources)
                    log.info("Reply")
                except:
                    log.exception("Something went wrong")

    async def grant(self, sender: str, id: int, reqno: int, resources: int) -> None:
        type = 5

        print("")
        print("GRANT")
        print("type:     ", str(type))
        print("id:       ", str(id))
        print("reqno:    ", str(reqno))
        print("resources:", str(resources))

        path = self.path(id)

        if sender in self.clients:
            if path in self.clients[sender]:
                resource = self.clients[sender][path]
                try:
                    await resource.dbus.grant(type, id, reqno, resources)
                except:
                    log.exception("Something went wrong")

    def idle_response(
        self,
        func: Callable[[str, int, int, int], Coroutine[None, None, None]],
        sender: str,
        id: int,
        reqno: int,
        resources: int,
    ) -> None:
        async def wrap() -> None:
            await asyncio.sleep(1)
            await func(sender, id, reqno, resources)

        task = asyncio.create_task(wrap())
        task.add_done_callback(self.background_tasks.discard)
        self.background_tasks.add(task)

    @dbus_method_async("iuuuuuussu", "iuuis", method_name="register")
    async def register(
        self,
        type: int,
        id: int,
        reqno: int,
        mandatory: int,
        optional: int,
        share: int,
        mask: int,
        app_id: str,
        klass: str,
        mode: int,
    ) -> tuple[int, int, int, int, str]:
        try:
            sender = get_current_message().sender

            error_code = 0
            error_string = "OK"

            print("")
            print("REGISTER", sender)
            print("type:     ", str(type))
            print("id:       ", str(id))
            print("reqno:    ", str(reqno))
            print("mandatory:", str(mandatory))
            print("optional: ", str(optional))
            print("share:    ", str(share))
            print("mask:     ", str(mask))
            print("app_id:   ", app_id)
            print("class:    ", klass)
            print("mode:     ", str(mode))

            client = {}

            if sender in self.clients:
                client = self.clients[sender]

            path = self.path(id)

            assert sender is not None

            proxy = Client.new_proxy(sender, path, bus=sd_bus_open_system())

            resource = Resource(mandatory, optional, proxy)

            client[path] = resource
            self.clients[sender] = client

            self.idle_response(self.advice, sender, id, reqno, resource.mandatory)

            return (9, id, reqno, error_code, error_string)

        except:
            log.exception('')

    @dbus_method_async("iuuuuuussu", "iuuis", method_name="update")
    async def update(
        self,
        type: int,
        id: int,
        reqno: int,
        mandatory: int,
        optional: int,
        share: int,
        mask: int,
        app_id: str,
        klass: str,
        mode: int,
    ) -> tuple[int, int, int, int, str]:
        try:
            sender = get_current_message().sender

            error_code = 0
            error_string = "OK"

            print("")
            print("UPDATE", sender)
            print("type:     ", str(type))
            print("id:       ", str(id))
            print("reqno:    ", str(reqno))
            print("mandatory:", str(mandatory))
            print("optional: ", str(optional))
            print("share:    ", str(share))
            print("mask:     ", str(mask))
            print("app_id:   ", app_id)
            print("class:    ", klass)
            print("mode:     ", str(mode))

            return (9, id, reqno, error_code, error_string)

        except:
            log.exception('')

    @dbus_method_async("iuu", "iuuis", method_name="acquire")
    async def acquire(
        self, type: int, id: int, reqno: int
    ) -> tuple[int, int, int, int, str]:
        try:
            sender = get_current_message().sender

            error_code = 0
            error_string = "OK"

            print("")
            print("ACQUIRE", sender)
            print("type:     ", str(type))
            print("id:       ", str(id))
            print("reqno:    ", str(reqno))

            assert sender is not None

            # find the client
            resource = self.clients[sender][self.path(id)]

            if resource.is_alien_call:
                log.info("switching to call mode")
                #            subprocess.run(['callaudiocli', '-m', '1'])
                await self.route_manager.route_output_for_call(True)

            self.idle_response(self.grant, sender, id, reqno, resource.mandatory)

            return (9, id, reqno, error_code, error_string)

        except:
            log.exception('')

    @dbus_method_async("iuu", "iuuis", method_name="release")
    async def release(
        self, type: int, id: int, reqno: int
    ) -> tuple[int, int, int, int, str]:
        try:
            sender = get_current_message().sender

            error_code = 0
            error_string = "OK"

            print("")
            print("RELEASE", sender)
            print("type:     ", str(type))
            print("id:       ", str(id))
            print("reqno:    ", str(reqno))

            assert sender is not None

            self.idle_response(self.grant, sender, id, reqno, 0)

            return (9, id, reqno, error_code, error_string)

        except:
            log.exception('')

    @dbus_method_async("iuu", "iuuis", method_name="unregister")
    async def unregister(
        self, type: int, id: int, reqno: int
    ) -> tuple[int, int, int, int, str]:
        try:
            sender = get_current_message().sender

            errorCode = 0
            errorString = "OK"

            print("")
            print("UNREGISTER", sender)
            print("type:     ", str(type))
            print("id:       ", str(id))
            print("reqno:    ", str(reqno))

            assert sender is not None

            client = self.clients[sender]
            path = self.path(id)
            resource = client[path]

            if resource.is_alien_call:
                log.info("switching back from call mode")
                #            subprocess.run(['callaudiocli', '-m', '0'])

                await self.route_manager.route_output_for_call(False)

            del client[path]

            if len(client) == 0:
                del self.clients[sender]

            return (9, id, reqno, errorCode, errorString)

        except:
            log.exception('')

    @dbus_method_async("iuusssis", "iuuis", method_name="audio")
    async def audio(
        self,
        type: int,
        id: int,
        reqno: int,
        group: str,
        pid: str,
        streamName: str,
        method: int,
        pattern: str,
    ) -> tuple[int, int, int, int, str]:
        try:
            sender = get_current_message().sender

            error_code = 0
            error_string = "OK"

            print("")
            print("AUDIO", sender)
            print("type:       ", str(type))
            print("id:         ", str(id))
            print("reqno:      ", str(reqno))
            print("group:      ", group)
            print("pid:        ", pid)
            print("stream name:", streamName)
            # typedef enum {
            #    resmsg_method_equals = 0,
            #    resmsg_method_startswith,
            #    resmsg_method_matches
            # } resmsg_match_method_t;
            print("method:     ", str(method))
            print("pattern:    ", pattern)

            assert sender is not None

            resource = self.clients[sender][self.path(id)]

            if streamName == "media.name" and method == 0 and pattern == "voice":
                log.info("detected voice call, will switch devices on acquire()")
                resource.is_alien_call = True

            return (9, id, reqno, error_code, error_string)

        except:
            log.exception('')

    @dbus_method_async("iuuu", "iuuis", method_name="video")
    async def video(
        self, type: int, id: int, reqno: int, pid: int
    ) -> tuple[int, int, int, int, str]:
        try:
            sender = get_current_message().sender

            error_code = 0
            error_string = "OK"

            print("")
            print("VIDEO", sender)
            print("type:       ", str(type))
            print("id:         ", str(id))
            print("reqno:      ", str(reqno))
            print("pid:        ", str(pid))

            return (9, id, reqno, error_code, error_string)

        except:
            log.exception('')


class AudioOutputRoute(IntEnum):
    EARPIECE = 1
    PHONE_SPEAKER = 2
    EXTERNAL_SPEAKER = 3
    HEADPHONE = 4


class OhmRouteType(IntFlag):
    OUTPUT = 1 << 0  # sink
    INPUT = 1 << 1  # source
    BUILTIN = 1 << 2
    WIRED = 1 << 3
    WIRELESS = 1 << 4
    VOICE = 1 << 5
    BLUETOOTH_SCO = 1 << 6
    BLUETOOTH_A2DP = 1 << 7
    HEADSET = 1 << 8
    HEADPHONE = 1 << 9
    USB = 1 << 10
    UNKNOWN = 1 << 11
    AVAILABLE = 1 << 25
    PREFERRED = 1 << 26
    ACTIVE = 1 << 27


class RouteManagerShim(
    DbusInterfaceCommonAsync, interface_name="org.nemomobile.Route.Manager"
):
    def __init__(self, pulse: pulsectl_asyncio.PulseAsync) -> None:
        super().__init__()

        self.pulse = pulse

        self.output_route_before_call: Optional[
            tuple[pulsectl.PulseSinkInfo, pulsectl.PulsePortInfo]
        ] = None
        self.output_route_before_speaker: Optional[
            tuple[pulsectl.PulseSinkInfo, pulsectl.PulsePortInfo]
        ] = None
        self.input_route_before_speaker: Optional[
            tuple[pulsectl.PulseSourceInfo, pulsectl.PulsePortInfo]
        ] = None

        self.background_tasks: set[asyncio.Task[None]] = set()

        async def listen() -> None:
            async for event in self.pulse.subscribe_events('all'):
                if event.t == "change":
                    log.info("pulse event happend")
                    await self.mce.sync_proximity_monitoring()

        task = asyncio.create_task(listen())
        task.add_done_callback(self.background_tasks.discard)
        self.background_tasks.add(task)

        # register signal handlers to cancel listener when program is asked to terminate
        # Alternatively, the PulseAudio event subscription can be ended by breaking/returning from the `async for` loop
#        for sig in (signal.SIGTERM, signal.SIGHUP, signal.SIGINT):
#            loop.add_signal_handler(sig, task.cancel)


    async def _sink_list(self) -> list[pulsectl.PulseSinkInfo]:
        sinks = await self.pulse.sink_list()
        assert isinstance(sinks, list)
        return sinks

    async def _source_list(self) -> list[pulsectl.PulseSourceInfo]:
        sources = await self.pulse.source_list()
        assert isinstance(sources, list)
        return sources

    @dbus_method_async("s", method_name="Enable")
    async def enable(self, route: str) -> None:
        try:
            log.info("route enable: %s", route)

            if route == "speaker":
                await self.use_speaker_in_call(True)

        except:
            log.exception('')

    @dbus_method_async("s", method_name="Disable")
    async def disable(self, route: str) -> None:
        try:
            log.info("route disable: %s", route)

            if route == "speaker":
                await self.use_speaker_in_call(False)

        except:
            log.exception('')

    @dbus_method_async(result_signature="susu", method_name="ActiveRoutes")
    async def active_routes(self) -> tuple[str, int, str, int]:
        try:
            OHM_EXT_ROUTE_TYPE_OUTPUT = 1 << 0  # sink
            OHM_EXT_ROUTE_TYPE_INPUT = 1 << 1  # source
            OHM_EXT_ROUTE_TYPE_BUILTIN = 1 << 2
            OHM_EXT_ROUTE_TYPE_WIRED = 1 << 3
            OHM_EXT_ROUTE_TYPE_WIRELESS = 1 << 4
            OHM_EXT_ROUTE_TYPE_VOICE = 1 << 5
            OHM_EXT_ROUTE_TYPE_BLUETOOTH_SCO = 1 << 6
            OHM_EXT_ROUTE_TYPE_BLUETOOTH_A2DP = 1 << 7
            OHM_EXT_ROUTE_TYPE_HEADSET = 1 << 8
            OHM_EXT_ROUTE_TYPE_HEADPHONE = 1 << 9
            OHM_EXT_ROUTE_TYPE_USB = 1 << 10
            OHM_EXT_ROUTE_TYPE_UNKNOWN = 1 << 11

            OHM_EXT_ROUTE_TYPE_AVAILABLE = 1 << 25
            OHM_EXT_ROUTE_TYPE_PREFERRED = 1 << 26
            OHM_EXT_ROUTE_TYPE_ACTIVE = 1 << 27

            routes = (
                "speaker",
                OHM_EXT_ROUTE_TYPE_OUTPUT
                | OHM_EXT_ROUTE_TYPE_BUILTIN
                | OHM_EXT_ROUTE_TYPE_AVAILABLE
                | OHM_EXT_ROUTE_TYPE_ACTIVE,
                "microphone",
                OHM_EXT_ROUTE_TYPE_INPUT | OHM_EXT_ROUTE_TYPE_BUILTIN,
            )

            log.info("ActiveRoutes: %s", routes)

            return routes

        except:
            log.exception('')

    @dbus_signal_async("su", signal_name="AudioRouteChanged")
    async def audio_route_changed(self) -> None:
        raise NotImplementedError

    def audio_route_changed_emit(self, name: str, type: OhmRouteType) -> None:
        # fairly certain the checker is wrong here
        self.audio_route_changed.emit((name, int(type)))  # type: ignore

    @dbus_signal_async("suu", signal_name="AudioFeatureChanged")
    async def audio_feature_changed(self) -> None:
        raise NotImplementedError

    def audio_feature_changed_emit(self, name: str, a: bool, b: bool) -> None:
        # fairly certain the checker is wrong here
        self.audio_feature_changed.emit((name, int(a), int(b)))  # type: ignore

    async def get_default_sink(self) -> pulsectl.PulseSinkInfo:
        sink_name = (await self.pulse.server_info()).default_sink_name
        for sink in await self._sink_list():
            if sink.name == sink_name:
                return sink

        raise Exception("No default sink found")

    async def get_default_source(self) -> pulsectl.PulseSourceInfo:
        source_name = (await self.pulse.server_info()).default_source_name
        for source in await self._source_list():
            if source.name == source_name:
                return source

        raise Exception("No default source found")

    async def find_private_output_for_call(
        self,
    ) -> tuple[pulsectl.PulseSinkInfo, pulsectl.PulsePortInfo]:
        # first try active sink
        sink = await self.get_default_sink()
        for port in sink.port_list:
            if port.available != "no" and port.type == "headphones":
                return (sink, port)

            if port.available != "no" and port.type == "earpiece":
                return (sink, port)

        # now try all sinks (these don't have priorities)
        for sink in await self._sink_list():
            # ports should be ordered by priority already
            for port in sink.port_list:
                if port.available != "no" and port.type == "headphones":
                    return (sink, port)

                if port.available != "no" and port.type == "earpiece":
                    return (sink, port)

        log.info("no earpiece found")
        raise Exception("No earpiece found")

    async def find_mic_for_output(
        self,
        sink: pulsectl.PulseSinkInfo,
        port: pulsectl.PulsePortInfo,
    ) -> tuple[pulsectl.PulseSourceInfo, pulsectl.PulsePortInfo]:
        # look for mic on same device as the output
        sink_device = sink.name.split('.')[1]
        log.info("looking at output dev: %s", sink_device)

        searching_for_type = "mic"

        for source in await self._source_list():
            device = source.name.split('.')[1]

            if device == sink_device:
                for source_port in source.port_list:
                    if source_port.available != "no" and source_port.type == searching_for_type:
                        return (source, source_port)

        return (None, None)

    async def find_best_output(
        self,
    ) -> tuple[pulsectl.PulseSinkInfo, pulsectl.PulsePortInfo]:
        # first try the highest priority port on the current sink
        sink = await self.get_default_sink()
        for port in sink.port_list:
            if port.available != "no":
                return (sink, port)

        # now try other sinks (these don't have priorities)
        for sink in await self._sink_list():
            for port in sink.port_list:
                if port.available != "no":
                    return (sink, port)

        raise Exception("No best output found")

    async def find_speaker_for_call(
        self,
    ) -> tuple[pulsectl.PulseSinkInfo, pulsectl.PulsePortInfo]:
        # if route before call happened to be speaker, use that
        if self.output_route_before_call is not None:
            (sink, port) = self.output_route_before_call
            if await self.route_still_exists(sink, port):
                if port.available != "no" and port.type == "speaker":
                    return (sink, port)

        # otherwise look for a speaker on current sink
        sink = await self.get_default_sink()
        for port in sink.port_list:
            if port.available != "no" and port.type == "speaker":
                return (sink, port)

        # otherwise try all sinks (these don't have priorities)
        for sink in await self._sink_list():
            # ports should be ordered by priority already
            for port in sink.port_list:
                if port.available != "no" and port.type == "speaker":
                    return (sink, port)

        log.info("no speaker found")
        raise Exception("No speaker found")

    async def route_still_exists(
        self,
        existing_sink: pulsectl.PulseSinkInfo,
        existing_port: pulsectl.PulsePortInfo,
    ) -> bool:
        log.info("checking if route still exists")
        for sink in await self._sink_list():
            if sink.name != existing_sink.name:
                continue

            for port in sink.port_list:
                if port.name == existing_port.name and port.available != "no":
                    print("yupppp")
                    return True

        log.info("that's a no")
        return False

    async def source_route_still_exists(
        self,
        existing_source: pulsectl.PulseSourceInfo,
        existing_port: pulsectl.PulsePortInfo,
    ) -> bool:
        log.info("checking if route still exists")
        for source in await self._source_list():
            if source.name != existing_source.name:
                continue

            for port in source.port_list:
                if port.name == existing_port.name and port.available != "no":
                    print("yupppp")
                    return True

        log.info("that's a no")
        return False

    async def switch_output(
        self,
        sink: pulsectl.PulseSinkInfo,
        port: pulsectl.PulsePortInfo,
    ) -> None:
        default_sink = await self.get_default_sink()

        if sink.name != default_sink.name:
            print("need to switch sink")
            await self.pulse.default_set(sink)
            for sink_input in await self.pulse.sink_input_list():
                print("moving stream over to new sink")
                await self.pulse.sink_input_move(sink_input.index, sink.index)

        if len(sink.port_list) > 1:
            await self.pulse.port_set(sink, port)

    async def switch_input(
        self,
        source: pulsectl.PulseSourceInfo,
        port: pulsectl.PulsePortInfo,
    ) -> None:
        default_source = await self.get_default_source()

        if source.name != default_source.name:
            print("need to switch source")
            await self.pulse.default_set(source)
            for source_output in await self.pulse.source_output_list():
                print("moving stream over to new source")
                await self.pulse.source_output_move(source_output.index, source.index)

        if len(source.port_list) > 1:
            await self.pulse.port_set(source, port)

    async def route_output_for_call(self, in_call: bool) -> None:
        log.info("routeOutputForCall %r", in_call)
        default_sink = await self.get_default_sink()

        log.info("cur route %s", default_sink.port_active.name)

        if in_call:
            # if any speaker (could also be bt) is in use, switch to a more
            # private device (earpiece or headphones), otherwise just leave
            # things as-is
            if default_sink.port_active.type == "speaker":
                self.output_route_before_call = (default_sink, default_sink.port_active)
                (sink, port) = await self.find_private_output_for_call()
                await self.switch_output(sink, port)

            self.audio_route_changed_emit(
                "speaker",
                OhmRouteType.OUTPUT | OhmRouteType.BUILTIN | OhmRouteType.AVAILABLE,
            )
            self.audio_route_changed_emit(
                "earpiece",
                OhmRouteType.OUTPUT
                | OhmRouteType.BUILTIN
                | OhmRouteType.VOICE
                | OhmRouteType.AVAILABLE
                | OhmRouteType.ACTIVE,
            )

            self.audio_feature_changed_emit("speaker", True, False)
        else:
            if default_sink.port_active.type == "earpiece":
                if self.output_route_before_call is not None:
                    log.info("Restoring output route from before call")
                    (sink, prev_port) = self.output_route_before_call
                    if not await self.route_still_exists(sink, prev_port):
                        log.info("Route no longer exists, finding new one")
                        (sink, prev_port) = await self.find_best_output()
                else:
                    (sink, prev_port) = await self.find_best_output()

                await self.switch_output(sink, prev_port)

            if self.input_route_before_speaker is not None:
                log.info("Restoring input route from before call")
                (source, prev_port) = self.input_route_before_speaker
                if await self.source_route_still_exists(source, prev_port):
                    await self.switch_input(source, prev_port)
                else:
                    log.info("Route no longer exists, not restoring")

            self.output_route_before_call = None
            self.output_route_before_speaker = None
            self.input_route_before_speaker = None

        log.info("new route: %s", (await self.get_default_sink()).port_active.name)

        await self.mce.sync_proximity_monitoring()

    async def use_speaker_in_call(self, use_speaker: bool) -> None:
        log.info("useSpeakerInCall %r", use_speaker)
        default_sink = await self.get_default_sink()

        log.info("cur route %s", default_sink.port_active.name)

        if use_speaker:
            if default_sink.port_active.type != "speaker":
                self.output_route_before_speaker = (default_sink, default_sink.port_active)
                (sink, port) = await self.find_speaker_for_call()
                await self.switch_output(sink, port)

                default_source = await self.get_default_source()
                if default_source.port_active.type != "mic":
                    (source, port) = await self.find_mic_for_output(sink, port)
                    if source != None:
                        log.info("Found an internal mic, switching")
                        self.input_route_before_speaker = (default_source, default_source.port_active)
                        await self.switch_input(source, port)

                self.audio_route_changed_emit(
                    "earpiece",
                    OhmRouteType.OUTPUT
                    | OhmRouteType.BUILTIN
                    | OhmRouteType.VOICE
                    | OhmRouteType.AVAILABLE,
                )
                self.audio_route_changed_emit(
                    "speaker",
                    OhmRouteType.OUTPUT
                    | OhmRouteType.BUILTIN
                    | OhmRouteType.AVAILABLE
                    | OhmRouteType.ACTIVE,
                )
                self.audio_feature_changed_emit("speaker", True, True)
            else:
                # we're not listening to sink/port changes from pulse,
                # so if output changed to a speaker underneath our feet, just change the route silently
                self.audio_route_changed_emit(
                    "earpiece",
                    OhmRouteType.OUTPUT
                    | OhmRouteType.BUILTIN
                    | OhmRouteType.VOICE
                    | OhmRouteType.AVAILABLE,
                )
                self.audio_route_changed_emit(
                    "speaker",
                    OhmRouteType.OUTPUT
                    | OhmRouteType.BUILTIN
                    | OhmRouteType.AVAILABLE
                    | OhmRouteType.ACTIVE,
                )
                self.audio_feature_changed_emit("speaker", True, True)
        else:
            if default_sink.port_active.type == "speaker":
                if self.output_route_before_speaker is not None:
                    log.info("Restoring output route from before speaker")
                    (sink, prev_port) = self.output_route_before_speaker
                    if not await self.route_still_exists(sink, prev_port):
                        log.info("Route no longer exists, finding new one")
                        (sink, prev_port) = await self.find_private_output_for_call()
                else:
                    (sink, prev_port) = await self.find_private_output_for_call()

                await self.switch_output(sink, prev_port)

                if self.input_route_before_speaker is not None:
                    log.info("Restoring input route from before speaker")
                    (source, prev_port) = self.input_route_before_speaker
                    if await self.source_route_still_exists(source, prev_port):
                        await self.switch_input(source, prev_port)
                    else:
                        log.info("Route no longer exists, not restoring")

                self.audio_route_changed_emit(
                    "speaker",
                    OhmRouteType.OUTPUT | OhmRouteType.BUILTIN | OhmRouteType.AVAILABLE,
                )
                self.audio_route_changed_emit(
                    "earpiece",
                    OhmRouteType.OUTPUT
                    | OhmRouteType.BUILTIN
                    | OhmRouteType.VOICE
                    | OhmRouteType.AVAILABLE
                    | OhmRouteType.ACTIVE,
                )
                self.audio_feature_changed_emit("speaker", True, False)
            else:
                # we're not listening to sink/port changes from pulse,
                # so if output changed to a speaker underneath our feet, just change the route silently
                self.audio_route_changed_emit(
                    "speaker",
                    OhmRouteType.OUTPUT | OhmRouteType.BUILTIN | OhmRouteType.AVAILABLE,
                )
                self.audio_route_changed_emit(
                    "earpiece",
                    OhmRouteType.OUTPUT
                    | OhmRouteType.BUILTIN
                    | OhmRouteType.VOICE
                    | OhmRouteType.AVAILABLE
                    | OhmRouteType.ACTIVE,
                )
                self.audio_feature_changed_emit("speaker", True, False)

            self.output_route_before_speaker = None
            self.input_route_before_speaker = None

        log.info("new route: %s", (await self.get_default_sink()).port_active.name)

        await self.mce.sync_proximity_monitoring()

    async def is_routing_to_earpiece(self) -> bool:
        default_sink = await self.get_default_sink()
        return default_sink.port_active.type == "earpiece"

    def set_mce(self, mce: MceShim) -> bool:
        self.mce = mce


class SensorDaemon(DbusInterfaceCommonAsync, interface_name="org.gnome.Shell.SensorDaemon"):
    @dbus_method_async(method_name="StartProximityMonitoring")
    async def start_proximity_monitoring() -> None:
        raise NotImplementedError

    @dbus_method_async(method_name="StopProximityMonitoring")
    async def stop_proximity_monitoring() -> None:
        raise NotImplementedError


class MceShim(DbusInterfaceCommonAsync, interface_name="com.nokia.mce.request"):
    def __init__(self, route_manager: RouteManagerShim) -> None:
        super().__init__()

        self.route_manager = route_manager

        self.sensor_daemon = SensorDaemon.new_proxy(
            "org.gnome.Shell.SensorDaemon", "/org/gnome/Shell/SensorDaemon"
        )

        self.in_call = False
        self.monitoring_proximity = False

    async def sync_proximity_monitoring(self) -> None:
        should_monitor = self.in_call and await self.route_manager.is_routing_to_earpiece()
        log.info("sync moni %d", should_monitor)
        if should_monitor != self.monitoring_proximity:
            self.monitoring_proximity = should_monitor

            if should_monitor:
                await self.sensor_daemon.start_proximity_monitoring()
            else:
                await self.sensor_daemon.stop_proximity_monitoring()

    @dbus_method_async("ss", "b", method_name="req_call_state_change")
    async def req_call_state_change(self, state: str, desc: str) -> bool:
        try:
            log.info("req_call_state_change: %s", state)

            if state == "active":
                self.in_call = True
            elif state == "none":
                self.in_call = False

            await self.sync_proximity_monitoring()

            return True

        except:
            log.exception('')


class Feedbackd(DbusInterfaceCommonAsync, interface_name="org.sigxcpu.Feedback"):
    @dbus_method_async("ssa{sv}i", "u", method_name="TriggerFeedback")
    async def trigger_feedback(
        self, app_id: str, event: str, hints: dict[str, Any], timeout: int
    ) -> int:
        raise NotImplementedError

    @dbus_method_async("u", method_name="EndFeedback")
    async def end_feedback(self, id: int) -> None:
        raise NotImplementedError


class NonGraphicFeedbackShim(
    DbusInterfaceCommonAsync, interface_name="com.nokia.NonGraphicFeedback1"
):
    def __init__(self) -> None:
        super().__init__()

        self.feedbackd = Feedbackd.new_proxy(
            "org.sigxcpu.Feedback", "/org/sigxcpu/Feedback"
        )
        self.current_id = -1

    def translate_feedback(
        self, name: str, params: dict[str, Any]
    ) -> tuple[str, dict[str, Any]]:
        hints = {}
        feedbackName = None


        if name == "feedback_press":
            # generic touch feedback
            feedbackName = "button-pressed"
        elif name == "pulldown_highlight":
            # another generic touch feedback
            feedbackName = "button-pressed"
        elif name == "vibra":
            # only vibration feedback, no sound
            feedbackName = "bell-terminal"
            hints["profile"] = ("s", "quiet")

        if 'media.vibra' in params:
            should_vibrate = params['media.vibra'][1]
            if not should_vibrate:
                # unfortunately we can only disable vibration by also disabling sound
                hints["profile"] = ("s", "silent")

        if 'haptic.sequence' in params:
            haptic_sequence = params['haptic.sequence'][1]
            # in format "on=timeMs"

        if 'haptic.type' in params:
            haptic_type = params['haptic.type'][1]
            # can be "touch"

        return (feedbackName, hints)

    @dbus_method_async("sa{sv}", "u", method_name="Play")
    async def play(self, name: str, params: dict[str, Any]) -> int:
        try:
            log.info("NonGraphicFeedbackShim Play: %s", name)
            print(params)

            (feedback_name, hints) = self.translate_feedback(name, params)

            if feedback_name == None:
                return 0

            print("NonGraphicFeedbackShim actually playing:", feedback_name, hints)
            self.current_id = await self.feedbackd.trigger_feedback(
                "aliendalvik", feedback_name, hints, -1
            )

            return self.current_id

        except:
            log.exception('')

    @dbus_method_async("u", "u", method_name="Stop")
    async def stop(self, feedback_id: int) -> int:
        try:
            log.info("NonGraphicFeedbackShim Stop: %i", feedback_id)
            await self.feedbackd.end_feedback(feedback_id)
            self.current_id = -1
            return 0

        except:
            log.exception('')


async def main() -> None:
    system = sd_bus_open_system()
    await asyncio.gather(
        *(
            system.request_name_async(name, 0)
            for name in [
                POLICY_DBUS_SERVICE,
                "com.nokia.NonGraphicFeedback1.Backend",
                "org.nemomobile.Route.Manager",
                "com.nokia.mce",
            ]
        )
    )

    async with pulsectl_asyncio.PulseAsync("my-client-name") as pulse:
        log.info("sinks: %r", await pulse.sink_list())

        route_manager = RouteManagerShim(pulse)
        route_manager.export_to_dbus("/org/nemomobile/Route/Manager", system)
        call_daemon = DummyPolicyDaemon(route_manager)
        call_daemon.export_to_dbus(POLICY_DBUS_PATH, system)
        mce = MceShim(route_manager)
        route_manager.set_mce(mce)
        mce.export_to_dbus("/com/nokia/mce/request", system)

        ngf = NonGraphicFeedbackShim()
        ngf.export_to_dbus("/com/nokia/NonGraphicFeedback1", system)

        while True:
            await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())


