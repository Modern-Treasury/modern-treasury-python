# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .bank_settings_param import BankSettingsParam
from .external_account_type import ExternalAccountType
from .shared.transaction_direction import TransactionDirection
from .wealth_and_employment_details_param import WealthAndEmploymentDetailsParam

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
    "LegalEntityLegalEntityAssociations",
    "LegalEntityLegalEntityAssociation",
    "LegalEntityLegalEntityAssociationsChildLegalEntity",
    "LegalEntityLegalEntityAssociationChildLegalEntity",
    "LegalEntityLegalEntityAssociationsChildLegalEntityAddresses",
    "LegalEntityLegalEntityAssociationChildLegalEntityAddress",
    "LegalEntityLegalEntityAssociationsChildLegalEntityIdentifications",
    "LegalEntityLegalEntityAssociationChildLegalEntityIdentification",
    "LegalEntityLegalEntityAssociationsChildLegalEntityPhoneNumbers",
    "LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber",
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

    account_number_type: Literal[
        "au_number",
        "clabe",
        "hk_number",
        "iban",
        "id_number",
        "nz_number",
        "other",
        "pan",
        "sg_number",
        "wallet_address",
    ]


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

    ledgerable_type: Literal["counterparty", "external_account", "internal_account", "virtual_account"]
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
            "sg_interbank_clearing_code",
            "swift",
            "za_national_clearing_code",
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
        "se_bankgirot",
        "sen",
        "sepa",
        "sg_giro",
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
            "cl_run",
            "cl_rut",
            "co_cedulas",
            "co_nit",
            "hn_id",
            "hn_rtn",
            "in_lei",
            "kr_brn",
            "kr_crn",
            "kr_rrn",
            "passport",
            "sa_tin",
            "sa_vat",
            "us_ein",
            "us_itin",
            "us_ssn",
            "vn_tin",
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


class LegalEntityLegalEntityAssociationChildLegalEntityAddress(TypedDict, total=False):
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


LegalEntityLegalEntityAssociationsChildLegalEntityAddresses = LegalEntityLegalEntityAssociationChildLegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntityAddress instead.
"""


class LegalEntityLegalEntityAssociationChildLegalEntityIdentification(TypedDict, total=False):
    id_number: Required[str]
    """The ID number of identification document."""

    id_type: Required[
        Literal[
            "ar_cuil",
            "ar_cuit",
            "br_cnpj",
            "br_cpf",
            "cl_run",
            "cl_rut",
            "co_cedulas",
            "co_nit",
            "hn_id",
            "hn_rtn",
            "in_lei",
            "kr_brn",
            "kr_crn",
            "kr_rrn",
            "passport",
            "sa_tin",
            "sa_vat",
            "us_ein",
            "us_itin",
            "us_ssn",
            "vn_tin",
        ]
    ]
    """The type of ID number."""

    issuing_country: Optional[str]
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """


LegalEntityLegalEntityAssociationsChildLegalEntityIdentifications = (
    LegalEntityLegalEntityAssociationChildLegalEntityIdentification
)
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntityIdentification instead.
"""


class LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber(TypedDict, total=False):
    phone_number: str


LegalEntityLegalEntityAssociationsChildLegalEntityPhoneNumbers = (
    LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber
)
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber instead.
"""


class LegalEntityLegalEntityAssociationChildLegalEntity(TypedDict, total=False):
    addresses: Iterable[LegalEntityLegalEntityAssociationChildLegalEntityAddress]
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettingsParam]

    business_name: Optional[str]
    """The business's legal business name."""

    citizenship_country: Optional[str]
    """The country of citizenship for an individual."""

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[LegalEntityLegalEntityAssociationChildLegalEntityIdentification]
    """A list of identifications for the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

    legal_entity_type: Literal["business", "individual"]
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ]
    """The business's legal structure."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str]
    """An individual's middle name."""

    phone_numbers: Iterable[LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber]

    politically_exposed_person: Optional[bool]
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str]
    """An individual's preferred name."""

    prefix: Optional[str]
    """An individual's prefix."""

    risk_rating: Optional[Literal["low", "medium", "high"]]
    """The risk rating of the legal entity. One of low, medium, high."""

    suffix: Optional[str]
    """An individual's suffix."""

    wealth_and_employment_details: Optional[WealthAndEmploymentDetailsParam]

    website: Optional[str]
    """The entity's primary website URL."""


LegalEntityLegalEntityAssociationsChildLegalEntity = LegalEntityLegalEntityAssociationChildLegalEntity
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntity instead.
"""


class LegalEntityLegalEntityAssociation(TypedDict, total=False):
    relationship_types: Required[List[Literal["beneficial_owner", "control_person"]]]

    child_legal_entity: LegalEntityLegalEntityAssociationChildLegalEntity
    """The child legal entity."""

    child_legal_entity_id: str
    """The ID of the child legal entity."""

    ownership_percentage: Optional[int]
    """The child entity's ownership percentage iff they are a beneficial owner."""

    title: Optional[str]
    """The job title of the child entity at the parent entity."""


LegalEntityLegalEntityAssociations = LegalEntityLegalEntityAssociation
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociation instead.
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

    bank_settings: Optional[BankSettingsParam]

    business_name: Optional[str]
    """The business's legal business name."""

    citizenship_country: Optional[str]
    """The country of citizenship for an individual."""

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[LegalEntityIdentification]
    """A list of identifications for the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

    legal_entity_associations: Optional[Iterable[LegalEntityLegalEntityAssociation]]
    """The legal entity associations and its child legal entities."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ]
    """The business's legal structure."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str]
    """An individual's middle name."""

    phone_numbers: Iterable[LegalEntityPhoneNumber]

    politically_exposed_person: Optional[bool]
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str]
    """An individual's preferred name."""

    prefix: Optional[str]
    """An individual's prefix."""

    risk_rating: Optional[Literal["low", "medium", "high"]]
    """The risk rating of the legal entity. One of low, medium, high."""

    suffix: Optional[str]
    """An individual's suffix."""

    wealth_and_employment_details: Optional[WealthAndEmploymentDetailsParam]

    website: Optional[str]
    """The entity's primary website URL."""
