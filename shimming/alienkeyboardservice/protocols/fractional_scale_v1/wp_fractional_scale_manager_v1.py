# This file has been autogenerated by the pywayland scanner

# Copyright © 2022 Kenny Levinsen
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
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
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
from .wp_fractional_scale_v1 import WpFractionalScaleV1


class WpFractionalScaleManagerV1(Interface):
    """Fractional surface scale information

    A global interface for requesting surfaces to use fractional scales.
    """

    name = "wp_fractional_scale_manager_v1"
    version = 1

    class error(enum.IntEnum):
        fractional_scale_exists = 0


class WpFractionalScaleManagerV1Proxy(Proxy[WpFractionalScaleManagerV1]):
    interface = WpFractionalScaleManagerV1

    @WpFractionalScaleManagerV1.request()
    def destroy(self) -> None:
        """Unbind the fractional surface scale interface

        Informs the server that the client will not be using this protocol
        object anymore. This does not affect any other objects,
        :class:`~pywayland.protocol.fractional_scale_v1.WpFractionalScaleV1`
        objects included.
        """
        self._marshal(0)
        self._destroy()

    @WpFractionalScaleManagerV1.request(
        Argument(ArgumentType.NewId, interface=WpFractionalScaleV1),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def get_fractional_scale(self, surface: WlSurface) -> Proxy[WpFractionalScaleV1]:
        """Extend surface interface for scale information

        Create an add-on object for the the
        :class:`~pywayland.protocol.wayland.WlSurface` to let the compositor
        request fractional scales. If the given
        :class:`~pywayland.protocol.wayland.WlSurface` already has a
        :class:`~pywayland.protocol.fractional_scale_v1.WpFractionalScaleV1`
        object associated, the fractional_scale_exists protocol error is
        raised.

        :param surface:
            the surface
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :returns:
            :class:`~pywayland.protocol.fractional_scale_v1.WpFractionalScaleV1`
            -- the new surface scale info interface id
        """
        id = self._marshal_constructor(1, WpFractionalScaleV1, surface)
        return id


class WpFractionalScaleManagerV1Resource(Resource):
    interface = WpFractionalScaleManagerV1


class WpFractionalScaleManagerV1Global(Global):
    interface = WpFractionalScaleManagerV1


WpFractionalScaleManagerV1._gen_c()
WpFractionalScaleManagerV1.proxy_class = WpFractionalScaleManagerV1Proxy
WpFractionalScaleManagerV1.resource_class = WpFractionalScaleManagerV1Resource
WpFractionalScaleManagerV1.global_class = WpFractionalScaleManagerV1Global
