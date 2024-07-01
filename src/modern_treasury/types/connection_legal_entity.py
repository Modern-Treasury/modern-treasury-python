# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectionLegalEntity"]


class ConnectionLegalEntity(BaseModel):
    id: str

    connection_id: str
    """The ID of the connection."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    legal_entity_id: str
    """The ID of the legal entity."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    status: Literal["completed", "denied", "failed", "processing"]
    """The status of the connection legal entity."""

    updated_at: datetime

    vendor_id: str
    """The ID of the legal entity at the vendor."""
