# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .identification_create_request import IdentificationCreateRequest
from .legal_entity_compliance_detail import LegalEntityComplianceDetail
from .legal_entity_address_create_request import LegalEntityAddressCreateRequest
from .legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = ["ChildLegalEntityCreate", "BankSettings", "PhoneNumbers", "PhoneNumber", "WealthAndEmploymentDetails"]


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


class PhoneNumber(BaseModel):
    phone_number: Optional[str] = None


PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""


class WealthAndEmploymentDetails(BaseModel):
    id: str

    annual_income: Optional[int] = None
    """The annual income of the individual."""

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
            "general_employee",
            "government_benefits",
            "homemaker",
            "inheritance_gift",
            "investment",
            "legal_settlement",
            "lottery",
            "real_estate",
            "retired",
            "retirement",
            "salary",
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

    business_name: Optional[str] = None
    """The business's legal business name."""

    citizenship_country: Optional[str] = None
    """The country of citizenship for an individual."""

    compliance_details: Optional[LegalEntityComplianceDetail] = None

    date_formed: Optional[date] = None
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Optional[date] = None
    """An individual's date of birth (YYYY-MM-DD)."""

    doing_business_as_names: Optional[List[str]] = None

    email: Optional[str] = None
    """The entity's primary email."""

    first_name: Optional[str] = None
    """An individual's first name."""

    identifications: Optional[List[IdentificationCreateRequest]] = None
    """A list of identifications for the legal entity."""

    industry_classifications: Optional[List[LegalEntityIndustryClassification]] = None
    """A list of industry classifications for the legal entity."""

    last_name: Optional[str] = None
    """An individual's last name."""

    legal_entity_type: Optional[Literal["business", "individual"]] = None
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ] = None
    """The business's legal structure."""

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str] = None
    """An individual's middle name."""

    phone_numbers: Optional[List[PhoneNumber]] = None

    politically_exposed_person: Optional[bool] = None
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str] = None
    """An individual's preferred name."""

    prefix: Optional[str] = None
    """An individual's prefix."""

    risk_rating: Optional[Literal["low", "medium", "high"]] = None
    """The risk rating of the legal entity. One of low, medium, high."""

    suffix: Optional[str] = None
    """An individual's suffix."""

    wealth_and_employment_details: Optional[WealthAndEmploymentDetails] = None

    website: Optional[str] = None
    """The entity's primary website URL."""
