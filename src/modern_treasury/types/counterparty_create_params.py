# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .shared import TransactionDirection
from .._utils import PropertyInfo
from .external_account_type import ExternalAccountType

__all__ = [
    "CounterpartyCreateParams",
    "Accounting",
    "Accounts",
    "Account",
    "AccountsAccountDetails",
    "AccountAccountDetail",
    "AccountsContactDetails",
    "AccountContactDetail",
    "AccountsLedgerAccount",
    "AccountLedgerAccount",
    "AccountsPartyAddress",
    "AccountPartyAddress",
    "AccountsRoutingDetails",
    "AccountRoutingDetail",
    "LegalEntity",
    "LegalEntityAddresses",
    "LegalEntityAddress",
    "LegalEntityIdentifications",
    "LegalEntityIdentification",
    "LegalEntityPhoneNumbers",
    "LegalEntityPhoneNumber",
]


class CounterpartyCreateParams(TypedDict, total=False):
    name: Required[Optional[str]]
    """A human friendly name for this counterparty."""

    accounting: Accounting

    accounts: Iterable[Account]
    """The accounts for this counterparty."""

    email: Optional[str]
    """The counterparty's email."""

    ledger_type: Literal["customer", "vendor"]
    """An optional type to auto-sync the counterparty to your ledger.

    Either `customer` or `vendor`.
    """

    legal_entity: LegalEntity

    legal_entity_id: Optional[str]
    """The id of the legal entity."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    send_remittance_advice: bool
    """
    Send an email to the counterparty whenever an associated payment order is sent
    to the bank.
    """

    taxpayer_identifier: str
    """Either a valid SSN or EIN."""

    verification_status: Literal["denied", "needs_approval", "unverified", "verified"]
    """The verification status of the counterparty."""


class Accounting(TypedDict, total=False):
    type: Literal["customer", "vendor"]
    """An optional type to auto-sync the counterparty to your ledger.

    Either `customer` or `vendor`.
    """


class AccountAccountDetail(TypedDict, total=False):
    account_number: Required[str]

    account_number_type: Literal["iban", "hk_number", "clabe", "wallet_address", "pan", "other"]


AccountsAccountDetails = AccountAccountDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountAccountDetail instead.
"""


class AccountContactDetail(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]


AccountsContactDetails = AccountContactDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountContactDetail instead.
"""


class AccountLedgerAccount(TypedDict, total=False):
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


AccountsLedgerAccount = AccountLedgerAccount
"""This type is deprecated and will be removed in a future release.

Please use AccountLedgerAccount instead.
"""


class AccountPartyAddress(TypedDict, total=False):
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


AccountsPartyAddress = AccountPartyAddress
"""This type is deprecated and will be removed in a future release.

Please use AccountPartyAddress instead.
"""


class AccountRoutingDetail(TypedDict, total=False):
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


AccountsRoutingDetails = AccountRoutingDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountRoutingDetail instead.
"""


class Account(TypedDict, total=False):
    account_details: Iterable[AccountAccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: Iterable[AccountContactDetail]

    ledger_account: AccountLedgerAccount
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

    party_address: AccountPartyAddress
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

    routing_details: Iterable[AccountRoutingDetail]


Accounts = Account
"""This type is deprecated and will be removed in a future release.

Please use Account instead.
"""


class LegalEntityAddress(TypedDict, total=False):
    country: Required[Optional[str]]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Required[Optional[str]]

    locality: Required[Optional[str]]
    """Locality or City."""

    postal_code: Required[Optional[str]]
    """The postal code of the address."""

    region: Required[Optional[str]]
    """Region or State."""

    address_types: List[Literal["business", "mailing", "other", "po_box", "residential"]]
    """The types of this address."""

    line2: Optional[str]


LegalEntityAddresses = LegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityAddress instead.
"""


class LegalEntityIdentification(TypedDict, total=False):
    id_number: Required[str]
    """The ID number of identification document."""

    id_type: Required[
        Literal[
            "ar_cuil",
            "ar_cuit",
            "br_cnpj",
            "br_cpf",
            "cl_nut",
            "co_cedulas",
            "co_nit",
            "hn_id",
            "hn_rtn",
            "passport",
            "us_ein",
            "us_itin",
            "us_ssn",
        ]
    ]
    """The type of ID number."""

    issuing_country: Optional[str]
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """


LegalEntityIdentifications = LegalEntityIdentification
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityIdentification instead.
"""


class LegalEntityPhoneNumber(TypedDict, total=False):
    phone_number: str


LegalEntityPhoneNumbers = LegalEntityPhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityPhoneNumber instead.
"""


class LegalEntity(TypedDict, total=False):
    legal_entity_type: Required[Literal["business", "individual"]]
    """The type of legal entity."""

    addresses: Iterable[LegalEntityAddress]
    """A list of addresses for the entity."""

    business_name: Optional[str]
    """The business's legal business name."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's data of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[LegalEntityIdentification]
    """A list of identifications for the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ]
    """The business's legal structure."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    phone_numbers: Iterable[LegalEntityPhoneNumber]

    website: Optional[str]
    """The entity's primary website URL."""
