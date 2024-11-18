# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .bank_settings_param import BankSettingsParam
from .wealth_and_employment_details_param import WealthAndEmploymentDetailsParam

__all__ = [
    "LegalEntityAssociationCreateParams",
    "ChildLegalEntity",
    "ChildLegalEntityAddresses",
    "ChildLegalEntityAddress",
    "ChildLegalEntityIdentifications",
    "ChildLegalEntityIdentification",
    "ChildLegalEntityPhoneNumbers",
    "ChildLegalEntityPhoneNumber",
]


class LegalEntityAssociationCreateParams(TypedDict, total=False):
    parent_legal_entity_id: Required[str]
    """The ID of the parent legal entity.

    This must be a business or joint legal entity.
    """

    relationship_types: Required[List[Literal["beneficial_owner", "control_person"]]]

    child_legal_entity: ChildLegalEntity
    """The child legal entity."""

    child_legal_entity_id: str
    """The ID of the child legal entity."""

    ownership_percentage: Optional[int]
    """The child entity's ownership percentage iff they are a beneficial owner."""

    title: Optional[str]
    """The job title of the child entity at the parent entity."""


class ChildLegalEntityAddress(TypedDict, total=False):
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


ChildLegalEntityAddresses = ChildLegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use ChildLegalEntityAddress instead.
"""


class ChildLegalEntityIdentification(TypedDict, total=False):
    id_number: Required[str]
    """The ID number of identification document."""

    id_type: Required[
        Literal[
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
    ]
    """The type of ID number."""

    issuing_country: Optional[str]
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """


ChildLegalEntityIdentifications = ChildLegalEntityIdentification
"""This type is deprecated and will be removed in a future release.

Please use ChildLegalEntityIdentification instead.
"""


class ChildLegalEntityPhoneNumber(TypedDict, total=False):
    phone_number: str


ChildLegalEntityPhoneNumbers = ChildLegalEntityPhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use ChildLegalEntityPhoneNumber instead.
"""


class ChildLegalEntity(TypedDict, total=False):
    addresses: Iterable[ChildLegalEntityAddress]
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettingsParam]

    business_name: Optional[str]
    """The business's legal business name."""

    citizenship_country: Optional[str]
    """The country of citizenship for an individual."""

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[ChildLegalEntityIdentification]
    """A list of identifications for the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

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

    phone_numbers: Iterable[ChildLegalEntityPhoneNumber]

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
