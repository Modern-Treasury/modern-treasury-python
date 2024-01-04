# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .shared import Currency
from .._models import BaseModel

__all__ = ["PaperItem"]


class PaperItem(BaseModel):
    id: str

    account_number: Optional[str] = None
    """The account number on the paper item."""

    account_number_safe: Optional[str] = None
    """The last 4 digits of the account_number."""

    amount: int
    """The amount of the paper item."""

    check_number: Optional[str] = None
    """The check number on the paper item."""

    created_at: datetime

    currency: Optional[Currency] = None
    """The currency of the paper item."""

    deposit_date: date
    """The date the paper item was deposited into your organization's bank account."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    lockbox_number: str
    """The identifier for the lockbox assigned by the bank."""

    memo_field: Optional[str] = None
    """The memo field on the paper item."""

    object: str

    remitter_name: Optional[str] = None
    """The name of the remitter on the paper item."""

    routing_number: Optional[str] = None
    """The routing number on the paper item."""

    status: Literal["completed", "pending", "returned"]
    """The current status of the paper item.

    One of `pending`, `completed`, or `returned`.
    """

    transaction_id: Optional[str] = None
    """The ID of the reconciled Transaction or `null`."""

    transaction_line_item_id: Optional[str] = None
    """The ID of the reconciled Transaction Line Item or `null`."""

    updated_at: datetime
