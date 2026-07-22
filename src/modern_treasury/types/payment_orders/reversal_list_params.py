# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

__all__ = ["ReversalListParams"]

class ReversalListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    per_page: int