# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LedgerAccountUpdateParams"]


class LedgerAccountUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """The description of the ledger account."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """The name of the ledger account."""

    normal_balance: Literal["credit", "debit"]
    """The normal balance of the ledger account."""
