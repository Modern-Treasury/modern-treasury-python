# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.accounts_type import AccountsType

__all__ = ["RoutingDetailListParams"]


class RoutingDetailListParams(TypedDict, total=False):
    accounts_type: Required[AccountsType]

    after_cursor: Optional[str]

    per_page: int
