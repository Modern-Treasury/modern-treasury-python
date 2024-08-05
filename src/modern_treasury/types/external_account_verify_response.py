# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .external_account import ExternalAccount

__all__ = ["ExternalAccountVerifyResponse", "ExternalAccountVerificationAttempt"]


class ExternalAccountVerificationAttempt(BaseModel):
    id: str

    created_at: datetime

    external_account_id: str
    """The ID of the external account."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    originating_account_id: str
    """The ID of the internal account where the micro-deposits originate from."""

    payment_type: Literal[
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
    """The type of payment that can be made to this account.

    Can be `ach`, `eft`, or `rtp`.
    """

    priority: Optional[Literal["high", "normal"]] = None
    """The priority of the payment. Can be `normal` or `high`."""

    status: Literal["cancelled", "failed", "pending_verification", "verified"]
    """The status of the verification attempt.

    Can be `pending_verification`, `verified`, `failed`, or `cancelled`.
    """

    updated_at: datetime


ExternalAccountVerifyResponse: TypeAlias = Union[ExternalAccount, ExternalAccountVerificationAttempt]
