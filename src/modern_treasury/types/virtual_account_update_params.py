# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["VirtualAccountUpdateParams"]


class VirtualAccountUpdateParams(TypedDict, total=False):
    counterparty_id: str

    ledger_account_id: str
    """The ledger account that you'd like to link to the virtual account."""

    metadata: Dict[str, str]

    name: Optional[str]
