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


from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)


class WpDrmLeaseConnectorV1(Interface):
    """A leasable drm connector

    Represents a DRM connector which is available for lease. These objects are
    created via :func:`WpDrmLeaseDeviceV1.connector()
    <pywayland.protocol.drm_lease_v1.WpDrmLeaseDeviceV1.connector>` events, and
    should be passed to lease requests via
    :func:`WpDrmLeaseRequestV1.request_connector()
    <pywayland.protocol.drm_lease_v1.WpDrmLeaseRequestV1.request_connector>`.
    Immediately after the :class:`WpDrmLeaseConnectorV1` object is created the
    compositor will send a name, a description, a connector_id and a done
    event. When the description is updated the compositor will send a
    description event followed by a done event.
    """

    name = "wp_drm_lease_connector_v1"
    version = 1


class WpDrmLeaseConnectorV1Proxy(Proxy[WpDrmLeaseConnectorV1]):
    interface = WpDrmLeaseConnectorV1

    @WpDrmLeaseConnectorV1.request()
    def destroy(self) -> None:
        """Destroy connector

        The client may send this request to indicate that it will not use this
        connector. Clients are encouraged to send this after receiving the
        "withdrawn" event so that the server can release the resources
        associated with this connector offer. Neither existing lease requests
        nor leases will be affected.
        """
        self._marshal(0)
        self._destroy()


class WpDrmLeaseConnectorV1Resource(Resource):
    interface = WpDrmLeaseConnectorV1

    @WpDrmLeaseConnectorV1.event(
        Argument(ArgumentType.String),
    )
    def name(self, name: str) -> None:
        """Name

        The compositor sends this event once the connector is created to
        indicate the name of this connector. This will not change for the
        duration of the Wayland session, but is not guaranteed to be consistent
        between sessions.

        If the compositor supports
        :class:`~pywayland.protocol.wayland.WlOutput` version 4 and this
        connector corresponds to a
        :class:`~pywayland.protocol.wayland.WlOutput`, the compositor should
        use the same name as for the
        :class:`~pywayland.protocol.wayland.WlOutput`.

        :param name:
            connector name
        :type name:
            `ArgumentType.String`
        """
        self._post_event(0, name)

    @WpDrmLeaseConnectorV1.event(
        Argument(ArgumentType.String),
    )
    def description(self, description: str) -> None:
        """Description

        The compositor sends this event once the connector is created to
        provide a human-readable description for this connector, which may be
        presented to the user. The compositor may send this event multiple
        times over the lifetime of this object to reflect changes in the
        description.

        :param description:
            connector description
        :type description:
            `ArgumentType.String`
        """
        self._post_event(1, description)

    @WpDrmLeaseConnectorV1.event(
        Argument(ArgumentType.Uint),
    )
    def connector_id(self, connector_id: int) -> None:
        """Connector_id

        The compositor sends this event once the connector is created to
        indicate the DRM object ID which represents the underlying connector
        that is being offered. Note that the final lease may include additional
        object IDs, such as CRTCs and planes.

        :param connector_id:
            DRM connector ID
        :type connector_id:
            `ArgumentType.Uint`
        """
        self._post_event(2, connector_id)

    @WpDrmLeaseConnectorV1.event()
    def done(self) -> None:
        """All properties have been sent

        This event is sent after all properties of a connector have been sent.
        This allows changes to the properties to be seen as atomic even if they
        happen via multiple events.
        """
        self._post_event(3)

    @WpDrmLeaseConnectorV1.event()
    def withdrawn(self) -> None:
        """Lease offer withdrawn

        Sent to indicate that the compositor will no longer honor requests for
        DRM leases which include this connector. The client may still issue a
        lease request including this connector, but the compositor will send
        :func:`WpDrmLeaseV1.finished()
        <pywayland.protocol.drm_lease_v1.WpDrmLeaseV1.finished>` without
        issuing a lease fd. Compositors are encouraged to send this event when
        they lose access to connector, for example when the connector is hot-
        unplugged, when the connector gets leased to a client or when the
        compositor loses DRM master.
        """
        self._post_event(4)


class WpDrmLeaseConnectorV1Global(Global):
    interface = WpDrmLeaseConnectorV1


WpDrmLeaseConnectorV1._gen_c()
WpDrmLeaseConnectorV1.proxy_class = WpDrmLeaseConnectorV1Proxy
WpDrmLeaseConnectorV1.resource_class = WpDrmLeaseConnectorV1Resource
WpDrmLeaseConnectorV1.global_class = WpDrmLeaseConnectorV1Global
