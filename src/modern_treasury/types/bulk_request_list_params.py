# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["BulkRequestListParams"]


class BulkRequestListParams(TypedDict, total=False):
    action_type: Literal["create", "update", "delete"]
    """One of create, or update."""

    after_cursor: Optional[str]

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    resource_type: Literal["payment_order", "ledger_transaction", "transaction", "expected_payment"]
    """One of payment_order, expected_payment, or ledger_transaction."""

    status: Literal["pending", "processing", "completed"]
    """One of pending, processing, or completed."""
