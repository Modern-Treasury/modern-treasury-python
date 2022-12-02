# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LedgerEntryListParams"]


class LedgerEntryListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    direction: Literal["credit", "debit"]
    """If true, response will include ledger entries that were deleted.

    When you update a ledger transaction to specify a new set of entries, the
    previous entries are deleted.
    """

    effective_at: Dict[str, str]
    """
    Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
    transaction's effective time. Format ISO8601
    """

    effective_date: Dict[str, str]
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
    ledger_account_lock_version%5Blte%5D=1000
    """

    ledger_transaction_id: str

    per_page: int

    show_deleted: bool
    """If true, response will include ledger entries that were deleted.

    When you update a ledger transaction to specify a new set of entries, the
    previous entries are deleted.
    """

    updated_at: Dict[str, str]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    updated_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """
