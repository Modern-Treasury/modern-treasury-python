# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .account_detail import AccountDetail
from .routing_detail import RoutingDetail

__all__ = ["VirtualAccount"]


class VirtualAccount(BaseModel):
    id: str

    account_details: List[AccountDetail]
    """An array of account detail objects."""

    counterparty_id: Optional[str] = None
    """The ID of a counterparty that the virtual account belongs to. Optional."""

    created_at: datetime

    credit_ledger_account_id: Optional[str] = None
    """The ID of a credit normal ledger account.

    When money enters the virtual account, this ledger account will be credited.
    Must be accompanied by a debit_ledger_account_id if present.
    """

    debit_ledger_account_id: Optional[str] = None
    """The ID of a debit normal ledger account.

    When money enters the virtual account, this ledger account will be debited. Must
    be accompanied by a credit_ledger_account_id if present.
    """

    description: Optional[str] = None
    """An optional free-form description for internal use."""

    discarded_at: Optional[datetime] = None

    internal_account_id: str
    """The ID of the internal account that the virtual account is in."""

    ledger_account_id: Optional[str] = None
    """
    If the virtual account links to a ledger account in Modern Treasury, the id of
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

    name: str
    """The name of the virtual account."""

    object: str

    routing_details: List[RoutingDetail]
    """An array of routing detail objects.

    These will be the routing details of the internal account.
    """

    updated_at: datetime
