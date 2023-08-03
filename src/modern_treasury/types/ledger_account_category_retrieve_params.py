# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LedgerAccountCategoryRetrieveParams", "Balances"]


class LedgerAccountCategoryRetrieveParams(TypedDict, total=False):
    balances: Balances
    """
    For example, if you want the balances as of a particular time (ISO8601), the
    encoded query string would be `balances%5Beffective_at%5D=2000-12-31T12:00:00Z`.
    The balances as of a time are inclusive of entries with that exact time.
    """


class Balances(TypedDict, total=False):
    as_of_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
