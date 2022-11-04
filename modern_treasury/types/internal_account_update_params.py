# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["InternalAccountUpdateParams"]


class InternalAccountUpdateParams(TypedDict, total=False):
    counterparty_id: str
    """The Counterparty associated to this account."""

    metadata: Dict[str, str]
    """Additional data in the form of key-value pairs.

    Pairs can be removed by passing an empty string or `null` as the value.
    """

    name: str
    """The nickname for the internal account."""

    parent_account_id: str
    """The parent internal account for this account."""
