# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ForeignExchangeQuoteListParams"]


class ForeignExchangeQuoteListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    base_currency: str
    """Currency to convert, often called the "sell" currency."""

    effective_at_end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """An inclusive upper bound for searching effective_at"""

    effective_at_start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """An inclusive lower bound for searching effective_at"""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The timestamp until which the quote must be booked by."""

    internal_account_id: str
    """The ID for the `InternalAccount` this quote is associated with."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    target_currency: str
    """Currency to convert the `base_currency` to, often called the "buy" currency."""
