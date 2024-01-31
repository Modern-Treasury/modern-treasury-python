# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .shared import Currency
from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .expected_payment import ExpectedPayment

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

    discarded_at: Optional[datetime] = None

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

    line2: Optional[str] = None


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

    line2: Optional[str] = None


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

    line2: Optional[str] = None


class Invoice(BaseModel):
    id: str

    amount_paid: int
    """
    Amount paid on the invoice in specified currency's smallest unit, e.g., $10 USD
    would be represented as 1000.
    """

    amount_remaining: int
    """
    Amount remaining due on the invoice in specified currency's smallest unit, e.g.,
    $10 USD would be represented as 1000.
    """

    contact_details: List[ContactDetail]
    """The invoicer's contact details displayed at the top of the invoice."""

    counterparty_billing_address: Optional[CounterpartyBillingAddress] = None
    """The counterparty's billing address."""

    counterparty_id: str
    """The ID of the counterparty receiving the invoice."""

    counterparty_shipping_address: Optional[CounterpartyShippingAddress] = None
    """The counterparty's shipping address where physical goods should be delivered."""

    created_at: datetime

    currency: Optional[Currency] = None
    """Currency that the invoice is denominated in. Defaults to `USD` if not provided."""

    description: str
    """A free-form description of the invoice."""

    due_date: datetime
    """A future date by when the invoice needs to be paid."""

    expected_payments: List[ExpectedPayment]
    """The expected payments created for an unpaid invoice."""

    fallback_payment_method: Optional[str] = None
    """
    When payment_method is automatic, the fallback payment method to use when an
    automatic payment fails. One of `manual` or `ui`.
    """

    hosted_url: str
    """The URL of the hosted web UI where the invoice can be viewed."""

    invoicer_address: Optional[InvoicerAddress] = None
    """The invoice issuer's business address."""

    ledger_account_settlement_id: Optional[str] = None
    """The ledger account settlement object linked to the invoice."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    notification_email_addresses: Optional[List[str]] = None
    """
    Emails in addition to the counterparty email to send invoice status
    notifications to. At least one email is required if notifications are enabled
    and the counterparty doesn't have an email.
    """

    notifications_enabled: bool
    """
    If true, the invoice will send email notifications to the invoice recipients
    about invoice status changes.
    """

    number: str
    """A unique record number assigned to each invoice that is issued."""

    object: str

    originating_account_id: str
    """The ID of the internal account the invoice should be paid to."""

    payment_effective_date: Optional[date] = None
    """Date transactions are to be posted to the participants' account.

    Defaults to the current business day or the next business day if the current day
    is a bank holiday or weekend. Format: yyyy-mm-dd.
    """

    payment_method: Optional[Literal["ui", "manual", "automatic"]] = None
    """
    When opening an invoice, whether to show the embedded payment UI , automatically
    debit the recipient, or rely on manual payment from the recipient.
    """

    payment_orders: List["PaymentOrder"]
    """
    The payment orders created for paying the invoice through the invoice payment
    UI.
    """

    payment_type: Optional[Literal["eft", "ach"]] = None
    """One of `ach` or `eft`."""

    pdf_url: Optional[str] = None
    """The URL where the invoice PDF can be downloaded."""

    receiving_account_id: Optional[str] = None
    """The receiving account ID. Can be an `internal_account`."""

    recipient_email: Optional[str] = None
    """The email of the recipient of the invoice.

    Leaving this value as null will fallback to using the counterparty's name.
    """

    recipient_name: Optional[str] = None
    """The name of the recipient of the invoice.

    Leaving this value as null will fallback to using the counterparty's name.
    """

    status: Literal["draft", "paid", "partially_paid", "payment_pending", "unpaid", "voided"]
    """The status of the invoice."""

    total_amount: int
    """
    Total amount due in specified currency's smallest unit, e.g., $10 USD would be
    represented as 1000.
    """

    transaction_line_item_ids: List[str]
    """IDs of transaction line items associated with an invoice."""

    updated_at: datetime

    virtual_account_id: Optional[str] = None
    """The ID of the virtual account the invoice should be paid to."""


from .payment_order import PaymentOrder

if PYDANTIC_V2:
    Invoice.model_rebuild()
    ContactDetail.model_rebuild()
    CounterpartyBillingAddress.model_rebuild()
    CounterpartyShippingAddress.model_rebuild()
    InvoicerAddress.model_rebuild()
else:
    Invoice.update_forward_refs()  # type: ignore
    ContactDetail.update_forward_refs()  # type: ignore
    CounterpartyBillingAddress.update_forward_refs()  # type: ignore
    CounterpartyShippingAddress.update_forward_refs()  # type: ignore
    InvoicerAddress.update_forward_refs()  # type: ignore
