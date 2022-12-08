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
        "provxchange",
        "rtp",
        "sen",
        "sepa",
        "signet",
        "wire",
    ]
]
