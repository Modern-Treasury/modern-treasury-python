# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BankAddress", "RoutingNumberLookupRequest"]


class BankAddress(BaseModel):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str]

    line2: Optional[str]

    locality: Optional[str]
    """Locality or City."""

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""


class RoutingNumberLookupRequest(BaseModel):
    bank_address: Optional[BankAddress]
    """The address of the bank."""

    bank_name: Optional[str]
    """The name of the bank."""

    routing_number: Optional[str]
    """The routing number of the bank."""

    routing_number_type: Optional[Literal["aba", "au_bsb", "ca_cpa", "gb_sort_code", "swift"]]
    """
    One of `aba`, `au_bsb`, `br_codigo`, `ca_cpa`, `cnaps`, `gb_sort_code`,
    `in_ifsc`, `my_branch_code`, or `swift`. In sandbox mode we currently only
    support `aba` and `swift` with routing numbers '123456789' and 'GRINUST0XXX'
    respectively.
    """

    sanctions: Optional[object]
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
        ]
    ]
    """An array of payment types that are supported for this routing number.

    This can include `ach`, `wire`, `rtp`, `sepa`, `bacs`, `au_becs` currently.
    """
