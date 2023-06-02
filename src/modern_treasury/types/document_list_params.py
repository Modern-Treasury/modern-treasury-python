# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    documentable_type: Required[
        Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
            "decisions",
        ]
    ]

    after_cursor: Optional[str]

    per_page: int
