# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Optional, Union, Dict

from datetime import date, datetime

from .._utils import PropertyInfo

from .shared.transaction_direction import TransactionDirection

__all__ = ["PaymentOrderListParams"]

class PaymentOrderListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str

    created_at_end: Annotated[Union[str, date], PropertyInfo(format = "iso8601")]
    """An inclusive upper bound for searching created_at"""

    created_at_start: Annotated[Union[str, date], PropertyInfo(format = "iso8601")]
    """An inclusive lower bound for searching created_at"""

    direction: TransactionDirection

    effective_date_end: Annotated[Union[str, date], PropertyInfo(format = "iso8601")]
    """An inclusive upper bound for searching effective_date"""

    effective_date_start: Annotated[Union[str, date], PropertyInfo(format = "iso8601")]
    """An inclusive lower bound for searching effective_date"""

    external_id: str

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

    process_after_end: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """An inclusive upper bound for searching process_after"""

    process_after_start: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """An inclusive lower bound for searching process_after"""

    reference_number: str
    """Query for records with the provided reference number"""

    status: Literal["approved", "cancelled", "completed", "denied", "failed", "held", "needs_approval", "pending", "processing", "returned", "reversed", "sent", "stopped"]

    transaction_id: str
    """The ID of a transaction that the payment order has been reconciled to."""

    type: Literal["ach", "au_becs", "bacs", "book", "card", "chats", "check", "cross_border", "dk_nets", "eft", "gb_fps", "masav", "mx_ccen", "neft", "nics", "nz_becs", "pl_elixir", "rtp", "se_bankgirot", "sepa", "sg_giro", "sic", "stablecoin", "wire", "zengin"]