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
from ..wayland import WlSeat
from .xdg_positioner import XdgPositioner


class XdgPopup(Interface):
    """Short-lived, popup surfaces for menus

    A popup surface is a short-lived, temporary surface. It can be used to
    implement for example menus, popovers, tooltips and other similar user
    interface concepts.

    A popup can be made to take an explicit grab. See :func:`XdgPopup.grab()`
    for details.

    When the popup is dismissed, a popup_done event will be sent out, and at
    the same time the surface will be unmapped. See the
    :func:`XdgPopup.popup_done()` event for details.

    Explicitly destroying the :class:`XdgPopup` object will also dismiss the
    popup and unmap the surface. Clients that want to dismiss the popup when
    another surface of their own is clicked should dismiss the popup using the
    destroy request.

    A newly created :class:`XdgPopup` will be stacked on top of all previously
    created :class:`XdgPopup` surfaces associated with the same
    :class:`~pywayland.protocol.xdg_shell.XdgToplevel`.

    The parent of an :class:`XdgPopup` must be mapped (see the
    :class:`~pywayland.protocol.xdg_shell.XdgSurface` description) before the
    :class:`XdgPopup` itself.

    The client must call :func:`WlSurface.commit()
    <pywayland.protocol.wayland.WlSurface.commit>` on the corresponding
    :class:`~pywayland.protocol.wayland.WlSurface` for the :class:`XdgPopup`
    state to take effect.
    """

    name = "xdg_popup"
    version = 5

    class error(enum.IntEnum):
        invalid_grab = 0


