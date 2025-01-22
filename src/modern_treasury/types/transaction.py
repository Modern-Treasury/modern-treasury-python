# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["Transaction", "ForeignExchangeRate"]


class ForeignExchangeRate(BaseModel):
    base_amount: int
    """
    Amount in the lowest denomination of the `base_currency` to convert, often
    called the "sell" amount.
    """

    base_currency: Currency
    """Currency to convert, often called the "sell" currency."""

    exponent: int
    """The exponent component of the rate.

    The decimal is calculated as `value` / (10 ^ `exponent`).
    """

    rate_string: str
    """A string representation of the rate."""

    target_amount: int
    """
    Amount in the lowest denomination of the `target_currency`, often called the
    "buy" amount.
    """

    target_currency: Currency
    """Currency to convert the `base_currency` to, often called the "buy" currency."""

    value: int
    """The whole number component of the rate.

    The decimal is calculated as `value` / (10 ^ `exponent`).
    """


class Transaction(BaseModel):
    id: str

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: Optional[date] = None
    """The date on which the transaction occurred."""

    as_of_time: Optional[str] = None
    """The time on which the transaction occurred.

    Depending on the granularity of the timestamp information received from the
    bank, it may be `null`.
    """

    as_of_timezone: Optional[str] = None
    """The timezone in which the `as_of_time` is represented.

    Can be `null` if the bank does not provide timezone info.
    """

    created_at: datetime

    currency: Currency
    """Currency that this transaction is denominated in."""

    custom_identifiers: Dict[str, str]
    """
    An object containing key-value pairs, each with a custom identifier as the key
    and a string value.
    """

    direction: str
    """Either `credit` or `debit`."""

    discarded_at: Optional[datetime] = None

    foreign_exchange_rate: Optional[ForeignExchangeRate] = None
    """Associated serialized foreign exchange rate information."""

    internal_account_id: str
    """The ID of the relevant Internal Account."""

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

    posted: bool
    """This field will be `true` if the transaction has posted to the account."""

    reconciled: bool
    """
    This field will be `true` if a transaction is reconciled by the Modern Treasury
    system. This means that it has transaction line items that sum up to the
    transaction's amount.
    """

    type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "chats",
        "check",
        "cross_border",
        "dk_nets",
        "eft",
        "hu_ics",
        "interac",
        "masav",
        "mx_ccen",
        "neft",
        "nics",
        "nz_becs",
        "pl_elixir",
        "provxchange",
        "ro_sent",
        "rtp",
        "se_bankgirot",
        "sen",
        "sepa",
        "sg_giro",
        "sic",
        "signet",
        "sknbi",
        "wire",
        "zengin",
        "other",
    ]
    """The type of the transaction.

    Examples could be `card, `ach`, `wire`, `check`, `rtp`, `book`, or `sen`.
    """

    updated_at: datetime

    vendor_code: Optional[str] = None
    """When applicable, the bank-given code that determines the transaction's category.

    For most banks this is the BAI2/BTRS transaction code.
    """

    vendor_code_type: Optional[
        Literal[
            "bai2",
            "banking_circle",
            "bankprov",
            "bnk_dev",
            "cleartouch",
            "column",
            "cross_river",
            "currencycloud",
            "dc_bank",
            "dwolla",
            "evolve",
            "goldman_sachs",
            "iso20022",
            "jpmc",
            "mx",
            "plaid",
            "pnc",
            "rspec_vendor",
            "signet",
            "silvergate",
            "swift",
            "us_bank",
            "user",
        ]
    ] = None
    """The type of `vendor_code` being reported.

    Can be one of `bai2`, `bankprov`, `bnk_dev`, `cleartouch`, `currencycloud`,
    `cross_river`, `dc_bank`, `dwolla`, `evolve`, `goldman_sachs`, `iso20022`,
    `jpmc`, `mx`, `signet`, `silvergate`, `swift`, `us_bank`, or others.
    """

    vendor_customer_id: Optional[str] = None
    """An identifier given to this transaction by the bank, often `null`."""

    vendor_id: Optional[str] = None
    """An identifier given to this transaction by the bank."""

    details: Optional[Dict[str, str]] = None
    """
    This field contains additional information that the bank provided about the
    transaction. This is structured data. Some of the data in here might overlap
    with what is in the `vendor_description`. For example, the OBI could be a part
    of the vendor description, and it would also be included in here. The attributes
    that are passed through the details field will vary based on your banking
    partner. Currently, the following keys may be in the details object:
    `originator_name`, `originator_to_beneficiary_information`.
    """

    vendor_description: Optional[str] = None
    """
    The transaction detail text that often appears in on your bank statement and in
    your banking portal.
    """
