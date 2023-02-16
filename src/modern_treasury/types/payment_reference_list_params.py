# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["PaymentReferenceListParams"]


class PaymentReferenceListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    per_page: int

    reference_number: str
    """The actual reference number assigned by the bank."""

    referenceable_id: str
    """The id of the referenceable to search for.

    Must be accompanied by the referenceable_type or will return an error.
    """

    referenceable_type: Literal["payment_order", "return", "reversal"]
    """One of the referenceable types.

    This must be accompanied by the id of the referenceable or will return an error.
    """
