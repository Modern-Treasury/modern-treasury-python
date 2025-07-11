# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .transaction_direction import TransactionDirection

__all__ = ["LedgerEntryCreateRequest"]


class LedgerEntryCreateRequest(BaseModel):
    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    direction: TransactionDirection
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_id: str
    """The ledger account that this ledger entry is associated with."""

    available_balance_amount: Optional[Dict[str, int]] = None
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s available balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    lock_version: Optional[int] = None
    """Lock version of the ledger account.

    This can be passed when creating a ledger transaction to only succeed if no
    ledger transactions have posted since the given version. See our post about
    Designing the Ledgers API with Optimistic Locking for more details.
    """

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    pending_balance_amount: Optional[Dict[str, int]] = None
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s pending balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    posted_balance_amount: Optional[Dict[str, int]] = None
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s posted balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    show_resulting_ledger_account_balances: Optional[bool] = None
    """
    If true, response will include the balance of the associated ledger account for
    the entry.
    """
