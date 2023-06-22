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
    For example, if you want the balances as of a particular effective date
    (YYYY-MM-DD), the encoded query string would be
    balances%5Bas_of_date%5D=2000-12-31. The balances as of a date are exclusive of
    entries with that exact date.
    """


class Balances(TypedDict, total=False):
    as_of_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
