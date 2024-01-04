# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Reversal"]


class Reversal(BaseModel):
    id: str

    created_at: datetime

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

    payment_order_id: Optional[str] = None
    """The ID of the relevant Payment Order."""

    reason: Literal[
        "duplicate",
        "incorrect_amount",
        "incorrect_receiving_account",
        "date_earlier_than_intended",
        "date_later_than_intended",
    ]
    """The reason for the reversal."""

    status: Literal["completed", "failed", "pending", "processing", "returned", "sent"]
    """The current status of the reversal."""

    updated_at: datetime
