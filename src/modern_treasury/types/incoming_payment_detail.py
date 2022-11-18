# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..types import shared, account_detail, routing_detail
from .._models import BaseModel

__all__ = ["VirtualAccount", "IncomingPaymentDetail"]


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


class IncomingPaymentDetail(BaseModel):
    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: str
    """The date on which the corresponding transaction will occur."""

    created_at: str

    currency: Optional[shared.Currency]
    """The currency of the incoming payment detail."""

    data: object
    """The raw data from the payment pre-notification file that we get from the bank."""

    direction: Literal["credit", "debit"]
    """One of `credit` or `debit`."""

    id: str

    internal_account_id: str
    """The ID of the Internal Account for the incoming payment detail.

    This is always present.
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

    object: str

    status: Literal["completed", "pending", "returned"]
    """The current status of the incoming payment order.

    One of `pending`, `completed`, or `returned`.
    """

    transaction_id: Optional[str]
    """The ID of the reconciled Transaction or `null`."""

    transaction_line_item_id: Optional[str]
    """The ID of the reconciled Transaction Line Item or `null`."""

    type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"]
    """One of: `ach`, `wire`, `check`, `rtp`, `sepa`, `signet`."""

    updated_at: str

    vendor_id: Optional[str]
    """The identifier of the vendor bank."""

    virtual_account: Optional[VirtualAccount]
    """
    If the incoming payment detail is in a virtual account, the serialized virtual
    account object.
    """

    virtual_account_id: Optional[str]
    """
    If the incoming payment detail is in a virtual account, the ID of the Virtual
    Account.
    """
