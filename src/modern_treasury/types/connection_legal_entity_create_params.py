# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .bank_settings_param import BankSettingsParam
from .wealth_and_employment_details_param import WealthAndEmploymentDetailsParam
from .shared_params.third_party_verification import ThirdPartyVerification
from .shared_params.identification_create_request import IdentificationCreateRequest
from .shared_params.legal_entity_address_create_request import LegalEntityAddressCreateRequest
from .shared_params.legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = [
    "ConnectionLegalEntityCreateParams",
    "LegalEntity",
    "LegalEntityDocuments",
    "LegalEntityDocument",
    "LegalEntityPhoneNumbers",
    "LegalEntityPhoneNumber",
    "LegalEntityRegulators",
    "LegalEntityRegulator",
]


class ConnectionLegalEntityCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the connection."""

    legal_entity: LegalEntity
    """The legal entity."""

    legal_entity_id: str
    """The ID of the legal entity."""


class LegalEntityDocument(TypedDict, total=False):
    document_type: Required[
        Literal[
            "articles_of_incorporation",
            "certificate_of_good_standing",
            "ein_letter",
            "generic",
            "identification_back",
            "identification_front",
            "proof_of_address",
        ]
    ]
    """A category given to the document, can be `null`."""

    file_data: Required[str]
    """Base64-encoded file content for the document."""

    filename: str
    """The original filename of the document."""


LegalEntityDocuments = LegalEntityDocument
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityDocument instead.
"""


class LegalEntityPhoneNumber(TypedDict, total=False):
    """A list of phone numbers in E.164 format."""

    phone_number: str


LegalEntityPhoneNumbers = LegalEntityPhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityPhoneNumber instead.
"""


class LegalEntityRegulator(TypedDict, total=False):
    jurisdiction: Required[str]
    """
    The country code where the regulator operates in the ISO 3166-1 alpha-2 format
    (e.g., "US", "CA", "GB").
    """

    name: Required[str]
    """Full name of the regulatory body."""

    registration_number: Required[str]
    """Registration or identification number with the regulator."""


LegalEntityRegulators = LegalEntityRegulator
"""This type is deprecated and will be removed in a future release.

Please use LegalEntityRegulator instead.
"""


class LegalEntity(TypedDict, total=False):
    """The legal entity."""

    addresses: Iterable[LegalEntityAddressCreateRequest]
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettingsParam]

    business_description: Optional[str]
    """A description of the business."""

    business_name: Optional[str]
    """The business's legal business name."""

    citizenship_country: Optional[str]
    """The country of citizenship for an individual."""

    compliance_details: Optional[object]

    connection_id: Optional[str]
    """The connection ID for the connection the legal entity is associated with.

    Defaults to the id of the connection designated with an is_default value of true
    or the id of an existing operational connection if only one is available. Pass
    in a value of null to prevent the connection from being associated with the
    legal entity.
    """

    country_of_incorporation: Optional[str]
    """
    The country code where the business is incorporated in the ISO 3166-1 alpha-2 or
    alpha-3 formats.
    """

    date_formed: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """An individual's date of birth (YYYY-MM-DD)."""

    documents: Iterable[LegalEntityDocument]
    """A list of documents to attach to the legal entity (e.g.

    articles of incorporation, certificate of good standing, proof of address).
    """

    doing_business_as_names: SequenceNotStr[str]

    email: Optional[str]
    """The entity's primary email."""

    expected_activity_volume: Optional[int]
    """Monthly expected transaction volume in USD."""

    external_id: Optional[str]
    """An optional user-defined 180 character unique identifier."""

    first_name: Optional[str]
    """An individual's first name."""

    identifications: Iterable[IdentificationCreateRequest]
    """A list of identifications for the legal entity."""

    industry_classifications: Iterable[LegalEntityIndustryClassification]
    """A list of industry classifications for the legal entity."""

    intended_use: Optional[str]
    """A description of the intended use of the legal entity."""

    last_name: Optional[str]
    """An individual's last name."""

    legal_entity_associations: Optional[Iterable["LegalEntityAssociationInlineCreate"]]
    """The legal entity associations and its child legal entities."""

    legal_entity_type: Literal["business", "individual"]
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ]
    """The business's legal structure."""

    listed_exchange: Optional[str]
    """ISO 10383 market identifier code."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str]
    """An individual's middle name."""

    operating_jurisdictions: SequenceNotStr[str]
    """
    A list of countries where the business operates (ISO 3166-1 alpha-2 or alpha-3
    codes).
    """

    phone_numbers: Iterable[LegalEntityPhoneNumber]

    politically_exposed_person: Optional[bool]
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str]
    """An individual's preferred name."""

    prefix: Optional[str]
    """An individual's prefix."""

    primary_social_media_sites: SequenceNotStr[str]
    """A list of primary social media URLs for the business."""

    regulators: Optional[Iterable[LegalEntityRegulator]]
    """Array of regulatory bodies overseeing this institution."""

    risk_rating: Optional[Literal["low", "medium", "high"]]
    """The risk rating of the legal entity. One of low, medium, high."""

    service_provider_legal_entity_id: Optional[str]
    """The UUID of the parent legal entity in the service provider tree."""

    suffix: Optional[str]
    """An individual's suffix."""

    third_party_verification: Optional[ThirdPartyVerification]
    """Deprecated. Use `third_party_verifications` instead."""

    third_party_verifications: Iterable[ThirdPartyVerification]
    """A list of third-party verifications run by external vendors."""

    ticker_symbol: Optional[str]
    """Stock ticker symbol for publicly traded companies."""

    wealth_and_employment_details: Optional[WealthAndEmploymentDetailsParam]

    website: Optional[str]
    """The entity's primary website URL."""


from .shared_params.legal_entity_association_inline_create import LegalEntityAssociationInlineCreate
