# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .ledger_entry import LedgerEntry

__all__ = ["LedgerTransaction"]


class LedgerTransaction(BaseModel):
    id: str

    archived_reason: Optional[str] = None
    """
    System-set reason why the ledger transaction was archived; currently only
    'balance_lock_failure' for transactions that violated balance constraints. Only
    populated when archive_on_balance_lock_failure is true and a balance lock
    violation occurs, otherwise null.
    """

    created_at: datetime

    description: Optional[str] = None
    """An optional description for internal use."""

    effective_at: datetime
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    effective_date: date
    """
    The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
    purposes.
    """

    external_id: Optional[str] = None
    """A unique string to represent the ledger transaction.

    Only one pending or posted ledger transaction may have this ID in the ledger.
    """

    ledger_entries: List[LedgerEntry]
    """An array of ledger entry objects."""

    ledger_id: str
    """The ID of the ledger this ledger transaction belongs to."""

    ledgerable_id: Optional[str] = None
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the id will be populated here, otherwise null.
    """

    ledgerable_type: Optional[
        Literal["expected_payment", "incoming_payment_detail", "paper_item", "payment_order", "return", "reversal"]
    ] = None
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the type will be populated here, otherwise null. This can be one of
    payment_order, incoming_payment_detail, expected_payment, return, paper_item, or
    reversal.
    """

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

    partially_posts_ledger_transaction_id: Optional[str] = None
    """The ID of the ledger transaction that this ledger transaction partially posts."""

    posted_at: Optional[datetime] = None
    """The time on which the ledger transaction posted.

    This is null if the ledger transaction is pending.
    """

    reversed_by_ledger_transaction_id: Optional[str] = None
    """The ID of the ledger transaction that reversed this ledger transaction."""

    reverses_ledger_transaction_id: Optional[str] = None
    """
    The ID of the original ledger transaction that this ledger transaction reverses.
    """

    status: Literal["archived", "pending", "posted"]
    """To post a ledger transaction at creation, use `posted`."""

    updated_at: datetime
