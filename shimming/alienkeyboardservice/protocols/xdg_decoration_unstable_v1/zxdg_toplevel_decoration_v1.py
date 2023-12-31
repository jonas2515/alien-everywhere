# This file has been autogenerated by the pywayland scanner

# Copyright © 2018 Simon Ser
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


class ZxdgToplevelDecorationV1(Interface):
    """Decoration object for a toplevel surface

    The decoration object allows the compositor to toggle server-side window
    decorations for a toplevel surface. The client can request to switch to
    another mode.

    The xdg_toplevel_decoration object must be destroyed before its
    :class:`~pywayland.protocol.xdg_shell.XdgToplevel`.
    """

    name = "zxdg_toplevel_decoration_v1"
    version = 1

    class error(enum.IntEnum):
        unconfigured_buffer = 0
        already_constructed = 1
        orphaned = 2

    class mode(enum.IntEnum):
        client_side = 1
        server_side = 2


class ZxdgToplevelDecorationV1Proxy(Proxy[ZxdgToplevelDecorationV1]):
    interface = ZxdgToplevelDecorationV1

    @ZxdgToplevelDecorationV1.request()
    def destroy(self) -> None:
        """Destroy the decoration object

        Switch back to a mode without any server-side decorations at the next
        commit.
        """
        self._marshal(0)
        self._destroy()

    @ZxdgToplevelDecorationV1.request(
        Argument(ArgumentType.Uint),
    )
    def set_mode(self, mode: int) -> None:
        """Set the decoration mode

        Set the toplevel surface decoration mode. This informs the compositor
        that the client prefers the provided decoration mode.

        After requesting a decoration mode, the compositor will respond by
        emitting an :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` event. The client
        should then update its content, drawing it without decorations if the
        received mode is server-side decorations. The client must also
        acknowledge the configure when committing the new content (see
        :func:`XdgSurface.ack_configure()
        <pywayland.protocol.xdg_shell.XdgSurface.ack_configure>`).

        The compositor can decide not to use the client's mode and enforce a
        different mode instead.

        Clients whose decoration mode depend on the
        :class:`~pywayland.protocol.xdg_shell.XdgToplevel` state may send a
        set_mode request in response to an :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` event and wait for
        the next :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` event to prevent
        unwanted state. Such clients are responsible for preventing configure
        loops and must make sure not to send multiple successive set_mode
        requests with the same decoration mode.

        :param mode:
            the decoration mode
        :type mode:
            `ArgumentType.Uint`
        """
        self._marshal(1, mode)

    @ZxdgToplevelDecorationV1.request()
    def unset_mode(self) -> None:
        """Unset the decoration mode

        Unset the toplevel surface decoration mode. This informs the compositor
        that the client doesn't prefer a particular decoration mode.

        This request has the same semantics as set_mode.
        """
        self._marshal(2)


class ZxdgToplevelDecorationV1Resource(Resource):
    interface = ZxdgToplevelDecorationV1

    @ZxdgToplevelDecorationV1.event(
        Argument(ArgumentType.Uint),
    )
    def configure(self, mode: int) -> None:
        """Suggest a surface change

        The configure event asks the client to change its decoration mode. The
        configured state should not be applied immediately. Clients must send
        an ack_configure in response to this event. See
        :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` and
        :func:`XdgSurface.ack_configure()
        <pywayland.protocol.xdg_shell.XdgSurface.ack_configure>` for details.

        A configure event can be sent at any time. The specified mode must be
        obeyed by the client.

        :param mode:
            the decoration mode
        :type mode:
            `ArgumentType.Uint`
        """
        self._post_event(0, mode)


class ZxdgToplevelDecorationV1Global(Global):
    interface = ZxdgToplevelDecorationV1


ZxdgToplevelDecorationV1._gen_c()
ZxdgToplevelDecorationV1.proxy_class = ZxdgToplevelDecorationV1Proxy
ZxdgToplevelDecorationV1.resource_class = ZxdgToplevelDecorationV1Resource
ZxdgToplevelDecorationV1.global_class = ZxdgToplevelDecorationV1Global
