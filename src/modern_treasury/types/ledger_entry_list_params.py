# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypedDict

from .shared import TransactionDirection

__all__ = ["LedgerEntryListParams", "OrderBy"]


class LedgerEntryListParams(TypedDict, total=False):
    id: List[str]
    """
    If you have specific IDs to retrieve in bulk, you can pass them as query
    parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.
    """

    after_cursor: Optional[str]

    as_of_lock_version: int
    """
    Shows all ledger entries that were present on a ledger account at a particular
    `lock_version`. You must also specify `ledger_account_id`.
    """

    direction: TransactionDirection
    """If true, response will include ledger entries that were deleted.

    When you update a ledger transaction to specify a new set of entries, the
    previous entries are deleted.
    """

    effective_at: Dict[str, Union[str, datetime]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    transaction's effective time. Format ISO8601
    """

    effective_date: Dict[str, Union[str, date]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    transaction's effective date. Format YYYY-MM-DD
    """

    ledger_account_category_id: str
    """Get all ledger entries that match the direction specified.

    One of `credit`, `debit`.
    """

    ledger_account_id: str

    ledger_account_lock_version: Dict[str, int]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    lock_version of a ledger account. For example, for all entries created at or
    before before lock_version 1000 of a ledger account, use
    `ledger_account_lock_version%5Blte%5D=1000`.
    """

    ledger_account_payout_id: str

    ledger_account_settlement_id: str

    ledger_account_statement_id: str
    """Get all ledger entries that are included in the ledger account statement."""

    ledger_transaction_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    order_by: OrderBy
    """Order by `created_at` or `effective_at` in `asc` or `desc` order.

    For example, to order by `effective_at asc`, use
    `order_by%5Beffective_at%5D=asc`. Ordering by only one field at a time is
    supported.
    """

    per_page: int

    show_balances: bool
    """If true, response will include the balances attached to the ledger entry.

    If there is no balance available, null will be returned instead.
    """

    show_deleted: bool
    """If true, response will include ledger entries that were deleted.

    When you update a ledger transaction to specify a new set of entries, the
    previous entries are deleted.
    """

    status: Literal["pending", "posted", "archived"]
    """Get all ledger entries that match the status specified.

    One of `pending`, `posted`, or `archived`.
    """

    updated_at: Dict[str, Union[str, datetime]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    updated_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """


class OrderBy(TypedDict, total=False):
    created_at: Literal["asc", "desc"]

    effective_at: Literal["asc", "desc"]
