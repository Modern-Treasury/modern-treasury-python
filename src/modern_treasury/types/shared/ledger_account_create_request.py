# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .transaction_direction import TransactionDirection

__all__ = ["LedgerAccountCreateRequest"]


class LedgerAccountCreateRequest(BaseModel):
    currency: str
    """The currency of the ledger account."""

    ledger_id: str
    """The id of the ledger that this account belongs to."""

    name: str
    """The name of the ledger account."""

    normal_balance: TransactionDirection
    """The normal balance of the ledger account."""

    currency_exponent: Optional[int] = None
    """The currency exponent of the ledger account."""

    description: Optional[str] = None
    """The description of the ledger account."""

    ledger_account_category_ids: Optional[List[str]] = None
    """
    The array of ledger account category ids that this ledger account should be a
    child of.
    """

    ledgerable_id: Optional[str] = None
    """
    If the ledger account links to another object in Modern Treasury, the id will be
    populated here, otherwise null.
    """

    ledgerable_type: Optional[Literal["counterparty", "external_account", "internal_account", "virtual_account"]] = None
    """
    If the ledger account links to another object in Modern Treasury, the type will
    be populated here, otherwise null. The value is one of internal_account or
    external_account.
    """

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
