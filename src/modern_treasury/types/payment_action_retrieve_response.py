# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PaymentActionRetrieveResponse"]


class PaymentActionRetrieveResponse(BaseModel):
    id: str

    actionable_id: Optional[str] = None
    """The ID of the associated actionable object."""

    actionable_type: Optional[str] = None
    """The type of the associated actionable object.

    One of `payment_order`, `expected_payment`.
    """

    created_at: datetime

    details: object
    """The specifc details of the payment action based on type."""

    internal_account_id: str
    """The ID of the internal account associated with the payment action."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    status: str
    """The current status of the payment action.

    One of `pending`, `processing`, `sent`, `cancelled`, or `failed`.
    """

    type: str
    """The type of the payment action. Determines the action to be taken."""

    updated_at: datetime
