# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    file: Required[FileTypes]

    document_type: str
    """A category given to the document, can be `null`."""

    documentable_id: str
    """The unique identifier for the associated object."""

    documentable_type: Literal[
        "connections",
        "counterparties",
        "expected_payments",
        "external_accounts",
        "identifications",
        "incoming_payment_details",
        "internal_accounts",
        "legal_entities",
        "organizations",
        "payment_orders",
        "transactions",
    ]
