# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    entity_id: str

    event_name: str

    event_time_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """An inclusive upper bound for when the event occurred"""

    event_time_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """An inclusive lower bound for when the event occurred"""

    per_page: int

    resource: str
