# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import TypedDict

__all__ = ["LedgerEventHandlerListParams"]


class LedgerEventHandlerListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    created_at: Dict[str, Union[str, datetime]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
    posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
    created_at%5Bgt%5D=2000-01-01T12:00:00Z.
    """

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    name: str

    per_page: int
