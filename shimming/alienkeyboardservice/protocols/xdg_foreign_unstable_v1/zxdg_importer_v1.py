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


from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)
from .zxdg_imported_v1 import ZxdgImportedV1


class ZxdgImporterV1(Interface):
    """Interface for importing surfaces

    A global interface used for importing surfaces exported by xdg_exporter.
    With this interface, a client can create a reference to a surface of
    another client.
    """

    name = "zxdg_importer_v1"
    version = 1


class ZxdgImporterV1Proxy(Proxy[ZxdgImporterV1]):
    interface = ZxdgImporterV1

    @ZxdgImporterV1.request()
    def destroy(self) -> None:
        """Destroy the xdg_importer object

        Notify the compositor that the xdg_importer object will no longer be
        used.
        """
        self._marshal(0)
        self._destroy()

    @ZxdgImporterV1.request(
        Argument(ArgumentType.NewId, interface=ZxdgImportedV1),
        Argument(ArgumentType.String),
    )
    def import_(self, handle: str) -> Proxy[ZxdgImportedV1]:
        """Import a surface

        The import request imports a surface from any client given a handle
        retrieved by exporting said surface using xdg_exporter.export. When
        called, a new xdg_imported object will be created. This new object
        represents the imported surface, and the importing client can
        manipulate its relationship using it. See xdg_imported for details.

        :param handle:
            the exported surface handle
        :type handle:
            `ArgumentType.String`
        :returns:
            :class:`~pywayland.protocol.xdg_foreign_unstable_v1.ZxdgImportedV1`
            -- the new xdg_imported object
        """
        id = self._marshal_constructor(1, ZxdgImportedV1, handle)
        return id


class ZxdgImporterV1Resource(Resource):
    interface = ZxdgImporterV1


class ZxdgImporterV1Global(Global):
    interface = ZxdgImporterV1


ZxdgImporterV1._gen_c()
ZxdgImporterV1.proxy_class = ZxdgImporterV1Proxy
ZxdgImporterV1.resource_class = ZxdgImporterV1Resource
ZxdgImporterV1.global_class = ZxdgImporterV1Global
