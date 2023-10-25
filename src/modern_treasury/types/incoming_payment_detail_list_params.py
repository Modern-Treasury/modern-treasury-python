# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .shared import TransactionDirection
from .._utils import PropertyInfo

__all__ = ["IncomingPaymentDetailListParams"]


class IncomingPaymentDetailListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    as_of_date_end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    Filters incoming payment details with an as_of_date starting on or before the
    specified date (YYYY-MM-DD).
    """

    as_of_date_start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    Filters incoming payment details with an as_of_date starting on or after the
    specified date (YYYY-MM-DD).
    """

    direction: TransactionDirection
    """One of `credit` or `debit`."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    status: Literal["completed", "pending", "returned"]
    """The current status of the incoming payment order.

    One of `pending`, `completed`, or `returned`.
    """

    type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"]
    """
    One of: `ach`, `book`, `check`, `eft`, `interac`, `rtp`, `sepa`, `signet`, or
    `wire`.
    """

    virtual_account_id: str
    """
    If the incoming payment detail is in a virtual account, the ID of the Virtual
    Account.
    """
