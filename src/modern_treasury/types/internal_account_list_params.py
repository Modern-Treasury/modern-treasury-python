# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..types import shared_params

__all__ = ["InternalAccountListParams"]


class InternalAccountListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    currency: shared_params.Currency
    """The currency associated with the internal account."""

    payment_direction: Literal["credit", "debit"]
    """The direction of payments that can be made by internal account."""

    payment_type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "check",
        "cross_border",
        "eft",
        "interac",
        "provxchange",
        "rtp",
        "sen",
        "sepa",
        "signet",
        "wire",
    ]
    """The type of payment that can be made by the internal account."""

    per_page: int