class XdgPopupProxy(Proxy[XdgPopup]):
    interface = XdgPopup

    @XdgPopup.request()
    def destroy(self) -> None:
        """Remove :class:`XdgPopup` interface

        This destroys the popup. Explicitly destroying the :class:`XdgPopup`
        object will also dismiss the popup, and unmap the surface.

        If this :class:`XdgPopup` is not the "topmost" popup, the
        :func:`XdgWmBase.not_the_topmost_popup()
        <pywayland.protocol.xdg_shell.XdgWmBase.not_the_topmost_popup>`
        protocol error will be sent.
        """
        self._marshal(0)
        self._destroy()

    @XdgPopup.request(
        Argument(ArgumentType.Object, interface=WlSeat),
        Argument(ArgumentType.Uint),
    )
    def grab(self, seat: WlSeat, serial: int) -> None:
        """Make the popup take an explicit grab

        This request makes the created popup take an explicit grab. An explicit
        grab will be dismissed when the user dismisses the popup, or when the
        client destroys the :class:`XdgPopup`. This can be done by the user
        clicking outside the surface, using the keyboard, or even locking the
        screen through closing the lid or a timeout.

        If the compositor denies the grab, the popup will be immediately
        dismissed.

        This request must be used in response to some sort of user action like
        a button press, key press, or touch down event. The serial number of
        the event should be passed as 'serial'.

        The parent of a grabbing popup must either be an
        :class:`~pywayland.protocol.xdg_shell.XdgToplevel` surface or another
        :class:`XdgPopup` with an explicit grab. If the parent is another
        :class:`XdgPopup` it means that the popups are nested, with this popup
        now being the topmost popup.

        Nested popups must be destroyed in the reverse order they were created
        in, e.g. the only popup you are allowed to destroy at all times is the
        topmost one.

        When compositors choose to dismiss a popup, they may dismiss every
        nested grabbing popup as well. When a compositor dismisses popups, it
        will follow the same dismissing order as required from the client.

        If the topmost grabbing popup is destroyed, the grab will be returned
        to the parent of the popup, if that parent previously had an explicit
        grab.

        If the parent is a grabbing popup which has already been dismissed,
        this popup will be immediately dismissed. If the parent is a popup that
        did not take an explicit grab, an error will be raised.

        During a popup grab, the client owning the grab will receive pointer
        and touch events for all their surfaces as normal (similar to an
        "owner-events" grab in X11 parlance), while the top most grabbing popup
        will always have keyboard focus.

        :param seat:
            the :class:`~pywayland.protocol.wayland.WlSeat` of the user event
        :type seat:
            :class:`~pywayland.protocol.wayland.WlSeat`
        :param serial:
            the serial of the user event
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(1, seat, serial)

    @XdgPopup.request(
        Argument(ArgumentType.Object, interface=XdgPositioner),
        Argument(ArgumentType.Uint),
        version=3,
    )
    def reposition(self, positioner: XdgPositioner, token: int) -> None:
        """Recalculate the popup's location

        Reposition an already-mapped popup. The popup will be placed given the
        details in the passed
        :class:`~pywayland.protocol.xdg_shell.XdgPositioner` object, and a
        :func:`XdgPopup.repositioned()` followed by
        :func:`XdgPopup.configure()` and :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` will be emitted in
        response. Any parameters set by the previous positioner will be
        discarded.

        The passed token will be sent in the corresponding
        :func:`XdgPopup.repositioned()` event. The new popup position will not
        take effect until the corresponding configure event is acknowledged by
        the client. See :func:`XdgPopup.repositioned()` for details. The token
        itself is opaque, and has no other special meaning.

        If multiple reposition requests are sent, the compositor may skip all
        but the last one.

        If the popup is repositioned in response to a configure event for its
        parent, the client should send an
        :func:`XdgPositioner.set_parent_configure()
        <pywayland.protocol.xdg_shell.XdgPositioner.set_parent_configure>` and
        possibly an :func:`XdgPositioner.set_parent_size()
        <pywayland.protocol.xdg_shell.XdgPositioner.set_parent_size>` request
        to allow the compositor to properly constrain the popup.

        If the popup is repositioned together with a parent that is being
        resized, but not in response to a configure event, the client should
        send an :func:`XdgPositioner.set_parent_size()
        <pywayland.protocol.xdg_shell.XdgPositioner.set_parent_size>` request.

        :param positioner:
        :type positioner:
            :class:`~pywayland.protocol.xdg_shell.XdgPositioner`
        :param token:
            reposition request token
        :type token:
            `ArgumentType.Uint`
        """
        self._marshal(2, positioner, token)


class XdgPopupResource(Resource):
    interface = XdgPopup

    @XdgPopup.event(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def configure(self, x: int, y: int, width: int, height: int) -> None:
        """Configure the popup surface

        This event asks the popup surface to configure itself given the
        configuration. The configured state should not be applied immediately.
        See :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` for details.

        The x and y arguments represent the position the popup was placed at
        given the :class:`~pywayland.protocol.xdg_shell.XdgPositioner` rule,
        relative to the upper left corner of the window geometry of the parent
        surface.

        For version 2 or older, the configure event for an :class:`XdgPopup` is
        only ever sent once for the initial configuration. Starting with
        version 3, it may be sent again if the popup is setup with an
        :class:`~pywayland.protocol.xdg_shell.XdgPositioner` with set_reactive
        requested, or in response to :func:`XdgPopup.reposition()` requests.

        :param x:
            x position relative to parent surface window geometry
        :type x:
            `ArgumentType.Int`
        :param y:
            y position relative to parent surface window geometry
        :type y:
            `ArgumentType.Int`
        :param width:
            window geometry width
        :type width:
            `ArgumentType.Int`
        :param height:
            window geometry height
        :type height:
            `ArgumentType.Int`
        """
        self._post_event(0, x, y, width, height)

    @XdgPopup.event()
    def popup_done(self) -> None:
        """Popup interaction is done

        The popup_done event is sent out when a popup is dismissed by the
        compositor. The client should destroy the :class:`XdgPopup` object at
        this point.
        """
        self._post_event(1)

    @XdgPopup.event(
        Argument(ArgumentType.Uint),
        version=3,
    )
    def repositioned(self, token: int) -> None:
        """Signal the completion of a repositioned request

        The repositioned event is sent as part of a popup configuration
        sequence, together with :func:`XdgPopup.configure()` and lastly
        :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` to notify the
        completion of a reposition request.

        The repositioned event is to notify about the completion of a
        :func:`XdgPopup.reposition()` request. The token argument is the token
        passed in the :func:`XdgPopup.reposition()` request.

        Immediately after this event is emitted, :func:`XdgPopup.configure()`
        and :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` will be sent with
        the updated size and position, as well as a new configure serial.

        The client should optionally update the content of the popup, but must
        acknowledge the new popup configuration for the new position to take
        effect. See :func:`XdgSurface.ack_configure()
        <pywayland.protocol.xdg_shell.XdgSurface.ack_configure>` for details.

        :param token:
            reposition request token
        :type token:
            `ArgumentType.Uint`
        """
        self._post_event(2, token)


class XdgPopupGlobal(Global):
    interface = XdgPopup


XdgPopup._gen_c()
XdgPopup.proxy_class = XdgPopupProxy
XdgPopup.resource_class = XdgPopupResource
XdgPopup.global_class = XdgPopupGlobal
