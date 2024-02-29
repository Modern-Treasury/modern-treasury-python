# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .account_detail import AccountDetail
from .routing_detail import RoutingDetail
from .external_account_type import ExternalAccountType

__all__ = [
    "Counterparty",
    "Accounts",
    "Account",
    "AccountsContactDetails",
    "AccountContactDetail",
    "AccountsPartyAddress",
    "AccountPartyAddress",
]


class AccountContactDetail(BaseModel):
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


AccountsContactDetails = AccountContactDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountContactDetail instead.
"""


class AccountPartyAddress(BaseModel):
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


AccountsPartyAddress = AccountPartyAddress
"""This type is deprecated and will be removed in a future release.

Please use AccountPartyAddress instead.
"""


class Account(BaseModel):
    id: Optional[str] = None

    account_details: Optional[List[AccountDetail]] = None

    account_type: Optional[ExternalAccountType] = None
    """Can be `checking`, `savings` or `other`."""

    contact_details: Optional[List[AccountContactDetail]] = None

    created_at: Optional[datetime] = None

    discarded_at: Optional[datetime] = None

    ledger_account_id: Optional[str] = None
    """
    If the external account links to a ledger account in Modern Treasury, the id of
    the ledger account will be populated here.
    """

    live_mode: Optional[bool] = None
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str] = None
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    object: Optional[str] = None

    party_address: Optional[AccountPartyAddress] = None
    """The address associated with the owner or `null`."""

    party_name: Optional[str] = None
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]] = None
    """Either `individual` or `business`."""

    routing_details: Optional[List[RoutingDetail]] = None

    updated_at: Optional[datetime] = None

    verification_status: Optional[Literal["pending_verification", "unverified", "verified"]] = None


Accounts = Account
"""This type is deprecated and will be removed in a future release.

Please use Account instead.
"""


class Counterparty(BaseModel):
    id: str

    accounts: List[Account]
    """The accounts for this counterparty."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    email: Optional[str] = None
    """The counterparty's email."""

    legal_entity_id: Optional[str] = None
    """The id of the legal entity."""

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
    """A human friendly name for this counterparty."""

    object: str

    send_remittance_advice: bool
    """
    Send an email to the counterparty whenever an associated payment order is sent
    to the bank.
    """

    updated_at: datetime

    verification_status: Literal["denied", "needs_approval", "unverified", "verified"]
    """The verification status of the counterparty."""
