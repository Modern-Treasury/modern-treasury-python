# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from datetime import date

from typing import Union, Iterable, Optional

from ..._utils import PropertyInfo

__all__ = ["BalanceReportCreateParams", "Balances", "Balance"]

class BalanceReportCreateParams(TypedDict, total=False):
    as_of_date: Required[Annotated[Union[str, date], PropertyInfo(format = "iso8601")]]
    """The date of the balance report in local time."""

    as_of_time: Required[str]
    """The time (24-hour clock) of the balance report in local time."""

    balance_report_type: Required[Literal["intraday", "other", "previous_day", "real_time"]]
    """The specific type of balance report.

    One of `intraday`, `previous_day`, `real_time`, or `other`.
    """

    balances: Required[Iterable[Balance]]
    """An array of `Balance` objects."""

class Balance(TypedDict, total=False):
    balance_type: Required[Literal["closing_available", "closing_ledger", "current_available", "current_ledger", "opening_available", "opening_available_next_business_day", "opening_ledger", "other", "previously_closed_book"]]
    """The specific type of balance reported.

    One of `opening_ledger`, `closing_ledger`, `current_ledger`,
    `opening_available`, `opening_available_next_business_day`, `closing_available`,
    `current_available`, 'previously_closed_book', or `other`.
    """

    vendor_code: Required[str]
    """The code used by the bank when reporting this specific balance."""

    vendor_code_type: Required[Optional[str]]
    """The type of `vendor_code` being reported.

    Can be one of `bai2`, `bankprov`, `bnk_dev`, `cleartouch`, `currencycloud`,
    `cross_river`, `dc_bank`, `dwolla`, `evolve`, `goldman_sachs`, `iso20022`,
    `jpmc`, `mx`, `silvergate`, `swift`, or `us_bank`.
    """

    amount: int
    """The balance amount."""

    amount_string: str
    """
    The amount of the balance as a string, preserving full precision for values that
    may exceed safe integer limits in some languages.
    """

Balances = Balance
"""This type is deprecated and will be removed in a future release.

Please use Balance instead.
"""