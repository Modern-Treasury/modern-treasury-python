# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .ledger_event_handler_variable import LedgerEventHandlerVariable

__all__ = [
    "LedgerEventHandler",
    "Conditions",
    "LedgerTransactionTemplate",
    "LedgerTransactionTemplateLedgerEntries",
    "LedgerTransactionTemplateLedgerEntry",
]


class Conditions(BaseModel):
    field: str
    """The LHS of the conditional."""

    operator: str
    """What the operator between the `field` and `value` is."""

    value: str
    """The RHS of the conditional."""


class LedgerTransactionTemplateLedgerEntry(BaseModel):
    amount: str
    """The LHS of the conditional."""

    direction: str
    """What the operator between the `field` and `value` is."""

    ledger_account_id: str
    """The RHS of the conditional."""


LedgerTransactionTemplateLedgerEntries = LedgerTransactionTemplateLedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use LedgerTransactionTemplateLedgerEntry instead.
"""


class LedgerTransactionTemplate(BaseModel):
    description: Optional[str] = None
    """An optional description for internal use."""

    effective_at: Optional[str] = None
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    ledger_entries: List[LedgerTransactionTemplateLedgerEntry]
    """An array of ledger entry objects."""

    status: Optional[str] = None
    """To post a ledger transaction at creation, use `posted`."""


class LedgerEventHandler(BaseModel):
    id: str

    conditions: Optional[Conditions] = None

    created_at: datetime

    description: Optional[str] = None
    """An optional description."""

    discarded_at: Optional[datetime] = None

    ledger_id: Optional[str] = None
    """The id of the ledger that this event handler belongs to."""

    ledger_transaction_template: LedgerTransactionTemplate

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
    """Name of the ledger event handler."""

    object: str

    updated_at: datetime

    variables: Optional[Dict[str, LedgerEventHandlerVariable]] = None
