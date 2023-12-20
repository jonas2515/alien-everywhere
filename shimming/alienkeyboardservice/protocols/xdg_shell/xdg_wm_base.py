# This file has been autogenerated by the pywayland scanner

# Copyright © 2008-2013 Kristian Høgsberg
# Copyright © 2013      Rafael Antognolli
# Copyright © 2013      Jasper St. Pierre
# Copyright © 2010-2013 Intel Corporation
# Copyright © 2015-2017 Samsung Electronics Co., Ltd
# Copyright © 2015-2017 Red Hat Inc.
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
from .xdg_positioner import XdgPositioner
from .xdg_surface import XdgSurface


class XdgWmBase(Interface):
    """Create desktop-style surfaces

    The :class:`XdgWmBase` interface is exposed as a global object enabling
    clients to turn their wl_surfaces into windows in a desktop environment. It
    defines the basic functionality needed for clients and the compositor to
    create windows that can be dragged, resized, maximized, etc, as well as
    creating transient windows such as popup menus.
    """

    name = "xdg_wm_base"
    version = 5

    class error(enum.IntEnum):
        role = 0
        defunct_surfaces = 1
        not_the_topmost_popup = 2
        invalid_popup_parent = 3
        invalid_surface_state = 4
        invalid_positioner = 5
        unresponsive = 6


class XdgWmBaseProxy(Proxy[XdgWmBase]):
    interface = XdgWmBase

    @XdgWmBase.request()
    def destroy(self) -> None:
        """Destroy :class:`XdgWmBase`

        Destroy this :class:`XdgWmBase` object.

        Destroying a bound :class:`XdgWmBase` object while there are surfaces
        still alive created by this :class:`XdgWmBase` object instance is
        illegal and will result in a defunct_surfaces error.
        """
        self._marshal(0)
        self._destroy()

    @XdgWmBase.request(
        Argument(ArgumentType.NewId, interface=XdgPositioner),
    )
    def create_positioner(self) -> Proxy[XdgPositioner]:
        """Create a positioner object

        Create a positioner object. A positioner object is used to position
        surfaces relative to some parent surface. See the interface description
        and :func:`XdgSurface.get_popup()
        <pywayland.protocol.xdg_shell.XdgSurface.get_popup>` for details.

        :returns:
            :class:`~pywayland.protocol.xdg_shell.XdgPositioner`
        """
        id = self._marshal_constructor(1, XdgPositioner)
        return id

    @XdgWmBase.request(
        Argument(ArgumentType.NewId, interface=XdgSurface),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def get_xdg_surface(self, surface: WlSurface) -> Proxy[XdgSurface]:
        """Create a shell surface from a surface

        This creates an :class:`~pywayland.protocol.xdg_shell.XdgSurface` for
        the given surface. While
        :class:`~pywayland.protocol.xdg_shell.XdgSurface` itself is not a role,
        the corresponding surface may only be assigned a role extending
        :class:`~pywayland.protocol.xdg_shell.XdgSurface`, such as
        :class:`~pywayland.protocol.xdg_shell.XdgToplevel` or
        :class:`~pywayland.protocol.xdg_shell.XdgPopup`. It is illegal to
        create an :class:`~pywayland.protocol.xdg_shell.XdgSurface` for a
        :class:`~pywayland.protocol.wayland.WlSurface` which already has an
        assigned role and this will result in a role error.

        This creates an :class:`~pywayland.protocol.xdg_shell.XdgSurface` for
        the given surface. An :class:`~pywayland.protocol.xdg_shell.XdgSurface`
        is used as basis to define a role to a given surface, such as
        :class:`~pywayland.protocol.xdg_shell.XdgToplevel` or
        :class:`~pywayland.protocol.xdg_shell.XdgPopup`. It also manages
        functionality shared between
        :class:`~pywayland.protocol.xdg_shell.XdgSurface` based surface roles.

        See the documentation of
        :class:`~pywayland.protocol.xdg_shell.XdgSurface` for more details
        about what an :class:`~pywayland.protocol.xdg_shell.XdgSurface` is and
        how it is used.

        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :returns:
            :class:`~pywayland.protocol.xdg_shell.XdgSurface`
        """
        id = self._marshal_constructor(2, XdgSurface, surface)
        return id

    @XdgWmBase.request(
        Argument(ArgumentType.Uint),
    )
    def pong(self, serial: int) -> None:
        """Respond to a ping event

        A client must respond to a ping event with a pong request or the client
        may be deemed unresponsive. See :func:`XdgWmBase.ping()` and
        :func:`XdgWmBase.error()`.unresponsive.

        :param serial:
            serial of the ping event
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(3, serial)


class XdgWmBaseResource(Resource):
    interface = XdgWmBase

    @XdgWmBase.event(
        Argument(ArgumentType.Uint),
    )
    def ping(self, serial: int) -> None:
        """Check if the client is alive

        The ping event asks the client if it's still alive. Pass the serial
        specified in the event back to the compositor by sending a "pong"
        request back with the specified serial. See :func:`XdgWmBase.pong()`.

        Compositors can use this to determine if the client is still alive.
        It's unspecified what will happen if the client doesn't respond to the
        ping request, or in what timeframe. Clients should try to respond in a
        reasonable amount of time. The “unresponsive” error is provided for
        compositors that wish to disconnect unresponsive clients.

        A compositor is free to ping in any way it wants, but a client must
        always respond to any :class:`XdgWmBase` object it created.

        :param serial:
            pass this to the pong request
        :type serial:
            `ArgumentType.Uint`
        """
        self._post_event(0, serial)


class XdgWmBaseGlobal(Global):
    interface = XdgWmBase


XdgWmBase._gen_c()
XdgWmBase.proxy_class = XdgWmBaseProxy
XdgWmBase.resource_class = XdgWmBaseResource
XdgWmBase.global_class = XdgWmBaseGlobal
