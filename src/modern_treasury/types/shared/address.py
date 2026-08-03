# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    id: str

    country: Optional[str] = None
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: datetime

    line1: Optional[str] = None

    line2: Optional[str] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[str] = None
    """Locality or City."""

    object: str

    postal_code: Optional[str] = None
    """The postal code of the address."""

    region: Optional[str] = None
    """Region or State."""

    updated_at: datetime
