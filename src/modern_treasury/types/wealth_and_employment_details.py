# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WealthAndEmploymentDetails"]


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
