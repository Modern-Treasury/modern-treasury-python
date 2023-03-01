# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaperItemListParams"]


class PaperItemListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    deposit_date_end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date"""

    deposit_date_start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date"""

    lockbox_number: str
    """
    Specify `lockbox_number` if you wish to see paper items that are associated with
    a specific lockbox number.
    """

    per_page: int
