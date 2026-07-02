# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "File"]


class File(BaseModel):
    content_type: Optional[str] = None
    """The MIME content type of the document."""

    filename: Optional[str] = None
    """The original filename of the document."""

    size: Optional[int] = None
    """The size of the document in bytes."""


class Document(BaseModel):
    id: str

    created_at: datetime

    discarded_at: Optional[datetime] = None

    document_type: Optional[str] = None
    """A category given to the document, can be `null`."""

    documentable_id: Optional[str] = None
    """The unique identifier for the associated object."""

    documentable_type: Optional[
        Literal[
            "connection",
            "counterparty",
            "expected_payment",
            "external_account",
            "identification",
            "incoming_payment_detail",
            "internal_account",
            "legal_entity",
            "organization",
            "payment_order",
            "transaction",
        ]
    ] = None
    """The type of the associated object.

    Currently can be one of `payment_order`, `transaction`, `expected_payment`,
    `counterparty`, `organization`, `case`, `internal_account`, `decision`, or
    `external_account`.
    """

    file: File

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    source: str
    """The source of the document. Can be `vendor`, `customer`, or `modern_treasury`."""

    updated_at: datetime
