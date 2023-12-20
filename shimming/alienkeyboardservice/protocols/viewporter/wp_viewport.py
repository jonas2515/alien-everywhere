# This file has been autogenerated by the pywayland scanner

# Copyright © 2013-2016 Collabora, Ltd.
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


class WpViewport(Interface):
    """Crop and scale interface to a :class:`~pywayland.protocol.wayland.WlSurface`

    An additional interface to a :class:`~pywayland.protocol.wayland.WlSurface`
    object, which allows the client to specify the cropping and scaling of the
    surface contents.

    This interface works with two concepts: the source rectangle (src_x, src_y,
    src_width, src_height), and the destination size (dst_width, dst_height).
    The contents of the source rectangle are scaled to the destination size,
    and content outside the source rectangle is ignored. This state is double-
    buffered, and is applied on the next :func:`WlSurface.commit()
    <pywayland.protocol.wayland.WlSurface.commit>`.

    The two parts of crop and scale state are independent: the source
    rectangle, and the destination size. Initially both are unset, that is, no
    scaling is applied. The whole of the current
    :class:`~pywayland.protocol.wayland.WlBuffer` is used as the source, and
    the surface size is as defined in :func:`WlSurface.attach()
    <pywayland.protocol.wayland.WlSurface.attach>`.

    If the destination size is set, it causes the surface size to become
    dst_width, dst_height. The source (rectangle) is scaled to exactly this
    size. This overrides whatever the attached
    :class:`~pywayland.protocol.wayland.WlBuffer` size is, unless the
    :class:`~pywayland.protocol.wayland.WlBuffer` is NULL. If the
    :class:`~pywayland.protocol.wayland.WlBuffer` is NULL, the surface has no
    content and therefore no size. Otherwise, the size is always at least 1x1
    in surface local coordinates.

    If the source rectangle is set, it defines what area of the
    :class:`~pywayland.protocol.wayland.WlBuffer` is taken as the source. If
    the source rectangle is set and the destination size is not set, then
    src_width and src_height must be integers, and the surface size becomes the
    source rectangle size. This results in cropping without scaling. If
    src_width or src_height are not integers and destination size is not set,
    the bad_size protocol error is raised when the surface state is applied.

    The coordinate transformations from buffer pixel coordinates up to the
    surface-local coordinates happen in the following order:   1.
    buffer_transform (:func:`WlSurface.set_buffer_transform()
    <pywayland.protocol.wayland.WlSurface.set_buffer_transform>`)   2.
    buffer_scale (:func:`WlSurface.set_buffer_scale()
    <pywayland.protocol.wayland.WlSurface.set_buffer_scale>`)   3. crop and
    scale (:class:`WpViewport`.set*) This means, that the source rectangle
    coordinates of crop and scale are given in the coordinates after the buffer
    transform and scale, i.e. in the coordinates that would be the surface-
    local coordinates if the crop and scale was not applied.

    If src_x or src_y are negative, the bad_value protocol error is raised.
    Otherwise, if the source rectangle is partially or completely outside of
    the non-NULL :class:`~pywayland.protocol.wayland.WlBuffer`, then the
    out_of_buffer protocol error is raised when the surface state is applied. A
    NULL :class:`~pywayland.protocol.wayland.WlBuffer` does not raise the
    out_of_buffer error.

    If the :class:`~pywayland.protocol.wayland.WlSurface` associated with the
    :class:`WpViewport` is destroyed, all :class:`WpViewport` requests except
    'destroy' raise the protocol error no_surface.

    If the :class:`WpViewport` object is destroyed, the crop and scale state is
    removed from the :class:`~pywayland.protocol.wayland.WlSurface`. The change
    will be applied on the next :func:`WlSurface.commit()
    <pywayland.protocol.wayland.WlSurface.commit>`.
    """

    name = "wp_viewport"
    version = 1

    class error(enum.IntEnum):
        bad_value = 0
        bad_size = 1
        out_of_buffer = 2
        no_surface = 3


class WpViewportProxy(Proxy[WpViewport]):
    interface = WpViewport

    @WpViewport.request()
    def destroy(self) -> None:
        """Remove scaling and cropping from the surface

        The associated wl_surface's crop and scale state is removed. The change
        is applied on the next :func:`WlSurface.commit()
        <pywayland.protocol.wayland.WlSurface.commit>`.
        """
        self._marshal(0)
        self._destroy()

    @WpViewport.request(
        Argument(ArgumentType.Fixed),
        Argument(ArgumentType.Fixed),
        Argument(ArgumentType.Fixed),
        Argument(ArgumentType.Fixed),
    )
    def set_source(self, x: float, y: float, width: float, height: float) -> None:
        """Set the source rectangle for cropping

        Set the source rectangle of the associated
        :class:`~pywayland.protocol.wayland.WlSurface`. See :class:`WpViewport`
        for the description, and relation to the
        :class:`~pywayland.protocol.wayland.WlBuffer` size.

        If all of x, y, width and height are -1.0, the source rectangle is
        unset instead. Any other set of values where width or height are zero
        or negative, or x or y are negative, raise the bad_value protocol
        error.

        The crop and scale state is double-buffered state, and will be applied
        on the next :func:`WlSurface.commit()
        <pywayland.protocol.wayland.WlSurface.commit>`.

        :param x:
            source rectangle x
        :type x:
            `ArgumentType.Fixed`
        :param y:
            source rectangle y
        :type y:
            `ArgumentType.Fixed`
        :param width:
            source rectangle width
        :type width:
            `ArgumentType.Fixed`
        :param height:
            source rectangle height
        :type height:
            `ArgumentType.Fixed`
        """
        self._marshal(1, x, y, width, height)

    @WpViewport.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def set_destination(self, width: int, height: int) -> None:
        """Set the surface size for scaling

        Set the destination size of the associated
        :class:`~pywayland.protocol.wayland.WlSurface`. See :class:`WpViewport`
        for the description, and relation to the
        :class:`~pywayland.protocol.wayland.WlBuffer` size.

        If width is -1 and height is -1, the destination size is unset instead.
        Any other pair of values for width and height that contains zero or
        negative values raises the bad_value protocol error.

        The crop and scale state is double-buffered state, and will be applied
        on the next :func:`WlSurface.commit()
        <pywayland.protocol.wayland.WlSurface.commit>`.

        :param width:
            surface width
        :type width:
            `ArgumentType.Int`
        :param height:
            surface height
        :type height:
            `ArgumentType.Int`
        """
        self._marshal(2, width, height)


class WpViewportResource(Resource):
    interface = WpViewport


class WpViewportGlobal(Global):
    interface = WpViewport


WpViewport._gen_c()
WpViewport.proxy_class = WpViewportProxy
WpViewport.resource_class = WpViewportResource
WpViewport.global_class = WpViewportGlobal
