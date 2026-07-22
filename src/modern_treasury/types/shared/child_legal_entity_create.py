# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List, Dict

from datetime import datetime, date

from .legal_entity_address_create_request import LegalEntityAddressCreateRequest

from ..bank_settings import BankSettings

from .identification_create_request import IdentificationCreateRequest

from .legal_entity_industry_classification import LegalEntityIndustryClassification

from .third_party_verification import ThirdPartyVerification

from ..wealth_and_employment_details import WealthAndEmploymentDetails

__all__ = ["ChildLegalEntityCreate", "Documents", "Document", "PhoneNumbers", "PhoneNumber", "Regulators", "Regulator", "TermsOfUse"]

class Document(BaseModel):
    document_type: Literal["articles_of_incorporation", "certificate_of_good_standing", "ein_letter", "generic", "identification_back", "identification_front", "proof_of_address"]
    """A category given to the document, can be `null`."""

    file_data: str
    """Base64-encoded file content for the document."""

    filename: Optional[str] = None
    """The original filename of the document."""

Documents = Document
"""This type is deprecated and will be removed in a future release.

Please use Document instead.
"""

class PhoneNumber(BaseModel):
    """A list of phone numbers in E.164 format."""
    phone_number: Optional[str] = None

PhoneNumbers = PhoneNumber
"""This type is deprecated and will be removed in a future release.

Please use PhoneNumber instead.
"""

class Regulator(BaseModel):
    jurisdiction: str
    """
    The country code where the regulator operates in the ISO 3166-1 alpha-2 format
    (e.g., "US", "CA", "GB").
    """

    name: str
    """Full name of the regulatory body."""

    registration_number: str
    """Registration or identification number with the regulator."""

Regulators = Regulator
"""This type is deprecated and will be removed in a future release.

Please use Regulator instead.
"""

class TermsOfUse(BaseModel):
    """Acceptance of terms of use by the legal entity."""
    accepted_at: Optional[datetime] = None
    """The ISO 8601 timestamp indicating when the terms of use were accepted."""

    ip_address: Optional[str] = None
    """The IP address from which the terms of use were accepted.

    Supports both IPv4 and IPv6 formats.
    """

class ChildLegalEntityCreate(BaseModel):
    addresses: Optional[List[LegalEntityAddressCreateRequest]] = None
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettings] = None

    business_description: Optional[str] = None
    """A description of the business."""

    business_name: Optional[str] = None
    """The business's legal business name."""

    citizenship_country: Optional[str] = None
    """The country of citizenship for an individual."""

    compliance_details: Optional[object] = None

    connection_id: Optional[str] = None
    """The connection ID for the connection the legal entity is associated with.

    Defaults to the id of the connection designated with an is_default value of true
    or the id of an existing operational connection if only one is available. Pass
    in a value of null to prevent the connection from being associated with the
    legal entity.
    """

    country_of_incorporation: Optional[str] = None
    """
    The country code where the business is incorporated in the ISO 3166-1 alpha-2 or
    alpha-3 formats.
    """

    date_formed: Optional[date] = None
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Optional[date] = None
    """An individual's date of birth (YYYY-MM-DD)."""

    documents: Optional[List[Document]] = None
    """A list of documents to attach to the legal entity (e.g.

    articles of incorporation, certificate of good standing, proof of address).
    """

    doing_business_as_names: Optional[List[str]] = None

    email: Optional[str] = None
    """The entity's primary email."""

    expected_activity_volume: Optional[int] = None
    """Monthly expected transaction volume in USD."""

    external_id: Optional[str] = None
    """An optional user-defined 180 character unique identifier."""

    first_name: Optional[str] = None
    """An individual's first name."""

    identifications: Optional[List[IdentificationCreateRequest]] = None
    """A list of identifications for the legal entity."""

    industry_classifications: Optional[List[LegalEntityIndustryClassification]] = None
    """A list of industry classifications for the legal entity."""

    intended_use: Optional[str] = None
    """A description of the intended use of the legal entity."""

    last_name: Optional[str] = None
    """An individual's last name."""

    legal_entity_associations: Optional[List["LegalEntityAssociationInlineCreate"]] = None
    """The legal entity associations and its child legal entities."""

    legal_entity_type: Optional[Literal["business", "individual"]] = None
    """The type of legal entity."""

    legal_structure: Optional[Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]] = None
    """The business's legal structure."""

    listed_exchange: Optional[str] = None
    """ISO 10383 market identifier code."""

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    middle_name: Optional[str] = None
    """An individual's middle name."""

    operating_jurisdictions: Optional[List[str]] = None
    """
    A list of countries where the business operates (ISO 3166-1 alpha-2 or alpha-3
    codes).
    """

    phone_numbers: Optional[List[PhoneNumber]] = None

    politically_exposed_person: Optional[bool] = None
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str] = None
    """An individual's preferred name."""

    prefix: Optional[str] = None
    """An individual's prefix."""

    primary_social_media_sites: Optional[List[str]] = None
    """A list of primary social media URLs for the business."""

    regulators: Optional[List[Regulator]] = None
    """Array of regulatory bodies overseeing this institution."""

    risk_rating: Optional[Literal["low", "medium", "high"]] = None
    """The risk rating of the legal entity. One of low, medium, high."""

    service_provider_legal_entity_id: Optional[str] = None
    """The UUID of the parent legal entity in the service provider tree."""

    suffix: Optional[str] = None
    """An individual's suffix."""

    terms_of_use: Optional[TermsOfUse] = None
    """Acceptance of terms of use by the legal entity."""

    third_party_verification: Optional[ThirdPartyVerification] = None
    """Deprecated. Use `third_party_verifications` instead."""

    third_party_verifications: Optional[List[ThirdPartyVerification]] = None
    """A list of third-party verifications run by external vendors."""

    ticker_symbol: Optional[str] = None
    """Stock ticker symbol for publicly traded companies."""

    wealth_and_employment_details: Optional[WealthAndEmploymentDetails] = None

    website: Optional[str] = None
    """The entity's primary website URL."""

from .legal_entity_association_inline_create import LegalEntityAssociationInlineCreate