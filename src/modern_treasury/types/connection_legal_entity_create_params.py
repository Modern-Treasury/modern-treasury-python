# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ConnectionLegalEntityCreateParams",
    "LegalEntity",
    "LegalEntityAddresses",
    "LegalEntityAddress",
    "LegalEntityIdentifications",
    "LegalEntityIdentification",
    "LegalEntityLegalEntityAssociations",
    "LegalEntityLegalEntityAssociation",
    "LegalEntityLegalEntityAssociationsChildLegalEntity",
    "LegalEntityLegalEntityAssociationChildLegalEntity",
    "LegalEntityLegalEntityAssociationsChildLegalEntityAddresses",
    "LegalEntityLegalEntityAssociationChildLegalEntityAddress",
    "LegalEntityLegalEntityAssociationsChildLegalEntityIdentifications",
    "LegalEntityLegalEntityAssociationChildLegalEntityIdentification",
    "LegalEntityLegalEntityAssociationsChildLegalEntityPhoneNumbers",
    "LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber",
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


class LegalEntityAddress(TypedDict, total=False):
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


LegalEntityAddresses = LegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityAddress instead.
"""


class LegalEntityIdentification(TypedDict, total=False):
    id_number: Required[str]
    """The ID number of identification document."""

    id_type: Required[
        Literal[
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


LegalEntityIdentifications = LegalEntityIdentification
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityIdentification instead.
"""


class LegalEntityLegalEntityAssociationChildLegalEntityAddress(TypedDict, total=False):
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


LegalEntityLegalEntityAssociationsChildLegalEntityAddresses = LegalEntityLegalEntityAssociationChildLegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntityAddress instead.
"""


class LegalEntityLegalEntityAssociationChildLegalEntityIdentification(TypedDict, total=False):
    id_number: Required[str]
    """The ID number of identification document."""

    id_type: Required[
        Literal[
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


LegalEntityLegalEntityAssociationsChildLegalEntityIdentifications = (
    LegalEntityLegalEntityAssociationChildLegalEntityIdentification
)
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntityIdentification instead.
"""


class LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber(TypedDict, total=False):
    phone_number: str


LegalEntityLegalEntityAssociationsChildLegalEntityPhoneNumbers = (
    LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber
)
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber instead.
"""


class LegalEntityLegalEntityAssociationChildLegalEntity(TypedDict, total=False):
    addresses: Iterable[LegalEntityLegalEntityAssociationChildLegalEntityAddress]
    """A list of addresses for the entity."""

    business_name: Optional[str]
    """The business's legal business name."""

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[LegalEntityLegalEntityAssociationChildLegalEntityIdentification]
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

    phone_numbers: Iterable[LegalEntityLegalEntityAssociationChildLegalEntityPhoneNumber]

    risk_rating: Optional[Literal["low", "medium", "high"]]
    """Translation missing: en.openapi.descriptions.legal_entity.schema.risk_rating"""

    website: Optional[str]
    """The entity's primary website URL."""


LegalEntityLegalEntityAssociationsChildLegalEntity = LegalEntityLegalEntityAssociationChildLegalEntity
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityLegalEntityAssociationChildLegalEntity instead.
"""


class LegalEntityLegalEntityAssociation(TypedDict, total=False):
    relationship_types: Required[List[Literal["beneficial_owner", "control_person"]]]

    child_legal_entity: LegalEntityLegalEntityAssociationChildLegalEntity
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
    addresses: Iterable[LegalEntityAddress]
    """A list of addresses for the entity."""

    business_name: Optional[str]
    """The business's legal business name."""

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    doing_business_as_names: List[str]

    email: Optional[str]
    """The entity's primary email."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[LegalEntityIdentification]
    """A list of identifications for the legal entity."""

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

    phone_numbers: Iterable[LegalEntityPhoneNumber]

    risk_rating: Optional[Literal["low", "medium", "high"]]
    """Translation missing: en.openapi.descriptions.legal_entity.schema.risk_rating"""

    website: Optional[str]
    """The entity's primary website URL."""
