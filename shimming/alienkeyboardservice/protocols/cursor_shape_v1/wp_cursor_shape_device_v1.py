# This file has been autogenerated by the pywayland scanner

# Copyright 2018 The Chromium Authors
# Copyright 2023 Simon Ser
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
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


class WpCursorShapeDeviceV1(Interface):
    """Cursor shape for a device

    This interface advertises the list of supported cursor shapes for a device,
    and allows clients to set the cursor shape.
    """

    name = "wp_cursor_shape_device_v1"
    version = 1

    class shape(enum.IntEnum):
        default = 1
        context_menu = 2
        help = 3
        pointer = 4
        progress = 5
        wait = 6
        cell = 7
        crosshair = 8
        text = 9
        vertical_text = 10
        alias = 11
        copy = 12
        move = 13
        no_drop = 14
        not_allowed = 15
        grab = 16
        grabbing = 17
        e_resize = 18
        n_resize = 19
        ne_resize = 20
        nw_resize = 21
        s_resize = 22
        se_resize = 23
        sw_resize = 24
        w_resize = 25
        ew_resize = 26
        ns_resize = 27
        nesw_resize = 28
        nwse_resize = 29
        col_resize = 30
        row_resize = 31
        all_scroll = 32
        zoom_in = 33
        zoom_out = 34

    class error(enum.IntEnum):
        invalid_shape = 1


class WpCursorShapeDeviceV1Proxy(Proxy[WpCursorShapeDeviceV1]):
    interface = WpCursorShapeDeviceV1

    @WpCursorShapeDeviceV1.request()
    def destroy(self) -> None:
        """Destroy the cursor shape device

        Destroy the cursor shape device.

        The device cursor shape remains unchanged.
        """
        self._marshal(0)
        self._destroy()

    @WpCursorShapeDeviceV1.request(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def set_shape(self, serial: int, shape: int) -> None:
        """Set device cursor to the shape

        Sets the device cursor to the specified shape. The compositor will
        change the cursor image based on the specified shape.

        The cursor actually changes only if the input device focus is one of
        the requesting client's surfaces. If any, the previous cursor image
        (surface or shape) is replaced.

        The "shape" argument must be a valid enum entry, otherwise the
        invalid_shape protocol error is raised.

        This is similar to the :func:`WlPointer.set_cursor()
        <pywayland.protocol.wayland.WlPointer.set_cursor>` and
        :func:`ZwpTabletToolV2.set_cursor()
        <pywayland.protocol.tablet_unstable_v2.ZwpTabletToolV2.set_cursor>`
        requests, but this request accepts a shape instead of contents in the
        form of a surface. Clients can mix set_cursor and set_shape requests.

        The serial parameter must match the latest :func:`WlPointer.enter()
        <pywayland.protocol.wayland.WlPointer.enter>` or
        :func:`ZwpTabletToolV2.proximity_in()
        <pywayland.protocol.tablet_unstable_v2.ZwpTabletToolV2.proximity_in>`
        serial number sent to the client. Otherwise the request will be
        ignored.

        :param serial:
            serial number of the enter event
        :type serial:
            `ArgumentType.Uint`
        :param shape:
        :type shape:
            `ArgumentType.Uint`
        """
        self._marshal(1, serial, shape)


class WpCursorShapeDeviceV1Resource(Resource):
    interface = WpCursorShapeDeviceV1


class WpCursorShapeDeviceV1Global(Global):
    interface = WpCursorShapeDeviceV1


WpCursorShapeDeviceV1._gen_c()
WpCursorShapeDeviceV1.proxy_class = WpCursorShapeDeviceV1Proxy
WpCursorShapeDeviceV1.resource_class = WpCursorShapeDeviceV1Resource
WpCursorShapeDeviceV1.global_class = WpCursorShapeDeviceV1Global
