# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EmbeddableFlowListParams"]


class EmbeddableFlowListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    per_page: int

    status: str

    template: Literal["legal_entity_onboarding", "account_collection", "payment"]
