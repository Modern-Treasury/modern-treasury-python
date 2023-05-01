# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..types import shared_params
from .._utils import PropertyInfo

__all__ = [
    "InvoiceUpdateParams",
    "ContactDetails",
    "ContactDetail",
    "CounterpartyBillingAddress",
    "CounterpartyShippingAddress",
    "InvoicerAddress",
]


class ContactDetail(TypedDict, total=False):
    contact_identifier: Required[str]

    contact_identifier_type: Required[Literal["email", "phone_number", "website"]]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]]

    id: Required[str]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


ContactDetails = ContactDetail
"""This type is deprecated and will be removed in a future release.

Please use ContactDetail instead.
"""


class CounterpartyBillingAddress(TypedDict, total=False):
    country: Required[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Required[str]

    locality: Required[str]
    """Locality or City."""

    postal_code: Required[str]
    """The postal code of the address."""

    region: Required[str]
    """Region or State."""

    line2: str


class CounterpartyShippingAddress(TypedDict, total=False):
    country: Required[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Required[str]

    locality: Required[str]
    """Locality or City."""

    postal_code: Required[str]
    """The postal code of the address."""

    region: Required[str]
    """Region or State."""

    line2: str


class InvoicerAddress(TypedDict, total=False):
    country: Required[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Required[str]

    locality: Required[str]
    """Locality or City."""

    postal_code: Required[str]
    """The postal code of the address."""

    region: Required[str]
    """Region or State."""

    line2: str


class InvoiceUpdateParams(TypedDict, total=False):
    contact_details: List[ContactDetail]
    """The invoicer's contact details displayed at the top of the invoice."""

    counterparty_billing_address: Optional[CounterpartyBillingAddress]
    """The counterparty's billing address."""

    counterparty_id: str
    """The ID of the counterparty receiving the invoice."""

    counterparty_shipping_address: Optional[CounterpartyShippingAddress]
    """The counterparty's shipping address where physical goods should be delivered."""

    currency: shared_params.Currency
    """Currency that the invoice is denominated in. Defaults to `USD` if not provided."""

    description: str
    """A free-form description of the invoice."""

    due_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """A future date by when the invoice needs to be paid."""

    include_payment_ui: bool
    """
    When opening an invoice, whether to show the embedded payment UI with the
    invoice. Default true.
    """

    invoicer_address: Optional[InvoicerAddress]
    """The invoice issuer's business address."""

    originating_account_id: str
    """The ID of the internal account the invoice should be paid to."""

    status: str
    """
    Invoice status must be updated in a `PATCH` request that does not modify any
    other invoice attributes. Valid state transitions are `draft` to `unpaid`,
    `draft` or `unpaid` to `void` and `unpaid` to `closed`.
    """
