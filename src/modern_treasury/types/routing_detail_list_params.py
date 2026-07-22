# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .shared.accounts_type import AccountsType

from typing import Optional

__all__ = ["RoutingDetailListParams"]

class RoutingDetailListParams(TypedDict, total=False):
    accounts_type: Required[AccountsType]

    after_cursor: Optional[str]

    per_page: int