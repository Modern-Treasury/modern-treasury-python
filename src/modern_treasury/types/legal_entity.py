# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LegalEntity", "Addresses", "Address", "Identifications", "Identification", "PhoneNumbers", "PhoneNumber"]


class Address(BaseModel):
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


Addresses = Address
"""This type is deprecated and will be removed in a future release.

Please use Address instead.
"""


class Identification(BaseModel):
    id: str

    created_at: datetime

    discarded_at: Optional[datetime] = None

    id_type: Literal[
        "ar_cuil",
        "ar_cuit",
        "br_cnpj",
        "br_cpf",
        "cl_nut",
        "co_cedulas",
        "co_nit",
        "hn_id",
        "hn_rtn",
        "passport",
        "us_ein",
        "us_itin",
        "us_ssn",
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


Identifications = Identification
"""This type is deprecated and will be removed in a future release.

Please use Identification instead.
"""


class PhoneNumber(BaseModel):
    phone_number: Optional[str] = None


PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""


class LegalEntity(BaseModel):
    id: Optional[str] = None

    addresses: Optional[List[Address]] = None
    """A list of addresses for the entity."""

    business_name: Optional[str] = None
    """The business's legal business name."""

    created_at: Optional[datetime] = None

    date_of_birth: Optional[date] = None
    """An individual's data of birth (YYYY-MM-DD)."""

    discarded_at: Optional[datetime] = None

    doing_business_as_names: Optional[List[str]] = None

    email: Optional[str] = None
    """The entity's primary email."""

    first_name: Optional[str] = None
    """An individual's first name."""

    identifications: Optional[List[Identification]] = None
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

    phone_numbers: Optional[List[PhoneNumber]] = None

    updated_at: Optional[datetime] = None

    website: Optional[str] = None
    """The entity's primary website URL."""
