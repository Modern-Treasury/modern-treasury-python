# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LegalEntityCreateParams",
    "Addresses",
    "Address",
    "Identifications",
    "Identification",
    "PhoneNumbers",
    "PhoneNumber",
]


class LegalEntityCreateParams(TypedDict, total=False):
    legal_entity_type: Required[Literal["business", "individual"]]
    """The type of legal entity."""

    addresses: Iterable[Address]
    """A list of addresses for the entity."""

    business_name: Optional[str]
    """The business's legal business name."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's data of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[Identification]
    """A list of identifications for the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ]
    """The business's legal structure."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    phone_numbers: Iterable[PhoneNumber]

    website: Optional[str]
    """The entity's primary website URL."""


class Address(TypedDict, total=False):
    country: Required[Optional[str]]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Required[Optional[str]]

    locality: Required[Optional[str]]
    """Locality or City."""

    postal_code: Required[Optional[str]]
    """The postal code of the address."""

    region: Required[Optional[str]]
    """Region or State."""

    address_types: List[Literal["business", "mailing", "other", "po_box", "residential"]]
    """The types of this address."""

    line2: Optional[str]


Addresses = Address
"""This type is deprecated and will be removed in a future release.

Please use Address instead.
"""


class Identification(TypedDict, total=False):
    id_number: Required[str]
    """The ID number of identification document."""

    id_type: Required[
        Literal[
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
    ]
    """The type of ID number."""

    issuing_country: Optional[str]
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """


Identifications = Identification
"""This type is deprecated and will be removed in a future release.

Please use Identification instead.
"""


class PhoneNumber(TypedDict, total=False):
    phone_number: str


PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""
