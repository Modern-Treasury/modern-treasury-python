# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentOrderListParams"]


class PaymentOrderListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str

    direction: Literal["credit", "debit"]

    effective_date_end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """An inclusive upper bound for searching effective_date"""

    effective_date_start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """An inclusive lower bound for searching effective_date"""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    originating_account_id: str

    per_page: int

    priority: Literal["high", "normal"]
    """Either `normal` or `high`.

    For ACH and EFT payments, `high` represents a same-day ACH or EFT transfer,
    respectively. For check payments, `high` can mean an overnight check rather than
    standard mail.
    """

    reference_number: str
    """Query for records with the provided reference number"""

    status: Literal[
        "approved",
        "cancelled",
        "completed",
        "denied",
        "failed",
        "needs_approval",
        "pending",
        "processing",
        "returned",
        "reversed",
        "sent",
    ]

    transaction_id: str
    """The ID of a transaction that the payment order has been reconciled to."""

    type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "check",
        "cross_border",
        "eft",
        "interac",
        "masav",
        "neft",
        "nics",
        "provxchange",
        "rtp",
        "se_bankgirot",
        "sen",
        "sepa",
        "sic",
        "signet",
        "wire",
        "zengin",
    ]
