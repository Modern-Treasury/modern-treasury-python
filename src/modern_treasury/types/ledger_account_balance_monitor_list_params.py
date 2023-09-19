# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import TypedDict

__all__ = ["LedgerAccountBalanceMonitorListParams"]


class LedgerAccountBalanceMonitorListParams(TypedDict, total=False):
    id: List[str]
    """
    If you have specific IDs to retrieve in bulk, you can pass them as query
    parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.
    """

    after_cursor: Optional[str]

    ledger_account_id: str
    """Query the balance monitors for a single ledger account."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int
