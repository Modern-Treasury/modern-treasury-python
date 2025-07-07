# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.ledger_balances import LedgerBalances
from .shared.transaction_direction import TransactionDirection

__all__ = ["LedgerEntry"]


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

    discarded_at: Optional[datetime] = None

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

    updated_at: datetime
