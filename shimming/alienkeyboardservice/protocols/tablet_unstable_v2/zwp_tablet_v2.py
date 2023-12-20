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


from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)


class ZwpTabletV2(Interface):
    """Graphics tablet device

    The wp_tablet interface represents one graphics tablet device. The tablet
    interface itself does not generate events; all events are generated by
    wp_tablet_tool objects when in proximity above a tablet.

    A tablet has a number of static characteristics, e.g. device name and
    pid/vid. These capabilities are sent in an event sequence after the
    wp_tablet_seat.tablet_added event. This initial event sequence is
    terminated by a wp_tablet.done event.
    """

    name = "zwp_tablet_v2"
    version = 1


class ZwpTabletV2Proxy(Proxy[ZwpTabletV2]):
    interface = ZwpTabletV2

    @ZwpTabletV2.request()
    def destroy(self) -> None:
        """Destroy the tablet object

        This destroys the client's resource for this tablet object.
        """
        self._marshal(0)
        self._destroy()


class ZwpTabletV2Resource(Resource):
    interface = ZwpTabletV2

    @ZwpTabletV2.event(
        Argument(ArgumentType.String),
    )
    def name(self, name: str) -> None:
        """Tablet device name

        This event is sent in the initial burst of events before the
        wp_tablet.done event.

        :param name:
            the device name
        :type name:
            `ArgumentType.String`
        """
        self._post_event(0, name)

    @ZwpTabletV2.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def id(self, vid: int, pid: int) -> None:
        """Tablet device usb vendor/product id

        This event is sent in the initial burst of events before the
        wp_tablet.done event.

        :param vid:
            USB vendor id
        :type vid:
            `ArgumentType.Uint`
        :param pid:
            USB product id
        :type pid:
            `ArgumentType.Uint`
        """
        self._post_event(1, vid, pid)

    @ZwpTabletV2.event(
        Argument(ArgumentType.String),
    )
    def path(self, path: str) -> None:
        """Path to the device

        A system-specific device path that indicates which device is behind
        this wp_tablet. This information may be used to gather additional
        information about the device, e.g. through libwacom.

        A device may have more than one device path. If so, multiple
        wp_tablet.path events are sent. A device may be emulated and not have a
        device path, and in that case this event will not be sent.

        The format of the path is unspecified, it may be a device node, a sysfs
        path, or some other identifier. It is up to the client to identify the
        string provided.

        This event is sent in the initial burst of events before the
        wp_tablet.done event.

        :param path:
            path to local device
        :type path:
            `ArgumentType.String`
        """
        self._post_event(2, path)

    @ZwpTabletV2.event()
    def done(self) -> None:
        """Tablet description events sequence complete

        This event is sent immediately to signal the end of the initial burst
        of descriptive events. A client may consider the static description of
        the tablet to be complete and finalize initialization of the tablet.
        """
        self._post_event(3)

    @ZwpTabletV2.event()
    def removed(self) -> None:
        """Tablet removed event

        Sent when the tablet has been removed from the system. When a tablet is
        removed, some tools may be removed.

        When this event is received, the client must wp_tablet.destroy the
        object.
        """
        self._post_event(4)


class ZwpTabletV2Global(Global):
    interface = ZwpTabletV2


ZwpTabletV2._gen_c()
ZwpTabletV2.proxy_class = ZwpTabletV2Proxy
ZwpTabletV2.resource_class = ZwpTabletV2Resource
ZwpTabletV2.global_class = ZwpTabletV2Global
