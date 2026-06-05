# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["LedgerBalance"]


class LedgerBalance(BaseModel):
    amount: int

    amount_string: str

    credits: int

    credits_string: str

    currency: str
    """The currency of the ledger account."""

    currency_exponent: int
    """The currency exponent of the ledger account."""

    debits: int

    debits_string: str
