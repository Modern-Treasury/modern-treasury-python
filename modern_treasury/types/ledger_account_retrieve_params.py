# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Balances", "LedgerAccountRetrieveParams"]


class Balances(TypedDict, total=False):
    as_of_date: str


class LedgerAccountRetrieveParams(TypedDict, total=False):
    balances: Balances
    """
    For example, if you want the balances as of a particular effective date
    (YYYY-MM-DD), the encoded query string would be
    balances%5Bas_of_date%5D=2000-12-31. The balances as of a date are inclusive of
    entries with that exact date.
    """
