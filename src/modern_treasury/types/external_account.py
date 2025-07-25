# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .account_detail import AccountDetail
from .routing_detail import RoutingDetail
from .shared.address import Address
from .external_account_type import ExternalAccountType
from .shared.contact_detail import ContactDetail

__all__ = ["ExternalAccount"]


class ExternalAccount(BaseModel):
    id: str

    account_details: List[AccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: List[ContactDetail]

    counterparty_id: Optional[str] = None

    created_at: datetime

    discarded_at: Optional[datetime] = None

    external_id: Optional[str] = None
    """An optional user-defined 180 character unique identifier."""

    ledger_account_id: Optional[str] = None
    """
    If the external account links to a ledger account in Modern Treasury, the id of
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

    name: Optional[str] = None
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    object: str

    party_address: Optional[Address] = None
    """The address associated with the owner or `null`."""

    party_name: str
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]] = None
    """Either `individual` or `business`."""

    routing_details: List[RoutingDetail]

    updated_at: datetime

    verification_source: Optional[Literal["ach_prenote", "microdeposits", "plaid"]] = None

    verification_status: Literal["pending_verification", "unverified", "verified"]
