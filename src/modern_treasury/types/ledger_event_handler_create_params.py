# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "LedgerEventHandlerCreateParams",
    "LedgerTransactionTemplate",
    "LedgerTransactionTemplateLedgerEntries",
    "LedgerTransactionTemplateLedgerEntry",
    "Conditions",
]


class LedgerEventHandlerCreateParams(TypedDict, total=False):
    ledger_transaction_template: Required[LedgerTransactionTemplate]

    name: Required[str]
    """Name of the ledger event handler."""

    conditions: Optional[Conditions]

    description: Optional[str]
    """An optional description."""

    ledger_id: str
    """The id of the ledger that this account belongs to."""

    metadata: Optional[Dict[str, str]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class LedgerTransactionTemplateLedgerEntry(TypedDict, total=False):
    amount: Required[str]
    """The field you're fetching from the `ledgerable_event`."""

    direction: Required[str]
    """What the operator between the `field` and `value` is.

    Currently only supports `equals`.
    """

    ledger_account_id: Required[str]
    """What raw string you are comparing the `field` against."""


LedgerTransactionTemplateLedgerEntries = LedgerTransactionTemplateLedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use LedgerTransactionTemplateLedgerEntry instead.
"""


class LedgerTransactionTemplate(TypedDict, total=False):
    description: Required[Optional[str]]
    """An optional description for internal use."""

    effective_at: Required[Optional[str]]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    ledger_entries: Required[List[LedgerTransactionTemplateLedgerEntry]]
    """An array of ledger entry objects."""

    metadata: Required[Optional[Dict[str, str]]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class Conditions(TypedDict, total=False):
    field: Required[str]
    """The field you're fetching from the `ledgerable_event`."""

    operator: Required[str]
    """What the operator between the `field` and `value` is.

    Currently only supports `equals`.
    """

    value: Required[str]
    """What raw string you are comparing the `field` against."""
