# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..types import shared_params

__all__ = ["AccountDetailListParams"]


class AccountDetailListParams(TypedDict, total=False):
    accounts_type: Required[shared_params.AccountsType]

    after_cursor: Optional[str]

    per_page: int
