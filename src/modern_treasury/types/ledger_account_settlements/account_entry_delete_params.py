# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AccountEntryDeleteParams"]


class AccountEntryDeleteParams(TypedDict, total=False):
    ledger_entry_ids: Required[Optional[Iterable[object]]]
    """
    The ids of the ledger entries that are to be added or removed from the ledger
    account settlement.
    """
