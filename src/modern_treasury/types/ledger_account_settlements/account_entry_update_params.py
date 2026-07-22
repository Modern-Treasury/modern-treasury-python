# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from ..._types import SequenceNotStr

__all__ = ["AccountEntryUpdateParams"]

class AccountEntryUpdateParams(TypedDict, total=False):
    ledger_entry_ids: Required[Optional[SequenceNotStr[str]]]
    """
    The ids of the ledger entries that are to be added or removed from the ledger
    account settlement.
    """