# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime

from .shared import TransactionDirection
from .._models import BaseModel

__all__ = [
    "LedgerAccountCategory",
    "Balances",
    "BalancesAvailableBalance",
    "BalancesPendingBalance",
    "BalancesPostedBalance",
]


class BalancesAvailableBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class BalancesPendingBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class BalancesPostedBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class Balances(BaseModel):
    available_balance: BalancesAvailableBalance
    """
    The available_balance is the sum of all posted inbound entries and pending
    outbound entries. For credit normal, available_amount = posted_credits -
    pending_debits; for debit normal, available_amount = posted_debits -
    pending_credits.
    """

    pending_balance: BalancesPendingBalance
    """The pending_balance is the sum of all pending and posted entries."""

    posted_balance: BalancesPostedBalance
    """The posted_balance is the sum of all posted entries."""


class LedgerAccountCategory(BaseModel):
    id: str

    balances: Balances
    """The pending, posted, and available balances for this ledger account category.

    The posted balance is the sum of all posted entries on the account. The pending
    balance is the sum of all pending and posted entries on the account. The
    available balance is the posted incoming entries minus the sum of the pending
    and posted outgoing amounts.
    """

    created_at: datetime

    description: Optional[str] = None
    """The description of the ledger account category."""

    discarded_at: Optional[datetime] = None

    ledger_id: str
    """The id of the ledger that this account category belongs to."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """The name of the ledger account category."""

    normal_balance: TransactionDirection
    """The normal balance of the ledger account category."""

    object: str

    updated_at: datetime
