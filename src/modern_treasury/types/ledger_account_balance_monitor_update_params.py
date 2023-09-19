# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["LedgerAccountBalanceMonitorUpdateParams"]


class LedgerAccountBalanceMonitorUpdateParams(TypedDict, total=False):
    description: str
    """An optional, free-form description for internal use."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
