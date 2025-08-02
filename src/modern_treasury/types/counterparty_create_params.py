# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .bank_settings_param import BankSettingsParam
from .external_account_type import ExternalAccountType
from .shared_params.address_request import AddressRequest
from .contact_detail_create_request_param import ContactDetailCreateRequestParam
from .wealth_and_employment_details_param import WealthAndEmploymentDetailsParam
from .shared_params.child_legal_entity_create import ChildLegalEntityCreate
from .shared_params.identification_create_request import IdentificationCreateRequest
from .shared_params.ledger_account_create_request import LedgerAccountCreateRequest
from .shared_params.legal_entity_compliance_detail import LegalEntityComplianceDetail
from .shared_params.legal_entity_address_create_request import LegalEntityAddressCreateRequest
from .shared_params.legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = [
    "CounterpartyCreateParams",
    "Accounting",
    "Accounts",
    "Account",
    "AccountsAccountDetails",
    "AccountAccountDetail",
    "AccountsRoutingDetails",
    "AccountRoutingDetail",
    "LegalEntity",
    "LegalEntityLegalEntityAssociations",
    "LegalEntityLegalEntityAssociation",
    "LegalEntityPhoneNumbers",
    "LegalEntityPhoneNumber",
]


class CounterpartyCreateParams(TypedDict, total=False):
    name: Required[Optional[str]]
    """A human friendly name for this counterparty."""

    query_external_id: Annotated[str, PropertyInfo(alias="external_id")]
    """An optional user-defined 180 character unique identifier."""

    accounting: Accounting

    accounts: Iterable[Account]
    """The accounts for this counterparty."""

    email: Optional[str]
    """The counterparty's email."""

    body_external_id: Annotated[Optional[str], PropertyInfo(alias="external_id")]
    """An optional user-defined 180 character unique identifier."""

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
        "base_address",
        "clabe",
        "ethereum_address",
        "hk_number",
        "iban",
        "id_number",
        "nz_number",
        "other",
        "pan",
        "polygon_address",
        "sg_number",
        "solana_address",
        "wallet_address",
    ]


AccountsAccountDetails = AccountAccountDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountAccountDetail instead.
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
            "il_bank_code",
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


AccountsRoutingDetails = AccountRoutingDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountRoutingDetail instead.
"""


class Account(TypedDict, total=False):
    account_details: Iterable[AccountAccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: Iterable[ContactDetailCreateRequestParam]

    external_id: Optional[str]
    """An optional user-defined 180 character unique identifier."""

    ledger_account: LedgerAccountCreateRequest
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

    party_address: AddressRequest
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


class LegalEntityLegalEntityAssociation(TypedDict, total=False):
    relationship_types: Required[List[Literal["authorized_signer", "beneficial_owner", "control_person"]]]

    child_legal_entity: ChildLegalEntityCreate
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

    addresses: Iterable[LegalEntityAddressCreateRequest]
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettingsParam]

    business_name: Optional[str]
    """The business's legal business name."""

    citizenship_country: Optional[str]
    """The country of citizenship for an individual."""

    compliance_details: Optional[LegalEntityComplianceDetail]

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[IdentificationCreateRequest]
    """A list of identifications for the legal entity."""

    industry_classifications: Iterable[LegalEntityIndustryClassification]
    """A list of industry classifications for the legal entity."""

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
