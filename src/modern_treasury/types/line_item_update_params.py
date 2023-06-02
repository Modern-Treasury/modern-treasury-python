# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LineItemUpdateParams"]


class LineItemUpdateParams(TypedDict, total=False):
    itemizable_type: Required[Literal["expected_payments", "payment_orders"]]

    itemizable_id: Required[str]

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
