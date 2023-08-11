# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LedgerAccountCategoryListParams", "Balances"]


class LedgerAccountCategoryListParams(TypedDict, total=False):
    id: List[str]
    """
    If you have specific IDs to retrieve in bulk, you can pass them as query
    parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.
    """

    after_cursor: Optional[str]

    balances: Balances
    """
    For example, if you want the balances as of a particular time (ISO8601), the
    encoded query string would be `balances%5Beffective_at%5D=2000-12-31T12:00:00Z`.
    The balances as of a time are inclusive of entries with that exact time.
    """

    ledger_account_id: str
    """
    Query categories which contain a ledger account directly or through child
    categories.
    """

    ledger_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    name: str

    parent_ledger_account_category_id: str
    """Query categories that are nested underneath a parent category"""

    per_page: int


class Balances(TypedDict, total=False):
    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
