# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LedgerAccountStatementCreateParams"]


class LedgerAccountStatementCreateParams(TypedDict, total=False):
    effective_at_lower_bound: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The inclusive lower bound of the effective_at timestamp of the ledger entries to
    be included in the ledger account statement.
    """

    effective_at_upper_bound: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The exclusive upper bound of the effective_at timestamp of the ledger entries to
    be included in the ledger account statement.
    """

    ledger_account_id: Required[str]
    """
    The id of the ledger account whose ledger entries are queried against, and its
    balances are computed as a result.
    """

    description: Optional[str]
    """The description of the ledger account statement."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
