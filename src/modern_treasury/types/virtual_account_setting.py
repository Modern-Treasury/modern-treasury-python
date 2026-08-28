# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["VirtualAccountSetting"]


class VirtualAccountSetting(BaseModel):
    id: str

    created_at: datetime

    external_id: Optional[str] = None
    """A user-defined identifier for the virtual account setting."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime
