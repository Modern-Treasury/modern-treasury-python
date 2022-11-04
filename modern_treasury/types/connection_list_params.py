# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ConnectionListParams"]


class ConnectionListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    entity: str
    """A string code representing the vendor (i.e. bank)."""

    per_page: int

    vendor_customer_id: str
    """An identifier assigned by the vendor to your organization."""
