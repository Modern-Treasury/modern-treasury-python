# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..shared import Currency
from ..._models import BaseModel

__all__ = ["BalanceReport", "Balances", "Balance"]


class Balance(BaseModel):
    id: str

    amount: int
    """The balance amount."""

    balance_type: Literal[
        "closing_available",
        "closing_ledger",
        "current_available",
        "current_ledger",
        "opening_available",
        "opening_available_next_business_day",
        "opening_ledger",
        "other",
    ]
    """The specific type of balance reported.

    One of `opening_ledger`, `closing_ledger`, `current_ledger`,
    `opening_available`, `opening_available_next_business_day`, `closing_available`,
    `current_available`, or `other`.
    """

    created_at: datetime

    currency: Optional[Currency] = None
    """The currency of the balance."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime

    vendor_code: str
    """The code used by the bank when reporting this specific balance."""

    vendor_code_type: Optional[str] = None
    """The type of `vendor_code` being reported.

    Can be one of `bai2`, `bankprov`, `bnk_dev`, `cleartouch`, `currencycloud`,
    `cross_river`, `dc_bank`, `dwolla`, `evolve`, `goldman_sachs`, `iso20022`,
    `jpmc`, `mx`, `signet`, `silvergate`, `swift`, or `us_bank`.
    """


Balances = Balance
"""This type is deprecated and will be removed in a future release.

Please use Balance instead.
"""


class BalanceReport(BaseModel):
    id: str

    as_of_date: date
    """The date of the balance report in local time."""

    as_of_time: Optional[str] = None
    """The time (24-hour clock) of the balance report in local time."""

    balance_report_type: Literal["intraday", "other", "previous_day", "real_time"]
    """The specific type of balance report.

    One of `intraday`, `previous_day`, `real_time`, or `other`.
    """

    balances: List[Balance]
    """An array of `Balance` objects."""

    created_at: datetime

    internal_account_id: str
    """The ID of one of your organization's Internal Accounts."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime
