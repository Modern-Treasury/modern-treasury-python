# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str

    due_date_end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """An inclusive upper bound for searching due_date"""

    due_date_start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """An inclusive lower bound for searching due_date"""

    expected_payment_id: str

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    number: str
    """A unique record number assigned to each invoice that is issued."""

    originating_account_id: str

    payment_order_id: str

    per_page: int

    status: Literal["draft", "paid", "partially_paid", "payment_pending", "unpaid", "voided"]
