# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    as_of_date_end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    Filters transactions with an `as_of_date` starting on or before the specified
    date (YYYY-MM-DD).
    """

    as_of_date_start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    Filters transactions with an `as_of_date` starting on or after the specified
    date (YYYY-MM-DD).
    """

    counterparty_id: str

    description: str
    """Filters for transactions including the queried string in the description."""

    direction: str

    internal_account_id: str
    """
    Specify `internal_account_id` if you wish to see transactions to/from a specific
    account.
    """

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    payment_type: str

    per_page: int

    posted: bool
    """Either `true` or `false`."""

    transactable_type: str

    vendor_id: str
    """
    Filters for transactions including the queried vendor id (an identifier given to
    transactions by the bank).
    """

    virtual_account_id: str
