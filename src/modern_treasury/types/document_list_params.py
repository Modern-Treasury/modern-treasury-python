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
        "counterparties",
        "expected_payments",
        "external_accounts",
        "identifications",
        "incoming_payment_details",
        "internal_accounts",
        "organizations",
        "paper_items",
        "payment_orders",
        "transactions",
        "connections",
    ]
    """The type of the associated object.

    Currently can be one of `payment_order`, `transaction`, `paper_item`,
    `expected_payment`, `counterparty`, `organization`, `case`, `internal_account`,
    `decision`, or `external_account`.
    """

    per_page: int
