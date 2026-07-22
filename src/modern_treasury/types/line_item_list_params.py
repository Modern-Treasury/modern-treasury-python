# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import Optional

__all__ = ["LineItemListParams"]

class LineItemListParams(TypedDict, total=False):
    itemizable_type: Required[Literal["expected_payments", "payment_orders"]]

    after_cursor: Optional[str]

    per_page: int