# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LegalEntityAssociationInlineCreate"]


class LegalEntityAssociationInlineCreate(BaseModel):
    relationship_types: List[Literal["authorized_signer", "beneficial_owner", "control_person"]]

    child_legal_entity: Optional["ChildLegalEntityCreate"] = None
    """The child legal entity."""

    child_legal_entity_id: Optional[str] = None
    """The ID of the child legal entity."""

    ownership_percentage: Optional[int] = None
    """The child entity's ownership percentage iff they are a beneficial owner."""

    title: Optional[str] = None
    """The job title of the child entity at the parent entity."""


from .child_legal_entity_create import ChildLegalEntityCreate
