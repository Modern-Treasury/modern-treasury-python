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
    "LegalEntityUpdateParams",
    "BankSettings",
    "PhoneNumbers",
    "PhoneNumber",
    "Regulators",
    "Regulator",
    "ThirdPartyVerification",
    "ThirdPartyVerifications",
    "WealthAndEmploymentDetails",
]


class LegalEntityUpdateParams(TypedDict, total=False):
    addresses: Iterable[LegalEntityAddressCreateRequest]
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettings]

    business_description: Optional[str]
    """A description of the business."""

    business_name: Optional[str]
    """The business's legal business name."""

    citizenship_country: Optional[str]
    """The country of citizenship for an individual."""

    country_of_incorporation: Optional[str]
    """
    The country code where the business is incorporated in the ISO 3166-1 alpha-2 or
    alpha-3 formats.
    """

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

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

    phone_numbers: Iterable[PhoneNumber]

    politically_exposed_person: Optional[bool]
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str]
    """An individual's preferred name."""

    prefix: Optional[str]
    """An individual's prefix."""

    primary_social_media_sites: SequenceNotStr[str]
    """A list of primary social media URLs for the business."""

    regulators: Optional[Iterable[Regulator]]
    """Array of regulatory bodies overseeing this institution."""

    risk_rating: Optional[Literal["low", "medium", "high"]]
    """The risk rating of the legal entity. One of low, medium, high."""

    service_provider_legal_entity_id: Optional[str]
    """The UUID of the parent legal entity in the service provider tree."""

    suffix: Optional[str]
    """An individual's suffix."""

    third_party_verification: Optional[ThirdPartyVerification]
    """Deprecated. Use `third_party_verifications` instead."""

    third_party_verifications: Iterable[ThirdPartyVerification]
    """A list of third-party verifications run by external vendors."""

    ticker_symbol: Optional[str]
    """Stock ticker symbol for publicly traded companies."""

    wealth_and_employment_details: Optional[WealthAndEmploymentDetails]

    website: Optional[str]
    """The entity's primary website URL."""


class BankSettings(TypedDict, total=False):
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


class PhoneNumber(TypedDict, total=False):
    """A list of phone numbers in E.164 format."""

    phone_number: str


PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""


class Regulator(TypedDict, total=False):
    jurisdiction: Required[str]
    """
    The country code where the regulator operates in the ISO 3166-1 alpha-2 format
    (e.g., "US", "CA", "GB").
    """

    name: Required[str]
    """Full name of the regulatory body."""

    registration_number: Required[str]
    """Registration or identification number with the regulator."""


Regulators = Regulator
"""This type is deprecated and will be removed in a future release.

Please use Regulator instead.
"""


class ThirdPartyVerification(TypedDict, total=False):
    """Deprecated. Use `third_party_verifications` instead."""

    outcome: Required[Literal["passed", "failed"]]
    """The outcome of the verification. One of `passed` or `failed`."""

    vendor: Required[Literal["persona", "middesk", "alloy", "sumsub", "veriff"]]
    """The vendor that performed the verification, e.g. `persona`."""

    vendor_verification_id: Required[str]
    """The identification of the third party verification in `vendor`'s system."""

    verification_category: Required[
        Literal["legal_name", "date_of_birth", "address", "government_id_number", "adverse_media"]
    ]
    """The category of verification performed."""

    verification_method: Required[str]
    """The method used to perform the verification."""

    verification_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp when the verification was performed."""

    comment: Optional[str]
    """An optional comment about the verification."""


class WealthAndEmploymentDetails(TypedDict, total=False):
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
