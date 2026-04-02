# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["PaymentOrderSubtype"]

PaymentOrderSubtype: TypeAlias = Optional[
    Literal[
        "0C",
        "0N",
        "0S",
        "CCD",
        "CIE",
        "CTX",
        "IAT",
        "PPD",
        "TEL",
        "WEB",
        "au_becs",
        "bacs",
        "base",
        "chats",
        "dk_nets",
        "eft",
        "ethereum",
        "hu_ics",
        "masav",
        "mx_ccen",
        "neft",
        "nics",
        "nz_becs",
        "pl_elixir",
        "polygon",
        "ro_sent",
        "se_bankgirot",
        "sepa",
        "sg_giro",
        "sic",
        "sknbi",
        "solana",
        "zengin",
    ]
]
