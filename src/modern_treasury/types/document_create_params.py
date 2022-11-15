# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    file: Required[FileTypes]

    document_type: str
    """A category given to the document, can be `null`."""
