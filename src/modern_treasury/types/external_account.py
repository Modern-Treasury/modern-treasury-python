# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .account_detail import AccountDetail
from .routing_detail import RoutingDetail
from .external_account_type import ExternalAccountType

__all__ = ["ExternalAccount", "ContactDetails", "ContactDetail", "PartyAddress"]


class ContactDetail(BaseModel):
    id: str

    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]

    created_at: datetime

    discarded_at: Optional[datetime] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime


ContactDetails = ContactDetail
"""This type is deprecated and will be removed in a future release.

Please use ContactDetail instead.
"""


class PartyAddress(BaseModel):
    id: str

    country: Optional[str] = None
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: datetime

    line1: Optional[str] = None

    line2: Optional[str] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Optional[str] = None
    """Locality or City."""

    object: str

    postal_code: Optional[str] = None
    """The postal code of the address."""

    region: Optional[str] = None
    """Region or State."""

    updated_at: datetime


class ExternalAccount(BaseModel):
    id: str

    account_details: List[AccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: List[ContactDetail]

    counterparty_id: Optional[str] = None

    created_at: datetime

    discarded_at: Optional[datetime] = None

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

    party_address: Optional[PartyAddress] = None
    """The address associated with the owner or `null`."""

    party_name: str
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]] = None
    """Either `individual` or `business`."""

    routing_details: List[RoutingDetail]

    updated_at: datetime

    verification_status: Literal["pending_verification", "unverified", "verified"]
