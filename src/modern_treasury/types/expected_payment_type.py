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
