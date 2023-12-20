# This file has been autogenerated by the pywayland scanner

# Copyright © 2018 NXP
# Copyright © 2019 Status Research & Development GmbH.
# Copyright © 2021 Xaver Hugl
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
from .wp_drm_lease_connector_v1 import WpDrmLeaseConnectorV1
from .wp_drm_lease_v1 import WpDrmLeaseV1


class WpDrmLeaseRequestV1(Interface):
    """Drm lease request

    A client that wishes to lease DRM resources will attach the list of
    connectors advertised with :func:`WpDrmLeaseDeviceV1.connector()
    <pywayland.protocol.drm_lease_v1.WpDrmLeaseDeviceV1.connector>` that they
    wish to lease, then use :func:`WpDrmLeaseRequestV1.submit()` to submit the
    request.
    """

    name = "wp_drm_lease_request_v1"
    version = 1

    class error(enum.IntEnum):
        wrong_device = 0
        duplicate_connector = 1
        empty_lease = 2


class WpDrmLeaseRequestV1Proxy(Proxy[WpDrmLeaseRequestV1]):
    interface = WpDrmLeaseRequestV1

    @WpDrmLeaseRequestV1.request(
        Argument(ArgumentType.Object, interface=WpDrmLeaseConnectorV1),
    )
    def request_connector(self, connector: WpDrmLeaseConnectorV1) -> None:
        """Request a connector for this lease

        Indicates that the client would like to lease the given connector. This
        is only used as a suggestion, the compositor may choose to include any
        resources in the lease it issues, or change the set of leased resources
        at any time. Compositors are however encouraged to include the
        requested connector and other resources necessary to drive the
        connected output in the lease.

        Requesting a connector that was created from a different lease device
        than this lease request raises the wrong_device error. Requesting a
        connector twice will raise the duplicate_connector error.

        :param connector:
        :type connector:
            :class:`~pywayland.protocol.drm_lease_v1.WpDrmLeaseConnectorV1`
        """
        self._marshal(0, connector)

    @WpDrmLeaseRequestV1.request(
        Argument(ArgumentType.NewId, interface=WpDrmLeaseV1),
    )
    def submit(self) -> Proxy[WpDrmLeaseV1]:
        """Submit the lease request

        Submits the lease request and creates a new
        :class:`~pywayland.protocol.drm_lease_v1.WpDrmLeaseV1` object. After
        calling submit the compositor will immediately destroy this object,
        issuing any more requests will cause a wl_diplay error. The compositor
        doesn't make any guarantees about the events of the lease object,
        clients cannot expect an immediate response. Not requesting any
        connectors before submitting the lease request will raise the
        empty_lease error.

        :returns:
            :class:`~pywayland.protocol.drm_lease_v1.WpDrmLeaseV1`
        """
        id = self._marshal_constructor(1, WpDrmLeaseV1)
        return id


class WpDrmLeaseRequestV1Resource(Resource):
    interface = WpDrmLeaseRequestV1


class WpDrmLeaseRequestV1Global(Global):
    interface = WpDrmLeaseRequestV1


WpDrmLeaseRequestV1._gen_c()
WpDrmLeaseRequestV1.proxy_class = WpDrmLeaseRequestV1Proxy
WpDrmLeaseRequestV1.resource_class = WpDrmLeaseRequestV1Resource
WpDrmLeaseRequestV1.global_class = WpDrmLeaseRequestV1Global
