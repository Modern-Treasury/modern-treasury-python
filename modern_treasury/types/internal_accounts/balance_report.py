# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Balances", "BalanceReport"]


class Balances(BaseModel):
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

    created_at: str

    currency: Optional[shared.Currency]
    """The currency of the balance."""

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: str

    vendor_code: str
    """The code used by the bank when reporting this specific balance."""

    vendor_code_type: Optional[
        Literal[
            "bai2",
            "bankprov",
            "bnk_dev",
            "cleartouch",
            "cross_river",
            "currencycloud",
            "dc_bank",
            "dwolla",
            "goldman_sachs",
            "iso20022",
            "jpmc",
            "mx",
            "signet",
            "silvergate",
            "swift",
            "us_bank",
        ]
    ]
    """The code used by the bank when reporting this specific balance."""


class BalanceReport(BaseModel):
    as_of_date: str
    """The date of the balance report in local time."""

    as_of_time: Optional[str]
    """The time (24-hour clock) of the balance report in local time."""

    balance_report_type: Literal["intraday", "other", "previous_day", "real_time"]
    """The specific type of balance report.

    One of `intraday`, `previous_day`, `real_time`, or `other`.
    """

    balances: List[Balances]
    """An array of `Balance` objects."""

    created_at: str

    id: str

    internal_account_id: str
    """The ID of one of your organization's Internal Accounts."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: str
