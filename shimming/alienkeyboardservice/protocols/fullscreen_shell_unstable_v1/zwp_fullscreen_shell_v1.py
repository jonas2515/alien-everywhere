# This file has been autogenerated by the pywayland scanner

# Copyright © 2016 Yong Bakos
# Copyright © 2015 Jason Ekstrand
# Copyright © 2015 Jonas Ådahl
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
from ..wayland import WlOutput
from ..wayland import WlSurface
from .zwp_fullscreen_shell_mode_feedback_v1 import ZwpFullscreenShellModeFeedbackV1


class ZwpFullscreenShellV1(Interface):
    """Displays a single surface per output

    Displays a single surface per output.

    This interface provides a mechanism for a single client to display simple
    full-screen surfaces.  While there technically may be multiple clients
    bound to this interface, only one of those clients should be shown at a
    time.

    To present a surface, the client uses either the present_surface or
    present_surface_for_mode requests.  Presenting a surface takes effect on
    the next :func:`WlSurface.commit()
    <pywayland.protocol.wayland.WlSurface.commit>`.  See the individual
    requests for details about scaling and mode switches.

    The client can have at most one surface per output at any time. Requesting
    a surface to be presented on an output that already has a surface replaces
    the previously presented surface.  Presenting a null surface removes its
    content and effectively disables the output. Exactly what happens when an
    output is "disabled" is compositor-specific.  The same surface may be
    presented on multiple outputs simultaneously.

    Once a surface is presented on an output, it stays on that output until
    either the client removes it or the compositor destroys the output.  This
    way, the client can update the output's contents by simply attaching a new
    buffer.

    Warning! The protocol described in this file is experimental and backward
    incompatible changes may be made. Backward compatible changes may be added
    together with the corresponding interface version bump. Backward
    incompatible changes are done by bumping the version number in the protocol
    and interface names and resetting the interface version. Once the protocol
    is to be declared stable, the 'z' prefix and the version number in the
    protocol and interface names are removed and the interface version number
    is reset.
    """

    name = "zwp_fullscreen_shell_v1"
    version = 1

    class capability(enum.IntEnum):
        arbitrary_modes = 1
        cursor_plane = 2

    class present_method(enum.IntEnum):
        default = 0
        center = 1
        zoom = 2
        zoom_crop = 3
        stretch = 4

    class error(enum.IntEnum):
        invalid_method = 0
        role = 1


class ZwpFullscreenShellV1Proxy(Proxy[ZwpFullscreenShellV1]):
    interface = ZwpFullscreenShellV1

    @ZwpFullscreenShellV1.request()
    def release(self) -> None:
        """Release the wl_fullscreen_shell interface

        Release the binding from the wl_fullscreen_shell interface.

        This destroys the server-side object and frees this binding.  If the
        client binds to wl_fullscreen_shell multiple times, it may wish to free
        some of those bindings.
        """
        self._marshal(0)
        self._destroy()

    @ZwpFullscreenShellV1.request(
        Argument(ArgumentType.Object, interface=WlSurface, nullable=True),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Object, interface=WlOutput, nullable=True),
    )
    def present_surface(self, surface: WlSurface | None, method: int, output: WlOutput | None) -> None:
        """Present surface for display

        Present a surface on the given output.

        If the output is null, the compositor will present the surface on
        whatever display (or displays) it thinks best.  In particular, this may
        replace any or all surfaces currently presented so it should not be
        used in combination with placing surfaces on specific outputs.

        The method parameter is a hint to the compositor for how the surface is
        to be presented.  In particular, it tells the compositor how to handle
        a size mismatch between the presented surface and the output.  The
        compositor is free to ignore this parameter.

        The "zoom", "zoom_crop", and "stretch" methods imply a scaling
        operation on the surface.  This will override any kind of output
        scaling, so the buffer_scale property of the surface is effectively
        ignored.

        This request gives the surface the role of a fullscreen shell surface.
        If the surface already has another role, it raises a role protocol
        error.

        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface` or `None`
        :param method:
        :type method:
            `ArgumentType.Uint`
        :param output:
        :type output:
            :class:`~pywayland.protocol.wayland.WlOutput` or `None`
        """
        self._marshal(1, surface, method, output)

    @ZwpFullscreenShellV1.request(
        Argument(ArgumentType.Object, interface=WlSurface),
        Argument(ArgumentType.Object, interface=WlOutput),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.NewId, interface=ZwpFullscreenShellModeFeedbackV1),
    )
    def present_surface_for_mode(self, surface: WlSurface, output: WlOutput, framerate: int) -> Proxy[ZwpFullscreenShellModeFeedbackV1]:
        """Present surface for display at a particular mode

        Presents a surface on the given output for a particular mode.

        If the current size of the output differs from that of the surface, the
        compositor will attempt to change the size of the output to match the
        surface.  The result of the mode-switch operation will be returned via
        the provided wl_fullscreen_shell_mode_feedback object.

        If the current output mode matches the one requested or if the
        compositor successfully switches the mode to match the surface, then
        the mode_successful event will be sent and the output will contain the
        contents of the given surface.  If the compositor cannot match the
        output size to the surface size, the mode_failed will be sent and the
        output will contain the contents of the previously presented surface
        (if any).  If another surface is presented on the given output before
        either of these has a chance to happen, the present_cancelled event
        will be sent.

        Due to race conditions and other issues unknown to the client, no mode-
        switch operation is guaranteed to succeed.  However, if the mode is one
        advertised by :func:`WlOutput.mode()
        <pywayland.protocol.wayland.WlOutput.mode>` or if the compositor
        advertises the ARBITRARY_MODES capability, then the client should
        expect that the mode-switch operation will usually succeed.

        If the size of the presented surface changes, the resulting output is
        undefined.  The compositor may attempt to change the output mode to
        compensate.  However, there is no guarantee that a suitable mode will
        be found and the client has no way to be notified of success or
        failure.

        The framerate parameter specifies the desired framerate for the output
        in mHz.  The compositor is free to ignore this parameter.  A value of 0
        indicates that the client has no preference.

        If the value of :func:`WlOutput.scale()
        <pywayland.protocol.wayland.WlOutput.scale>` differs from
        :func:`WlSurface.buffer_scale()
        <pywayland.protocol.wayland.WlSurface.buffer_scale>`, then the
        compositor may choose a mode that matches either the buffer size or the
        surface size.  In either case, the surface will fill the output.

        This request gives the surface the role of a fullscreen shell surface.
        If the surface already has another role, it raises a role protocol
        error.

        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :param output:
        :type output:
            :class:`~pywayland.protocol.wayland.WlOutput`
        :param framerate:
        :type framerate:
            `ArgumentType.Int`
        :returns:
            :class:`~pywayland.protocol.fullscreen_shell_unstable_v1.ZwpFullscreenShellModeFeedbackV1`
        """
        feedback = self._marshal_constructor(2, ZwpFullscreenShellModeFeedbackV1, surface, output, framerate)
        return feedback


class ZwpFullscreenShellV1Resource(Resource):
    interface = ZwpFullscreenShellV1

    @ZwpFullscreenShellV1.event(
        Argument(ArgumentType.Uint),
    )
    def capability(self, capability: int) -> None:
        """Advertises a capability of the compositor

        Advertises a single capability of the compositor.

        When the wl_fullscreen_shell interface is bound, this event is emitted
        once for each capability advertised.  Valid capabilities are given by
        the wl_fullscreen_shell.capability enum.  If clients want to take
        advantage of any of these capabilities, they should use a
        :func:`WlDisplay.sync() <pywayland.protocol.wayland.WlDisplay.sync>`
        request immediately after binding to ensure that they receive all the
        capability events.

        :param capability:
        :type capability:
            `ArgumentType.Uint`
        """
        self._post_event(0, capability)


class ZwpFullscreenShellV1Global(Global):
    interface = ZwpFullscreenShellV1


ZwpFullscreenShellV1._gen_c()
ZwpFullscreenShellV1.proxy_class = ZwpFullscreenShellV1Proxy
ZwpFullscreenShellV1.resource_class = ZwpFullscreenShellV1Resource
ZwpFullscreenShellV1.global_class = ZwpFullscreenShellV1Global
