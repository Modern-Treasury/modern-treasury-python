# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.address_request import AddressRequest

__all__ = ["RoutingNumberLookupRequest"]


class RoutingNumberLookupRequest(BaseModel):
    bank_address: Optional[AddressRequest] = None
    """The address of the bank."""

    bank_name: Optional[str] = None
    """The name of the bank."""

    routing_number: Optional[str] = None
    """The routing number of the bank."""

    routing_number_type: Optional[
        Literal[
            "aba",
            "au_bsb",
            "ca_cpa",
            "gb_sort_code",
            "in_ifsc",
            "nz_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
            "za_national_clearing_code",
        ]
    ] = None
    """The type of routing number.

    See https://docs.moderntreasury.com/platform/reference/routing-detail-object for
    more details. In sandbox mode we currently only support `aba` and `swift` with
    routing numbers '123456789' and 'GRINUST0XXX' respectively.
    """

    sanctions: Optional[Dict[str, object]] = None
    """
    An object containing key-value pairs, each with a sanctions list as the key and
    a boolean value representing whether the bank is on that particular sanctions
    list. Currently, this includes eu_con, uk_hmt, us_ofac, and un sanctions lists.
    """

    supported_payment_types: Optional[
        List[
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
        ]
    ] = None
    """An array of payment types that are supported for this routing number.

    This can include `ach`, `wire`, `rtp`, `sepa`, `bacs`, `au_becs`, and 'fednow'
    currently.
    """
