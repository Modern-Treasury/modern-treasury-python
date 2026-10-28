# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LegalEntityRegulator"]


class LegalEntityRegulator(TypedDict, total=False):
    jurisdiction: Required[str]
    """
    The country code where the regulator operates in the ISO 3166-1 alpha-2 format
    (e.g., "US", "CA", "GB").
    """

    name: Required[str]
    """Full name of the regulatory body."""

    registration_number: Required[str]
    """Registration or identification number with the regulator."""
