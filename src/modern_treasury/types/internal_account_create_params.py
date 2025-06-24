# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.transaction_direction import TransactionDirection

__all__ = ["InternalAccountCreateParams", "AccountCapabilities", "AccountCapability", "PartyAddress"]


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

    account_capabilities: Iterable[AccountCapability]
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


class AccountCapabilityTyped(TypedDict, total=False):
    id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    direction: Required[TransactionDirection]
    """One of `debit` or `credit`.

    Indicates the direction of money movement this capability is responsible for.
    """

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    identifier: Required[Optional[str]]
    """
    A unique reference assigned by your bank for tracking and recognizing payment
    files. It is important this is formatted exactly how the bank assigned it.
    """

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    payment_type: Required[
        Literal[
            "ach",
            "au_becs",
            "bacs",
            "base",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "ethereum",
            "hu_ics",
            "interac",
            "masav",
            "mx_ccen",
            "neft",
            "nics",
            "nz_becs",
            "pl_elixir",
            "polygon",
            "provxchange",
            "ro_sent",
            "rtp",
            "se_bankgirot",
            "sen",
            "sepa",
            "sg_giro",
            "sic",
            "signet",
            "sknbi",
            "solana",
            "wire",
            "zengin",
        ]
    ]
    """
    Indicates the the type of payment this capability is responsible for
    originating.
    """

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


AccountCapability: TypeAlias = Union[AccountCapabilityTyped, Dict[str, builtins.object]]

AccountCapabilities = AccountCapability
"""This type is deprecated and will be removed in a future release.

Please use AccountCapability instead.
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
