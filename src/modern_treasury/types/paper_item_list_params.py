# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PaperItemListParams"]


class PaperItemListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    deposit_date_end: str
    """Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date"""

    deposit_date_start: str
    """Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date"""

    lockbox_number: str
    """
    Specify `lockbox_number` if you wish to see paper items that are associated with
    a specific lockbox number.
    """

    per_page: int
