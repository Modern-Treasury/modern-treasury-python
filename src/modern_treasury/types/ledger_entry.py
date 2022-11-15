# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LedgerEntry"]


class LedgerEntry(BaseModel):
    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 30 digits.
    """

    created_at: str

    direction: Literal["credit", "debit"]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    discarded_at: Optional[str]

    id: str

    ledger_account_currency: str
    """The currency of the ledger account."""

    ledger_account_currency_exponent: int
    """The currency exponent of the ledger account."""

    ledger_account_id: str
    """The ledger account that this ledger entry is associated with."""

    ledger_account_lock_version: Optional[int]
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

    object: str

    updated_at: str
