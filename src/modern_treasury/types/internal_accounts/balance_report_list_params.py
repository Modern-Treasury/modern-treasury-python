# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BalanceReportListParams"]


class BalanceReportListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    as_of_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The date of the balance report in local time."""

    balance_report_type: Literal["intraday", "other", "previous_day", "real_time"]
    """The specific type of balance report.

    One of `intraday`, `previous_day`, `real_time`, or `other`.
    """

    per_page: int
