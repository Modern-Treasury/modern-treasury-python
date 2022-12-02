# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params
from .._types import FileTypes

__all__ = [
    "Accounting",
    "ReceivingAccountPartyAddress",
    "ReceivingAccountAccountDetails",
    "ReceivingAccountRoutingDetails",
    "ReceivingAccountContactDetails",
    "ReceivingAccount",
    "LedgerTransactionLedgerEntries",
    "LedgerTransaction",
    "LineItems",
    "Documents",
    "PaymentOrderCreateParams",
]


class Accounting(TypedDict, total=False):
    account_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    class_id: Optional[str]
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """


class ReceivingAccountPartyAddress(TypedDict, total=False):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str]

    line2: Optional[str]

    locality: Optional[str]
    """Locality or City."""

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""


class ReceivingAccountAccountDetails(TypedDict, total=False):
    account_number: Required[str]

    account_number_type: Literal["iban", "clabe", "wallet_address", "pan", "other"]


class ReceivingAccountRoutingDetails(TypedDict, total=False):
    routing_number: Required[str]

    routing_number_type: Required[
        Literal["aba", "swift", "au_bsb", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "br_codigo"]
    ]

    payment_type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "check",
        "eft",
        "cross_border",
        "interac",
        "provxchange",
        "rtp",
        "sen",
        "sepa",
        "signet",
        "wire",
    ]


class ReceivingAccountContactDetails(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number"]


class ReceivingAccount(TypedDict, total=False):
    account_details: List[ReceivingAccountAccountDetails]

    account_type: Literal["cash", "checking", "loan", "non_resident", "other", "overdraft", "savings"]
    """Can be `checking`, `savings` or `other`."""

    contact_details: List[ReceivingAccountContactDetails]

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    party_address: ReceivingAccountPartyAddress
    """Required if receiving wire payments."""

    party_identifier: str

    party_name: str
    """
    If this value isn't provided, it will be inherited from the counterparty's name.
    """

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""

    plaid_processor_token: str
    """
    If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
    you can pass the processor token in this field.
    """

    routing_details: List[ReceivingAccountRoutingDetails]


class LedgerTransactionLedgerEntries(TypedDict, total=False):
    amount: Required[int]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    direction: Required[Literal["credit", "debit"]]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_id: Required[str]
    """The ledger account that this ledger entry is associated with."""

    available_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s available balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    lock_version: Optional[int]
    """Lock version of the ledger account.

    This can be passed when creating a ledger transaction to only succeed if no
    ledger transactions have posted since the given version. See our post about
    Designing the Ledgers API with Optimistic Locking for more details.
    """

    pending_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s pending balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    posted_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s posted balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """


class LedgerTransaction(TypedDict, total=False):
    effective_date: Required[str]
    """
    The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
    purposes.
    """

    ledger_entries: Required[List[LedgerTransactionLedgerEntries]]
    """An array of ledger entry objects."""

    description: Optional[str]
    """An optional description for internal use."""

    external_id: str
    """A unique string to represent the ledger transaction.

    Only one pending or posted ledger transaction may have this ID in the ledger.
    """

    ledgerable_id: str
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the id will be populated here, otherwise null.
    """

    ledgerable_type: Literal[
        "counterparty",
        "expected_payment",
        "incoming_payment_detail",
        "internal_account",
        "line_item",
        "paper_item",
        "payment_order",
        "payment_order_attempt",
        "return",
        "reversal",
    ]
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the type will be populated here, otherwise null. This can be one of
    payment_order, incoming_payment_detail, expected_payment, return, or reversal.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Literal["archived", "pending", "posted"]
    """To post a ledger transaction at creation, use `posted`."""


class LineItems(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    description: Optional[str]
    """A free-form description of the line item."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class Documents(TypedDict, total=False):
    file: Required[FileTypes]

    document_type: str
    """A category given to the document, can be `null`."""


class PaymentOrderCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000 (cents). For RTP, the maximum amount
    allowed by the network is $100,000.
    """

    direction: Required[Literal["credit", "debit"]]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    originating_account_id: Required[str]
    """The ID of one of your organization's internal accounts."""

    type: Required[
        Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
    ]
    """
    One of `ach`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`, `bacs`,
    `au_becs`, `interac`, `signet`, `provexchange`.
    """

    accounting: Accounting

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    accounting_ledger_class_id: Optional[str]
    """The ID of one of your accounting ledger classes.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    charge_bearer: Optional[Literal["shared", "sender", "receiver"]]
    """The party that will pay the fees for the payment order.

    Only applies to wire payment orders. Can be one of shared, sender, or receiver,
    which correspond respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.
    """

    currency: shared_params.Currency
    """Defaults to the currency of the originating account."""

    description: Optional[str]
    """An optional description for internal use."""

    documents: List[Documents]
    """An array of documents to be attached to the payment order.

    Note that if you attach documents, the request's content type must be
    `multipart/form-data`.
    """

    effective_date: str
    """Date transactions are to be posted to the participants' account.

    Defaults to the current business day or the next business day if the current day
    is a bank holiday or weekend. Format: yyyy-mm-dd.
    """

    expires_at: Optional[str]
    """RFP payments require an expires_at. This value must be past the effective_date."""

    fallback_type: Literal["ach"]
    """
    A payment type to fallback to if the original type is not valid for the
    receiving account. Currently, this only supports falling back from RTP to ACH
    (type=rtp and fallback_type=ach)
    """

    foreign_exchange_contract: Optional[str]
    """
    If present, indicates a specific foreign exchange contract number that has been
    generated by your financial institution.
    """

    foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]]
    """
    Indicates the type of FX transfer to initiate, can be either
    `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
    currency matches the originating account currency.
    """

    ledger_transaction: LedgerTransaction
    """
    Specifies a ledger transaction object that will be created with the payment
    order. If the ledger transaction cannot be created, then the payment order
    creation will fail. The resulting ledger transaction will mirror the status of
    the payment order.
    """

    line_items: List[LineItems]
    """An array of line items that must sum up to the amount of the payment order."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    nsf_protected: bool
    """A boolean to determine if NSF Protection is enabled for this payment order.

    Note that this setting must also be turned on in your organization settings
    page.
    """

    originating_party_name: Optional[str]
    """
    If present, this will replace your default company name on receiver's bank
    statement. This field can only be used for ACH payments currently. For ACH, only
    the first 16 characters of this string will be used. Any additional characters
    will be truncated.
    """

    priority: Literal["high", "normal"]
    """Either `normal` or `high`.

    For ACH and EFT payments, `high` represents a same-day ACH or EFT transfer,
    respectively. For check payments, `high` can mean an overnight check rather than
    standard mail.
    """

    purpose: Optional[str]
    """
    For `wire`, this is usually the purpose which is transmitted via the
    "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
    this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
    CPA Code that will be attached to the payment.
    """

    receiving_account: ReceivingAccount
    """Either `receiving_account` or `receiving_account_id` must be present.

    When using `receiving_account_id`, you may pass the id of an external account or
    an internal account.
    """

    receiving_account_id: str
    """Either `receiving_account` or `receiving_account_id` must be present.

    When using `receiving_account_id`, you may pass the id of an external account or
    an internal account.
    """

    remittance_information: Optional[str]
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    send_remittance_advice: Optional[bool]
    """Send an email to the counterparty when the payment order is sent to the bank.

    If `null`, `send_remittance_advice` on the Counterparty is used.
    """

    statement_descriptor: Optional[str]
    """An optional descriptor which will appear in the receiver's statement.

    For `check` payments this field will be used as the memo line. For `ach` the
    maximum length is 10 characters. Note that for ACH payments, the name on your
    bank account will be included automatically by the bank, so you can use the
    characters for other useful information. For `eft` the maximum length is 15
    characters.
    """

    subtype: Optional[Literal["CCD", "CIE", "CTX", "IAT", "PPD", "TEL", "WEB", "neft"]]
    """
    An additional layer of classification for the type of payment order you are
    doing. This field is only used for `ach` payment orders currently. For `ach`
    payment orders, the `subtype` represents the SEC code. We currently support
    `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.
    """

    transaction_monitoring_enabled: bool
    """
    A flag that determines whether a payment order should go through transaction
    monitoring.
    """

    ultimate_originating_party_identifier: Optional[str]
    """Identifier of the ultimate originator of the payment order."""

    ultimate_originating_party_name: Optional[str]
    """Name of the ultimate originator of the payment order."""

    ultimate_receiving_party_identifier: Optional[str]
    """Identifier of the ultimate funds recipient."""

    ultimate_receiving_party_name: Optional[str]
    """Name of the ultimate funds recipient."""
