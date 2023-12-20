# This file has been autogenerated by the pywayland scanner

# Copyright © 2021 Emmanuel Gil Peyrot
# Copyright © 2022 Xaver Hugl
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
from .wp_content_type_v1 import WpContentTypeV1


class WpContentTypeManagerV1(Interface):
    """Surface content type manager

    This interface allows a client to describe the kind of content a surface
    will display, to allow the compositor to optimize its behavior for it.

    Warning! The protocol described in this file is currently in the testing
    phase. Backward compatible changes may be added together with the
    corresponding interface version bump. Backward incompatible changes can
    only be done by creating a new major version of the extension.
    """

    name = "wp_content_type_manager_v1"
    version = 1

    class error(enum.IntEnum):
        already_constructed = 0


class WpContentTypeManagerV1Proxy(Proxy[WpContentTypeManagerV1]):
    interface = WpContentTypeManagerV1

    @WpContentTypeManagerV1.request()
    def destroy(self) -> None:
        """Destroy the content type manager object

        Destroy the content type manager. This doesn't destroy objects created
        with the manager.
        """
        self._marshal(0)
        self._destroy()

    @WpContentTypeManagerV1.request(
        Argument(ArgumentType.NewId, interface=WpContentTypeV1),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def get_surface_content_type(self, surface: WlSurface) -> Proxy[WpContentTypeV1]:
        """Create a new toplevel decoration object

        Create a new content type object associated with the given surface.

        Creating a :class:`~pywayland.protocol.content_type_v1.WpContentTypeV1`
        from a :class:`~pywayland.protocol.wayland.WlSurface` which already has
        one attached is a client error: already_constructed.

        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :returns:
            :class:`~pywayland.protocol.content_type_v1.WpContentTypeV1`
        """
        id = self._marshal_constructor(1, WpContentTypeV1, surface)
        return id


class WpContentTypeManagerV1Resource(Resource):
    interface = WpContentTypeManagerV1


class WpContentTypeManagerV1Global(Global):
    interface = WpContentTypeManagerV1


WpContentTypeManagerV1._gen_c()
WpContentTypeManagerV1.proxy_class = WpContentTypeManagerV1Proxy
WpContentTypeManagerV1.resource_class = WpContentTypeManagerV1Resource
WpContentTypeManagerV1.global_class = WpContentTypeManagerV1Global