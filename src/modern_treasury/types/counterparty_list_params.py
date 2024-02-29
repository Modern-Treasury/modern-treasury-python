# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CounterpartyListParams"]


class CounterpartyListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    created_at_lower_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Used to return counterparties created after some datetime."""

    created_at_upper_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Used to return counterparties created before some datetime."""

    email: str
    """Performs a partial string match of the email field.

    This is also case insensitive.
    """

    legal_entity_id: str
    """Filters for counterparties with the given legal entity ID."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    name: str
    """Performs a partial string match of the name field.

    This is also case insensitive.
    """

    per_page: int
