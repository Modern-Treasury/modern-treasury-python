# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentRequestListParams"]


class PaymentRequestListParams(TypedDict, total=False):
    id: str

    after_cursor: Optional[str]

    created_at_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    created_at_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    internal_account_id: str

    payment_type: Literal["wire"]

    per_page: int

    status: Literal["approved", "cancelled", "declined", "pending"]
