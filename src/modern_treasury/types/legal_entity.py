# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .document import Document
from .bank_settings import BankSettings
from .wealth_and_employment_details import WealthAndEmploymentDetails
from .shared.third_party_verification import ThirdPartyVerification
from .shared.legal_entity_industry_classification import LegalEntityIndustryClassification

__all__ = [
    "LegalEntity",
    "Addresses",
    "Address",
    "Identifications",
    "Identification",
    "PhoneNumbers",
    "PhoneNumber",
    "Regulators",
    "Regulator",
    "TermsOfUse",
]


class Address(BaseModel):
    id: str

    address_types: List[
        Literal["business", "business_physical", "business_registered", "mailing", "other", "po_box", "residential"]
    ]
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

    primary: Optional[bool] = None
    """Whether this address is the primary address for the legal entity.

    Optional; when omitted it is inferred from the address types.
    """

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

    documents: List[Document]

    expiration_date: Optional[date] = None
    """
    The date when the Identification is no longer considered valid by the issuing
    authority.
    """

    id_type: Literal[
        "ar_cuil",
        "ar_cuit",
        "at_atin",
        "at_vat",
        "au_abn",
        "au_tfn",
        "be_ent",
        "be_nrn",
        "br_cnpj",
        "br_cpf",
        "ca_bn",
        "ca_sin",
        "ch_ahv",
        "ch_uid",
        "cl_run",
        "cl_rut",
        "co_cedulas",
        "co_nit",
        "cy_tin",
        "cz_ico",
        "cz_rc",
        "de_stid",
        "de_stnr",
        "de_vat",
        "dk_cpr",
        "dk_cvr",
        "drivers_license",
        "ee_ik",
        "ee_rk",
        "es_nie",
        "es_nif",
        "fi_hetu",
        "fi_ytj",
        "fr_nif",
        "fr_siren",
        "fr_vat",
        "gb_nino",
        "gb_utr",
        "gb_vat",
        "generic_international",
        "gr_vat",
        "hn_id",
        "hn_rtn",
        "hr_oib",
        "hu_adj",
        "hu_anum",
        "ie_pps",
        "ie_trn",
        "in_lei",
        "is_knt",
        "it_cf",
        "it_piva",
        "jp_hb",
        "jp_mn",
        "kr_brn",
        "kr_crn",
        "kr_rrn",
        "li_peid",
        "lt_ak",
        "lt_jak",
        "lu_mtc",
        "lu_vat",
        "lv_pk",
        "lv_rn",
        "mt_tin",
        "mt_vat",
        "mx_curp",
        "mx_ine",
        "mx_rfc",
        "national_id",
        "nl_bsn",
        "nl_btw",
        "nl_rsin",
        "no_fdn",
        "no_mva",
        "no_orgnr",
        "nz_ird",
        "passport",
        "pl_nip",
        "pl_pesel",
        "pt_nif",
        "ro_cnp",
        "ro_cui",
        "sa_tin",
        "sa_vat",
        "se_orgnr",
        "se_pnmr",
        "sg_fin",
        "sg_nric",
        "sg_uen",
        "si_dav",
        "si_tin",
        "sk_ico",
        "sk_rc",
        "us_ein",
        "us_itin",
        "us_ssn",
        "uy_rut",
        "vn_tin",
    ]
    """The type of ID number."""

    issuing_country: Optional[str] = None
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """

    issuing_region: Optional[str] = None
    """The region in which the identifcation was issued."""

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


class LegalEntity(BaseModel):
    id: str

    addresses: List[Address]
    """A list of addresses for the entity."""

    bank_settings: Optional[BankSettings] = None

    business_description: Optional[str] = None
    """A description of the business."""

    business_name: Optional[str] = None
    """The business's legal business name."""

    citizenship_country: Optional[str] = None
    """The country of citizenship for an individual."""

    compliance_details: Optional[object] = None

    country_of_incorporation: Optional[str] = None
    """
    The country where the business is incorporated, as an ISO 3166-1 alpha-2 country
    code (e.g. US).
    """

    created_at: datetime

    date_formed: Optional[date] = None
    """A business's formation date (YYYY-MM-DD)."""

    date_of_birth: Optional[date] = None
    """An individual's date of birth (YYYY-MM-DD)."""

    discarded_at: Optional[datetime] = None

    documents: List[Document]

    doing_business_as_names: List[str]

    email: Optional[str] = None
    """The entity's primary email."""

    expected_activity_volume: Optional[int] = None
    """Monthly expected transaction volume in USD."""

    external_id: Optional[str] = None
    """An optional user-defined 180 character unique identifier."""

    first_name: Optional[str] = None
    """An individual's first name."""

    identifications: List[Identification]
    """A list of identifications for the legal entity."""

    industry_classifications: List[LegalEntityIndustryClassification]
    """A list of industry classifications for the legal entity."""

    intended_use: Optional[str] = None
    """A description of the intended use of the legal entity."""

    last_name: Optional[str] = None
    """An individual's last name."""

    legal_entity_type: Literal["business", "individual"]
    """The type of legal entity."""

    legal_structure: Optional[
        Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
    ] = None
    """The business's legal structure."""

    listed_exchange: Optional[str] = None
    """ISO 10383 market identifier code."""

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

    operating_jurisdictions: List[str]
    """
    A list of countries where the business operates, as ISO 3166-1 alpha-2 country
    codes (e.g. ["US", "CA"]).
    """

    phone_numbers: List[PhoneNumber]

    politically_exposed_person: Optional[bool] = None
    """Whether the individual is a politically exposed person."""

    preferred_name: Optional[str] = None
    """An individual's preferred name."""

    prefix: Optional[str] = None
    """An individual's prefix."""

    primary_social_media_sites: List[str]
    """A list of primary social media URLs for the business."""

    regulators: Optional[List[Regulator]] = None
    """Array of regulatory bodies overseeing this institution."""

    risk_rating: Optional[Literal["low", "medium", "high"]] = None
    """The risk rating of the legal entity. One of low, medium, high."""

    service_provider_legal_entity_id: Optional[str] = None
    """The UUID of the parent legal entity in the service provider tree."""

    status: Optional[Literal["active", "denied", "pending", "suspended"]] = None
    """The activation status of the legal entity.

    One of pending, active, suspended, or denied.
    """

    suffix: Optional[str] = None
    """An individual's suffix."""

    terms_of_use: Optional[TermsOfUse] = None
    """Acceptance of terms of use by the legal entity."""

    third_party_verification: Optional[ThirdPartyVerification] = None
    """Deprecated. Use `third_party_verifications` instead."""

    third_party_verifications: List[ThirdPartyVerification]
    """A list of third-party verifications run by external vendors."""

    ticker_symbol: Optional[str] = None
    """Stock ticker symbol for publicly traded companies."""

    updated_at: datetime

    wealth_and_employment_details: Optional[WealthAndEmploymentDetails] = None

    website: Optional[str] = None
    """The entity's primary website URL."""

    legal_entity_associations: Optional[List["LegalEntityAssociation"]] = None
    """The legal entity associations and its child legal entities."""


from .legal_entity_association import LegalEntityAssociation
