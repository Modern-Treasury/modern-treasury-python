# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    documentable_id: str
    """The unique identifier for the associated object."""

    documentable_type: Literal[
        "connection",
        "counterparty",
        "expected_payment",
        "identification",
        "incoming_payment_detail",
        "internal_account",
        "legal_entity",
        "payment_order",
        "return",
        "transaction",
    ]
    """The type of the associated object.

    Currently can be one of `connection`, `counterparty`, `expected_payment`,
    `identification`, `incoming_payment_detail`, `internal_account`, `legal_entity`,
    `payment_order`, `return`, or `transaction`.
    """

    per_page: int
