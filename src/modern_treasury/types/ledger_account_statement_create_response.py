# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime

from .shared import TransactionDirection
from .._models import BaseModel

__all__ = [
    "LedgerAccountStatementCreateResponse",
    "EndingBalance",
    "EndingBalanceAvailableBalance",
    "EndingBalancePendingBalance",
    "EndingBalancePostedBalance",
    "StartingBalance",
    "StartingBalanceAvailableBalance",
    "StartingBalancePendingBalance",
    "StartingBalancePostedBalance",
]


class EndingBalanceAvailableBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class EndingBalancePendingBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class EndingBalancePostedBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class EndingBalance(BaseModel):
    available_balance: EndingBalanceAvailableBalance
    """
    The available_balance is the sum of all posted inbound entries and pending
    outbound entries. For credit normal, available_amount = posted_credits -
    pending_debits; for debit normal, available_amount = posted_debits -
    pending_credits.
    """

    pending_balance: EndingBalancePendingBalance
    """The pending_balance is the sum of all pending and posted entries."""

    posted_balance: EndingBalancePostedBalance
    """The posted_balance is the sum of all posted entries."""


class StartingBalanceAvailableBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class StartingBalancePendingBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class StartingBalancePostedBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class StartingBalance(BaseModel):
    available_balance: StartingBalanceAvailableBalance
    """
    The available_balance is the sum of all posted inbound entries and pending
    outbound entries. For credit normal, available_amount = posted_credits -
    pending_debits; for debit normal, available_amount = posted_debits -
    pending_credits.
    """

    pending_balance: StartingBalancePendingBalance
    """The pending_balance is the sum of all pending and posted entries."""

    posted_balance: StartingBalancePostedBalance
    """The posted_balance is the sum of all posted entries."""


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

    ending_balance: EndingBalance
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

    starting_balance: StartingBalance
    """
    The pending, posted, and available balances for this ledger account at the
    `effective_at_lower_bound`. The posted balance is the sum of all posted entries
    on the account. The pending balance is the sum of all pending and posted entries
    on the account. The available balance is the posted incoming entries minus the
    sum of the pending and posted outgoing amounts.
    """

    updated_at: datetime
