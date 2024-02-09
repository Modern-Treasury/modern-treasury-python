# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime

from .shared import Currency
from .._models import BaseModel

__all__ = ["ForeignExchangeQuote", "ForeignExchangeRate"]


class ForeignExchangeRate(BaseModel):
    base_amount: int
    """
    Amount in the lowest denomination of the `base_currency` to convert, often
    called the "sell" amount.
    """

    base_currency: Optional[Currency] = None
    """Currency to convert, often called the "sell" currency."""

    exponent: int
    """The exponent component of the rate.

    The decimal is calculated as `value` / (10 ^ `exponent`).
    """

    rate_string: str
    """A string representation of the rate."""

    target_amount: int
    """
    Amount in the lowest denomination of the `target_currency`, often called the
    "buy" amount.
    """

    target_currency: Optional[Currency] = None
    """Currency to convert the `base_currency` to, often called the "buy" currency."""

    value: int
    """The whole number component of the rate.

    The decimal is calculated as `value` / (10 ^ `exponent`).
    """


class ForeignExchangeQuote(BaseModel):
    id: str

    created_at: datetime

    effective_at: datetime
    """The timestamp until when the quoted rate is valid."""

    expires_at: datetime
    """The timestamp until which the quote must be booked by."""

    foreign_exchange_indicator: str
    """
    Either `fixed_to_variable` if the `base_amount` was specified, or
    `variable_to_fixed` if the `target_amount` was specified when requesting the
    quote.
    """

    foreign_exchange_rate: ForeignExchangeRate
    """The serialized rate information represented by this quote."""

    internal_account_id: str
    """The ID for the `InternalAccount` this quote is associated with."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    object: str

    updated_at: datetime

    vendor_id: Optional[str] = None
    """This vendor assigned ID for this quote."""
