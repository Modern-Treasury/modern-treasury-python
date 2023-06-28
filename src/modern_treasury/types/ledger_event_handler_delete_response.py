# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "LedgerEventHandlerDeleteResponse",
    "Conditions",
    "LedgerTransactionTemplate",
    "LedgerTransactionTemplateLedgerEntries",
    "LedgerTransactionTemplateLedgerEntry",
]


class Conditions(BaseModel):
    field: str
    """The field you're fetching from the `ledgerable_event`."""

    operator: str
    """What the operator between the `field` and `value` is.

    Currently only supports `equals`.
    """

    value: str
    """What raw string you are comparing the `field` against."""


class LedgerTransactionTemplateLedgerEntry(BaseModel):
    amount: str
    """The field you're fetching from the `ledgerable_event`."""

    direction: str
    """What the operator between the `field` and `value` is.

    Currently only supports `equals`.
    """

    ledger_account_id: str
    """What raw string you are comparing the `field` against."""


LedgerTransactionTemplateLedgerEntries = LedgerTransactionTemplateLedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use LedgerTransactionTemplateLedgerEntry instead.
"""


class LedgerTransactionTemplate(BaseModel):
    description: Optional[str]
    """An optional description for internal use."""

    effective_at: Optional[str]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    ledger_entries: List[LedgerTransactionTemplateLedgerEntry]
    """An array of ledger entry objects."""

    metadata: Optional[Dict[str, str]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class LedgerEventHandlerDeleteResponse(BaseModel):
    id: str

    conditions: Optional[Conditions]

    created_at: datetime

    description: Optional[str]
    """An optional description."""

    discarded_at: Optional[datetime]

    ledger_transaction_template: LedgerTransactionTemplate

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
    """Name of the ledger event handler."""

    object: str

    updated_at: datetime
