# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    created_at: str

    data: object
    """The body of the event."""

    entity_id: str
    """The ID of the entity for the event."""

    event_name: str
    """The name of the event."""

    event_time: str
    """The time of the event."""

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    resource: str
    """The type of resource for the event."""

    updated_at: str
