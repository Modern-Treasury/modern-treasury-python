# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .connection import Connection
from .account_detail import AccountDetail
from .routing_detail import RoutingDetail
from .shared.address import Address
from .shared.currency import Currency
from .shared.transaction_direction import TransactionDirection

__all__ = ["InternalAccount", "AccountCapabilities", "AccountCapability"]


class AccountCapability(BaseModel):
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


AccountCapabilities = AccountCapability
"""This type is deprecated and will be removed in a future release.

Please use AccountCapability instead.
"""


class InternalAccount(BaseModel):
    id: str

    account_capabilities: List[AccountCapability]
    """
    An array of AccountCapability objects that list the originating abilities of the
    internal account and any relevant information for them.
    """

    account_details: List[AccountDetail]
    """An array of account detail objects."""

    account_type: Optional[
        Literal[
            "base_wallet",
            "cash",
            "checking",
            "crypto_wallet",
            "ethereum_wallet",
            "general_ledger",
            "loan",
            "non_resident",
            "other",
            "overdraft",
            "polygon_wallet",
            "savings",
            "solana_wallet",
        ]
    ] = None
    """Can be checking, savings or other."""

    connection: Connection
    """Specifies which financial institution the accounts belong to."""

    counterparty_id: Optional[str] = None
    """The Counterparty associated to this account."""

    created_at: datetime

    currency: Currency
    """The currency of the account."""

    ledger_account_id: Optional[str] = None
    """
    If the internal account links to a ledger account in Modern Treasury, the id of
    the ledger account will be populated here.
    """

    legal_entity_id: Optional[str] = None
    """The Legal Entity associated to this account."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str] = None
    """A nickname for the account."""

    object: str

    parent_account_id: Optional[str] = None
    """The parent InternalAccount of this account."""

    party_address: Optional[Address] = None
    """The address associated with the owner or null."""

    party_name: str
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]] = None
    """Either individual or business."""

    routing_details: List[RoutingDetail]
    """An array of routing detail objects."""

    status: Optional[Literal["active", "closed", "pending_activation", "pending_closure", "suspended"]] = None
    """The internal account status."""

    updated_at: datetime

    vendor_id: Optional[str] = None
    """The vendor ID associated with this account."""
