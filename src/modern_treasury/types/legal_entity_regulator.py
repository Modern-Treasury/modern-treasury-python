# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LegalEntityRegulator"]


class LegalEntityRegulator(BaseModel):
    jurisdiction: str
    """
    The country code where the regulator operates in the ISO 3166-1 alpha-2 format
    (e.g., "US", "CA", "GB").
    """

    name: str
    """Full name of the regulatory body."""

    registration_number: str
    """Registration or identification number with the regulator."""
