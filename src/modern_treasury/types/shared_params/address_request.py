# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AddressRequest"]


class AddressRequest(TypedDict, total=False):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str]

    line2: Optional[str]

    locality: Optional[str]
    """Locality or City.

    Use the full city name rather than an abbreviation (e.g. San Francisco).
    """

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State.

    This field is free-form; for US states, we recommend a two-letter code (e.g.
    CA). Full state names are also accepted.
    """
