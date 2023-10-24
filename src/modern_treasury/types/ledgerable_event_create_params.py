# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LedgerableEventCreateParams"]


class LedgerableEventCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the ledgerable event."""

    custom_data: Optional[object]
    """Additionally data to be used by the Ledger Event Handler."""

    description: Optional[str]
    """Description of the ledgerable event."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
