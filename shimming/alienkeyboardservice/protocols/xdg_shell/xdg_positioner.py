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


class XdgPositioner(Interface):
    """Child surface positioner

    The :class:`XdgPositioner` provides a collection of rules for the placement
    of a child surface relative to a parent surface. Rules can be defined to
    ensure the child surface remains within the visible area's borders, and to
    specify how the child surface changes its position, such as sliding along
    an axis, or flipping around a rectangle. These positioner-created rules are
    constrained by the requirement that a child surface must intersect with or
    be at least partially adjacent to its parent surface.

    See the various requests for details about possible rules.

    At the time of the request, the compositor makes a copy of the rules
    specified by the :class:`XdgPositioner`. Thus, after the request is
    complete the :class:`XdgPositioner` object can be destroyed or reused;
    further changes to the object will have no effect on previous usages.

    For an :class:`XdgPositioner` object to be considered complete, it must
    have a non-zero size set by set_size, and a non-zero anchor rectangle set
    by set_anchor_rect. Passing an incomplete :class:`XdgPositioner` object
    when positioning a surface raises an invalid_positioner error.
    """

    name = "xdg_positioner"
    version = 5

    class error(enum.IntEnum):
        invalid_input = 0

    class anchor(enum.IntEnum):
        none = 0
        top = 1
        bottom = 2
        left = 3
        right = 4
        top_left = 5
        bottom_left = 6
        top_right = 7
        bottom_right = 8

    class gravity(enum.IntEnum):
        none = 0
        top = 1
        bottom = 2
        left = 3
        right = 4
        top_left = 5
        bottom_left = 6
        top_right = 7
        bottom_right = 8

    class constraint_adjustment(enum.IntFlag):
        none = 0
        slide_x = 1
        slide_y = 2
        flip_x = 4
        flip_y = 8
        resize_x = 16
        resize_y = 32


