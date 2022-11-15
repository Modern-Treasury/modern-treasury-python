# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BalancesPendingBalance", "BalancesPostedBalance", "BalancesAvailableBalance", "Balances", "LedgerAccount"]


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


class BalancesAvailableBalance(BaseModel):
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


class LedgerAccount(BaseModel):
    balances: Balances
    """The pending, posted, and available balances for this ledger account.

    The posted balance is the sum of all posted entries on the account. The pending
    balance is the sum of all pending and posted entries on the account. The
    available balance is the posted incoming entries minus the sum of the pending
    and posted outgoing amounts.
    """

    created_at: str

    description: Optional[str]
    """The description of the ledger account."""

    discarded_at: Optional[str]

    id: str

    ledger_id: str
    """The id of the ledger that this account belongs to."""

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

    normal_balance: Literal["credit", "debit"]
    """The normal balance of the ledger account."""

    object: str

    updated_at: str
