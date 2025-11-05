# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["HoldCreateParams"]


class HoldCreateParams(TypedDict, total=False):
    status: Required[Literal["active"]]
    """The status of the hold"""

    target_id: Required[str]
    """The ID of the target to hold"""

    target_type: Required[Literal["payment_order"]]
    """The type of target to hold"""

    metadata: Optional[Dict[str, str]]
    """Additional metadata for the hold"""

    reason: Optional[str]
    """The reason for the hold"""
