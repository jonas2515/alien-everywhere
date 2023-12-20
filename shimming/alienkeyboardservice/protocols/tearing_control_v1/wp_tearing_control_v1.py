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


class WpTearingControlV1(Interface):
    """Per-surface tearing control interface

    An additional interface to a :class:`~pywayland.protocol.wayland.WlSurface`
    object, which allows the client to hint to the compositor if the content on
    the surface is suitable for presentation with tearing. The default
    presentation hint is vsync. See presentation_hint for more details.
    """

    name = "wp_tearing_control_v1"
    version = 1

    class presentation_hint(enum.IntEnum):
        vsync = 0
        async_ = 1


class WpTearingControlV1Proxy(Proxy[WpTearingControlV1]):
    interface = WpTearingControlV1

    @WpTearingControlV1.request(
        Argument(ArgumentType.Uint),
    )
    def set_presentation_hint(self, hint: int) -> None:
        """Set presentation hint

        Set the presentation hint for the associated
        :class:`~pywayland.protocol.wayland.WlSurface`. This state is double-
        buffered and is applied on the next :func:`WlSurface.commit()
        <pywayland.protocol.wayland.WlSurface.commit>`.

        The compositor is free to dynamically respect or ignore this hint based
        on various conditions like hardware capabilities, surface state and
        user preferences.

        :param hint:
        :type hint:
            `ArgumentType.Uint`
        """
        self._marshal(0, hint)

    @WpTearingControlV1.request()
    def destroy(self) -> None:
        """Destroy tearing control object

        Destroy this surface tearing object and revert the presentation hint to
        vsync. The change will be applied on the next :func:`WlSurface.commit()
        <pywayland.protocol.wayland.WlSurface.commit>`.
        """
        self._marshal(1)
        self._destroy()


class WpTearingControlV1Resource(Resource):
    interface = WpTearingControlV1


class WpTearingControlV1Global(Global):
    interface = WpTearingControlV1


WpTearingControlV1._gen_c()
WpTearingControlV1.proxy_class = WpTearingControlV1Proxy
WpTearingControlV1.resource_class = WpTearingControlV1Resource
WpTearingControlV1.global_class = WpTearingControlV1Global
