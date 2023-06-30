# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LedgerEntryRetrieveParams"]


class LedgerEntryRetrieveParams(TypedDict, total=False):
    show_balances: bool
    """If true, response will include the balances attached to the ledger entry.

    If there is no balance available, null will be returned instead.
    """
