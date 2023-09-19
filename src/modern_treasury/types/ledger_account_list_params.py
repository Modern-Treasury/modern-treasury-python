# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LedgerAccountListParams",
    "AvailableBalanceAmount",
    "Balances",
    "PendingBalanceAmount",
    "PostedBalanceAmount",
]


class LedgerAccountListParams(TypedDict, total=False):
    id: List[str]
    """
    If you have specific IDs to retrieve in bulk, you can pass them as query
    parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.
    """

    after_cursor: Optional[str]

    available_balance_amount: AvailableBalanceAmount
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
    filter by balance amount.
    """

    balances: Balances
    """
    Use `balances[effective_at_lower_bound]` and
    `balances[effective_at_upper_bound]` to get the balances change between the two
    timestamps. The lower bound is inclusive while the upper bound is exclusive of
    the provided timestamps. If no value is supplied the balances will be retrieved
    not including that bound.
    """

    created_at: Dict[str, Union[str, datetime]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    created at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    created_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """

    currency: str

    ledger_account_category_id: str

    ledger_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    name: str

    pending_balance_amount: PendingBalanceAmount
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
    filter by balance amount.
    """

    per_page: int

    posted_balance_amount: PostedBalanceAmount
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
    filter by balance amount.
    """

    updated_at: Dict[str, Union[str, datetime]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    updated at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    updated_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """


class AvailableBalanceAmount(TypedDict, total=False):
    eq: int

    gt: int

    gte: int

    lt: int

    lte: int

    not_eq: int


class Balances(TypedDict, total=False):
    as_of_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    effective_at_lower_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    effective_at_upper_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class PendingBalanceAmount(TypedDict, total=False):
    eq: int

    gt: int

    gte: int

    lt: int

    lte: int

    not_eq: int


class PostedBalanceAmount(TypedDict, total=False):
    eq: int

    gt: int

    gte: int

    lt: int

    lte: int

    not_eq: int
