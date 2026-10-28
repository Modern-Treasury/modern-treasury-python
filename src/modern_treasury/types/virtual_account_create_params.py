# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .shared_params.address_request import AddressRequest
from .account_detail_create_request_param import AccountDetailCreateRequestParam
from .routing_detail_create_request_param import RoutingDetailCreateRequestParam
from .shared_params.ledger_account_create_request import LedgerAccountCreateRequest

__all__ = ["VirtualAccountCreateParams"]


class VirtualAccountCreateParams(TypedDict, total=False):
    internal_account_id: Required[str]
    """The ID of the internal account that this virtual account is associated with."""

    name: Required[str]
    """The name of the virtual account."""

    account_details: Iterable[AccountDetailCreateRequestParam]
    """An array of account detail objects."""

    counterparty_id: str
    """The ID of the counterparty that the virtual account belongs to."""

    credit_ledger_account_id: str
    """The ID of a credit normal ledger account.

    When money leaves the virtual account, this ledger account will be credited.
    Must be accompanied by a debit_ledger_account_id if present.
    """

    debit_ledger_account_id: str
    """The ID of a debit normal ledger account.

    When money enters the virtual account, this ledger account will be debited. Must
    be accompanied by a credit_ledger_account_id if present.
    """

    description: str
    """An optional description for internal use."""

    external_id: Optional[str]
    """A user-defined identifier for the virtual account."""

    ledger_account: LedgerAccountCreateRequest
    """Specifies a ledger account object that will be created with the virtual account.

    The resulting ledger account is linked to the virtual account for auto-ledgering
    IPDs.
    """

    ledger_account_id: str
    """The ledger account that you'd like to link to the virtual account."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    party_address: AddressRequest
    """The address of the owner of the virtual account.

    When absent, the internal account's party address is used.
    """

    routing_details: Iterable[RoutingDetailCreateRequestParam]
    """An array of routing detail objects."""

    virtual_account_setting_id: str
    """The ID of the virtual account setting used to allocate this virtual account."""
