# This file has been autogenerated by the pywayland scanner

# Copyright © 2008-2011 Kristian Høgsberg
# Copyright © 2010-2011 Intel Corporation
# Copyright © 2012-2013 Collabora, Ltd.
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
from .wl_buffer import WlBuffer
from .wl_callback import WlCallback
from .wl_output import WlOutput
from .wl_region import WlRegion


class WlSurface(Interface):
    """An onscreen surface

    A surface is a rectangular area that may be displayed on zero or more
    outputs, and shown any number of times at the compositor's discretion. They
    can present wl_buffers, receive user input, and define a local coordinate
    system.

    The size of a surface (and relative positions on it) is described in
    surface-local coordinates, which may differ from the buffer coordinates of
    the pixel content, in case a buffer_transform or a buffer_scale is used.

    A surface without a "role" is fairly useless: a compositor does not know
    where, when or how to present it. The role is the purpose of a
    :class:`WlSurface`. Examples of roles are a cursor for a pointer (as set by
    :func:`WlPointer.set_cursor()
    <pywayland.protocol.wayland.WlPointer.set_cursor>`), a drag icon
    (:func:`WlDataDevice.start_drag()
    <pywayland.protocol.wayland.WlDataDevice.start_drag>`), a sub-surface
    (:func:`WlSubcompositor.get_subsurface()
    <pywayland.protocol.wayland.WlSubcompositor.get_subsurface>`), and a window
    as defined by a shell protocol (e.g. :func:`WlShell.get_shell_surface()
    <pywayland.protocol.wayland.WlShell.get_shell_surface>`).

    A surface can have only one role at a time. Initially a :class:`WlSurface`
    does not have a role. Once a :class:`WlSurface` is given a role, it is set
    permanently for the whole lifetime of the :class:`WlSurface` object. Giving
    the current role again is allowed, unless explicitly forbidden by the
    relevant interface specification.

    Surface roles are given by requests in other interfaces such as
    :func:`WlPointer.set_cursor()
    <pywayland.protocol.wayland.WlPointer.set_cursor>`. The request should
    explicitly mention that this request gives a role to a :class:`WlSurface`.
    Often, this request also creates a new protocol object that represents the
    role and adds additional functionality to :class:`WlSurface`. When a client
    wants to destroy a :class:`WlSurface`, they must destroy this role object
    before the :class:`WlSurface`, otherwise a defunct_role_object error is
    sent.

    Destroying the role object does not remove the role from the
    :class:`WlSurface`, but it may stop the :class:`WlSurface` from "playing
    the role". For instance, if a
    :class:`~pywayland.protocol.wayland.WlSubsurface` object is destroyed, the
    :class:`WlSurface` it was created for will be unmapped and forget its
    position and z-order. It is allowed to create a
    :class:`~pywayland.protocol.wayland.WlSubsurface` for the same
    :class:`WlSurface` again, but it is not allowed to use the
    :class:`WlSurface` as a cursor (cursor is a different role than sub-
    surface, and role switching is not allowed).
    """

    name = "wl_surface"
    version = 6

    class error(enum.IntEnum):
        invalid_scale = 0
        invalid_transform = 1
        invalid_size = 2
        invalid_offset = 3
        defunct_role_object = 4


