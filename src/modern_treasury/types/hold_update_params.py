# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["HoldUpdateParams"]


class HoldUpdateParams(TypedDict, total=False):
    status: Required[Literal["resolved"]]
    """The new status of the hold"""

    resolution: Optional[str]
    """The resolution of the hold"""
