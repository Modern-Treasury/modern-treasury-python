# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional

from ..types import account_detail, routing_detail
from .._models import BaseModel

__all__ = ["VirtualAccount"]


class VirtualAccount(BaseModel):
    account_details: List[account_detail.AccountDetail]
    """An array of account detail objects."""

    counterparty_id: Optional[str]
    """The ID of a counterparty that the virtual account belongs to. Optional."""

    created_at: str

    credit_ledger_account_id: Optional[str]
    """The ID of a credit normal ledger account.

    When money enters the virtual account, this ledger account will be credited.
    Must be accompanied by a debit_ledger_account_id if present.
    """

    debit_ledger_account_id: Optional[str]
    """The ID of a debit normal ledger account.

    When money enters the virtual account, this ledger account will be debited. Must
    be accompanied by a credit_ledger_account_id if present.
    """

    description: Optional[str]
    """An optional free-form description for internal use."""

    discarded_at: Optional[str]

    id: str

    internal_account_id: str
    """The ID of the internal account that the virtual account is in."""

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

    routing_details: List[routing_detail.RoutingDetail]
    """An array of routing detail objects.

    These will be the routing details of the internal account.
    """

    updated_at: str
