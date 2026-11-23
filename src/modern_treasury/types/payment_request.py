# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["PaymentRequest"]


class PaymentRequest(BaseModel):
    id: str

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    created_at: datetime

    currency: Currency
    """Three-letter ISO currency code."""

    description: Optional[str] = None

    internal_account_id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    requesting_party_name: str

    requesting_routing_number: str

    status: Literal["approved", "cancelled", "declined", "pending"]

    type: Literal["wire"]

    updated_at: datetime
