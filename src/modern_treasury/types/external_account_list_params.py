# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ExternalAccountListParams"]


class ExternalAccountListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    party_name: str
    """Searches the ExternalAccount's party_name AND the Counterparty's party_name"""

    per_page: int
