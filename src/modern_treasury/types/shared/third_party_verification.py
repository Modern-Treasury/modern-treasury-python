# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ThirdPartyVerification"]


class ThirdPartyVerification(BaseModel):
    outcome: Literal["passed", "failed"]
    """The outcome of the verification. One of `passed` or `failed`."""

    vendor: Literal["persona", "middesk", "alloy", "sumsub", "veriff"]
    """The vendor that performed the verification, e.g. `persona`."""

    vendor_verification_id: str
    """The identification of the third party verification in `vendor`'s system."""

    verification_category: Literal["legal_name", "date_of_birth", "address", "government_id_number", "adverse_media"]
    """The category of verification performed."""

    verification_method: str
    """The method used to perform the verification."""

    verification_time: datetime
    """The timestamp when the verification was performed."""

    comment: Optional[str] = None
    """An optional comment about the verification."""
