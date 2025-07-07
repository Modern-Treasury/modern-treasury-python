# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.ledger_balances import LedgerBalances
from .shared.transaction_direction import TransactionDirection

__all__ = ["LedgerAccountStatementCreateResponse"]


class LedgerAccountStatementCreateResponse(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None
    """The description of the ledger account statement."""

    effective_at_lower_bound: datetime
    """
    The inclusive lower bound of the effective_at timestamp of the ledger entries to
    be included in the ledger account statement.
    """

    effective_at_upper_bound: datetime
    """
    The exclusive upper bound of the effective_at timestamp of the ledger entries to
    be included in the ledger account statement.
    """

    ending_balance: LedgerBalances
    """
    The pending, posted, and available balances for this ledger account at the
    `effective_at_upper_bound`. The posted balance is the sum of all posted entries
    on the account. The pending balance is the sum of all pending and posted entries
    on the account. The available balance is the posted incoming entries minus the
    sum of the pending and posted outgoing amounts.
    """

    ledger_account_id: str
    """
    The id of the ledger account whose ledger entries are queried against, and its
    balances are computed as a result.
    """

    ledger_account_lock_version: int
    """Lock version of the ledger account at the time of statement generation."""

    ledger_account_normal_balance: TransactionDirection
    """The normal balance of the ledger account."""

    ledger_id: str
    """The id of the ledger that this ledger account statement belongs to."""

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

    starting_balance: LedgerBalances
    """
    The pending, posted, and available balances for this ledger account at the
    `effective_at_lower_bound`. The posted balance is the sum of all posted entries
    on the account. The pending balance is the sum of all pending and posted entries
    on the account. The available balance is the posted incoming entries minus the
    sum of the pending and posted outgoing amounts.
    """

    updated_at: datetime
