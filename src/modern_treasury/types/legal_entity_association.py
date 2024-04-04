# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

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
        "cl_rut",
        "co_cedulas",
        "co_nit",
        "hn_id",
        "hn_rtn",
        "in_lei",
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
    id: Optional[str] = None

    addresses: Optional[List[ChildLegalEntityAddress]] = None
    """A list of addresses for the entity."""

    business_name: Optional[str] = None
    """The business's legal business name."""

    created_at: Optional[datetime] = None

    date_formed: Optional[date] = None
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Optional[date] = None
    """An individual's date of birth (YYYY-MM-DD)."""

    discarded_at: Optional[datetime] = None

    doing_business_as_names: Optional[List[str]] = None

    email: Optional[str] = None
    """The entity's primary email."""

    first_name: Optional[str] = None
    """An individual's first name."""

    identifications: Optional[List[ChildLegalEntityIdentification]] = None
    """A list of identifications for the legal entity."""

    last_name: Optional[str] = None
    """An individual's last name."""

    legal_entity_type: Optional[Literal["business", "individual", "joint"]] = None
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ] = None
    """The business's legal structure."""

    live_mode: Optional[bool] = None
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    object: Optional[str] = None

    phone_numbers: Optional[List[ChildLegalEntityPhoneNumber]] = None

    updated_at: Optional[datetime] = None

    website: Optional[str] = None
    """The entity's primary website URL."""


class LegalEntityAssociation(BaseModel):
    id: Optional[str] = None

    child_legal_entity: Optional[ChildLegalEntity] = None
    """The child legal entity."""

    created_at: Optional[datetime] = None

    discarded_at: Optional[datetime] = None

    live_mode: Optional[bool] = None
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str] = None

    ownership_percentage: Optional[int] = None
    """The child entity's ownership percentage iff they are a beneficial owner."""

    parent_legal_entity_id: Optional[str] = None
    """The ID of the parent legal entity.

    This must be a business or joint legal entity.
    """

    relationship_types: Optional[List[Literal["beneficial_owner", "control_person"]]] = None

    title: Optional[str] = None
    """The job title of the child entity at the parent entity."""

    updated_at: Optional[datetime] = None
