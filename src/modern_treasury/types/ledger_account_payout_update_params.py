# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LedgerAccountPayoutUpdateParams"]


class LedgerAccountPayoutUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """The description of the ledger account payout."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Literal["posted", "archived"]
    """To post a pending ledger account payout, use `posted`.

    To archive a pending ledger transaction, use `archived`.
    """
