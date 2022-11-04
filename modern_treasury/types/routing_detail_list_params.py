# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RoutingDetailListParams"]


class RoutingDetailListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    per_page: int
