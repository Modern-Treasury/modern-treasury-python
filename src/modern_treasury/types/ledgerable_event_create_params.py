# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LedgerableEventCreateParams"]


class LedgerableEventCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    name: Required[str]
    """Name of the ledgerable event."""

    currency: Optional[str]
    """An ISO 4217 conformed currency or a custom currency."""

    currency_exponent: Optional[int]
    """Must be included if currency is a custom currency.

    The currency_exponent cannot exceed 30.
    """

    custom_data: Optional[object]
    """Additionally data to be used by the Ledger Event Handler."""

    description: Optional[str]
    """Description of the ledgerable event."""

    direction: Optional[str]
    """One of `credit`, `debit`."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
