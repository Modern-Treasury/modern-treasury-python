# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared.currency import Currency

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
    """Can be `ach`, `eft`, or `rtp`."""

    currency: Currency
    """Defaults to the currency of the originating account."""

    fallback_type: Literal["ach"]
    """
    A payment type to fallback to if the original type is not valid for the
    receiving account. Currently, this only supports falling back from RTP to ACH
    (payment_type=rtp and fallback_type=ach)
    """

    priority: Literal["high", "normal"]
    """Either `normal` or `high`.

    For ACH payments, `high` represents a same-day ACH transfer. This will apply to
    both `payment_type` and `fallback_type`.
    """
