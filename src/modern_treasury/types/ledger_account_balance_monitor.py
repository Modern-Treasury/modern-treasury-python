# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "LedgerAccountBalanceMonitor",
    "AlertCondition",
    "CurrentLedgerAccountBalanceState",
    "CurrentLedgerAccountBalanceStateBalances",
    "CurrentLedgerAccountBalanceStateBalancesAvailableBalance",
    "CurrentLedgerAccountBalanceStateBalancesPendingBalance",
    "CurrentLedgerAccountBalanceStateBalancesPostedBalance",
]


class AlertCondition(BaseModel):
    field: str
    """
    One of `available_balance_amount`, `pending_balance_amount`,
    `posted_balance_amount`, `ledger_account_lock_version`.
    """

    operator: str
    """A logical operator to compare the `field` against the `value`.

    One of `less_than`, `less_than_or_equals`, `equals`, `greater_than_or_equals`,
    `greater_than`.
    """

    value: int
    """
    The monitor's `current_ledger_account_balance_state.triggered` will be `true`
    when comparing the `field` to this integer value using the `operator` is
    logically true.
    """


class CurrentLedgerAccountBalanceStateBalancesAvailableBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class CurrentLedgerAccountBalanceStateBalancesPendingBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class CurrentLedgerAccountBalanceStateBalancesPostedBalance(BaseModel):
    amount: int

    credits: int

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int


class CurrentLedgerAccountBalanceStateBalances(BaseModel):
    available_balance: CurrentLedgerAccountBalanceStateBalancesAvailableBalance
    """
    The available_balance is the sum of all posted inbound entries and pending
    outbound entries. For credit normal, available_amount = posted_credits -
    pending_debits; for debit normal, available_amount = posted_debits -
    pending_credits.
    """

    pending_balance: CurrentLedgerAccountBalanceStateBalancesPendingBalance
    """The pending_balance is the sum of all pending and posted entries."""

    posted_balance: CurrentLedgerAccountBalanceStateBalancesPostedBalance
    """The posted_balance is the sum of all posted entries."""


class CurrentLedgerAccountBalanceState(BaseModel):
    balances: CurrentLedgerAccountBalanceStateBalances

    ledger_account_lock_version: int
    """The current lock version of the ledger account."""

    triggered: bool
    """
    If `true`, the ledger account's balances satisfy the `alert_condition` at this
    lock version.
    """


class LedgerAccountBalanceMonitor(BaseModel):
    id: str

    alert_condition: AlertCondition
    """Describes the condition that must be satisfied for the monitor to be triggered."""

    created_at: datetime

    current_ledger_account_balance_state: CurrentLedgerAccountBalanceState
    """
    The ledger account's balances and the monitor state as of the current ledger
    account lock version.
    """

    description: Optional[str] = None
    """An optional, free-form description for internal use."""

    discarded_at: Optional[datetime] = None

    ledger_account_id: str
    """The ledger account associated with this balance monitor."""

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

    updated_at: datetime
