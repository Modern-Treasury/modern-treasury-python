# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AccountCollectionFlowCreateParams"]


class AccountCollectionFlowCreateParams(TypedDict, total=False):
    counterparty_id: Required[str]
    """Required."""

    payment_types: Required[List[str]]
