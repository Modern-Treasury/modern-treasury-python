# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    documentable_id: Required[str]
    """The unique identifier for the associated object."""

    documentable_type: Required[
        Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "incoming_payment_details",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
            "decisions",
            "connections",
        ]
    ]

    file: Required[FileTypes]

    document_type: str
    """A category given to the document, can be `null`."""
