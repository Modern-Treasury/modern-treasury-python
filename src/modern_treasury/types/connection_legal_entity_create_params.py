# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.identification_create_request import IdentificationCreateRequest
from .shared_params.legal_entity_address_create_request import LegalEntityAddressCreateRequest
from .shared_params.legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = [
    "ConnectionLegalEntityCreateParams",
    "LegalEntity",
    "LegalEntityBankSettings",
    "LegalEntityDocuments",
    "LegalEntityDocument",
    "LegalEntityPhoneNumbers",
    "LegalEntityPhoneNumber",
    "LegalEntityRegulators",
    "LegalEntityRegulator",
    "LegalEntityThirdPartyVerification",
    "LegalEntityWealthAndEmploymentDetails",
]


class ConnectionLegalEntityCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the connection."""

    legal_entity: LegalEntity
    """The legal entity."""

    legal_entity_id: str
    """The ID of the legal entity."""


class LegalEntityBankSettings(TypedDict, total=False):
    id: Required[str]

    backup_withholding_percentage: Required[Optional[int]]
    """The percentage of backup withholding to apply to the legal entity."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    enable_backup_withholding: Required[Optional[bool]]
    """Whether backup withholding is enabled.

    See more here -
    https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding.
    """

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    privacy_opt_out: Required[Optional[bool]]
    """Cross River Bank specific setting to opt out of privacy policy."""

    regulation_o: Required[Optional[bool]]
    """
    It covers, among other types of insider loans, extensions of credit by a member
    bank to an executive officer, director, or principal shareholder of the member
    bank; a bank holding company of which the member bank is a subsidiary; and any
    other subsidiary of that bank holding company.
    """

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


class LegalEntityDocument(TypedDict, total=False):
    document_type: Required[
        Literal[
            "articles_of_incorporation",
            "certificate_of_good_standing",
            "ein_letter",
            "identification_back",
            "identification_front",
            "proof_of_address",
        ]
    ]
    """A category given to the document, can be `null`."""

    file_data: Required[str]
    """Base64-encoded file content for the document."""

    filename: str
    """The original filename of the document."""


LegalEntityDocuments = LegalEntityDocument
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityDocument instead.
"""


class LegalEntityPhoneNumber(TypedDict, total=False):
    """A list of phone numbers in E.164 format."""

    phone_number: str


LegalEntityPhoneNumbers = LegalEntityPhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityPhoneNumber instead.
"""


class LegalEntityRegulator(TypedDict, total=False):
    jurisdiction: Required[str]
    """
    The country code where the regulator operates in the ISO 3166-1 alpha-2 format
    (e.g., "US", "CA", "GB").
    """

    name: Required[str]
    """Full name of the regulatory body."""

    registration_number: Required[str]
    """Registration or identification number with the regulator."""


LegalEntityRegulators = LegalEntityRegulator
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityRegulator instead.
"""


class LegalEntityThirdPartyVerification(TypedDict, total=False):
    """Information describing a third-party verification run by an external vendor."""

    vendor: Required[Literal["persona"]]
    """The vendor that performed the verification, e.g. `persona`."""

    vendor_verification_id: Required[str]
    """The identification of the third party verification in `vendor`'s system."""


class LegalEntityWealthAndEmploymentDetails(TypedDict, total=False):
    id: Required[str]

    annual_income: Required[Optional[int]]
    """The annual income of the individual in USD."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    employer_country: Required[Optional[str]]
    """The country in which the employer is located."""

    employer_name: Required[Optional[str]]
    """The name of the employer."""

    employer_state: Required[Optional[str]]
    """The state in which the employer is located."""

    employment_status: Required[Optional[Literal["employed", "retired", "self_employed", "student", "unemployed"]]]
    """The employment status of the individual."""

    income_country: Required[Optional[str]]
    """The country in which the individual's income is earned."""

    income_source: Required[
        Optional[
            Literal[
                "family_support",
                "government_benefits",
                "inheritance",
                "investments",
                "rental_income",
                "retirement",
                "salary",
                "self_employed",
            ]
        ]
    ]
    """The source of the individual's income."""

    income_state: Required[Optional[str]]
    """The state in which the individual's income is earned."""

    industry: Required[
        Optional[
            Literal[
                "accounting",
                "agriculture",
                "automotive",
                "chemical_manufacturing",
                "construction",
                "educational_medical",
                "food_service",
                "finance",
                "gasoline",
                "health_stores",
                "laundry",
                "maintenance",
                "manufacturing",
                "merchant_wholesale",
                "mining",
                "performing_arts",
                "professional_non_legal",
                "public_administration",
                "publishing",
                "real_estate",
                "recreation_gambling",
                "religious_charity",
                "rental_services",
                "retail_clothing",
                "retail_electronics",
                "retail_food",
                "retail_furnishing",
                "retail_home",
                "retail_non_store",
                "retail_sporting",
                "transportation",
                "travel",
                "utilities",
            ]
        ]
    ]
    """The industry of the individual."""

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    occupation: Required[
        Optional[
            Literal[
                "consulting",
                "executive",
                "finance_accounting",
                "food_services",
                "government",
                "healthcare",
                "legal_services",
                "manufacturing",
                "other",
                "sales",
                "science_engineering",
                "technology",
            ]
        ]
    ]
    """The occupation of the individual."""

    source_of_funds: Required[
        Optional[
            Literal[
                "alimony",
                "annuity",
                "business_owner",
                "business_revenue",
                "debt_financing",
                "general_employee",
                "government_benefits",
                "homemaker",
                "inheritance_gift",
                "intercompany_loan",
                "investment",
                "investor_funding",
                "legal_settlement",
                "lottery",
                "real_estate",
                "retained_earnings_or_savings",
                "retired",
                "retirement",
                "salary",
                "sale_of_business_assets",
                "sale_of_real_estate",
                "self_employed",
                "senior_executive",
                "trust_income",
            ]
        ]
    ]
    """The source of the individual's funds."""

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    wealth_source: Required[
        Optional[
            Literal[
                "business_sale",
                "family_support",
                "government_benefits",
                "inheritance",
                "investments",
                "other",
                "rental_income",
                "retirement",
                "salary",
                "self_employed",
            ]
        ]
    ]
    """The source of the individual's wealth."""


