# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReturnCreateParams"]


class ReturnCreateParams(TypedDict, total=False):
    returnable_id: Required[Optional[str]]
    """The ID of the object being returned or `null`."""

    returnable_type: Required[Literal["incoming_payment_detail"]]
    """The type of object being returned.

    Currently, this may only be incoming_payment_detail.
    """

    additional_information: Optional[str]
    """Some returns may include additional information from the bank.

    In these cases, this string will be present.
    """

    code: Optional[
        Literal[
            "901",
            "902",
            "903",
            "904",
            "905",
            "907",
            "908",
            "909",
            "910",
            "911",
            "912",
            "914",
            "C01",
            "C02",
            "C03",
            "C05",
            "C06",
            "C07",
            "C08",
            "C09",
            "C13",
            "C14",
            "R01",
            "R02",
            "R03",
            "R04",
            "R05",
            "R06",
            "R07",
            "R08",
            "R09",
            "R10",
            "R11",
            "R12",
            "R14",
            "R15",
            "R16",
            "R17",
            "R20",
            "R21",
            "R22",
            "R23",
            "R24",
            "R29",
            "R31",
            "R33",
            "R37",
            "R38",
            "R39",
            "R51",
            "R52",
            "R53",
            "currencycloud",
        ]
    ]
    """The return code. For ACH returns, this is the required ACH return code."""

    date_of_death: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    If the return code is `R14` or `R15` this is the date the deceased counterparty
    passed away.
    """

    reason: Optional[str]
    """An optional description of the reason for the return.

    This is for internal usage and will not be transmitted to the bank.”
    """
