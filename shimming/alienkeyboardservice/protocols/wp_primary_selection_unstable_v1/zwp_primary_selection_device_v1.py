# This file has been autogenerated by the pywayland scanner

# Copyright © 2015, 2016 Red Hat
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
from .zwp_primary_selection_offer_v1 import ZwpPrimarySelectionOfferV1
from .zwp_primary_selection_source_v1 import ZwpPrimarySelectionSourceV1


class ZwpPrimarySelectionDeviceV1(Interface):
    name = "zwp_primary_selection_device_v1"
    version = 1


class ZwpPrimarySelectionDeviceV1Proxy(Proxy[ZwpPrimarySelectionDeviceV1]):
    interface = ZwpPrimarySelectionDeviceV1

    @ZwpPrimarySelectionDeviceV1.request(
        Argument(ArgumentType.Object, interface=ZwpPrimarySelectionSourceV1, nullable=True),
        Argument(ArgumentType.Uint),
    )
    def set_selection(self, source: ZwpPrimarySelectionSourceV1 | None, serial: int) -> None:
        """Set the primary selection

        Replaces the current selection. The previous owner of the primary
        selection will receive a wp_primary_selection_source.cancelled event.

        To unset the selection, set the source to NULL.

        :param source:
        :type source:
            :class:`~pywayland.protocol.wp_primary_selection_unstable_v1.ZwpPrimarySelectionSourceV1` or `None`
        :param serial:
            serial of the event that triggered this request
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(0, source, serial)

    @ZwpPrimarySelectionDeviceV1.request()
    def destroy(self) -> None:
        """Destroy the primary selection device

        Destroy the primary selection device.
        """
        self._marshal(1)
        self._destroy()


class ZwpPrimarySelectionDeviceV1Resource(Resource):
    interface = ZwpPrimarySelectionDeviceV1

    @ZwpPrimarySelectionDeviceV1.event(
        Argument(ArgumentType.NewId, interface=ZwpPrimarySelectionOfferV1),
    )
    def data_offer(self, offer: ZwpPrimarySelectionOfferV1) -> None:
        """Introduce a new wp_primary_selection_offer

        Introduces a new wp_primary_selection_offer object that may be used to
        receive the current primary selection. Immediately following this
        event, the new wp_primary_selection_offer object will send
        wp_primary_selection_offer.offer events to describe the offered mime
        types.

        :param offer:
        :type offer:
            :class:`~pywayland.protocol.wp_primary_selection_unstable_v1.ZwpPrimarySelectionOfferV1`
        """
        self._post_event(0, offer)

    @ZwpPrimarySelectionDeviceV1.event(
        Argument(ArgumentType.Object, interface=ZwpPrimarySelectionOfferV1, nullable=True),
    )
    def selection(self, id: ZwpPrimarySelectionOfferV1 | None) -> None:
        """Advertise a new primary selection

        The wp_primary_selection_device.selection event is sent to notify the
        client of a new primary selection. This event is sent after the
        wp_primary_selection.data_offer event introducing this object, and
        after the offer has announced its mimetypes through
        wp_primary_selection_offer.offer.

        The data_offer is valid until a new offer or NULL is received or until
        the client loses keyboard focus. The client must destroy the previous
        selection data_offer, if any, upon receiving this event.

        :param id:
        :type id:
            :class:`~pywayland.protocol.wp_primary_selection_unstable_v1.ZwpPrimarySelectionOfferV1` or `None`
        """
        self._post_event(1, id)


class ZwpPrimarySelectionDeviceV1Global(Global):
    interface = ZwpPrimarySelectionDeviceV1


ZwpPrimarySelectionDeviceV1._gen_c()
ZwpPrimarySelectionDeviceV1.proxy_class = ZwpPrimarySelectionDeviceV1Proxy
ZwpPrimarySelectionDeviceV1.resource_class = ZwpPrimarySelectionDeviceV1Resource
ZwpPrimarySelectionDeviceV1.global_class = ZwpPrimarySelectionDeviceV1Global
