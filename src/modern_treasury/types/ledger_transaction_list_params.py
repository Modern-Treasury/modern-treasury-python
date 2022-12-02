# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LedgerTransactionListParams"]


class LedgerTransactionListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    effective_at: Dict[str, str]
    """
    Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by
    effective at. For example, for all transactions after Jan 1 2000, use
    effective_at%5Bgt%5D=2000-01-01T00:00:00:00.000Z.
    """

    effective_date: Dict[str, str]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by
    effective date. For example, for all dates after Jan 1 2000, use
    effective_date%5Bgt%5D=2000-01-01.
    """

    external_id: str

    ledger_account_category_id: str

    ledger_account_id: str

    ledger_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    posted_at: Dict[str, str]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    posted_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """

    status: Literal["pending", "posted", "archived"]

    updated_at: Dict[str, str]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    updated_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """
