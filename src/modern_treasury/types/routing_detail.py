# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.address import Address

__all__ = ["RoutingDetail"]


class RoutingDetail(BaseModel):
    id: str

    bank_address: Optional[Address] = None

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
            "base",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "ethereum",
            "hu_ics",
            "interac",
            "masav",
            "mx_ccen",
            "neft",
            "nics",
            "nz_becs",
            "pl_elixir",
            "polygon",
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
            "solana",
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
        "il_bank_code",
        "in_ifsc",
        "jp_zengin_code",
        "mx_bank_identifier",
        "my_branch_code",
        "nz_national_clearing_code",
        "pl_national_clearing_code",
        "se_bankgiro_clearing_code",
        "sg_interbank_clearing_code",
        "swift",
        "za_national_clearing_code",
    ]
    """The type of routing number.

    See https://docs.moderntreasury.com/platform/reference/routing-detail-object for
    more details.
    """

    updated_at: datetime
