# This file has been autogenerated by the pywayland scanner

# Copyright © 2021 Xaver Hugl
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

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
from ..wayland import WlSurface
from .wp_tearing_control_v1 import WpTearingControlV1


class WpTearingControlManagerV1(Interface):
    """Protocol for tearing control

    For some use cases like games or drawing tablets it can make sense to
    reduce latency by accepting tearing with the use of asynchronous page
    flips. This global is a factory interface, allowing clients to inform which
    type of presentation the content of their surfaces is suitable for.

    Graphics APIs like EGL or Vulkan, that manage the buffer queue and commits
    of a :class:`~pywayland.protocol.wayland.WlSurface` themselves, are likely
    to be using this extension internally. If a client is using such an API for
    a :class:`~pywayland.protocol.wayland.WlSurface`, it should not directly
    use this extension on that surface, to avoid raising a
    tearing_control_exists protocol error.

    Warning! The protocol described in this file is currently in the testing
    phase. Backward compatible changes may be added together with the
    corresponding interface version bump. Backward incompatible changes can
    only be done by creating a new major version of the extension.
    """

    name = "wp_tearing_control_manager_v1"
    version = 1

    class error(enum.IntEnum):
        tearing_control_exists = 0


class WpTearingControlManagerV1Proxy(Proxy[WpTearingControlManagerV1]):
    interface = WpTearingControlManagerV1

    @WpTearingControlManagerV1.request()
    def destroy(self) -> None:
        """Destroy tearing control factory object

        Destroy this tearing control factory object. Other objects, including
        :class:`~pywayland.protocol.tearing_control_v1.WpTearingControlV1`
        objects created by this factory, are not affected by this request.
        """
        self._marshal(0)
        self._destroy()

    @WpTearingControlManagerV1.request(
        Argument(ArgumentType.NewId, interface=WpTearingControlV1),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def get_tearing_control(self, surface: WlSurface) -> Proxy[WpTearingControlV1]:
        """Extend surface interface for tearing control

        Instantiate an interface extension for the given
        :class:`~pywayland.protocol.wayland.WlSurface` to request asynchronous
        page flips for presentation.

        If the given :class:`~pywayland.protocol.wayland.WlSurface` already has
        a :class:`~pywayland.protocol.tearing_control_v1.WpTearingControlV1`
        object associated, the tearing_control_exists protocol error is raised.

        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :returns:
            :class:`~pywayland.protocol.tearing_control_v1.WpTearingControlV1`
        """
        id = self._marshal_constructor(1, WpTearingControlV1, surface)
        return id


class WpTearingControlManagerV1Resource(Resource):
    interface = WpTearingControlManagerV1


class WpTearingControlManagerV1Global(Global):
    interface = WpTearingControlManagerV1


WpTearingControlManagerV1._gen_c()
WpTearingControlManagerV1.proxy_class = WpTearingControlManagerV1Proxy
WpTearingControlManagerV1.resource_class = WpTearingControlManagerV1Resource
WpTearingControlManagerV1.global_class = WpTearingControlManagerV1Global