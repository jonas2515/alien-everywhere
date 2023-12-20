# This file has been autogenerated by the pywayland scanner

# Copyright 2021 Isaac Freund
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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


class ExtSessionLockSurfaceV1(Interface):
    """A surface displayed while the session is locked

    The client may use lock surfaces to display a screensaver, render a dialog
    to enter a password and unlock the session, or however else it sees fit.

    On binding this interface the compositor will immediately send the first
    configure event. After making the ack_configure request in response to this
    event the client should attach and commit the first buffer. Committing the
    surface before acking the first configure is a protocol error. Committing
    the surface with a null buffer at any time is a protocol error.

    The compositor is free to handle keyboard/pointer focus for lock surfaces
    however it chooses. A reasonable way to do this would be to give the first
    lock surface created keyboard focus and change keyboard focus if the user
    clicks on other surfaces.
    """

    name = "ext_session_lock_surface_v1"
    version = 1

    class error(enum.IntEnum):
        commit_before_first_ack = 0
        null_buffer = 1
        dimensions_mismatch = 2
        invalid_serial = 3


class ExtSessionLockSurfaceV1Proxy(Proxy[ExtSessionLockSurfaceV1]):
    interface = ExtSessionLockSurfaceV1

    @ExtSessionLockSurfaceV1.request()
    def destroy(self) -> None:
        """Destroy the lock surface object

        This informs the compositor that the lock surface object will no longer
        be used.

        It is recommended for a lock client to destroy lock surfaces if their
        corresponding :class:`~pywayland.protocol.wayland.WlOutput` global is
        removed.

        If a lock surface on an active output is destroyed before the
        :func:`ExtSessionLockV1.unlock_and_destroy()
        <pywayland.protocol.ext_session_lock_v1.ExtSessionLockV1.unlock_and_destroy>`
        event is sent, the compositor must fall back to rendering a solid
        color.
        """
        self._marshal(0)
        self._destroy()

    @ExtSessionLockSurfaceV1.request(
        Argument(ArgumentType.Uint),
    )
    def ack_configure(self, serial: int) -> None:
        """Ack a configure event

        When a configure event is received, if a client commits the surface in
        response to the configure event, then the client must make an
        ack_configure request sometime before the commit request, passing along
        the serial of the configure event.

        If the client receives multiple configure events before it can respond
        to one, it only has to ack the last configure event.

        A client is not required to commit immediately after sending an
        ack_configure request - it may even ack_configure several times before
        its next surface commit.

        A client may send multiple ack_configure requests before committing,
        but only the last request sent before a commit indicates which
        configure event the client really is responding to.

        Sending an ack_configure request consumes the configure event
        referenced by the given serial, as well as all older configure events
        sent on this object.

        It is a protocol error to issue multiple ack_configure requests
        referencing the same configure event or to issue an ack_configure
        request referencing a configure event older than the last configure
        event acked for a given lock surface.

        :param serial:
            serial from the configure event
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(1, serial)


class ExtSessionLockSurfaceV1Resource(Resource):
    interface = ExtSessionLockSurfaceV1

    @ExtSessionLockSurfaceV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def configure(self, serial: int, width: int, height: int) -> None:
        """The client should resize its surface

        This event is sent once on binding the interface and may be sent again
        at the compositor's discretion, for example if output geometry changes.

        The width and height are in surface-local coordinates and are exact
        requirements. Failing to match these surface dimensions in the next
        commit after acking a configure is a protocol error.

        :param serial:
            serial for use in ack_configure
        :type serial:
            `ArgumentType.Uint`
        :param width:
        :type width:
            `ArgumentType.Uint`
        :param height:
        :type height:
            `ArgumentType.Uint`
        """
        self._post_event(0, serial, width, height)


class ExtSessionLockSurfaceV1Global(Global):
    interface = ExtSessionLockSurfaceV1


ExtSessionLockSurfaceV1._gen_c()
ExtSessionLockSurfaceV1.proxy_class = ExtSessionLockSurfaceV1Proxy
ExtSessionLockSurfaceV1.resource_class = ExtSessionLockSurfaceV1Resource
ExtSessionLockSurfaceV1.global_class = ExtSessionLockSurfaceV1Global