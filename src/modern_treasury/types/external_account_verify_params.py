# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

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
    """Both ach and eft are supported payment types."""

    currency: shared_params.Currency
    """Defaults to the currency of the originating account."""
