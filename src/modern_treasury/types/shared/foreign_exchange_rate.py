# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .currency import Currency
from ..._models import BaseModel

__all__ = ["ForeignExchangeRate"]


class ForeignExchangeRate(BaseModel):
    base_amount: int
    """
    Amount in the lowest denomination of the `base_currency` to convert, often
    called the "sell" amount.
    """

    base_currency: Currency
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

    target_currency: Currency
    """Currency to convert the `base_currency` to, often called the "buy" currency."""

    value: int
    """The whole number component of the rate.

    The decimal is calculated as `value` / (10 ^ `exponent`).
    """
