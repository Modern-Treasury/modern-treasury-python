# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LedgerAccountPayoutListParams"]


class LedgerAccountPayoutListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    payout_ledger_account_id: str

    per_page: int
