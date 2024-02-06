# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .ledger_event_handler_variable_param import LedgerEventHandlerVariableParam

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

    variables: Optional[Dict[str, LedgerEventHandlerVariableParam]]


class LedgerTransactionTemplateLedgerEntry(TypedDict, total=False):
    amount: Required[str]
    """The LHS of the conditional."""

    direction: Required[str]
    """What the operator between the `field` and `value` is."""

    ledger_account_id: Required[str]
    """The RHS of the conditional."""


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

    ledger_entries: Required[Iterable[LedgerTransactionTemplateLedgerEntry]]
    """An array of ledger entry objects."""

    status: Required[Optional[str]]
    """To post a ledger transaction at creation, use `posted`."""


class Conditions(TypedDict, total=False):
    field: Required[str]
    """The LHS of the conditional."""

    operator: Required[str]
    """What the operator between the `field` and `value` is."""

    value: Required[str]
    """The RHS of the conditional."""