class LegalEntity(TypedDict, total=False):
    """The legal entity."""

    addresses: Iterable[LegalEntityAddressCreateRequest]
    """A list of addresses for the entity."""

    bank_settings: Optional[LegalEntityBankSettings]

    business_description: Optional[str]
    """A description of the business."""

    business_name: Optional[str]
    """The business's legal business name."""

    citizenship_country: Optional[str]
    """The country of citizenship for an individual."""

    compliance_details: Optional[object]

    connection_id: Optional[str]
    """The connection ID for the connection the legal entity is associated with.

    Defaults to the id of the connection designated with an is_default value of true
    or the id of an existing operational connection if only one is available. Pass
    in a value of null to prevent the connection from being associated with the
    legal entity.
    """

    country_of_incorporation: Optional[str]
    """
    The country code where the business is incorporated in the ISO 3166-1 alpha-2 or
    alpha-3 formats.
    """

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    documents: Iterable[LegalEntityDocument]
    """A list of documents to attach to the legal entity (e.g.

    articles of incorporation, certificate of good standing, proof of address).
    """

    doing_business_as_names: SequenceNotStr[str]

    email: Optional[str]
    """The entity's primary email."""

    expected_activity_volume: Optional[int]
    """Monthly expected transaction volume in USD."""

    external_id: Optional[str]
    """An optional user-defined 180 character unique identifier."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[IdentificationCreateRequest]
    """A list of identifications for the legal entity."""

    industry_classifications: Iterable[LegalEntityIndustryClassification]
    """A list of industry classifications for the legal entity."""

    intended_use: Optional[str]
    """A description of the intended use of the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

    legal_entity_associations: Optional[Iterable["LegalEntityAssociationInlineCreate"]]
    """The legal entity associations and its child legal entities."""

    legal_entity_type: Literal["business", "individual"]
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ]
    """The business's legal structure."""

    listed_exchange: Optional[str]
    """ISO 10383 market identifier code."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str]
    """An individual's middle name."""

    operating_jurisdictions: SequenceNotStr[str]
    """
    A list of countries where the business operates (ISO 3166-1 alpha-2 or alpha-3
    codes).
    """

    phone_numbers: Iterable[LegalEntityPhoneNumber]

    politically_exposed_person: Optional[bool]
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str]
    """An individual's preferred name."""

    prefix: Optional[str]
    """An individual's prefix."""

    primary_social_media_sites: SequenceNotStr[str]
    """A list of primary social media URLs for the business."""

    regulators: Optional[Iterable[LegalEntityRegulator]]
    """Array of regulatory bodies overseeing this institution."""

    risk_rating: Optional[Literal["low", "medium", "high"]]
    """The risk rating of the legal entity. One of low, medium, high."""

    service_provider_legal_entity_id: Optional[str]
    """The UUID of the parent legal entity in the service provider tree."""

    suffix: Optional[str]
    """An individual's suffix."""

    third_party_verification: Optional[LegalEntityThirdPartyVerification]
    """Information describing a third-party verification run by an external vendor."""

    ticker_symbol: Optional[str]
    """Stock ticker symbol for publicly traded companies."""

    wealth_and_employment_details: Optional[LegalEntityWealthAndEmploymentDetails]

    website: Optional[str]
    """The entity's primary website URL."""


from .shared_params.legal_entity_association_inline_create import LegalEntityAssociationInlineCreate
