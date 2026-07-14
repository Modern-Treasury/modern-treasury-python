# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

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
    """Translation missing: en.openapi.descriptions.payment_order.query_params.status"""

    target_id: Optional[str]
    """
    Translation missing:
    en.openapi.descriptions.payment_order.query_params.target_id
    """

    target_type: Optional[Literal["payment_order"]]
    """
    Translation missing:
    en.openapi.descriptions.payment_order.query_params.target_type
    """
