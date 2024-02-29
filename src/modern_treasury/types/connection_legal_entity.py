# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectionLegalEntity"]


class ConnectionLegalEntity(BaseModel):
    id: Optional[str] = None

    connection_id: Optional[str] = None
    """The ID of the connection."""

    created_at: Optional[datetime] = None

    discarded_at: Optional[datetime] = None

    legal_entity_id: Optional[str] = None
    """The ID of the legal entity."""

    live_mode: Optional[bool] = None
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str] = None

    status: Optional[Literal["completed", "denied", "failed", "processing"]] = None
    """The status of the connection legal entity."""

    updated_at: Optional[datetime] = None
