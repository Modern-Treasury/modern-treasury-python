# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .third_party_verification import ThirdPartyVerification
from .identification_create_request import IdentificationCreateRequest
from .legal_entity_address_create_request import LegalEntityAddressCreateRequest
from .legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = [
    "ChildLegalEntityCreate",
    "BankSettings",
    "Documents",
    "Document",
    "PhoneNumbers",
    "PhoneNumber",
    "Regulators",
    "Regulator",
    "WealthAndEmploymentDetails",
]


class BankSettings(BaseModel):
    id: str

    backup_withholding_percentage: Optional[int] = None
    """The percentage of backup withholding to apply to the legal entity."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    enable_backup_withholding: Optional[bool] = None
    """Whether backup withholding is enabled.

    See more here -
    https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding.
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    privacy_opt_out: Optional[bool] = None
    """Cross River Bank specific setting to opt out of privacy policy."""

    regulation_o: Optional[bool] = None
    """
    It covers, among other types of insider loans, extensions of credit by a member
    bank to an executive officer, director, or principal shareholder of the member
    bank; a bank holding company of which the member bank is a subsidiary; and any
    other subsidiary of that bank holding company.
    """

    updated_at: datetime


class Document(BaseModel):
    document_type: Literal[
        "articles_of_incorporation",
        "certificate_of_good_standing",
        "ein_letter",
        "generic",
        "identification_back",
        "identification_front",
        "proof_of_address",
    ]
    """A category given to the document, can be `null`."""

    file_data: str
    """Base64-encoded file content for the document."""

    filename: Optional[str] = None
    """The original filename of the document."""


Documents = Document
"""This type is deprecated and will be removed in a future release.

Please use Document instead.
"""


class PhoneNumber(BaseModel):
    """A list of phone numbers in E.164 format."""

    phone_number: Optional[str] = None


PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""


class Regulator(BaseModel):
    jurisdiction: str
    """
    The country code where the regulator operates in the ISO 3166-1 alpha-2 format
    (e.g., "US", "CA", "GB").
    """

    name: str
    """Full name of the regulatory body."""

    registration_number: str
    """Registration or identification number with the regulator."""


Regulators = Regulator
"""This type is deprecated and will be removed in a future release.

Please use Regulator instead.
"""


class WealthAndEmploymentDetails(BaseModel):
    id: str

    annual_income: Optional[int] = None
    """The annual income of the individual in USD."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    employer_country: Optional[str] = None
    """The country in which the employer is located."""

    employer_name: Optional[str] = None
    """The name of the employer."""

    employer_state: Optional[str] = None
    """The state in which the employer is located."""

    employment_status: Optional[Literal["employed", "retired", "self_employed", "student", "unemployed"]] = None
    """The employment status of the individual."""

    income_country: Optional[str] = None
    """The country in which the individual's income is earned."""

    income_source: Optional[
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
    ] = None
    """The source of the individual's income."""

    income_state: Optional[str] = None
    """The state in which the individual's income is earned."""

    industry: Optional[
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
    ] = None
    """The industry of the individual."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    occupation: Optional[
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
    ] = None
    """The occupation of the individual."""

    source_of_funds: Optional[
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
    ] = None
    """The source of the individual's funds."""

    updated_at: datetime

    wealth_source: Optional[
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
    ] = None
    """The source of the individual's wealth."""


class ChildLegalEntityCreate(BaseModel):
    addresses: Optional[List[LegalEntityAddressCreateRequest]] = None
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettings] = None

    business_description: Optional[str] = None
    """A description of the business."""

    business_name: Optional[str] = None
    """The business's legal business name."""

    citizenship_country: Optional[str] = None
    """The country of citizenship for an individual."""

    compliance_details: Optional[object] = None

    connection_id: Optional[str] = None
    """The connection ID for the connection the legal entity is associated with.

    Defaults to the id of the connection designated with an is_default value of true
    or the id of an existing operational connection if only one is available. Pass
    in a value of null to prevent the connection from being associated with the
    legal entity.
    """

    country_of_incorporation: Optional[str] = None
    """
    The country code where the business is incorporated in the ISO 3166-1 alpha-2 or
    alpha-3 formats.
    """

    date_formed: Optional[date] = None
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Optional[date] = None
    """An individual's date of birth (YYYY-MM-DD)."""

    documents: Optional[List[Document]] = None
    """A list of documents to attach to the legal entity (e.g.

    articles of incorporation, certificate of good standing, proof of address).
    """

    doing_business_as_names: Optional[List[str]] = None

    email: Optional[str] = None
    """The entity's primary email."""

    expected_activity_volume: Optional[int] = None
    """Monthly expected transaction volume in USD."""

    external_id: Optional[str] = None
    """An optional user-defined 180 character unique identifier."""

    first_name: Optional[str] = None
    """An individual's first name."""

    identifications: Optional[List[IdentificationCreateRequest]] = None
    """A list of identifications for the legal entity."""

    industry_classifications: Optional[List[LegalEntityIndustryClassification]] = None
    """A list of industry classifications for the legal entity."""

    intended_use: Optional[str] = None
    """A description of the intended use of the legal entity."""

    last_name: Optional[str] = None
    """An individual's last name."""

    legal_entity_associations: Optional[List["LegalEntityAssociationInlineCreate"]] = None
    """The legal entity associations and its child legal entities."""

    legal_entity_type: Optional[Literal["business", "individual"]] = None
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ] = None
    """The business's legal structure."""

    listed_exchange: Optional[str] = None
    """ISO 10383 market identifier code."""

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str] = None
    """An individual's middle name."""

    operating_jurisdictions: Optional[List[str]] = None
    """
    A list of countries where the business operates (ISO 3166-1 alpha-2 or alpha-3
    codes).
    """

    phone_numbers: Optional[List[PhoneNumber]] = None

    politically_exposed_person: Optional[bool] = None
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str] = None
    """An individual's preferred name."""

    prefix: Optional[str] = None
    """An individual's prefix."""

    primary_social_media_sites: Optional[List[str]] = None
    """A list of primary social media URLs for the business."""

    regulators: Optional[List[Regulator]] = None
    """Array of regulatory bodies overseeing this institution."""

    risk_rating: Optional[Literal["low", "medium", "high"]] = None
    """The risk rating of the legal entity. One of low, medium, high."""

    service_provider_legal_entity_id: Optional[str] = None
    """The UUID of the parent legal entity in the service provider tree."""

    suffix: Optional[str] = None
    """An individual's suffix."""

    third_party_verification: Optional[ThirdPartyVerification] = None
    """Deprecated. Use `third_party_verifications` instead."""

    third_party_verifications: Optional[List[ThirdPartyVerification]] = None
    """A list of third-party verifications run by external vendors."""

    ticker_symbol: Optional[str] = None
    """Stock ticker symbol for publicly traded companies."""

    wealth_and_employment_details: Optional[WealthAndEmploymentDetails] = None

    website: Optional[str] = None
    """The entity's primary website URL."""


from .legal_entity_association_inline_create import LegalEntityAssociationInlineCreate
