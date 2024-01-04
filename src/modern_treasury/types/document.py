# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "DocumentDetails", "DocumentDetail", "File"]


class DocumentDetail(BaseModel):
    id: str

    created_at: datetime

    discarded_at: Optional[datetime] = None

    document_identifier: str

    document_identifier_type: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime


DocumentDetails = DocumentDetail
"""This type is deprecated and will be removed in a future release.

Please use DocumentDetail instead.
"""


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

    document_details: List[DocumentDetail]

    document_type: Optional[str] = None
    """A category given to the document, can be `null`."""

    documentable_id: str
    """The unique identifier for the associated object."""

    documentable_type: Literal[
        "case",
        "counterparty",
        "expected_payment",
        "external_account",
        "incoming_payment_detail",
        "internal_account",
        "organization",
        "paper_item",
        "payment_order",
        "transaction",
        "decision",
        "connection",
    ]
    """The type of the associated object.

    Currently can be one of `payment_order`, `transaction`, `paper_item`,
    `expected_payment`, `counterparty`, `organization`, `case`, `internal_account`,
    `decision`, or `external_account`.
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
