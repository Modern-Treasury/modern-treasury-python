# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.transaction_direction import TransactionDirection

__all__ = ["AccountCapabilityParam"]


class AccountCapabilityParamTyped(TypedDict, total=False):
    id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    direction: Required[TransactionDirection]
    """One of `debit` or `credit`.

    Indicates the direction of money movement this capability is responsible for.
    """

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    identifier: Required[Optional[str]]
    """
    A unique reference assigned by your bank for tracking and recognizing payment
    files. It is important this is formatted exactly how the bank assigned it.
    """

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    payment_type: Required[
        Literal[
            "ach",
            "au_becs",
            "bacs",
            "base",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "ethereum",
            "gb_fps",
            "hu_ics",
            "interac",
            "masav",
            "mx_ccen",
            "neft",
            "nics",
            "nz_becs",
            "pl_elixir",
            "polygon",
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
            "solana",
            "wire",
            "zengin",
        ]
    ]
    """
    Indicates the the type of payment this capability is responsible for
    originating.
    """

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


AccountCapabilityParam: TypeAlias = Union[AccountCapabilityParamTyped, Dict[str, builtins.object]]
