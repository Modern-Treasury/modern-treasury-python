# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Dict

__all__ = ["LedgerAccountBalanceMonitorUpdateParams"]

class LedgerAccountBalanceMonitorUpdateParams(TypedDict, total=False):
    description: str
    """An optional, free-form description for internal use."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """