# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional

__all__ = ["ConnectionLegalEntityListParams"]

class ConnectionLegalEntityListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    connection_id: str

    legal_entity_id: str

    per_page: int

    status: Literal["completed", "denied", "failed", "processing", "suspended"]