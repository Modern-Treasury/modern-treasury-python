# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LegalEntityAddressCreateRequest"]


class LegalEntityAddressCreateRequest(TypedDict, total=False):
    country: Required[Optional[str]]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Required[Optional[str]]

    locality: Required[Optional[str]]
    """Locality or City.

    Use the full city name rather than an abbreviation (e.g. San Francisco).
    """

    postal_code: Required[Optional[str]]
    """The postal code of the address."""

    region: Required[Optional[str]]
    """Region or State.

    This field is free-form; for US states, we recommend a two-letter code (e.g.
    CA). Full state names are also accepted.
    """

    address_types: List[
        Literal["business", "business_physical", "business_registered", "mailing", "other", "po_box", "residential"]
    ]
    """The types of this address."""

    line2: Optional[str]

    primary: Optional[bool]
    """Whether this address is the primary address for the legal entity.

    Optional; when omitted it is inferred from the address types.
    """
