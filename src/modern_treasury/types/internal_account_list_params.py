# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from ..types import shared_params

__all__ = ["InternalAccountListParams"]


class InternalAccountListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    currency: shared_params.Currency
    """The currency associated with the internal account."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

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
        "masav",
        "neft",
        "provxchange",
        "rtp",
        "sen",
        "sepa",
        "signet",
        "wire",
    ]
    """The type of payment that can be made by the internal account."""

    per_page: int
