# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InternalAccountCreateParams"]


class InternalAccountCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """The identifier of the financial institution the account belongs to."""

    currency: Required[Literal["USD", "CAD"]]
    """Either "USD" or "CAD".

    Internal accounts created at Increase only supports "USD".
    """

    name: Required[str]
    """The nickname of the account."""

    party_name: Required[str]
    """The legal name of the entity which owns the account."""

    counterparty_id: str
    """The Counterparty associated to this account."""

    entity_id: str
    """The identifier of the entity at Increase which owns the account."""

    parent_account_id: str
    """The parent internal account of this new account."""
