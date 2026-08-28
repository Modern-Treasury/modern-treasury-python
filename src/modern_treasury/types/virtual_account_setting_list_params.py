# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VirtualAccountSettingListParams"]


class VirtualAccountSettingListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    external_id: str
    """A user-defined identifier for the virtual account setting."""

    per_page: int
