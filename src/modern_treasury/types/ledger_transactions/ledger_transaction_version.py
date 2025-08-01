# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.ledger_balances import LedgerBalances
from ..shared.transaction_direction import TransactionDirection

__all__ = ["LedgerTransactionVersion", "LedgerEntries", "LedgerEntry"]


class LedgerEntry(BaseModel):
    id: str

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    created_at: datetime

    direction: TransactionDirection
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_currency: str
    """The currency of the ledger account."""

    ledger_account_currency_exponent: int
    """The currency exponent of the ledger account."""

    ledger_account_id: str
    """The ledger account that this ledger entry is associated with."""

    ledger_account_lock_version: Optional[int] = None
    """Lock version of the ledger account.

    This can be passed when creating a ledger transaction to only succeed if no
    ledger transactions have posted since the given version. See our post about
    Designing the Ledgers API with Optimistic Locking for more details.
    """

    ledger_transaction_id: str
    """The ledger transaction that this ledger entry is associated with."""

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

    resulting_ledger_account_balances: Optional[LedgerBalances] = None
    """
    The pending, posted, and available balances for this ledger entry's ledger
    account. The posted balance is the sum of all posted entries on the account. The
    pending balance is the sum of all pending and posted entries on the account. The
    available balance is the posted incoming entries minus the sum of the pending
    and posted outgoing amounts. Please see
    https://docs.moderntreasury.com/docs/transaction-status-and-balances for more
    details.
    """

    status: Literal["archived", "pending", "posted"]
    """Equal to the state of the ledger transaction when the ledger entry was created.

    One of `pending`, `posted`, or `archived`.
    """


LedgerEntries = LedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use LedgerEntry instead.
"""


class LedgerTransactionVersion(BaseModel):
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

    ledger_transaction_id: str
    """The ID of the ledger transaction"""

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
    payment_order, incoming_payment_detail, expected_payment, return, or reversal.
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
    """The ID of the original ledger transaction.

    that this ledger transaction reverses.
    """

    status: Literal["archived", "pending", "posted"]
    """One of `pending`, `posted`, or `archived`."""

    version: int
    """Version number of the ledger transaction."""
