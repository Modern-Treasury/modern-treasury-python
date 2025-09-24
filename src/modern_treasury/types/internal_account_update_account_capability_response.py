# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.transaction_direction import TransactionDirection

__all__ = ["InternalAccountUpdateAccountCapabilityResponse"]


class InternalAccountUpdateAccountCapabilityResponse(BaseModel):
    id: str

    created_at: datetime

    direction: TransactionDirection
    """One of `debit` or `credit`.

    Indicates the direction of money movement this capability is responsible for.
    """

    discarded_at: Optional[datetime] = None

    identifier: Optional[str] = None
    """
    A unique reference assigned by your bank for tracking and recognizing payment
    files. It is important this is formatted exactly how the bank assigned it.
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    payment_type: Literal[
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
    """
    Indicates the the type of payment this capability is responsible for
    originating.
    """

    updated_at: datetime

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]
