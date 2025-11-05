# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HoldListResponse"]


class HoldListResponse(BaseModel):
    id: str

    created_at: datetime

    object: Literal["hold"]
    """The type of object"""

    status: Literal["active", "resolved"]
    """The status of the hold"""

    target_id: str
    """The ID of the target being held"""

    target_type: Literal["payment_order"]
    """The type of target being held"""

    updated_at: datetime

    live_mode: Optional[bool] = None
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the hold"""

    reason: Optional[str] = None
    """The reason for the hold"""

    resolution: Optional[str] = None
    """The resolution of the hold"""

    resolved_at: Optional[datetime] = None
    """When the hold was resolved"""
