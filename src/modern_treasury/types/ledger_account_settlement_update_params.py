# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LedgerAccountSettlementUpdateParams"]


class LedgerAccountSettlementUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """The description of the ledger account settlement."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    skip_settlement_ledger_transaction: Optional[bool]
    """It is set to `false` by default.

    It should be set to `true` when migrating existing settlements.
    """

    status: Literal["posted", "archived"]
    """To post a pending ledger account settlement, use `posted`.

    To archive a pending ledger transaction, use `archived`.
    """
