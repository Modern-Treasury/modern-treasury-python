# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.ledger_balances import LedgerBalances
from .shared.transaction_direction import TransactionDirection

__all__ = ["LedgerAccountCategory"]


class LedgerAccountCategory(BaseModel):
    id: str

    balances: LedgerBalances
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

    external_id: Optional[str] = None
    """An optional user-defined 180 character unique identifier."""

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
