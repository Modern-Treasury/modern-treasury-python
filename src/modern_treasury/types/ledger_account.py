# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.ledger_balance import LedgerBalance
from .shared.transaction_direction import TransactionDirection

__all__ = ["LedgerAccount", "Balances"]


class Balances(BaseModel):
    available_balance: LedgerBalance
    """
    The available_balance is the sum of all posted inbound entries and pending
    outbound entries. For credit normal, available_amount = posted_credits -
    pending_debits; for debit normal, available_amount = posted_debits -
    pending_credits.
    """

    effective_at_lower_bound: Optional[datetime] = None
    """
    The inclusive lower bound of the effective_at timestamp for the returned
    balances.
    """

    effective_at_upper_bound: Optional[datetime] = None
    """
    The exclusive upper bound of the effective_at timestamp for the returned
    balances.
    """

    pending_balance: LedgerBalance
    """The pending_balance is the sum of all pending and posted entries."""

    posted_balance: LedgerBalance
    """The posted_balance is the sum of all posted entries."""


class LedgerAccount(BaseModel):
    id: str

    balances: Balances
    """The pending, posted, and available balances for this ledger account.

    The posted balance is the sum of all posted entries on the account. The pending
    balance is the sum of all pending and posted entries on the account. The
    available balance is the posted incoming entries minus the sum of the pending
    and posted outgoing amounts.
    """

    created_at: datetime

    description: Optional[str] = None
    """The description of the ledger account."""

    discarded_at: Optional[datetime] = None

    external_id: Optional[str] = None
    """An optional user-defined 180 character unique identifier."""

    ledger_id: str
    """The id of the ledger that this account belongs to."""

    ledgerable_id: Optional[str] = None
    """
    If the ledger account links to another object in Modern Treasury, the id will be
    populated here, otherwise null.
    """

    ledgerable_type: Optional[Literal["counterparty", "external_account", "internal_account", "virtual_account"]] = None
    """
    If the ledger account links to another object in Modern Treasury, the type will
    be populated here, otherwise null. The value is one of internal_account or
    external_account.
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    lock_version: int
    """Lock version of the ledger account."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """The name of the ledger account."""

    normal_balance: TransactionDirection
    """The normal balance of the ledger account."""

    object: str

    updated_at: datetime
