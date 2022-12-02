# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["Balances", "LedgerAccountListParams"]


class Balances(TypedDict, total=False):
    as_of_date: str


class LedgerAccountListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    balances: Balances
    """
    For example, if you want the balances as of a particular effective date
    (YYYY-MM-DD), the encoded query string would be
    balances%5Bas_of_date%5D=2000-12-31. The balances as of a date are inclusive of
    entries with that exact date.
    """

    id: str

    ledger_account_category_id: str

    ledger_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    name: str

    per_page: int

    updated_at: Dict[str, str]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    updated_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """
