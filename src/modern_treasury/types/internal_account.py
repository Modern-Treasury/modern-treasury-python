# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .connection import Connection
from .account_detail import AccountDetail
from .routing_detail import RoutingDetail
from .shared.address import Address
from .shared.currency import Currency
from .account_capability import AccountCapability

__all__ = ["InternalAccount"]


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

    contra_ledger_account_id: Optional[str] = None
    """
    If the internal account links to a contra ledger account in Modern Treasury, the
    id of the contra ledger account will be populated here.
    """

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
