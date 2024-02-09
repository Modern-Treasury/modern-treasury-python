# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared import TransactionDirection

__all__ = ["LedgerAccountCreateParams"]


class LedgerAccountCreateParams(TypedDict, total=False):
    currency: Required[str]
    """The currency of the ledger account."""

    ledger_id: Required[str]
    """The id of the ledger that this account belongs to."""

    name: Required[str]
    """The name of the ledger account."""

    normal_balance: Required[TransactionDirection]
    """The normal balance of the ledger account."""

    currency_exponent: Optional[int]
    """The currency exponent of the ledger account."""

    description: Optional[str]
    """The description of the ledger account."""

    ledger_account_category_ids: List[str]
    """
    The array of ledger account category ids that this ledger account should be a
    child of.
    """

    ledgerable_id: str
    """
    If the ledger account links to another object in Modern Treasury, the id will be
    populated here, otherwise null.
    """

    ledgerable_type: Literal["external_account", "internal_account", "virtual_account"]
    """
    If the ledger account links to another object in Modern Treasury, the type will
    be populated here, otherwise null. The value is one of internal_account or
    external_account.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
