# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AddressRequest"]


class AddressRequest(BaseModel):
    country: Optional[str] = None
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str] = None

    line2: Optional[str] = None

    locality: Optional[str] = None
    """Locality or City."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    region: Optional[str] = None
    """Region or State."""
