# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .shared import Currency
from .._utils import PropertyInfo

__all__ = ["ForeignExchangeQuoteCreateParams"]


class ForeignExchangeQuoteCreateParams(TypedDict, total=False):
    internal_account_id: Required[str]
    """The ID for the `InternalAccount` this quote is associated with."""

    target_currency: Required[Optional[Currency]]
    """Currency to convert the `base_currency` to, often called the "buy" currency."""

    base_amount: int
    """
    Amount in the lowest denomination of the `base_currency` to convert, often
    called the "sell" amount.
    """

    base_currency: Optional[Currency]
    """Currency to convert, often called the "sell" currency."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The timestamp until when the quoted rate is valid."""

    target_amount: int
    """
    Amount in the lowest denomination of the `target_currency`, often called the
    "buy" amount.
    """
