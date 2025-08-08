# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel
from ..bank_settings import BankSettings
from .identification_create_request import IdentificationCreateRequest
from ..wealth_and_employment_details import WealthAndEmploymentDetails
from .legal_entity_compliance_detail import LegalEntityComplianceDetail
from .legal_entity_address_create_request import LegalEntityAddressCreateRequest
from .legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = ["ChildLegalEntityCreate", "PhoneNumbers", "PhoneNumber"]


class PhoneNumber(BaseModel):
    phone_number: Optional[str] = None


PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""


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
