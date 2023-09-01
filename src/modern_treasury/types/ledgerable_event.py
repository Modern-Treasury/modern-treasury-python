# File generated from our OpenAPI spec by Stainless.

import builtins
from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LedgerableEvent"]


class LedgerableEvent(BaseModel):
    id: str

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    created_at: datetime

    currency: str
    """An ISO 4217 conformed currency or a custom currency."""

    currency_exponent: Optional[int]
    """Must be included if currency is a custom currency.

    The currency_exponent cannot exceed 30.
    """

    custom_data: Optional[builtins.object]
    """Additionally data to be used by the Ledger Event Handler."""

    description: Optional[str]
    """Description of the ledgerable event."""

    direction: Optional[str]
    """One of `credit`, `debit`."""

    ledger_event_handler_id: str
    """Id of the ledger event handler that is used to create a ledger transaction."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """Name of the ledgerable event."""

    object: str

    updated_at: datetime
