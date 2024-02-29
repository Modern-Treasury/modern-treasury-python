# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InternalAccountCreateParams", "PartyAddress"]


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

    legal_entity_id: str
    """The LegalEntity associated to this account."""

    parent_account_id: str
    """The parent internal account of this new account."""

    party_address: PartyAddress
    """The address associated with the owner or null."""

    vendor_attributes: Dict[str, str]
    """
    A hash of vendor specific attributes that will be used when creating the account
    at the vendor specified by the given connection.
    """


class PartyAddress(TypedDict, total=False):
    country: Required[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Required[str]

    locality: Required[str]
    """Locality or City."""

    postal_code: Required[str]
    """The postal code of the address."""

    region: Required[str]
    """Region or State."""

    line2: str
