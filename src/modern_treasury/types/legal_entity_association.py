# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LegalEntityAssociation"]


class LegalEntityAssociation(BaseModel):
    id: str

    child_legal_entity: "ChildLegalEntity"
    """The child legal entity."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    ownership_percentage: Optional[int] = None
    """The child entity's ownership percentage iff they are a beneficial owner."""

    parent_legal_entity_id: str
    """The ID of the parent legal entity.

    This must be a business or joint legal entity.
    """

    relationship_types: List[Literal["authorized_signer", "beneficial_owner", "control_person"]]

    title: Optional[str] = None
    """The job title of the child entity at the parent entity."""

    updated_at: datetime


from .child_legal_entity import ChildLegalEntity
