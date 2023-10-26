# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

__all__ = ["ExpectedPaymentType"]

ExpectedPaymentType = Optional[
    Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "chats",
        "check",
        "cross_border",
        "eft",
        "interac",
        "masav",
        "neft",
        "nics",
        "nz_becs",
        "provxchange",
        "rtp",
        "se_bankgirot",
        "sen",
        "sepa",
        "sg_giro",
        "sic",
        "signet",
        "wire",
        "zengin",
    ]
]
