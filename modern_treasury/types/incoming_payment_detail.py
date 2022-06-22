# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "VirtualAccountAccountDetails",
    "VirtualAccountRoutingDetailsBankAddress",
    "VirtualAccountRoutingDetails",
    "VirtualAccount",
    "IncomingPaymentDetail",
]


class VirtualAccountAccountDetails(BaseModel):
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


class VirtualAccountRoutingDetailsBankAddress(BaseModel):
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


class VirtualAccountRoutingDetails(BaseModel):
    bank_address: Optional[VirtualAccountRoutingDetailsBankAddress]

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


class VirtualAccount(BaseModel):
    account_details: List[VirtualAccountAccountDetails]
    """An array of account detail objects."""

    counterparty_id: Optional[str]
    """The ID of a counterparty that the virtual account belongs to. Optional."""

    created_at: str

    credit_ledger_account_id: Optional[str]
    """The ID of a credit normal ledger account.

    When money enters the virtual account, this ledger account will be credited.
    Must be accompanied by a debit_ledger_account_id if present.
    """

    debit_ledger_account_id: Optional[str]
    """The ID of a debit normal ledger account.

    When money enters the virtual account, this ledger account will be debited. Must
    be accompanied by a credit_ledger_account_id if present.
    """

    description: Optional[str]
    """An optional free-form description for internal use."""

    discarded_at: Optional[str]

    id: str

    internal_account_id: str
    """The ID of the internal account that the virtual account is in."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """The name of the virtual account."""

    object: str

    routing_details: List[VirtualAccountRoutingDetails]
    """An array of routing detail objects.

    These will be the routing details of the internal account.
    """

    updated_at: str


class IncomingPaymentDetail(BaseModel):
    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: str
    """The date on which the corresponding transaction will occur."""

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
    """The currency of the incoming payment detail."""

    data: object
    """The raw data from the payment pre-notification file that we get from the bank."""

    direction: Literal["credit", "debit"]
    """One of `credit` or `debit`."""

    id: str

    internal_account_id: str
    """The ID of the Internal Account for the incoming payment detail.

    This is always present.
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    object: str

    status: Literal["completed", "pending", "returned"]
    """The current status of the incoming payment order.

    One of `pending`, `completed`, or `returned`.
    """

    transaction_id: Optional[str]
    """The ID of the reconciled Transaction or `null`."""

    transaction_line_item_id: Optional[str]
    """The ID of the reconciled Transaction Line Item or `null`."""

    type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"]
    """One of: `ach`, `wire`, `check`, `rtp`, `sepa`, `signet`."""

    updated_at: str

    vendor_id: Optional[str]
    """The identifier of the vendor bank."""

    virtual_account: Optional[VirtualAccount]
    """
    If the incoming payment detail is in a virtual account, the serialized virtual
    account object.
    """

    virtual_account_id: Optional[str]
    """
    If the incoming payment detail is in a virtual account, the ID of the Virtual
    Account.
    """
