# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoutingDetail", "BankAddress"]


class BankAddress(BaseModel):
    id: str

    country: Optional[str] = None
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: datetime

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

    region: Optional[str] = None
    """Region or State."""

    updated_at: datetime


class RoutingDetail(BaseModel):
    id: str

    bank_address: Optional[BankAddress] = None

    bank_name: str
    """The name of the bank."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

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
        ]
    ] = None
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
        "dk_interbank_clearing_code",
        "gb_sort_code",
        "hk_interbank_clearing_code",
        "hu_interbank_clearing_code",
        "id_sknbi_code",
        "in_ifsc",
        "jp_zengin_code",
        "mx_bank_identifier",
        "my_branch_code",
        "nz_national_clearing_code",
        "pl_national_clearing_code",
        "se_bankgiro_clearing_code",
        "swift",
    ]
    """The type of routing number.

    See https://docs.moderntreasury.com/platform/reference/routing-detail-object for
    more details.
    """

    updated_at: datetime
