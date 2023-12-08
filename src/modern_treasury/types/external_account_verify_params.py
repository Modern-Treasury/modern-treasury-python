# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .shared import Currency

__all__ = ["ExternalAccountVerifyParams"]


class ExternalAccountVerifyParams(TypedDict, total=False):
    originating_account_id: Required[str]
    """The ID of the internal account where the micro-deposits originate from.

    Both credit and debit capabilities must be enabled.
    """

    payment_type: Required[
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
    """Both ach and eft are supported payment types."""

    currency: Optional[Currency]
    """Defaults to the currency of the originating account."""
