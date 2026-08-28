# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["CaseListParams"]


class CaseListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    per_page: int

    status: Literal["open", "resolved"]
    """The status of the case."""

    subject_id: str
    """The ID of the object the case is about."""

    subject_type: Literal["legal_entity"]
    """The type of the object the case is about."""
