# File generated from our OpenAPI spec by Stainless.

from typing import Dict
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BulkRequest"]


class BulkRequest(BaseModel):
    id: str

    action_type: Literal["create", "update"]
    """One of create, or update."""

    created_at: datetime

    failed_result_count: int
    """Total number of failed bulk results so far for this request"""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    object: str

    resource_type: Literal["payment_order", "ledger_transaction", "expected_payment"]
    """One of payment_order, expected_payment, or ledger_transaction."""

    status: Literal["pending", "processing", "completed"]
    """One of pending, processing, or completed."""

    success_result_count: int
    """Total number of successful bulk results so far for this request"""

    total_resource_count: int
    """Total number of items in the `resources` array.

    Once a bulk request is completed, `success_result_count` + `failed_result_count`
    will be equal to `total_result_count`.
    """

    updated_at: datetime
