# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .shared import TransactionDirection
from .._utils import PropertyInfo

__all__ = ["LedgerTransactionUpdateParams", "LedgerEntries", "LedgerEntry"]


class LedgerTransactionUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """An optional description for internal use."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    ledger_entries: Iterable[LedgerEntry]
    """An array of ledger entry objects."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Literal["archived", "pending", "posted"]
    """To post a ledger transaction at creation, use `posted`."""


class LedgerEntry(TypedDict, total=False):
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


LedgerEntries = LedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use LedgerEntry instead.
"""
