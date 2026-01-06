# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .account_capability_param import AccountCapabilityParam

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

    account_capabilities: Iterable[AccountCapabilityParam]
    """
    An array of AccountCapability objects that list the originating abilities of the
    internal account and any relevant information for them.
    """

    account_type: Literal[
        "base_wallet",
        "cash",
        "checking",
        "crypto_wallet",
        "ethereum_wallet",
        "general_ledger",
        "loan",
        "non_resident",
        "other",
        "overdraft",
        "polygon_wallet",
        "savings",
        "solana_wallet",
    ]
    """
    The account type, used to provision the appropriate account at the financial
    institution.
    """

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
    """The address associated with the owner or null."""

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
