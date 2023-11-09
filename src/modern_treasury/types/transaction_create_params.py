# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionCreateParams"]


class TransactionCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: Required[Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]]
    """The date on which the transaction occurred."""

    direction: Required[str]
    """Either `credit` or `debit`."""

    internal_account_id: Required[str]
    """The ID of the relevant Internal Account."""

    vendor_code: Required[str]
    """When applicable, the bank-given code that determines the transaction's category.

    For most banks this is the BAI2/BTRS transaction code.
    """

    vendor_code_type: Required[str]
    """The type of `vendor_code` being reported.

    Can be one of `bai2`, `bankprov`, `bnk_dev`, `cleartouch`, `currencycloud`,
    `cross_river`, `dc_bank`, `dwolla`, `evolve`, `goldman_sachs`, `iso20022`,
    `jpmc`, `mx`, `signet`, `silvergate`, `swift`, `us_bank`, or others.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    posted: bool
    """This field will be `true` if the transaction has posted to the account."""

    vendor_description: Optional[str]
    """
    The transaction detail text that often appears in on your bank statement and in
    your banking portal.
    """
