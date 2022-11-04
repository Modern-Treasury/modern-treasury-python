# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = ["PaperItem"]


class PaperItem(BaseModel):
    account_number: Optional[str]
    """The account number on the paper item."""

    amount: int
    """The amount of the paper item."""

    check_number: Optional[str]
    """The check number on the paper item."""

    created_at: str

    currency: Optional[shared.Currency]
    """The currency of the paper item."""

    deposit_date: str
    """The date the paper item was deposited into your organization's bank account."""

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    lockbox_number: str
    """The identifier for the lockbox assigned by the bank."""

    memo_field: Optional[str]
    """The memo field on the paper item."""

    object: str

    remitter_name: Optional[str]
    """The name of the remitter on the paper item."""

    routing_number: Optional[str]
    """The routing number on the paper item."""

    status: Literal["completed", "pending", "returned"]
    """The current status of the paper item.

    One of `pending`, `completed`, or `returned`.
    """

    transaction_id: Optional[str]
    """The ID of the reconciled Transaction or `null`."""

    transaction_line_item_id: Optional[str]
    """The ID of the reconciled Transaction Line Item or `null`."""

    updated_at: str
