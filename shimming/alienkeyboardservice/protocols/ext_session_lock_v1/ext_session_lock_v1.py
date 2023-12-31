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
from ..wayland import WlOutput
from ..wayland import WlSurface
from .ext_session_lock_surface_v1 import ExtSessionLockSurfaceV1


class ExtSessionLockV1(Interface):
    """Manage lock state and create lock surfaces

    In response to the creation of this object the compositor must send either
    the locked or finished event.

    The locked event indicates that the session is locked. This means that the
    compositor must stop rendering and providing input to normal clients.
    Instead the compositor must blank all outputs with an opaque color such
    that their normal content is fully hidden.

    The only surfaces that should be rendered while the session is locked are
    the lock surfaces created through this interface and optionally, at the
    compositor's discretion, special privileged surfaces such as input methods
    or portions of desktop shell UIs.

    The locked event must not be sent until a new "locked" frame (either from a
    session lock surface or the compositor blanking the output) has been
    presented on all outputs and no security sensitive normal/unlocked content
    is possibly visible.

    The finished event should be sent immediately on creation of this object if
    the compositor decides that the locked event will not be sent.

    The compositor may wait for the client to create and render session lock
    surfaces before sending the locked event to avoid displaying intermediate
    blank frames. However, it must impose a reasonable time limit if waiting
    and send the locked event as soon as the hard requirements described above
    can be met if the time limit expires. Clients should immediately create
    lock surfaces for all outputs on creation of this object to make this
    possible.

    This behavior of the locked event is required in order to prevent possible
    race conditions with clients that wish to suspend the system or similar
    after locking the session. Without these semantics, clients triggering a
    suspend after receiving the locked event would race with the first "locked"
    frame being presented and normal/unlocked frames might be briefly visible
    as the system is resumed if the suspend operation wins the race.

    If the client dies while the session is locked, the compositor must not
    unlock the session in response. It is acceptable for the session to be
    permanently locked if this happens. The compositor may choose to continue
    to display the lock surfaces the client had mapped before it died or
    alternatively fall back to a solid color, this is compositor policy.

    Compositors may also allow a secure way to recover the session, the details
    of this are compositor policy. Compositors may allow a new client to create
    a :class:`ExtSessionLockV1` object and take responsibility for unlocking
    the session, they may even start a new lock client instance automatically.
    """

    name = "ext_session_lock_v1"
    version = 1

    class error(enum.IntEnum):
        invalid_destroy = 0
        invalid_unlock = 1
        role = 2
        duplicate_output = 3
        already_constructed = 4


class ExtSessionLockV1Proxy(Proxy[ExtSessionLockV1]):
    interface = ExtSessionLockV1

    @ExtSessionLockV1.request()
    def destroy(self) -> None:
        """Destroy the session lock

        This informs the compositor that the lock object will no longer be
        used. Existing objects created through this interface remain valid.

        After this request is made, lock surfaces created through this object
        should be destroyed by the client as they will no longer be used by the
        compositor.

        It is a protocol error to make this request if the locked event was
        sent, the unlock_and_destroy request must be used instead.
        """
        self._marshal(0)
        self._destroy()

    @ExtSessionLockV1.request(
        Argument(ArgumentType.NewId, interface=ExtSessionLockSurfaceV1),
        Argument(ArgumentType.Object, interface=WlSurface),
        Argument(ArgumentType.Object, interface=WlOutput),
    )
    def get_lock_surface(self, surface: WlSurface, output: WlOutput) -> Proxy[ExtSessionLockSurfaceV1]:
        """Create a lock surface for a given output

        The client is expected to create lock surfaces for all outputs
        currently present and any new outputs as they are advertised. These
        won't be displayed by the compositor unless the lock is successful and
        the locked event is sent.

        Providing a :class:`~pywayland.protocol.wayland.WlSurface` which
        already has a role or already has a buffer attached or committed is a
        protocol error, as is attaching/committing a buffer before the first
        :func:`ExtSessionLockSurfaceV1.configure()
        <pywayland.protocol.ext_session_lock_v1.ExtSessionLockSurfaceV1.configure>`
        event.

        Attempting to create more than one lock surface for a given output is a
        duplicate_output protocol error.

        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :param output:
        :type output:
            :class:`~pywayland.protocol.wayland.WlOutput`
        :returns:
            :class:`~pywayland.protocol.ext_session_lock_v1.ExtSessionLockSurfaceV1`
        """
        id = self._marshal_constructor(1, ExtSessionLockSurfaceV1, surface, output)
        return id

    @ExtSessionLockV1.request()
    def unlock_and_destroy(self) -> None:
        """Unlock the session, destroying the object

        This request indicates that the session should be unlocked, for example
        because the user has entered their password and it has been verified by
        the client.

        This request also informs the compositor that the lock object will no
        longer be used and should be destroyed. Existing objects created
        through this interface remain valid.

        After this request is made, lock surfaces created through this object
        should be destroyed by the client as they will no longer be used by the
        compositor.

        It is a protocol error to make this request if the locked event has not
        been sent. In that case, the lock object must be destroyed using the
        destroy request.

        Note that a correct client that wishes to exit directly after unlocking
        the session must use the :func:`WlDisplay.sync()
        <pywayland.protocol.wayland.WlDisplay.sync>` request to ensure the
        server receives and processes the unlock_and_destroy request. Otherwise
        there is no guarantee that the server has unlocked the session due to
        the asynchronous nature of the Wayland protocol. For example, the
        server might terminate the client with a protocol error before it
        processes the unlock_and_destroy request.
        """
        self._marshal(2)
        self._destroy()


class ExtSessionLockV1Resource(Resource):
    interface = ExtSessionLockV1

    @ExtSessionLockV1.event()
    def locked(self) -> None:
        """Session successfully locked

        This client is now responsible for displaying graphics while the
        session is locked and deciding when to unlock the session.

        The locked event must not be sent until a new "locked" frame has been
        presented on all outputs and no security sensitive normal/unlocked
        content is possibly visible.

        If this event is sent, making the destroy request is a protocol error,
        the lock object must be destroyed using the unlock_and_destroy request.
        """
        self._post_event(0)

    @ExtSessionLockV1.event()
    def finished(self) -> None:
        """The session lock object should be destroyed

        The compositor has decided that the session lock should be destroyed as
        it will no longer be used by the compositor. Exactly when this event is
        sent is compositor policy, but it must never be sent more than once for
        a given session lock object.

        This might be sent because there is already another
        :class:`ExtSessionLockV1` object held by a client, or the compositor
        has decided to deny the request to lock the session for some other
        reason. This might also be sent because the compositor implements some
        alternative, secure way to authenticate and unlock the session.

        The finished event should be sent immediately on creation of this
        object if the compositor decides that the locked event will not be
        sent.

        If the locked event is sent on creation of this object the finished
        event may still be sent at some later time in this object's lifetime.
        This is compositor policy.

        Upon receiving this event, the client should make either the destroy
        request or the unlock_and_destroy request, depending on whether or not
        the locked event was received on this object.
        """
        self._post_event(1)


class ExtSessionLockV1Global(Global):
    interface = ExtSessionLockV1


ExtSessionLockV1._gen_c()
ExtSessionLockV1.proxy_class = ExtSessionLockV1Proxy
ExtSessionLockV1.resource_class = ExtSessionLockV1Resource
ExtSessionLockV1.global_class = ExtSessionLockV1Global
