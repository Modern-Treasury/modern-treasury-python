# File generated from our OpenAPI spec by Stainless.

from typing import Dict
from datetime import datetime

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    id: str

    created_at: datetime

    data: Dict[str, object]
    """The body of the event."""

    entity_id: str
    """The ID of the entity for the event."""

    event_name: str
    """The name of the event."""

    event_time: datetime
    """The time of the event."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    resource: str
    """The type of resource for the event."""

    updated_at: datetime
