# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountDetailListParams"]


class AccountDetailListParams(TypedDict, total=False):
    accounts_type: Required[Literal["external_accounts", "internal_accounts"]]

    after_cursor: Optional[str]

    per_page: int
