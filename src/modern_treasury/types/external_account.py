# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import account_detail, routing_detail, external_account_type
from .._models import BaseModel

__all__ = ["ExternalAccount", "ContactDetails", "ContactDetail", "PartyAddress"]


class ContactDetail(BaseModel):
    id: str

    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]

    created_at: datetime

    discarded_at: Optional[datetime]

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


class ExternalAccount(BaseModel):
    id: str

    account_details: List[account_detail.AccountDetail]

    account_type: external_account_type.ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: List[ContactDetail]

    counterparty_id: Optional[str]

    created_at: datetime

    discarded_at: Optional[datetime]

    ledger_account_id: Optional[str]
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

    updated_at: datetime

    verification_status: Literal["pending_verification", "unverified", "verified"]
