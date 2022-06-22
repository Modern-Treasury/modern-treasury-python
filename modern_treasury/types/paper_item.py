# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaperItem"]


class PaperItem(BaseModel):
    account_number: Optional[str]
    """The account number on the paper item."""

    amount: int
    """The amount of the paper item."""

    check_number: Optional[str]
    """The check number on the paper item."""

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
    """The currency of the paper item."""

    deposit_date: str
    """The date the paper item was deposited into your organization's bank account."""

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    lockbox_number: str
    """The identifier for the lockbox assigned by the bank."""

    memo_field: Optional[str]
    """The memo field on the paper item."""

    object: str

    remitter_name: Optional[str]
    """The name of the remitter on the paper item."""

    routing_number: Optional[str]
    """The routing number on the paper item."""

    status: Literal["completed", "pending", "returned"]
    """The current status of the paper item.

    One of `pending`, `completed`, or `returned`.
    """

    transaction_id: Optional[str]
    """The ID of the reconciled Transaction or `null`."""

    transaction_line_item_id: Optional[str]
    """The ID of the reconciled Transaction Line Item or `null`."""

    updated_at: str
