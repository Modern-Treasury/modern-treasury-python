# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .bank_settings_param import BankSettingsParam
from .wealth_and_employment_details_param import WealthAndEmploymentDetailsParam
from .shared_params.legal_entity_compliance_detail import LegalEntityComplianceDetail
from .shared_params.legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = [
    "LegalEntityCreateParams",
    "Addresses",
    "Address",
    "Identifications",
    "Identification",
    "LegalEntityAssociations",
    "LegalEntityAssociation",
    "LegalEntityAssociationsChildLegalEntity",
    "LegalEntityAssociationChildLegalEntity",
    "LegalEntityAssociationsChildLegalEntityAddresses",
    "LegalEntityAssociationChildLegalEntityAddress",
    "LegalEntityAssociationsChildLegalEntityIdentifications",
    "LegalEntityAssociationChildLegalEntityIdentification",
    "LegalEntityAssociationsChildLegalEntityPhoneNumbers",
    "LegalEntityAssociationChildLegalEntityPhoneNumber",
    "PhoneNumbers",
    "PhoneNumber",
]


class LegalEntityCreateParams(TypedDict, total=False):
    legal_entity_type: Required[Literal["business", "individual"]]
    """The type of legal entity."""

    addresses: Iterable[Address]
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

    identifications: Iterable[Identification]
    """A list of identifications for the legal entity."""

    industry_classifications: Iterable[LegalEntityIndustryClassification]
    """A list of industry classifications for the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

    legal_entity_associations: Optional[Iterable[LegalEntityAssociation]]
    """The legal entity associations and its child legal entities."""

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

    phone_numbers: Iterable[PhoneNumber]

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
            "cl_run",
            "cl_rut",
            "co_cedulas",
            "co_nit",
            "drivers_license",
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

    expiration_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    The date when the Identification is no longer considered valid by the issuing
    authority.
    """

    issuing_country: Optional[str]
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """

    issuing_region: Optional[str]
    """The region in which the identifcation was issued."""


Identifications = Identification
"""This type is deprecated and will be removed in a future release.

Please use Identification instead.
"""


class LegalEntityAssociationChildLegalEntityAddress(TypedDict, total=False):
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


LegalEntityAssociationsChildLegalEntityAddresses = LegalEntityAssociationChildLegalEntityAddress
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityAssociationChildLegalEntityAddress instead.
"""


class LegalEntityAssociationChildLegalEntityIdentification(TypedDict, total=False):
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
            "drivers_license",
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

    expiration_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    The date when the Identification is no longer considered valid by the issuing
    authority.
    """

    issuing_country: Optional[str]
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """

    issuing_region: Optional[str]
    """The region in which the identifcation was issued."""


LegalEntityAssociationsChildLegalEntityIdentifications = LegalEntityAssociationChildLegalEntityIdentification
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityAssociationChildLegalEntityIdentification instead.
"""


class LegalEntityAssociationChildLegalEntityPhoneNumber(TypedDict, total=False):
    phone_number: str


LegalEntityAssociationsChildLegalEntityPhoneNumbers = LegalEntityAssociationChildLegalEntityPhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityAssociationChildLegalEntityPhoneNumber instead.
"""


class LegalEntityAssociationChildLegalEntity(TypedDict, total=False):
    addresses: Iterable[LegalEntityAssociationChildLegalEntityAddress]
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

    identifications: Iterable[LegalEntityAssociationChildLegalEntityIdentification]
    """A list of identifications for the legal entity."""

    industry_classifications: Iterable[LegalEntityIndustryClassification]
    """A list of industry classifications for the legal entity."""

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

    phone_numbers: Iterable[LegalEntityAssociationChildLegalEntityPhoneNumber]

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


LegalEntityAssociationsChildLegalEntity = LegalEntityAssociationChildLegalEntity
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityAssociationChildLegalEntity instead.
"""


class LegalEntityAssociation(TypedDict, total=False):
    relationship_types: Required[List[Literal["beneficial_owner", "control_person"]]]

    child_legal_entity: LegalEntityAssociationChildLegalEntity
    """The child legal entity."""

    child_legal_entity_id: str
    """The ID of the child legal entity."""

    ownership_percentage: Optional[int]
    """The child entity's ownership percentage iff they are a beneficial owner."""

    title: Optional[str]
    """The job title of the child entity at the parent entity."""


LegalEntityAssociations = LegalEntityAssociation
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityAssociation instead.
"""


class PhoneNumber(TypedDict, total=False):
    phone_number: str


PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""
