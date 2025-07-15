# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .bank_settings_param import BankSettingsParam
from .wealth_and_employment_details_param import WealthAndEmploymentDetailsParam
from .shared_params.child_legal_entity_create import ChildLegalEntityCreate
from .shared_params.identification_create_request import IdentificationCreateRequest
from .shared_params.legal_entity_compliance_detail import LegalEntityComplianceDetail
from .shared_params.legal_entity_address_create_request import LegalEntityAddressCreateRequest
from .shared_params.legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = [
    "ConnectionLegalEntityCreateParams",
    "LegalEntity",
    "LegalEntityLegalEntityAssociations",
    "LegalEntityLegalEntityAssociation",
    "LegalEntityPhoneNumbers",
    "LegalEntityPhoneNumber",
]


class ConnectionLegalEntityCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the connection."""

    legal_entity: LegalEntity
    """The legal entity."""

    legal_entity_id: str
    """The ID of the legal entity."""


class LegalEntityLegalEntityAssociation(TypedDict, total=False):
    relationship_types: Required[List[Literal["beneficial_owner", "control_person"]]]

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
