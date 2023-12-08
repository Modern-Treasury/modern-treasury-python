# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoutingNumberLookupRequest", "BankAddress"]


class BankAddress(BaseModel):
    country: Optional[str] = None
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str] = None

    line2: Optional[str] = None

    locality: Optional[str] = None
    """Locality or City."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    region: Optional[str] = None
    """Region or State."""


class RoutingNumberLookupRequest(BaseModel):
    bank_address: Optional[BankAddress] = None
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
        ]
    ] = None
    """An array of payment types that are supported for this routing number.

    This can include `ach`, `wire`, `rtp`, `sepa`, `bacs`, `au_becs` currently.
    """
