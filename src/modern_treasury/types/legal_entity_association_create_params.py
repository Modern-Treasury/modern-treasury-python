# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.child_legal_entity_create import ChildLegalEntityCreate

__all__ = ["LegalEntityAssociationCreateParams"]


class LegalEntityAssociationCreateParams(TypedDict, total=False):
    parent_legal_entity_id: Required[str]
    """The ID of the parent legal entity.

    This must be a business or joint legal entity.
    """

    relationship_types: Required[List[Literal["authorized_signer", "beneficial_owner", "control_person"]]]

    child_legal_entity: ChildLegalEntityCreate
    """The child legal entity."""

    child_legal_entity_id: str
    """The ID of the child legal entity."""

    ownership_percentage: Optional[int]
    """The child entity's ownership percentage iff they are a beneficial owner."""

    title: Optional[str]
    """The job title of the child entity at the parent entity."""
