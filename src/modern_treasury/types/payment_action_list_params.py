# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentActionListParams", "CreatedAt"]


class PaymentActionListParams(TypedDict, total=False):
    actionable_id: str
    """The ID of the associated actionable object."""

    actionable_type: str
    """The type of the associated actionable object.

    One of `payment_order`, `expected_payment`.
    """

    after_cursor: Optional[str]

    created_at: CreatedAt
    """
    Filter by `created_at` using comparison operators like `gt` (>), `gte` (>=),
    `lt` (<), `lte` (<=), or `eq` (=) to filter by the created at timestamp. For
    example, `created_at[gte]=2024-01-01T00:00:00Z`
    """

    internal_account_id: str
    """The ID of one of your internal accounts."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    status: Literal["pending", "processable", "processing", "sent", "failed", "cancelled"]
    """Filter by payment actions of a specific status."""

    type: Literal["stop", "issue"]
    """The type of payment action."""


class CreatedAt(TypedDict, total=False):
    eq: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
