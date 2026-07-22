# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from .._types import FileTypes

__all__ = ["DocumentCreateParams"]

class DocumentCreateParams(TypedDict, total=False):
    file: Required[FileTypes]

    document_type: str
    """A category given to the document, can be `null`."""

    documentable_id: str
    """The unique identifier for the associated object."""

    documentable_type: Literal["connection", "counterparty", "expected_payment", "external_account", "identification", "incoming_payment_detail", "internal_account", "legal_entity", "organization", "payment_order", "transaction"]