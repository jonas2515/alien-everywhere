# This file has been autogenerated by the pywayland scanner

# Copyright © 2015-2016 Red Hat Inc.
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
from .zxdg_exported_v2 import ZxdgExportedV2


class ZxdgExporterV2(Interface):
    """Interface for exporting surfaces

    A global interface used for exporting surfaces that can later be imported
    using xdg_importer.
    """

    name = "zxdg_exporter_v2"
    version = 1

    class error(enum.IntEnum):
        invalid_surface = 0


class ZxdgExporterV2Proxy(Proxy[ZxdgExporterV2]):
    interface = ZxdgExporterV2

    @ZxdgExporterV2.request()
    def destroy(self) -> None:
        """Destroy the xdg_exporter object

        Notify the compositor that the xdg_exporter object will no longer be
        used.
        """
        self._marshal(0)
        self._destroy()

    @ZxdgExporterV2.request(
        Argument(ArgumentType.NewId, interface=ZxdgExportedV2),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def export_toplevel(self, surface: WlSurface) -> Proxy[ZxdgExportedV2]:
        """Export a toplevel surface

        The export_toplevel request exports the passed surface so that it can
        later be imported via xdg_importer. When called, a new xdg_exported
        object will be created and xdg_exported.handle will be sent
        immediately. See the corresponding interface and event for details.

        A surface may be exported multiple times, and each exported handle may
        be used to create an xdg_imported multiple times. Only
        :class:`~pywayland.protocol.xdg_shell.XdgToplevel` equivalent surfaces
        may be exported, otherwise an invalid_surface protocol error is sent.

        :param surface:
            the surface to export
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :returns:
            :class:`~pywayland.protocol.xdg_foreign_unstable_v2.ZxdgExportedV2`
            -- the new xdg_exported object
        """
        id = self._marshal_constructor(1, ZxdgExportedV2, surface)
        return id


class ZxdgExporterV2Resource(Resource):
    interface = ZxdgExporterV2


class ZxdgExporterV2Global(Global):
    interface = ZxdgExporterV2


ZxdgExporterV2._gen_c()
ZxdgExporterV2.proxy_class = ZxdgExporterV2Proxy
ZxdgExporterV2.resource_class = ZxdgExporterV2Resource
ZxdgExporterV2.global_class = ZxdgExporterV2Global
