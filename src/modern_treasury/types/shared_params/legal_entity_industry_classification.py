# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LegalEntityIndustryClassification"]


class LegalEntityIndustryClassification(TypedDict, total=False):
    id: Required[str]

    classification_codes: Required[List[str]]
    """The industry classification codes for the legal entity."""

    classification_type: Required[
        Literal[
            "anzsic",
            "bics",
            "gics",
            "hsics",
            "icb",
            "isic",
            "mgecs",
            "nace",
            "naics",
            "rbics",
            "sic",
            "sni",
            "trbc",
            "uksic",
            "unspsc",
        ]
    ]
    """The classification system of the classification codes."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
