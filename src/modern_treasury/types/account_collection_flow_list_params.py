# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AccountCollectionFlowListParams"]


class AccountCollectionFlowListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    client_token: str

    counterparty_id: str

    external_account_id: str

    per_page: int

    status: str
