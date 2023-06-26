# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LineItemListParams"]


class LineItemListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    per_page: int

    type: Optional[Literal["originating", "receiving"]]
