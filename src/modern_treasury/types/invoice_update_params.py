# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.currency import Currency
from .payment_order_type import PaymentOrderType

__all__ = [
    "InvoiceUpdateParams",
    "ContactDetails",
    "ContactDetail",
    "CounterpartyBillingAddress",
    "CounterpartyShippingAddress",
    "InvoiceLineItems",
    "InvoiceLineItem",
    "InvoicerAddress",
]


class InvoiceUpdateParams(TypedDict, total=False):
    contact_details: Iterable[ContactDetail]
    """The invoicer's contact details displayed at the top of the invoice."""

    counterparty_billing_address: Optional[CounterpartyBillingAddress]
    """The counterparty's billing address."""

    counterparty_id: str
    """The ID of the counterparty receiving the invoice."""

    counterparty_shipping_address: Optional[CounterpartyShippingAddress]
    """The counterparty's shipping address where physical goods should be delivered."""

    currency: Currency
    """Currency that the invoice is denominated in. Defaults to `USD` if not provided."""

    description: str
    """A free-form description of the invoice."""

    due_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """A future date by when the invoice needs to be paid."""

    fallback_payment_method: Optional[str]
    """
    When payment_method is automatic, the fallback payment method to use when an
    automatic payment fails. One of `manual` or `ui`.
    """

    ingest_ledger_entries: Optional[bool]
    """Whether to ingest the ledger_entries to populate the invoice line items.

    If this is false, then a line item must be provided. If this is true, line_items
    must be empty. Ignored if ledger_account_settlement_id is empty.
    """

    invoice_line_items: Optional[Iterable[InvoiceLineItem]]
    """An array of invoice line items.

    The API supports a maximum of 50 invoice line items per invoice. If a greater
    number of invoice line items is required, please contact support.
    """

    invoicer_address: Optional[InvoicerAddress]
    """The invoice issuer's business address."""

    ledger_account_settlement_id: Optional[str]
    """The ID of the virtual account the invoice should be paid to."""

    metadata: Optional[Dict[str, str]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    notification_email_addresses: Optional[List[str]]
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

    originating_account_id: str
    """The ID of the internal account the invoice should be paid to."""

    payment_effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date transactions are to be posted to the participants' account.

    Defaults to the current business day or the next business day if the current day
    is a bank holiday or weekend. Format: yyyy-mm-dd.
    """

    payment_method: Literal["ui", "manual", "automatic"]
    """The method by which the invoice can be paid.

    `ui` will show the embedded payment collection flow. `automatic` will
    automatically initiate payment based upon the account details of the
    receiving_account id.\nIf the invoice amount is positive, the automatically
    initiated payment order's direction will be debit. If the invoice amount is
    negative, the automatically initiated payment order's direction will be credit.
    One of `manual`, `ui`, or `automatic`.
    """

    payment_type: PaymentOrderType
    """
    One of `ach`, `se_bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`,
    `sepa`, `bacs`, `au_becs`, `interac`, `neft`, `nics`,
    `nz_national_clearing_code`, `sic`, `signet`, `provexchange`, `zengin`.
    """

    receiving_account_id: str
    """The receiving account ID. Can be an `external_account`."""

    recipient_email: Optional[str]
    """The email of the recipient of the invoice.

    Leaving this value as null will fallback to using the counterparty's name.
    """

    recipient_name: Optional[str]
    """The name of the recipient of the invoice.

    Leaving this value as null will fallback to using the counterparty's name.
    """

    remind_after_overdue_days: Optional[Iterable[int]]
    """
    Number of days after due date when overdue reminder emails will be sent out to
    invoice recipients.
    """

    status: str
    """
    Invoice status must be updated in a `PATCH` request that does not modify any
    other invoice attributes. Valid state transitions are `draft` to `unpaid`,
    `draft` or `unpaid` to `voided`, and `draft` or `unpaid` to `paid`.
    """

    virtual_account_id: Optional[str]
    """The ID of the virtual account the invoice should be paid to."""


class ContactDetail(TypedDict, total=False):
    id: Required[str]

    contact_identifier: Required[str]

    contact_identifier_type: Required[Literal["email", "phone_number", "website"]]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

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


class InvoiceLineItem(TypedDict, total=False):
    name: Required[str]
    """The name of the line item, typically a product or SKU name."""

    unit_amount: Required[int]
    """
    The cost per unit of the product or service that this line item is for,
    specified in the invoice currency's smallest unit.
    """

    description: str
    """An optional free-form description of the line item."""

    direction: str
    """Either `debit` or `credit`.

    `debit` indicates that a client owes the business money and increases the
    invoice's `total_amount` due. `credit` has the opposite intention and effect.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    quantity: int
    """The number of units of a product or service that this line item is for.

    Must be a whole number. Defaults to 1 if not provided.
    """

    unit_amount_decimal: str
    """
    The cost per unit of the product or service that this line item is for,
    specified in the invoice currency's smallest unit. Accepts decimal strings with
    up to 12 decimals
    """


InvoiceLineItems = InvoiceLineItem
"""This type is deprecated and will be removed in a future release.

Please use InvoiceLineItem instead.
"""


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
