# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = [
    "Invoice",
    "ContactDetails",
    "ContactDetail",
    "CounterpartyBillingAddress",
    "CounterpartyShippingAddress",
    "InvoicerAddress",
]


class ContactDetail(BaseModel):
    id: str

    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]

    created_at: datetime

    discarded_at: Optional[datetime]

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime


ContactDetails = ContactDetail
"""This type is deprecated and will be removed in a future release.

Please use ContactDetail instead.
"""


class CounterpartyBillingAddress(BaseModel):
    country: str
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: str

    locality: str
    """Locality or City."""

    postal_code: str
    """The postal code of the address."""

    region: str
    """Region or State."""

    line2: Optional[str]


class CounterpartyShippingAddress(BaseModel):
    country: str
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: str

    locality: str
    """Locality or City."""

    postal_code: str
    """The postal code of the address."""

    region: str
    """Region or State."""

    line2: Optional[str]


class InvoicerAddress(BaseModel):
    country: str
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: str

    locality: str
    """Locality or City."""

    postal_code: str
    """The postal code of the address."""

    region: str
    """Region or State."""

    line2: Optional[str]


class Invoice(BaseModel):
    id: str

    contact_details: List[ContactDetail]
    """The invoicer's contact details displayed at the top of the invoice."""

    counterparty_billing_address: Optional[CounterpartyBillingAddress]
    """The counterparty's billing address."""

    counterparty_id: str
    """The ID of the counterparty receiving the invoice."""

    counterparty_shipping_address: Optional[CounterpartyShippingAddress]
    """The counterparty's shipping address where physical goods should be delivered."""

    created_at: datetime

    currency: Optional[shared.Currency]
    """Currency that the invoice is denominated in. Defaults to `USD` if not provided."""

    description: str
    """A free-form description of the invoice."""

    due_date: datetime
    """A future date by when the invoice needs to be paid."""

    hosted_url: str
    """The URL of the hosted web UI where the invoice can be viewed."""

    invoicer_address: Optional[InvoicerAddress]
    """The invoice issuer's business address."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    number: str
    """A unique record number assigned to each invoice that is issued."""

    object: str

    originating_account_id: str
    """The ID of the internal account the invoice should be paid to."""

    payment_orders: List[payment_order.PaymentOrder]
    """
    The payment orders created for paying the invoice through the invoice payment
    UI.
    """

    pdf_url: Optional[str]
    """The URL where the invoice PDF can be downloaded."""

    status: Literal["draft", "paid", "payment_pending", "unpaid", "voided"]
    """The status of the invoice."""

    total_amount: int
    """
    Total amount due in specified currency's smallest unit, e.g., $10 USD would be
    represented as 1000.
    """

    updated_at: datetime


from ..types import payment_order

Invoice.update_forward_refs()
ContactDetail.update_forward_refs()
CounterpartyBillingAddress.update_forward_refs()
CounterpartyShippingAddress.update_forward_refs()
InvoicerAddress.update_forward_refs()
