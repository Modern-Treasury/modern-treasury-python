# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File", "Document"]


class File(BaseModel):
    content_type: Optional[str]
    """The MIME content type of the document."""

    filename: Optional[str]
    """The original filename of the document."""

    size: Optional[int]
    """The size of the document in bytes."""


class Document(BaseModel):
    created_at: str

    discarded_at: Optional[str]

    document_type: Optional[str]
    """A category given to the document, can be `null`."""

    documentable_id: str
    """The unique identifier for the associated object."""

    documentable_type: Literal[
        "case",
        "counterparty",
        "expected_payment",
        "external_account",
        "internal_account",
        "organization",
        "paper_item",
        "payment_order",
        "transaction",
    ]
    """The type of the associated object.

    Currently can be one of `payment_order`, `transaction`, `paper_item`,
    `expected_payment`, `counterparty`, `organization`, `case`, `internal_account`
    or `external_account`.
    """

    file: File

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: str
