# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["TransactionUpdateParams"]


class TransactionUpdateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """Additional data in the form of key-value pairs.

    Pairs can be removed by passing an empty string or `null` as the value.
    """
