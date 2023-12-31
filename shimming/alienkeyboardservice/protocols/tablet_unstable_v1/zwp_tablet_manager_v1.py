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
from ..wayland import WlSeat
from .zwp_tablet_seat_v1 import ZwpTabletSeatV1


class ZwpTabletManagerV1(Interface):
    """Controller object for graphic tablet devices

    An object that provides access to the graphics tablets available on this
    system. All tablets are associated with a seat, to get access to the actual
    tablets, use wp_tablet_manager.get_tablet_seat.
    """

    name = "zwp_tablet_manager_v1"
    version = 1


class ZwpTabletManagerV1Proxy(Proxy[ZwpTabletManagerV1]):
    interface = ZwpTabletManagerV1

    @ZwpTabletManagerV1.request(
        Argument(ArgumentType.NewId, interface=ZwpTabletSeatV1),
        Argument(ArgumentType.Object, interface=WlSeat),
    )
    def get_tablet_seat(self, seat: WlSeat) -> Proxy[ZwpTabletSeatV1]:
        """Get the tablet seat

        Get the wp_tablet_seat object for the given seat. This object provides
        access to all graphics tablets in this seat.

        :param seat:
            The :class:`~pywayland.protocol.wayland.WlSeat` object to retrieve
            the tablets for
        :type seat:
            :class:`~pywayland.protocol.wayland.WlSeat`
        :returns:
            :class:`~pywayland.protocol.tablet_unstable_v1.ZwpTabletSeatV1`
        """
        tablet_seat = self._marshal_constructor(0, ZwpTabletSeatV1, seat)
        return tablet_seat

    @ZwpTabletManagerV1.request()
    def destroy(self) -> None:
        """Release the memory for the tablet manager object

        Destroy the wp_tablet_manager object. Objects created from this object
        are unaffected and should be destroyed separately.
        """
        self._marshal(1)
        self._destroy()


class ZwpTabletManagerV1Resource(Resource):
    interface = ZwpTabletManagerV1


class ZwpTabletManagerV1Global(Global):
    interface = ZwpTabletManagerV1


ZwpTabletManagerV1._gen_c()
ZwpTabletManagerV1.proxy_class = ZwpTabletManagerV1Proxy
ZwpTabletManagerV1.resource_class = ZwpTabletManagerV1Resource
ZwpTabletManagerV1.global_class = ZwpTabletManagerV1Global
