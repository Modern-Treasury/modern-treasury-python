# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LegalEntityAssociationCreateParams",
    "AssociatedLegalEntity",
    "AssociatedLegalEntityAddresses",
    "AssociatedLegalEntityAddress",
    "AssociatedLegalEntityIdentifications",
    "AssociatedLegalEntityIdentification",
    "AssociatedLegalEntityPhoneNumbers",
    "AssociatedLegalEntityPhoneNumber",
]


class LegalEntityAssociationCreateParams(TypedDict, total=False):
    relationship_types: Required[List[Literal["beneficial_owner", "control_person"]]]

    associated_legal_entity: AssociatedLegalEntity
    """The associated legal entity."""

    associated_legal_entity_id: str
    """The ID of the associated legal entity."""

    associator_legal_entity_id: str
    """The ID of the associator legal entity.

    This must be a business or joint legal entity.
    """

    ownership_percentage: Optional[int]
    """The associated entity's ownership percentage iff they are a beneficial owner."""

    title: Optional[str]
    """The job title of the associated entity at the associator entity."""


class AssociatedLegalEntityAddress(TypedDict, total=False):
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


AssociatedLegalEntityAddresses = AssociatedLegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use AssociatedLegalEntityAddress instead.
"""


class AssociatedLegalEntityIdentification(TypedDict, total=False):
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


AssociatedLegalEntityIdentifications = AssociatedLegalEntityIdentification
"""This type is deprecated and will be removed in a future release.

Please use AssociatedLegalEntityIdentification instead.
"""


class AssociatedLegalEntityPhoneNumber(TypedDict, total=False):
    phone_number: str


AssociatedLegalEntityPhoneNumbers = AssociatedLegalEntityPhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use AssociatedLegalEntityPhoneNumber instead.
"""


class AssociatedLegalEntity(TypedDict, total=False):
    addresses: Iterable[AssociatedLegalEntityAddress]
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

    identifications: Iterable[AssociatedLegalEntityIdentification]
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

    phone_numbers: Iterable[AssociatedLegalEntityPhoneNumber]

    website: Optional[str]
    """The entity's primary website URL."""
