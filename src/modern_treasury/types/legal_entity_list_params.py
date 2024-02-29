# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LegalEntityListParams"]


class LegalEntityListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    legal_entity_type: Literal["business", "individual"]

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    show_deleted: str
