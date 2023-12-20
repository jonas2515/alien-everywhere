# This file has been autogenerated by the pywayland scanner

# Copyright © 2015 Samsung Electronics Co., Ltd
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


from pywayland.protocol_core import Global, Interface, Proxy, Resource


class ZwpIdleInhibitorV1(Interface):
    """Context object for inhibiting idle behavior

    An idle inhibitor prevents the output that the associated surface is
    visible on from being set to a state where it is not visually usable due to
    lack of user interaction (e.g. blanked, dimmed, locked, set to power save,
    etc.)  Any screensaver processes are also blocked from displaying.

    If the surface is destroyed, unmapped, becomes occluded, loses visibility,
    or otherwise becomes not visually relevant for the user, the idle inhibitor
    will not be honored by the compositor; if the surface subsequently regains
    visibility the inhibitor takes effect once again. Likewise, the inhibitor
    isn't honored if the system was already idled at the time the inhibitor was
    established, although if the system later de-idles and re-idles the
    inhibitor will take effect.
    """

    name = "zwp_idle_inhibitor_v1"
    version = 1


class ZwpIdleInhibitorV1Proxy(Proxy[ZwpIdleInhibitorV1]):
    interface = ZwpIdleInhibitorV1

    @ZwpIdleInhibitorV1.request()
    def destroy(self) -> None:
        """Destroy the idle inhibitor object

        Remove the inhibitor effect from the associated
        :class:`~pywayland.protocol.wayland.WlSurface`.
        """
        self._marshal(0)
        self._destroy()


class ZwpIdleInhibitorV1Resource(Resource):
    interface = ZwpIdleInhibitorV1


class ZwpIdleInhibitorV1Global(Global):
    interface = ZwpIdleInhibitorV1


ZwpIdleInhibitorV1._gen_c()
ZwpIdleInhibitorV1.proxy_class = ZwpIdleInhibitorV1Proxy
ZwpIdleInhibitorV1.resource_class = ZwpIdleInhibitorV1Resource
ZwpIdleInhibitorV1.global_class = ZwpIdleInhibitorV1Global
