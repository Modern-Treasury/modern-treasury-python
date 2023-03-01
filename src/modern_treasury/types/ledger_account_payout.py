# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LedgerAccountPayout"]


class LedgerAccountPayout(BaseModel):
    amount: Optional[int]
    """The amount of the ledger account payout."""

    created_at: datetime

    currency: str
    """The currency of the ledger account payout."""

    currency_exponent: Optional[int]
    """The currency exponent of the ledger account payout."""

    description: Optional[str]
    """The description of the ledger account payout."""

    effective_at_upper_bound: str
    """
    The maximum effective_at timestamp of the ledger entries to be included in the
    ledger account payout. The default value is the created_at timestamp of the
    ledger account payout.
    """

    funding_ledger_account_id: str
    """
    The id of the funding ledger account that sends to or receives funds from the
    payout ledger account.
    """

    id: str

    ledger_transaction_id: Optional[str]
    """The ledger transaction that this payout is associated with."""

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

    payout_ledger_account_id: str
    """
    The id of the payout ledger account whose ledger entries are queried against,
    and its balance is reduced as a result.
    """

    status: Literal["archived", "archiving", "pending", "posted", "processing"]
    """The status of the ledger account payout.

    One of `processing`, `pending`, `posted`, `archiving` or `archived`.
    """

    updated_at: datetime
