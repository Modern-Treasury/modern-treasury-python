# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared import TransactionDirection
from .external_account_type import ExternalAccountType

__all__ = [
    "ExternalAccountCreateParams",
    "AccountDetails",
    "AccountDetail",
    "ContactDetails",
    "ContactDetail",
    "LedgerAccount",
    "PartyAddress",
    "RoutingDetails",
    "RoutingDetail",
]


class ExternalAccountCreateParams(TypedDict, total=False):
    counterparty_id: Required[Optional[str]]

    account_details: Iterable[AccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: Iterable[ContactDetail]

    ledger_account: LedgerAccount
    """Specifies a ledger account object that will be created with the external
    account.

    The resulting ledger account is linked to the external account for
    auto-ledgering Payment objects. See
    https://docs.moderntreasury.com/docs/linking-to-other-modern-treasury-objects
    for more details.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    party_address: PartyAddress
    """Required if receiving wire payments."""

    party_identifier: str

    party_name: str
    """
    If this value isn't provided, it will be inherited from the counterparty's name.
    """

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""

    plaid_processor_token: str
    """
    If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
    you can pass the processor token in this field.
    """

    routing_details: Iterable[RoutingDetail]


class AccountDetail(TypedDict, total=False):
    account_number: Required[str]

    account_number_type: Literal["iban", "hk_number", "clabe", "wallet_address", "pan", "other"]


AccountDetails = AccountDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountDetail instead.
"""


class ContactDetail(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]


ContactDetails = ContactDetail
"""This type is deprecated and will be removed in a future release.

Please use ContactDetail instead.
"""


class LedgerAccount(TypedDict, total=False):
    currency: Required[str]
    """The currency of the ledger account."""

    ledger_id: Required[str]
    """The id of the ledger that this account belongs to."""

    name: Required[str]
    """The name of the ledger account."""

    normal_balance: Required[TransactionDirection]
    """The normal balance of the ledger account."""

    currency_exponent: Optional[int]
    """The currency exponent of the ledger account."""

    description: Optional[str]
    """The description of the ledger account."""

    ledger_account_category_ids: List[str]
    """
    The array of ledger account category ids that this ledger account should be a
    child of.
    """

    ledgerable_id: str
    """
    If the ledger account links to another object in Modern Treasury, the id will be
    populated here, otherwise null.
    """

    ledgerable_type: Literal["external_account", "internal_account", "virtual_account"]
    """
    If the ledger account links to another object in Modern Treasury, the type will
    be populated here, otherwise null. The value is one of internal_account or
    external_account.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class PartyAddress(TypedDict, total=False):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str]

    line2: Optional[str]

    locality: Optional[str]
    """Locality or City."""

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""


class RoutingDetail(TypedDict, total=False):
    routing_number: Required[str]

    routing_number_type: Required[
        Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "mx_bank_identifier",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ]
    ]

    payment_type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "chats",
        "check",
        "cross_border",
        "dk_nets",
        "eft",
        "hu_ics",
        "interac",
        "masav",
        "mx_ccen",
        "neft",
        "nics",
        "nz_becs",
        "pl_elixir",
        "provxchange",
        "ro_sent",
        "rtp",
        "sg_giro",
        "se_bankgirot",
        "sen",
        "sepa",
        "sic",
        "signet",
        "sknbi",
        "wire",
        "zengin",
    ]


RoutingDetails = RoutingDetail
"""This type is deprecated and will be removed in a future release.

Please use RoutingDetail instead.
"""
