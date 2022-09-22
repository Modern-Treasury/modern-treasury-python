# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    entity_id: str

    event_name: str

    event_time_end: str
    """An inclusive upper bound for when the event occurred"""

    event_time_start: str
    """An inclusive lower bound for when the event occurred"""

    per_page: int

    resource: str
