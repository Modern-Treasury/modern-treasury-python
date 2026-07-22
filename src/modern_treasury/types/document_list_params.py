# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional

__all__ = ["DocumentListParams"]

class DocumentListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    documentable_id: str
    """The unique identifier for the associated object."""

    documentable_type: Literal["connection", "counterparty", "expected_payment", "external_account", "identification", "incoming_payment_detail", "internal_account", "legal_entity", "organization", "payment_order", "transaction"]
    """The type of the associated object.

    Currently can be one of `payment_order`, `transaction`, `expected_payment`,
    `counterparty`, `organization`, `case`, `internal_account`, `decision`, or
    `external_account`.
    """

    per_page: int