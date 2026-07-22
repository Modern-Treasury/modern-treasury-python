# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Dict, Optional

__all__ = ["LineItemListParams"]

class LineItemListParams(TypedDict, total=False):
    id: Dict[str, str]

    after_cursor: Optional[str]

    per_page: int

    transaction_id: str

    type: Optional[Literal["originating", "receiving"]]