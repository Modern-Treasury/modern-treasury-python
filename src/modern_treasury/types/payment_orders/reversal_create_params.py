# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..shared import TransactionDirection
from ..._utils import PropertyInfo

__all__ = [
    "ReversalCreateParams",
    "LedgerTransaction",
    "LedgerTransactionLedgerEntries",
    "LedgerTransactionLedgerEntry",
]


class ReversalCreateParams(TypedDict, total=False):
    reason: Required[
        Literal[
            "duplicate",
            "incorrect_amount",
            "incorrect_receiving_account",
            "date_earlier_than_intended",
            "date_later_than_intended",
        ]
    ]
    """The reason for the reversal.

    Must be one of `duplicate`, `incorrect_amount`, `incorrect_receiving_account`,
    `date_earlier_than_intended`, `date_later_than_intended`.
    """

    ledger_transaction: LedgerTransaction
    """Specifies a ledger transaction object that will be created with the reversal.

    If the ledger transaction cannot be created, then the reversal creation will
    fail. The resulting ledger transaction will mirror the status of the reversal.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
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
