# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["LedgerAccountCategoryListParams"]


class LedgerAccountCategoryListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    ledger_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    name: str

    parent_ledger_account_category_id: str
    """Query categories that are nested underneath a parent category"""

    per_page: int
