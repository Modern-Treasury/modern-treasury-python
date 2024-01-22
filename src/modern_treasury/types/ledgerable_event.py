# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LedgerableEvent"]


class LedgerableEvent(BaseModel):
    id: str

    created_at: datetime

    custom_data: Optional[object] = None
    """Additionally data to be used by the Ledger Event Handler."""

    description: Optional[str] = None
    """Description of the ledgerable event."""

    ledger_event_handler_id: str
    """Id of the ledger event handler that is used to create a ledger transaction."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """Name of the ledgerable event."""

    object: str

    updated_at: datetime