class XdgPositionerProxy(Proxy[XdgPositioner]):
    interface = XdgPositioner

    @XdgPositioner.request()
    def destroy(self) -> None:
        """Destroy the :class:`XdgPositioner` object

        Notify the compositor that the :class:`XdgPositioner` will no longer be
        used.
        """
        self._marshal(0)
        self._destroy()

    @XdgPositioner.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def set_size(self, width: int, height: int) -> None:
        """Set the size of the to-be positioned rectangle

        Set the size of the surface that is to be positioned with the
        positioner object. The size is in surface-local coordinates and
        corresponds to the window geometry. See
        :func:`XdgSurface.set_window_geometry()
        <pywayland.protocol.xdg_shell.XdgSurface.set_window_geometry>`.

        If a zero or negative size is set the invalid_input error is raised.

        :param width:
            width of positioned rectangle
        :type width:
            `ArgumentType.Int`
        :param height:
            height of positioned rectangle
        :type height:
            `ArgumentType.Int`
        """
        self._marshal(1, width, height)

    @XdgPositioner.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def set_anchor_rect(self, x: int, y: int, width: int, height: int) -> None:
        """Set the anchor rectangle within the parent surface

        Specify the anchor rectangle within the parent surface that the child
        surface will be placed relative to. The rectangle is relative to the
        window geometry as defined by :func:`XdgSurface.set_window_geometry()
        <pywayland.protocol.xdg_shell.XdgSurface.set_window_geometry>` of the
        parent surface.

        When the :class:`XdgPositioner` object is used to position a child
        surface, the anchor rectangle may not extend outside the window
        geometry of the positioned child's parent surface.

        If a negative size is set the invalid_input error is raised.

        :param x:
            x position of anchor rectangle
        :type x:
            `ArgumentType.Int`
        :param y:
            y position of anchor rectangle
        :type y:
            `ArgumentType.Int`
        :param width:
            width of anchor rectangle
        :type width:
            `ArgumentType.Int`
        :param height:
            height of anchor rectangle
        :type height:
            `ArgumentType.Int`
        """
        self._marshal(2, x, y, width, height)

    @XdgPositioner.request(
        Argument(ArgumentType.Uint),
    )
    def set_anchor(self, anchor: int) -> None:
        """Set anchor rectangle anchor

        Defines the anchor point for the anchor rectangle. The specified anchor
        is used derive an anchor point that the child surface will be
        positioned relative to. If a corner anchor is set (e.g. 'top_left' or
        'bottom_right'), the anchor point will be at the specified corner;
        otherwise, the derived anchor point will be centered on the specified
        edge, or in the center of the anchor rectangle if no edge is specified.

        :param anchor:
            anchor
        :type anchor:
            `ArgumentType.Uint`
        """
        self._marshal(3, anchor)

    @XdgPositioner.request(
        Argument(ArgumentType.Uint),
    )
    def set_gravity(self, gravity: int) -> None:
        """Set child surface gravity

        Defines in what direction a surface should be positioned, relative to
        the anchor point of the parent surface. If a corner gravity is
        specified (e.g. 'bottom_right' or 'top_left'), then the child surface
        will be placed towards the specified gravity; otherwise, the child
        surface will be centered over the anchor point on any axis that had no
        gravity specified. If the gravity is not in the ‘gravity’ enum, an
        invalid_input error is raised.

        :param gravity:
            gravity direction
        :type gravity:
            `ArgumentType.Uint`
        """
        self._marshal(4, gravity)

    @XdgPositioner.request(
        Argument(ArgumentType.Uint),
    )
    def set_constraint_adjustment(self, constraint_adjustment: int) -> None:
        """Set the adjustment to be done when constrained

        Specify how the window should be positioned if the originally intended
        position caused the surface to be constrained, meaning at least
        partially outside positioning boundaries set by the compositor. The
        adjustment is set by constructing a bitmask describing the adjustment
        to be made when the surface is constrained on that axis.

        If no bit for one axis is set, the compositor will assume that the
        child surface should not change its position on that axis when
        constrained.

        If more than one bit for one axis is set, the order of how adjustments
        are applied is specified in the corresponding adjustment descriptions.

        The default adjustment is none.

        :param constraint_adjustment:
            bit mask of constraint adjustments
        :type constraint_adjustment:
            `ArgumentType.Uint`
        """
        self._marshal(5, constraint_adjustment)

    @XdgPositioner.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def set_offset(self, x: int, y: int) -> None:
        """Set surface position offset

        Specify the surface position offset relative to the position of the
        anchor on the anchor rectangle and the anchor on the surface. For
        example if the anchor of the anchor rectangle is at (x, y), the surface
        has the gravity bottom|right, and the offset is (ox, oy), the
        calculated surface position will be (x + ox, y + oy). The offset
        position of the surface is the one used for constraint testing. See
        set_constraint_adjustment.

        An example use case is placing a popup menu on top of a user interface
        element, while aligning the user interface element of the parent
        surface with some user interface element placed somewhere in the popup
        surface.

        :param x:
            surface position x offset
        :type x:
            `ArgumentType.Int`
        :param y:
            surface position y offset
        :type y:
            `ArgumentType.Int`
        """
        self._marshal(6, x, y)

    @XdgPositioner.request(version=3)
    def set_reactive(self) -> None:
        """Continuously reconstrain the surface

        When set reactive, the surface is reconstrained if the conditions used
        for constraining changed, e.g. the parent window moved.

        If the conditions changed and the popup was reconstrained, an
        :func:`XdgPopup.configure()
        <pywayland.protocol.xdg_shell.XdgPopup.configure>` event is sent with
        updated geometry, followed by an :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` event.
        """
        self._marshal(7)

    @XdgPositioner.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        version=3,
    )
    def set_parent_size(self, parent_width: int, parent_height: int) -> None:
        """

        Set the parent window geometry the compositor should use when
        positioning the popup. The compositor may use this information to
        determine the future state the popup should be constrained using. If
        this doesn't match the dimension of the parent the popup is eventually
        positioned against, the behavior is undefined.

        The arguments are given in the surface-local coordinate space.

        :param parent_width:
            future window geometry width of parent
        :type parent_width:
            `ArgumentType.Int`
        :param parent_height:
            future window geometry height of parent
        :type parent_height:
            `ArgumentType.Int`
        """
        self._marshal(8, parent_width, parent_height)

    @XdgPositioner.request(
        Argument(ArgumentType.Uint),
        version=3,
    )
    def set_parent_configure(self, serial: int) -> None:
        """Set parent configure this is a response to

        Set the serial of an :func:`XdgSurface.configure()
        <pywayland.protocol.xdg_shell.XdgSurface.configure>` event this
        positioner will be used in response to. The compositor may use this
        information together with set_parent_size to determine what future
        state the popup should be constrained using.

        :param serial:
            serial of parent configure event
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(9, serial)


class XdgPositionerResource(Resource):
    interface = XdgPositioner


class XdgPositionerGlobal(Global):
    interface = XdgPositioner


XdgPositioner._gen_c()
XdgPositioner.proxy_class = XdgPositionerProxy
XdgPositioner.resource_class = XdgPositionerResource
XdgPositioner.global_class = XdgPositionerGlobal