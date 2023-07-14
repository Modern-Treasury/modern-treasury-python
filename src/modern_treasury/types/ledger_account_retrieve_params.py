# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LedgerAccountRetrieveParams", "Balances"]


class LedgerAccountRetrieveParams(TypedDict, total=False):
    balances: Balances
    """
    Use `balances[effective_at_lower_bound]` and
    `balances[effective_at_upper_bound]` to get the balances change between the two
    timestamps. The lower bound is inclusive while the upper bound is exclusive of
    the provided timestamps. If no value is supplied the balances will be retrieved
    not including that bound. Use `balances[as_of_lock_version]` to retrieve a
    balance as of a specific Ledger Account `lock_version`.
    """


class Balances(TypedDict, total=False):
    as_of_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    as_of_lock_version: int

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    effective_at_lower_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    effective_at_upper_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
