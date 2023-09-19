# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RoutingDetailCreateParams"]


class RoutingDetailCreateParams(TypedDict, total=False):
    accounts_type: Required[Literal["external_accounts"]]

    routing_number: Required[str]
    """The routing number of the bank."""

    routing_number_type: Required[
        Literal[
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
    ]
    """One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`."""

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
