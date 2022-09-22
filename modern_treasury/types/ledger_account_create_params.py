# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LedgerAccountCreateParams"]


class LedgerAccountCreateParams(TypedDict, total=False):
    currency: Required[str]
    """The currency of the ledger account."""

    ledger_id: Required[str]
    """The id of the ledger that this account belongs to."""

    name: Required[str]
    """The name of the ledger account."""

    normal_balance: Required[Literal["credit", "debit"]]
    """The normal balance of the ledger account."""

    currency_exponent: Optional[int]
    """The currency exponent of the ledger account."""

    description: Optional[str]
    """The description of the ledger account."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