class WlSurfaceProxy(Proxy[WlSurface]):
    interface = WlSurface

    @WlSurface.request()
    def destroy(self) -> None:
        """Delete surface

        Deletes the surface and invalidates its object ID.
        """
        self._marshal(0)
        self._destroy()

    @WlSurface.request(
        Argument(ArgumentType.Object, interface=WlBuffer, nullable=True),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def attach(self, buffer: WlBuffer | None, x: int, y: int) -> None:
        """Set the surface contents

        Set a buffer as the content of this surface.

        The new size of the surface is calculated based on the buffer size
        transformed by the inverse buffer_transform and the inverse
        buffer_scale. This means that at commit time the supplied buffer size
        must be an integer multiple of the buffer_scale. If that's not the
        case, an invalid_size error is sent.

        The x and y arguments specify the location of the new pending buffer's
        upper left corner, relative to the current buffer's upper left corner,
        in surface-local coordinates. In other words, the x and y, combined
        with the new surface size define in which directions the surface's size
        changes. Setting anything other than 0 as x and y arguments is
        discouraged, and should instead be replaced with using the separate
        :func:`WlSurface.offset()` request.

        When the bound :class:`WlSurface` version is 5 or higher, passing any
        non-zero x or y is a protocol violation, and will result in an
        'invalid_offset' error being raised. The x and y arguments are ignored
        and do not change the pending state. To achieve equivalent semantics,
        use :func:`WlSurface.offset()`.

        Surface contents are double-buffered state, see
        :func:`WlSurface.commit()`.

        The initial surface contents are void; there is no content.
        :func:`WlSurface.attach()` assigns the given
        :class:`~pywayland.protocol.wayland.WlBuffer` as the pending
        :class:`~pywayland.protocol.wayland.WlBuffer`.
        :func:`WlSurface.commit()` makes the pending
        :class:`~pywayland.protocol.wayland.WlBuffer` the new surface contents,
        and the size of the surface becomes the size calculated from the
        :class:`~pywayland.protocol.wayland.WlBuffer`, as described above.
        After commit, there is no pending buffer until the next attach.

        Committing a pending :class:`~pywayland.protocol.wayland.WlBuffer`
        allows the compositor to read the pixels in the
        :class:`~pywayland.protocol.wayland.WlBuffer`. The compositor may
        access the pixels at any time after the :func:`WlSurface.commit()`
        request. When the compositor will not access the pixels anymore, it
        will send the :func:`WlBuffer.release()
        <pywayland.protocol.wayland.WlBuffer.release>` event. Only after
        receiving :func:`WlBuffer.release()
        <pywayland.protocol.wayland.WlBuffer.release>`, the client may reuse
        the :class:`~pywayland.protocol.wayland.WlBuffer`. A
        :class:`~pywayland.protocol.wayland.WlBuffer` that has been attached
        and then replaced by another attach instead of committed will not
        receive a release event, and is not used by the compositor.

        If a pending :class:`~pywayland.protocol.wayland.WlBuffer` has been
        committed to more than one :class:`WlSurface`, the delivery of
        :func:`WlBuffer.release()
        <pywayland.protocol.wayland.WlBuffer.release>` events becomes
        undefined. A well behaved client should not rely on
        :func:`WlBuffer.release()
        <pywayland.protocol.wayland.WlBuffer.release>` events in this case.
        Alternatively, a client could create multiple
        :class:`~pywayland.protocol.wayland.WlBuffer` objects from the same
        backing storage or use wp_linux_buffer_release.

        Destroying the :class:`~pywayland.protocol.wayland.WlBuffer` after
        :func:`WlBuffer.release()
        <pywayland.protocol.wayland.WlBuffer.release>` does not change the
        surface contents. Destroying the
        :class:`~pywayland.protocol.wayland.WlBuffer` before
        :func:`WlBuffer.release()
        <pywayland.protocol.wayland.WlBuffer.release>` is allowed as long as
        the underlying buffer storage isn't re-used (this can happen e.g. on
        client process termination). However, if the client destroys the
        :class:`~pywayland.protocol.wayland.WlBuffer` before receiving the
        :func:`WlBuffer.release()
        <pywayland.protocol.wayland.WlBuffer.release>` event and mutates the
        underlying buffer storage, the surface contents become undefined
        immediately.

        If :func:`WlSurface.attach()` is sent with a NULL
        :class:`~pywayland.protocol.wayland.WlBuffer`, the following
        :func:`WlSurface.commit()` will remove the surface content.

        :param buffer:
            buffer of surface contents
        :type buffer:
            :class:`~pywayland.protocol.wayland.WlBuffer` or `None`
        :param x:
            surface-local x coordinate
        :type x:
            `ArgumentType.Int`
        :param y:
            surface-local y coordinate
        :type y:
            `ArgumentType.Int`
        """
        self._marshal(1, buffer, x, y)

    @WlSurface.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def damage(self, x: int, y: int, width: int, height: int) -> None:
        """Mark part of the surface damaged

        This request is used to describe the regions where the pending buffer
        is different from the current surface contents, and where the surface
        therefore needs to be repainted. The compositor ignores the parts of
        the damage that fall outside of the surface.

        Damage is double-buffered state, see :func:`WlSurface.commit()`.

        The damage rectangle is specified in surface-local coordinates, where x
        and y specify the upper left corner of the damage rectangle.

        The initial value for pending damage is empty: no damage.
        :func:`WlSurface.damage()` adds pending damage: the new pending damage
        is the union of old pending damage and the given rectangle.

        :func:`WlSurface.commit()` assigns pending damage as the current
        damage, and clears pending damage. The server will clear the current
        damage as it repaints the surface.

        Note! New clients should not use this request. Instead damage can be
        posted with :func:`WlSurface.damage_buffer()` which uses buffer
        coordinates instead of surface coordinates.

        :param x:
            surface-local x coordinate
        :type x:
            `ArgumentType.Int`
        :param y:
            surface-local y coordinate
        :type y:
            `ArgumentType.Int`
        :param width:
            width of damage rectangle
        :type width:
            `ArgumentType.Int`
        :param height:
            height of damage rectangle
        :type height:
            `ArgumentType.Int`
        """
        self._marshal(2, x, y, width, height)

    @WlSurface.request(
        Argument(ArgumentType.NewId, interface=WlCallback),
    )
    def frame(self) -> Proxy[WlCallback]:
        """Request a frame throttling hint

        Request a notification when it is a good time to start drawing a new
        frame, by creating a frame callback. This is useful for throttling
        redrawing operations, and driving animations.

        When a client is animating on a :class:`WlSurface`, it can use the
        'frame' request to get notified when it is a good time to draw and
        commit the next frame of animation. If the client commits an update
        earlier than that, it is likely that some updates will not make it to
        the display, and the client is wasting resources by drawing too often.

        The frame request will take effect on the next
        :func:`WlSurface.commit()`. The notification will only be posted for
        one frame unless requested again. For a :class:`WlSurface`, the
        notifications are posted in the order the frame requests were
        committed.

        The server must send the notifications so that a client will not send
        excessive updates, while still allowing the highest possible update
        rate for clients that wait for the reply before drawing again. The
        server should give some time for the client to draw and commit after
        sending the frame callback events to let it hit the next output
        refresh.

        A server should avoid signaling the frame callbacks if the surface is
        not visible in any way, e.g. the surface is off-screen, or completely
        obscured by other opaque surfaces.

        The object returned by this request will be destroyed by the compositor
        after the callback is fired and as such the client must not attempt to
        use it after that point.

        The callback_data passed in the callback is the current time, in
        milliseconds, with an undefined base.

        :returns:
            :class:`~pywayland.protocol.wayland.WlCallback` -- callback object
            for the frame request
        """
        callback = self._marshal_constructor(3, WlCallback)
        return callback

    @WlSurface.request(
        Argument(ArgumentType.Object, interface=WlRegion, nullable=True),
    )
    def set_opaque_region(self, region: WlRegion | None) -> None:
        """Set opaque region

        This request sets the region of the surface that contains opaque
        content.

        The opaque region is an optimization hint for the compositor that lets
        it optimize the redrawing of content behind opaque regions.  Setting an
        opaque region is not required for correct behaviour, but marking
        transparent content as opaque will result in repaint artifacts.

        The opaque region is specified in surface-local coordinates.

        The compositor ignores the parts of the opaque region that fall outside
        of the surface.

        Opaque region is double-buffered state, see :func:`WlSurface.commit()`.

        :func:`WlSurface.set_opaque_region()` changes the pending opaque
        region. :func:`WlSurface.commit()` copies the pending region to the
        current region. Otherwise, the pending and current regions are never
        changed.

        The initial value for an opaque region is empty. Setting the pending
        opaque region has copy semantics, and the
        :class:`~pywayland.protocol.wayland.WlRegion` object can be destroyed
        immediately. A NULL :class:`~pywayland.protocol.wayland.WlRegion`
        causes the pending opaque region to be set to empty.

        :param region:
            opaque region of the surface
        :type region:
            :class:`~pywayland.protocol.wayland.WlRegion` or `None`
        """
        self._marshal(4, region)

    @WlSurface.request(
        Argument(ArgumentType.Object, interface=WlRegion, nullable=True),
    )
    def set_input_region(self, region: WlRegion | None) -> None:
        """Set input region

        This request sets the region of the surface that can receive pointer
        and touch events.

        Input events happening outside of this region will try the next surface
        in the server surface stack. The compositor ignores the parts of the
        input region that fall outside of the surface.

        The input region is specified in surface-local coordinates.

        Input region is double-buffered state, see :func:`WlSurface.commit()`.

        :func:`WlSurface.set_input_region()` changes the pending input region.
        :func:`WlSurface.commit()` copies the pending region to the current
        region. Otherwise the pending and current regions are never changed,
        except cursor and icon surfaces are special cases, see
        :func:`WlPointer.set_cursor()
        <pywayland.protocol.wayland.WlPointer.set_cursor>` and
        :func:`WlDataDevice.start_drag()
        <pywayland.protocol.wayland.WlDataDevice.start_drag>`.

        The initial value for an input region is infinite. That means the whole
        surface will accept input. Setting the pending input region has copy
        semantics, and the :class:`~pywayland.protocol.wayland.WlRegion` object
        can be destroyed immediately. A NULL
        :class:`~pywayland.protocol.wayland.WlRegion` causes the input region
        to be set to infinite.

        :param region:
            input region of the surface
        :type region:
            :class:`~pywayland.protocol.wayland.WlRegion` or `None`
        """
        self._marshal(5, region)

    @WlSurface.request()
    def commit(self) -> None:
        """Commit pending surface state

        Surface state (input, opaque, and damage regions, attached buffers,
        etc.) is double-buffered. Protocol requests modify the pending state,
        as opposed to the current state in use by the compositor. A commit
        request atomically applies all pending state, replacing the current
        state. After commit, the new pending state is as documented for each
        related request.

        On commit, a pending :class:`~pywayland.protocol.wayland.WlBuffer` is
        applied first, and all other state second. This means that all
        coordinates in double-buffered state are relative to the new
        :class:`~pywayland.protocol.wayland.WlBuffer` coming into use, except
        for :func:`WlSurface.attach()` itself. If there is no pending
        :class:`~pywayland.protocol.wayland.WlBuffer`, the coordinates are
        relative to the current surface contents.

        All requests that need a commit to become effective are documented to
        affect double-buffered state.

        Other interfaces may add further double-buffered surface state.
        """
        self._marshal(6)

    @WlSurface.request(
        Argument(ArgumentType.Int),
        version=2,
    )
    def set_buffer_transform(self, transform: int) -> None:
        """Sets the buffer transformation

        This request sets an optional transformation on how the compositor
        interprets the contents of the buffer attached to the surface. The
        accepted values for the transform parameter are the values for
        :func:`WlOutput.transform()
        <pywayland.protocol.wayland.WlOutput.transform>`.

        Buffer transform is double-buffered state, see
        :func:`WlSurface.commit()`.

        A newly created surface has its buffer transformation set to normal.

        :func:`WlSurface.set_buffer_transform()` changes the pending buffer
        transformation. :func:`WlSurface.commit()` copies the pending buffer
        transformation to the current one. Otherwise, the pending and current
        values are never changed.

        The purpose of this request is to allow clients to render content
        according to the output transform, thus permitting the compositor to
        use certain optimizations even if the display is rotated. Using
        hardware overlays and scanning out a client buffer for fullscreen
        surfaces are examples of such optimizations. Those optimizations are
        highly dependent on the compositor implementation, so the use of this
        request should be considered on a case-by-case basis.

        Note that if the transform value includes 90 or 270 degree rotation,
        the width of the buffer will become the surface height and the height
        of the buffer will become the surface width.

        If transform is not one of the values from the
        :func:`WlOutput.transform()
        <pywayland.protocol.wayland.WlOutput.transform>` enum the
        invalid_transform protocol error is raised.

        :param transform:
            transform for interpreting buffer contents
        :type transform:
            `ArgumentType.Int`
        """
        self._marshal(7, transform)

    @WlSurface.request(
        Argument(ArgumentType.Int),
        version=3,
    )
    def set_buffer_scale(self, scale: int) -> None:
        """Sets the buffer scaling factor

        This request sets an optional scaling factor on how the compositor
        interprets the contents of the buffer attached to the window.

        Buffer scale is double-buffered state, see :func:`WlSurface.commit()`.

        A newly created surface has its buffer scale set to 1.

        :func:`WlSurface.set_buffer_scale()` changes the pending buffer scale.
        :func:`WlSurface.commit()` copies the pending buffer scale to the
        current one. Otherwise, the pending and current values are never
        changed.

        The purpose of this request is to allow clients to supply higher
        resolution buffer data for use on high resolution outputs. It is
        intended that you pick the same buffer scale as the scale of the output
        that the surface is displayed on. This means the compositor can avoid
        scaling when rendering the surface on that output.

        Note that if the scale is larger than 1, then you have to attach a
        buffer that is larger (by a factor of scale in each dimension) than the
        desired surface size.

        If scale is not positive the invalid_scale protocol error is raised.

        :param scale:
            positive scale for interpreting buffer contents
        :type scale:
            `ArgumentType.Int`
        """
        self._marshal(8, scale)

    @WlSurface.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        version=4,
    )
    def damage_buffer(self, x: int, y: int, width: int, height: int) -> None:
        """Mark part of the surface damaged using buffer coordinates

        This request is used to describe the regions where the pending buffer
        is different from the current surface contents, and where the surface
        therefore needs to be repainted. The compositor ignores the parts of
        the damage that fall outside of the surface.

        Damage is double-buffered state, see :func:`WlSurface.commit()`.

        The damage rectangle is specified in buffer coordinates, where x and y
        specify the upper left corner of the damage rectangle.

        The initial value for pending damage is empty: no damage.
        :func:`WlSurface.damage_buffer()` adds pending damage: the new pending
        damage is the union of old pending damage and the given rectangle.

        :func:`WlSurface.commit()` assigns pending damage as the current
        damage, and clears pending damage. The server will clear the current
        damage as it repaints the surface.

        This request differs from :func:`WlSurface.damage()` in only one way -
        it takes damage in buffer coordinates instead of surface-local
        coordinates. While this generally is more intuitive than surface
        coordinates, it is especially desirable when using
        :class:`~pywayland.protocol.viewporter.WpViewport` or when a drawing
        library (like EGL) is unaware of buffer scale and buffer transform.

        Note: Because buffer transformation changes and damage requests may be
        interleaved in the protocol stream, it is impossible to determine the
        actual mapping between surface and buffer damage until
        :func:`WlSurface.commit()` time. Therefore, compositors wishing to take
        both kinds of damage into account will have to accumulate damage from
        the two requests separately and only transform from one to the other
        after receiving the :func:`WlSurface.commit()`.

        :param x:
            buffer-local x coordinate
        :type x:
            `ArgumentType.Int`
        :param y:
            buffer-local y coordinate
        :type y:
            `ArgumentType.Int`
        :param width:
            width of damage rectangle
        :type width:
            `ArgumentType.Int`
        :param height:
            height of damage rectangle
        :type height:
            `ArgumentType.Int`
        """
        self._marshal(9, x, y, width, height)

    @WlSurface.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        version=5,
    )
    def offset(self, x: int, y: int) -> None:
        """Set the surface contents offset

        The x and y arguments specify the location of the new pending buffer's
        upper left corner, relative to the current buffer's upper left corner,
        in surface-local coordinates. In other words, the x and y, combined
        with the new surface size define in which directions the surface's size
        changes.

        Surface location offset is double-buffered state, see
        :func:`WlSurface.commit()`.

        This request is semantically equivalent to and the replaces the x and y
        arguments in the :func:`WlSurface.attach()` request in
        :class:`WlSurface` versions prior to 5. See :func:`WlSurface.attach()`
        for details.

        :param x:
            surface-local x coordinate
        :type x:
            `ArgumentType.Int`
        :param y:
            surface-local y coordinate
        :type y:
            `ArgumentType.Int`
        """
        self._marshal(10, x, y)


