# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Dict

__all__ = ["LedgerEntryUpdateParams"]

class LedgerEntryUpdateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """