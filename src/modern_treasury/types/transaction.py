# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = ["Transaction"]


class Transaction(BaseModel):
    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: Optional[str]
    """The date on which the transaction occurred."""

    as_of_time: Optional[str]
    """The time on which the transaction occurred.

    Depending on the granularity of the timestamp information received from the
    bank, it may be `null`.
    """

    created_at: str

    currency: Optional[shared.Currency]
    """Currency that this transaction is denominated in."""

    details: Dict[str, str]
    """
    This field contains additional information that the bank provided about the
    transaction. This is structured data. Some of the data in here might overlap
    with what is in the `vendor_description`. For example, the OBI could be a part
    of the vendor description, and it would also be included in here. The attributes
    that are passed through the details field will vary based on your banking
    partner. Currently, the following keys may be in the details object:
    `originator_name`, `originator_to_beneficiary_information`.
    """

    direction: str
    """Either `credit` or `debit`."""

    discarded_at: Optional[str]

    id: str

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
        "check",
        "cross_border",
        "eft",
        "interac",
        "provxchange",
        "rtp",
        "sen",
        "sepa",
        "signet",
        "wire",
    ]
    """The type of the transaction.

    Can be one of `ach`, `wire`, `check`, `rtp`, `book`, or `sen`.
    """

    updated_at: str

    vendor_code: Optional[str]
    """When applicable, the bank-given code that determines the transaction's category.

    For most banks this is the BAI2/BTRS transaction code.
    """

    vendor_code_type: Optional[
        Literal[
            "bai2",
            "bankprov",
            "bnk_dev",
            "cleartouch",
            "cross_river",
            "currencycloud",
            "dc_bank",
            "dwolla",
            "goldman_sachs",
            "iso20022",
            "jpmc",
            "mx",
            "signet",
            "silvergate",
            "swift",
            "us_bank",
        ]
    ]
    """The type of vendor_code being reported.

    Can be one of `bai2`, `swift`, `cleartouch`, or `silvergate`.
    """

    vendor_customer_id: Optional[str]
    """An identifier given to this transaction by the bank, often `null`."""

    vendor_description: Optional[str]
    """
    The transaction detail text that often appears in on your bank statement and in
    your banking portal.
    """

    vendor_id: Optional[str]
    """An identifier given to this transaction by the bank."""
