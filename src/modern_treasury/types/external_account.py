# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..types import account_detail, routing_detail
from .._models import BaseModel

__all__ = ["PartyAddress", "ContactDetails", "ExternalAccount"]


class PartyAddress(BaseModel):
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


class ContactDetails(BaseModel):
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


class ExternalAccount(BaseModel):
    account_details: List[account_detail.AccountDetail]

    account_type: Literal["cash", "checking", "loan", "non_resident", "other", "overdraft", "savings"]
    """Can be `checking`, `savings` or `other`."""

    contact_details: List[ContactDetails]

    counterparty_id: Optional[str]

    created_at: str

    discarded_at: Optional[str]

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
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    object: str

    party_address: Optional[PartyAddress]
    """The address associated with the owner or `null`."""

    party_name: str
    """The legal name of the entity which owns the account."""

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""

    routing_details: List[routing_detail.RoutingDetail]

    updated_at: str

    verification_status: Literal["pending_verification", "unverified", "verified"]
