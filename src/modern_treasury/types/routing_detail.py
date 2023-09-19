# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoutingDetail", "BankAddress"]


class BankAddress(BaseModel):
    id: str

    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: datetime

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

    updated_at: datetime


class RoutingDetail(BaseModel):
    id: str

    bank_address: Optional[BankAddress]

    bank_name: str
    """The name of the bank."""

    created_at: datetime

    discarded_at: Optional[datetime]

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
            "cross_border",
            "eft",
            "interac",
            "masav",
            "neft",
            "nics",
            "provxchange",
            "rtp",
            "se_bankgirot",
            "sen",
            "sepa",
            "sic",
            "signet",
            "wire",
            "zengin",
        ]
    ]
    """
    If the routing detail is to be used for a specific payment type this field will
    be populated, otherwise null.
    """

    routing_number: str
    """The routing number of the bank."""

    routing_number_type: Literal[
        "aba",
        "au_bsb",
        "br_codigo",
        "ca_cpa",
        "chips",
        "cnaps",
        "gb_sort_code",
        "in_ifsc",
        "jp_zengin_code",
        "my_branch_code",
        "se_bankgiro_clearing_code",
        "swift",
    ]
    """One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`."""

    updated_at: datetime
