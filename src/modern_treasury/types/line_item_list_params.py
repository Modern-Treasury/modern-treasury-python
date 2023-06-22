# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LineItemListParams"]


class LineItemListParams(TypedDict, total=False):
    itemizable_type: Required[Literal["expected_payments", "payment_orders"]]

    after_cursor: Optional[str]

    per_page: int
