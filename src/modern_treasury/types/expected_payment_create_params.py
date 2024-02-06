# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .shared import Currency, TransactionDirection
from .._utils import PropertyInfo
from .expected_payment_type import ExpectedPaymentType

__all__ = [
    "ExpectedPaymentCreateParams",
    "LedgerTransaction",
    "LedgerTransactionLedgerEntries",
    "LedgerTransactionLedgerEntry",
    "LineItems",
    "LineItem",
]


class ExpectedPaymentCreateParams(TypedDict, total=False):
    amount_lower_bound: Required[int]
    """The lowest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_upper_bound: Required[int]
    """The highest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    direction: Required[TransactionDirection]
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: Required[str]
    """The ID of the Internal Account for the expected payment."""

    counterparty_id: Optional[str]
    """The ID of the counterparty you expect for this payment."""

    currency: Optional[Currency]
    """Must conform to ISO 4217. Defaults to the currency of the internal account."""

    date_lower_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The earliest date the payment may come in. Format: yyyy-mm-dd"""

    date_upper_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The latest date the payment may come in. Format: yyyy-mm-dd"""

    description: Optional[str]
    """An optional description for internal use."""

    ledger_transaction: LedgerTransaction
    """
    Specifies a ledger transaction object that will be created with the expected
    payment. If the ledger transaction cannot be created, then the expected payment
    creation will fail. The resulting ledger transaction will mirror the status of
    the expected payment.
    """

    ledger_transaction_id: str
    """Either ledger_transaction or ledger_transaction_id can be provided.

    Only a pending ledger transaction can be attached upon expected payment
    creation. Once the expected payment is created, the status of the ledger
    transaction tracks the expected payment automatically.
    """

    line_items: Iterable[LineItem]

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    reconciliation_filters: Optional[object]
    """The reconciliation filters you have for this payment."""

    reconciliation_groups: Optional[object]
    """The reconciliation groups you have for this payment."""

    reconciliation_rule_variables: Optional[Iterable[object]]
    """An array of reconciliation rule variables for this payment."""

    remittance_information: Optional[str]
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    statement_descriptor: Optional[str]
    """The statement description you expect to see on the transaction.

    For ACH payments, this will be the full line item passed from the bank. For wire
    payments, this will be the OBI field on the wire. For check payments, this will
    be the memo field.
    """

    type: Optional[ExpectedPaymentType]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet, wire.
    """


class LedgerTransactionLedgerEntry(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    direction: Required[TransactionDirection]
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

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
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

    show_resulting_ledger_account_balances: Optional[bool]
    """
    If true, response will include the balance of the associated ledger account for
    the entry.
    """


LedgerTransactionLedgerEntries = LedgerTransactionLedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use LedgerTransactionLedgerEntry instead.
"""


class LedgerTransaction(TypedDict, total=False):
    ledger_entries: Required[Iterable[LedgerTransactionLedgerEntry]]
    """An array of ledger entry objects."""

    description: Optional[str]
    """An optional description for internal use."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
    purposes.
    """

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


class LineItem(TypedDict, total=False):
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


LineItems = LineItem
"""This type is deprecated and will be removed in a future release.

Please use LineItem instead.
"""
