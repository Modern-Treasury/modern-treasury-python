# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..types import account_detail, routing_detail
from .._models import BaseModel

__all__ = ["AccountsPartyAddress", "AccountsContactDetails", "Accounts", "Counterparty"]


class AccountsPartyAddress(BaseModel):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: str

    id: str

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

    updated_at: str


class AccountsContactDetails(BaseModel):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number"]

    created_at: str

    discarded_at: Optional[str]

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: str


class Accounts(BaseModel):
    account_details: Optional[List[account_detail.AccountDetail]]

    account_type: Optional[Literal["cash", "checking", "loan", "non_resident", "other", "overdraft", "savings"]]
    """Can be `checking`, `savings` or `other`."""

    contact_details: Optional[List[AccountsContactDetails]]

    created_at: Optional[str]

    discarded_at: Optional[str]

    id: Optional[str]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    object: Optional[str]

    party_address: Optional[AccountsPartyAddress]
    """The address associated with the owner or `null`."""

    party_name: Optional[str]
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""

    routing_details: Optional[List[routing_detail.RoutingDetail]]

    updated_at: Optional[str]

    verification_status: Optional[Literal["pending_verification", "unverified", "verified"]]


class Counterparty(BaseModel):
    accounts: List[Accounts]
    """The accounts for this counterparty."""

    created_at: str

    discarded_at: Optional[str]

    email: Optional[str]
    """The counterparty's email."""

    id: str

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
    """A human friendly name for this counterparty."""

    object: str

    send_remittance_advice: bool
    """
    Send an email to the counterparty whenever an associated payment order is sent
    to the bank.
    """

    updated_at: str
