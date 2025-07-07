# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .ledger_balance import LedgerBalance

__all__ = ["LedgerBalances"]


class LedgerBalances(BaseModel):
    available_balance: LedgerBalance
    """
    The available_balance is the sum of all posted inbound entries and pending
    outbound entries. For credit normal, available_amount = posted_credits -
    pending_debits; for debit normal, available_amount = posted_debits -
    pending_credits.
    """

    pending_balance: LedgerBalance
    """The pending_balance is the sum of all pending and posted entries."""

    posted_balance: LedgerBalance
    """The posted_balance is the sum of all posted entries."""
