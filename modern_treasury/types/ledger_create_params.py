# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LedgerCreateParams"]


class LedgerCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the ledger."""

    description: Optional[str]
    """An optional free-form description for internal use."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
