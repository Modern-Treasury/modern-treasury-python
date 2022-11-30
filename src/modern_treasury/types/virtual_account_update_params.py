# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["VirtualAccountUpdateParams"]


class VirtualAccountUpdateParams(TypedDict, total=False):
    counterparty_id: str

    metadata: Dict[str, str]

    name: Optional[str]
