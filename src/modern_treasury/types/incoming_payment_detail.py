# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .shared import Currency, TransactionDirection
from .._models import BaseModel
from .virtual_account import VirtualAccount

__all__ = ["IncomingPaymentDetail"]


class IncomingPaymentDetail(BaseModel):
    id: str

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: date
    """The date on which the corresponding transaction will occur."""

    created_at: datetime

    currency: Optional[Currency] = None
    """The currency of the incoming payment detail."""

    data: Dict[str, object]
    """The raw data from the payment pre-notification file that we get from the bank."""

    direction: TransactionDirection
    """One of `credit` or `debit`."""

    internal_account_id: str
    """The ID of the Internal Account for the incoming payment detail.

    This is always present.
    """

    ledger_transaction_id: Optional[str] = None
    """
    The ID of the ledger transaction linked to the incoming payment detail or
    `null`.
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

    originating_account_number_safe: Optional[str] = None
    """
    The last 4 digits of the originating account_number for the incoming payment
    detail.
    """

    originating_account_number_type: Optional[
        Literal["clabe", "hk_number", "iban", "other", "pan", "wallet_address"]
    ] = None
    """The type of the originating account number for the incoming payment detail."""

    originating_routing_number: Optional[str] = None
    """The routing number of the originating account for the incoming payment detail."""

    originating_routing_number_type: Optional[
        Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "in_ifsc",
            "jp_zengin_code",
            "mx_bank_identifier",
            "my_branch_code",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ]
    ] = None
    """The type of the originating routing number for the incoming payment detail."""

    status: Literal["completed", "pending", "returned"]
    """The current status of the incoming payment order.

    One of `pending`, `completed`, or `returned`.
    """

    transaction_id: Optional[str] = None
    """The ID of the reconciled Transaction or `null`."""

    transaction_line_item_id: Optional[str] = None
    """The ID of the reconciled Transaction Line Item or `null`."""

    type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"]
    """
    One of: `ach`, `book`, `check`, `eft`, `interac`, `rtp`, `sepa`, `signet`, or
    `wire`.
    """

    updated_at: datetime

    vendor_id: Optional[str] = None
    """The identifier of the vendor bank."""

    virtual_account: Optional[VirtualAccount] = None
    """
    If the incoming payment detail is in a virtual account, the serialized virtual
    account object.
    """

    virtual_account_id: Optional[str] = None
    """
    If the incoming payment detail is in a virtual account, the ID of the Virtual
    Account.
    """

    originating_account_number: Optional[str] = None
    """The account number of the originating account for the incoming payment detail."""
