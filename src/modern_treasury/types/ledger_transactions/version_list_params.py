# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import TypedDict

__all__ = ["VersionListParams"]


class VersionListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    created_at: Dict[str, Union[str, datetime]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    created_at timestamp. For example, for all dates after Jan 1 2000 12:00 UTC, use
    created_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """

    ledger_account_statement_id: str
    """
    Get all ledger transaction versions that are included in the ledger account
    statement.
    """

    ledger_transaction_id: str
    """
    Get all the ledger transaction versions corresponding to the ID of a ledger
    transaction.
    """

    per_page: int

    version: Dict[str, int]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    version. For example, for all versions after 2, use version%5Bgt%5D=2.
    """
