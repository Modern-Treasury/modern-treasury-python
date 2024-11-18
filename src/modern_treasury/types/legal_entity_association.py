# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .bank_settings import BankSettings
from .wealth_and_employment_details import WealthAndEmploymentDetails

__all__ = [
    "LegalEntityAssociation",
    "ChildLegalEntity",
    "ChildLegalEntityAddresses",
    "ChildLegalEntityAddress",
    "ChildLegalEntityIdentifications",
    "ChildLegalEntityIdentification",
    "ChildLegalEntityPhoneNumbers",
    "ChildLegalEntityPhoneNumber",
]


class ChildLegalEntityAddress(BaseModel):
    id: str

    address_types: List[Literal["business", "mailing", "other", "po_box", "residential"]]
    """The types of this address."""

    country: Optional[str] = None
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[str] = None
    """Locality or City."""

    object: str

    postal_code: Optional[str] = None
    """The postal code of the address."""

    region: Optional[str] = None
    """Region or State."""

    updated_at: datetime


ChildLegalEntityAddresses = ChildLegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use ChildLegalEntityAddress instead.
"""


class ChildLegalEntityIdentification(BaseModel):
    id: str

    created_at: datetime

    discarded_at: Optional[datetime] = None

    id_type: Literal[
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
    """The type of ID number."""

    issuing_country: Optional[str] = None
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime


ChildLegalEntityIdentifications = ChildLegalEntityIdentification
"""This type is deprecated and will be removed in a future release.

Please use ChildLegalEntityIdentification instead.
"""


class ChildLegalEntityPhoneNumber(BaseModel):
    phone_number: Optional[str] = None


ChildLegalEntityPhoneNumbers = ChildLegalEntityPhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use ChildLegalEntityPhoneNumber instead.
"""


class ChildLegalEntity(BaseModel):
    id: str

    addresses: List[ChildLegalEntityAddress]
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettings] = None

    business_name: Optional[str] = None
    """The business's legal business name."""

    citizenship_country: Optional[str] = None
    """The country of citizenship for an individual."""

    created_at: datetime

    date_formed: Optional[date] = None
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Optional[date] = None
    """An individual's date of birth (YYYY-MM-DD)."""

    discarded_at: Optional[datetime] = None

    doing_business_as_names: List[str]

    email: Optional[str] = None
    """The entity's primary email."""

    first_name: Optional[str] = None
    """An individual's first name."""

    identifications: List[ChildLegalEntityIdentification]
    """A list of identifications for the legal entity."""

    last_name: Optional[str] = None
    """An individual's last name."""

    legal_entity_type: Literal["business", "individual", "joint"]
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ] = None
    """The business's legal structure."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str] = None
    """An individual's middle name."""

    object: str

    phone_numbers: List[ChildLegalEntityPhoneNumber]

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

    updated_at: datetime

    wealth_and_employment_details: Optional[WealthAndEmploymentDetails] = None

    website: Optional[str] = None
    """The entity's primary website URL."""


class LegalEntityAssociation(BaseModel):
    id: str

    child_legal_entity: ChildLegalEntity
    """The child legal entity."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    ownership_percentage: Optional[int] = None
    """The child entity's ownership percentage iff they are a beneficial owner."""

    parent_legal_entity_id: str
    """The ID of the parent legal entity.

    This must be a business or joint legal entity.
    """

    relationship_types: List[Literal["beneficial_owner", "control_person"]]

    title: Optional[str] = None
    """The job title of the child entity at the parent entity."""

    updated_at: datetime
