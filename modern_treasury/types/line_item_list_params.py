# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LineItemListParams"]


class LineItemListParams(TypedDict, total=False):
    after_cursor: str

    per_page: int
