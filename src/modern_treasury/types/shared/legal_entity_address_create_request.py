# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LegalEntityAddressCreateRequest"]


class LegalEntityAddressCreateRequest(BaseModel):
    country: Optional[str] = None
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str] = None

    locality: Optional[str] = None
    """Locality or City."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    region: Optional[str] = None
    """Region or State."""

    address_types: Optional[List[Literal["business", "mailing", "other", "po_box", "residential"]]] = None
    """The types of this address."""

    line2: Optional[str] = None
