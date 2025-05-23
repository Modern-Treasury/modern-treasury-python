# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["BulkResultListParams"]


class BulkResultListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    entity_id: str
    """Unique identifier for the result entity object."""

    entity_type: Literal[
        "payment_order",
        "ledger_account",
        "ledger_transaction",
        "expected_payment",
        "transaction",
        "entity_link",
        "transaction_line_item",
        "bulk_error",
    ]
    """The type of the request that created this result.

    bulk_request is the only supported `request_type`
    """

    per_page: int

    request_id: str
    """Unique identifier for the request that created this bulk result.

    This is the ID of the bulk request when `request_type` is bulk_request
    """

    request_type: Literal["bulk_request"]
    """The type of the request that created this result.

    bulk_request is the only supported `request_type`
    """

    status: Literal["pending", "successful", "failed"]
    """One of successful or failed."""
