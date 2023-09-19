# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LineItemListParams"]


class LineItemListParams(TypedDict, total=False):
    id: Dict[str, str]

    after_cursor: Optional[str]

    per_page: int

    transaction_id: str

    type: Optional[Literal["originating", "receiving"]]
