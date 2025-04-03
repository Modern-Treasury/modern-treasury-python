# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LegalEntityComplianceDetail"]


class LegalEntityComplianceDetail(BaseModel):
    id: str

    created_at: datetime

    discarded_at: Optional[datetime] = None

    issuer: str
    """The issuer of the compliance token."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    token_expires_at: Optional[datetime] = None
    """The timestamp when the compliance token expires."""

    token_issued_at: Optional[datetime] = None
    """The timestamp when the compliance token was issued."""

    token_url: Optional[str] = None
    """The URL to the compliance token. (ex. provider portal URL)"""

    updated_at: datetime

    validated: bool
    """Whether entity corresponding to the compliance token has been validated."""

    validated_at: Optional[datetime] = None
    """The timestamp when the entity was validated."""
