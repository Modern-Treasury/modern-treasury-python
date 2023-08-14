# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .shared import Currency
from .._models import BaseModel
from .connection import Connection
from .account_detail import AccountDetail
from .routing_detail import RoutingDetail

__all__ = ["InternalAccount", "PartyAddress"]


class PartyAddress(BaseModel):
    id: str

    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: datetime

    line1: Optional[str]

    line2: Optional[str]

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[str]
    """Locality or City."""

    object: str

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""

    updated_at: datetime


class InternalAccount(BaseModel):
    id: str

    account_details: List[AccountDetail]
    """An array of account detail objects."""

    account_type: Optional[Literal["cash", "checking", "loan", "non_resident", "other", "overdraft", "savings"]]
    """Can be checking, savings or other."""

    connection: Connection
    """Specifies which financial institution the accounts belong to."""

    counterparty_id: Optional[str]
    """The Counterparty associated to this account."""

    created_at: datetime

    currency: Optional[Currency]
    """The currency of the account."""

    ledger_account_id: Optional[str]
    """
    If the internal account links to a ledger account in Modern Treasury, the id of
    the ledger account will be populated here.
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the account."""

    object: str

    parent_account_id: Optional[str]
    """The parent InternalAccount of this account."""

    party_address: Optional[PartyAddress]
    """The address associated with the owner or null."""

    party_name: str
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]]
    """Either individual or business."""

    routing_details: List[RoutingDetail]
    """An array of routing detail objects."""

    updated_at: datetime
