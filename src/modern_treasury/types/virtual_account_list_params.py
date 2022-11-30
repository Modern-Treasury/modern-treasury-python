# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["VirtualAccountListParams"]


class VirtualAccountListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str

    internal_account_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int
