# This file has been autogenerated by the pywayland scanner

# Copyright © 2022 Simon Ser
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


from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)
from ..wayland import WlBuffer


class WpSinglePixelBufferManagerV1(Interface):
    """Global factory for single-pixel buffers

    The :class:`WpSinglePixelBufferManagerV1` interface is a factory for
    single-pixel buffers.
    """

    name = "wp_single_pixel_buffer_manager_v1"
    version = 1


class WpSinglePixelBufferManagerV1Proxy(Proxy[WpSinglePixelBufferManagerV1]):
    interface = WpSinglePixelBufferManagerV1

    @WpSinglePixelBufferManagerV1.request()
    def destroy(self) -> None:
        """Destroy the manager

        Destroy the :class:`WpSinglePixelBufferManagerV1` object.

        The child objects created via this interface are unaffected.
        """
        self._marshal(0)
        self._destroy()

    @WpSinglePixelBufferManagerV1.request(
        Argument(ArgumentType.NewId, interface=WlBuffer),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def create_u32_rgba_buffer(self, r: int, g: int, b: int, a: int) -> Proxy[WlBuffer]:
        """Create a 1×1 buffer from 32-bit rgba values

        Create a single-pixel buffer from four 32-bit RGBA values.

        Unless specified in another protocol extension, the RGBA values use
        pre-multiplied alpha.

        The width and height of the buffer are 1.

        :param r:
            value of the buffer's red channel
        :type r:
            `ArgumentType.Uint`
        :param g:
            value of the buffer's green channel
        :type g:
            `ArgumentType.Uint`
        :param b:
            value of the buffer's blue channel
        :type b:
            `ArgumentType.Uint`
        :param a:
            value of the buffer's alpha channel
        :type a:
            `ArgumentType.Uint`
        :returns:
            :class:`~pywayland.protocol.wayland.WlBuffer`
        """
        id = self._marshal_constructor(1, WlBuffer, r, g, b, a)
        return id


class WpSinglePixelBufferManagerV1Resource(Resource):
    interface = WpSinglePixelBufferManagerV1


class WpSinglePixelBufferManagerV1Global(Global):
    interface = WpSinglePixelBufferManagerV1


WpSinglePixelBufferManagerV1._gen_c()
WpSinglePixelBufferManagerV1.proxy_class = WpSinglePixelBufferManagerV1Proxy
WpSinglePixelBufferManagerV1.resource_class = WpSinglePixelBufferManagerV1Resource
WpSinglePixelBufferManagerV1.global_class = WpSinglePixelBufferManagerV1Global
