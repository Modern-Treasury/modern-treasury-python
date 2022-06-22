# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PartyAddress",
    "AccountDetails",
    "RoutingDetailsBankAddress",
    "RoutingDetails",
    "Connection",
    "InternalAccount",
]


class PartyAddress(BaseModel):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: str

    id: str

    line1: Optional[str]

    line2: Optional[str]

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[str]
    """Locality or City."""

    object: str

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""

    updated_at: str


class AccountDetails(BaseModel):
    account_number: str

    account_number_type: Literal["iban", "clabe", "wallet_address", "pan", "other"]
    """
    Supports iban and clabe, otherwise other if the bank account number is in a
    generic format.
    """

    created_at: str

    discarded_at: Optional[str]

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: str


class RoutingDetailsBankAddress(BaseModel):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: str

    id: str

    line1: Optional[str]

    line2: Optional[str]

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[str]
    """Locality or City."""

    object: str

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""

    updated_at: str


class RoutingDetails(BaseModel):
    bank_address: Optional[RoutingDetailsBankAddress]

    bank_name: str

    created_at: str

    discarded_at: Optional[str]

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    payment_type: Optional[
        Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
    ]
    """
    If the routing detail is to be used for a specific payment type this field will
    be populated, otherwise null.
    """

    routing_number: str
    """The routing number of the bank."""

    routing_number_type: Literal[
        "aba", "swift", "au_bsb", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "br_codigo"
    ]

    updated_at: str


class Connection(BaseModel):
    created_at: str

    discarded_at: Optional[str]

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: str

    vendor_customer_id: Optional[str]
    """The identifier of the vendor bank."""

    vendor_id: str
    """The identifier of the vendor bank."""

    vendor_name: str
    """The name of the vendor bank."""


class InternalAccount(BaseModel):
    account_details: List[AccountDetails]
    """An array of account detail objects."""

    account_type: Optional[Literal["checking", "other", "savings"]]
    """Can be checking, savings or other."""

    connection: Connection
    """Specifies which financial institution the accounts belong to."""

    created_at: str

    currency: Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BCH",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTC",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNH",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EEK",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GBX",
        "GEL",
        "GGP",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "IMP",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JEP",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MRU",
        "MTL",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SKK",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMM",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XCD",
        "XDR",
        "XFU",
        "XOF",
        "XPD",
        "XPF",
        "XPT",
        "XTS",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
        "ZWD",
        "ZWL",
        "ZWN",
        "ZWR",
    ]
    """The currency of the account."""

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the account."""

    object: str

    parent_account_id: Optional[str]

    party_address: Optional[PartyAddress]
    """The address associated with the owner or null."""

    party_name: str
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]]
    """Either individual or business."""

    routing_details: List[RoutingDetails]
    """An array of routing detail objects."""

    updated_at: str
