# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LegalEntityIndustryClassification"]


class LegalEntityIndustryClassification(BaseModel):
    id: str

    classification_codes: List[str]
    """The industry classification codes for the legal entity."""

    classification_type: Literal[
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
    """The classification system of the classification codes."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime
