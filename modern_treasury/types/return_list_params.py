# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ReturnListParams"]


class ReturnListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str
    """
    Specify `counterparty_id` if you wish to see returns that occurred with a
    specific counterparty.
    """

    internal_account_id: str
    """
    Specify `internal_account_id` if you wish to see returns to/from a specific
    account.
    """

    per_page: int

    returnable_id: str
    """The ID of a valid returnable. Must be accompanied by `returnable_type`."""

    returnable_type: Literal["incoming_payment_detail", "paper_item", "payment_order", "reversal"]
    """One of `payment_order`, `paper_item`, `reversal`, or `incoming_payment_detail`.

    Must be accompanied by `returnable_id`.
    """