class WlSurfaceResource(Resource):
    interface = WlSurface

    @WlSurface.event(
        Argument(ArgumentType.Object, interface=WlOutput),
    )
    def enter(self, output: WlOutput) -> None:
        """Surface enters an output

        This is emitted whenever a surface's creation, movement, or resizing
        results in some part of it being within the scanout region of an
        output.

        Note that a surface may be overlapping with zero or more outputs.

        :param output:
            output entered by the surface
        :type output:
            :class:`~pywayland.protocol.wayland.WlOutput`
        """
        self._post_event(0, output)

    @WlSurface.event(
        Argument(ArgumentType.Object, interface=WlOutput),
    )
    def leave(self, output: WlOutput) -> None:
        """Surface leaves an output

        This is emitted whenever a surface's creation, movement, or resizing
        results in it no longer having any part of it within the scanout region
        of an output.

        Clients should not use the number of outputs the surface is on for
        frame throttling purposes. The surface might be hidden even if no leave
        event has been sent, and the compositor might expect new surface
        content updates even if no enter event has been sent. The frame event
        should be used instead.

        :param output:
            output left by the surface
        :type output:
            :class:`~pywayland.protocol.wayland.WlOutput`
        """
        self._post_event(1, output)

    @WlSurface.event(
        Argument(ArgumentType.Int),
        version=6,
    )
    def preferred_buffer_scale(self, factor: int) -> None:
        """Preferred buffer scale for the surface

        This event indicates the preferred buffer scale for this surface. It is
        sent whenever the compositor's preference changes.

        It is intended that scaling aware clients use this event to scale their
        content and use :func:`WlSurface.set_buffer_scale()` to indicate the
        scale they have rendered with. This allows clients to supply a higher
        detail buffer.

        :param factor:
            preferred scaling factor
        :type factor:
            `ArgumentType.Int`
        """
        self._post_event(2, factor)

    @WlSurface.event(
        Argument(ArgumentType.Uint),
        version=6,
    )
    def preferred_buffer_transform(self, transform: int) -> None:
        """Preferred buffer transform for the surface

        This event indicates the preferred buffer transform for this surface.
        It is sent whenever the compositor's preference changes.

        It is intended that transform aware clients use this event to apply the
        transform to their content and use
        :func:`WlSurface.set_buffer_transform()` to indicate the transform they
        have rendered with.

        :param transform:
            preferred transform
        :type transform:
            `ArgumentType.Uint`
        """
        self._post_event(3, transform)


class WlSurfaceGlobal(Global):
    interface = WlSurface


WlSurface._gen_c()
WlSurface.proxy_class = WlSurfaceProxy
WlSurface.resource_class = WlSurfaceResource
WlSurface.global_class = WlSurfaceGlobal
