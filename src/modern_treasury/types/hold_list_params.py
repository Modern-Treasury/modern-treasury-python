# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional, Dict

__all__ = ["HoldListParams"]

class HoldListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    status: Optional[Literal["active", "resolved"]]
    """Only return holds for a specific status."""

    target_id: Optional[str]
    """Only return holds for a specific target ID."""

    target_type: Optional[Literal["payment_order"]]
    """Only return holds for a specific target type."""