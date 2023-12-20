# This file has been autogenerated by the pywayland scanner

# Copyright 2014 © Stephen "Lyude" Chandler Paul
# Copyright 2015-2016 © Red Hat, Inc.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice (including the
# next paragraph) shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import enum

from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)


class ZwpTabletPadStripV2(Interface):
    """Pad strip

    A linear interaction area, such as the strips found in Wacom Cintiq models.

    Events on a strip are logically grouped by the wl_tablet_pad_strip.frame
    event.
    """

    name = "zwp_tablet_pad_strip_v2"
    version = 1

    class source(enum.IntEnum):
        finger = 1


class ZwpTabletPadStripV2Proxy(Proxy[ZwpTabletPadStripV2]):
    interface = ZwpTabletPadStripV2

    @ZwpTabletPadStripV2.request(
        Argument(ArgumentType.String),
        Argument(ArgumentType.Uint),
    )
    def set_feedback(self, description: str, serial: int) -> None:
        """Set compositor feedback

        Requests the compositor to use the provided feedback string associated
        with this strip. This request should be issued immediately after a
        wp_tablet_pad_group.mode_switch event from the corresponding group is
        received, or whenever the strip is mapped to a different action. See
        wp_tablet_pad_group.mode_switch for more details.

        Clients are encouraged to provide context-aware descriptions for the
        actions associated with the strip, and compositors may use this
        information to offer visual feedback about the button layout (eg. on-
        screen displays).

        The provided string 'description' is a UTF-8 encoded string to be
        associated with this ring, and is considered user-visible; general
        internationalization rules apply.

        The serial argument will be that of the last
        wp_tablet_pad_group.mode_switch event received for the group of this
        strip. Requests providing other serials than the most recent one will
        be ignored.

        :param description:
            strip description
        :type description:
            `ArgumentType.String`
        :param serial:
            serial of the mode switch event
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(0, description, serial)

    @ZwpTabletPadStripV2.request()
    def destroy(self) -> None:
        """Destroy the strip object

        This destroys the client's resource for this strip object.
        """
        self._marshal(1)
        self._destroy()


class ZwpTabletPadStripV2Resource(Resource):
    interface = ZwpTabletPadStripV2

    @ZwpTabletPadStripV2.event(
        Argument(ArgumentType.Uint),
    )
    def source(self, source: int) -> None:
        """Strip event source

        Source information for strip events.

        This event does not occur on its own. It is sent before a
        wp_tablet_pad_strip.frame event and carries the source information for
        all events within that frame.

        The source specifies how this event was generated. If the source is
        wp_tablet_pad_strip.source.finger, a wp_tablet_pad_strip.stop event
        will be sent when the user lifts their finger off the device.

        This event is optional. If the source is unknown for an interaction, no
        event is sent.

        :param source:
            the event source
        :type source:
            `ArgumentType.Uint`
        """
        self._post_event(0, source)

    @ZwpTabletPadStripV2.event(
        Argument(ArgumentType.Uint),
    )
    def position(self, position: int) -> None:
        """Position changed

        Sent whenever the position on a strip changes.

        The position is normalized to a range of [0, 65535], the 0-value
        represents the top-most and/or left-most position of the strip in the
        pad's current rotation.

        :param position:
            the current position
        :type position:
            `ArgumentType.Uint`
        """
        self._post_event(1, position)

    @ZwpTabletPadStripV2.event()
    def stop(self) -> None:
        """Interaction stopped

        Stop notification for strip events.

        For some wp_tablet_pad_strip.source types, a wp_tablet_pad_strip.stop
        event is sent to notify a client that the interaction with the strip
        has terminated. This enables the client to implement kinetic scrolling.
        See the wp_tablet_pad_strip.source documentation for information on
        when this event may be generated.

        Any wp_tablet_pad_strip.position events with the same source after this
        event should be considered as the start of a new interaction.
        """
        self._post_event(2)

    @ZwpTabletPadStripV2.event(
        Argument(ArgumentType.Uint),
    )
    def frame(self, time: int) -> None:
        """End of a strip event sequence

        Indicates the end of a set of events that represent one logical
        hardware strip event. A client is expected to accumulate the data in
        all events within the frame before proceeding.

        All wp_tablet_pad_strip events before a wp_tablet_pad_strip.frame event
        belong logically together. For example, on termination of a finger
        interaction on a strip the compositor will send a
        wp_tablet_pad_strip.source event, a wp_tablet_pad_strip.stop event and
        a wp_tablet_pad_strip.frame event.

        A wp_tablet_pad_strip.frame event is sent for every logical event
        group, even if the group only contains a single wp_tablet_pad_strip
        event. Specifically, a client may get a sequence: position, frame,
        position, frame, etc.

        :param time:
            timestamp with millisecond granularity
        :type time:
            `ArgumentType.Uint`
        """
        self._post_event(3, time)


class ZwpTabletPadStripV2Global(Global):
    interface = ZwpTabletPadStripV2


ZwpTabletPadStripV2._gen_c()
ZwpTabletPadStripV2.proxy_class = ZwpTabletPadStripV2Proxy
ZwpTabletPadStripV2.resource_class = ZwpTabletPadStripV2Resource
ZwpTabletPadStripV2.global_class = ZwpTabletPadStripV2Global
