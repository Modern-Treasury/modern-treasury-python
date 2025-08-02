# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WealthAndEmploymentDetailsParam"]


class WealthAndEmploymentDetailsParam(TypedDict, total=False):
    id: Required[str]

    annual_income: Required[Optional[int]]
    """The annual income of the individual."""

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
