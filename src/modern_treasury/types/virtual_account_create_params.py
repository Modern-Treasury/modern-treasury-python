# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from .account_detail_create_param import AccountDetailCreateParam
from .routing_detail_create_param import RoutingDetailCreateParam
from .shared_params.ledger_account_create_request import LedgerAccountCreateRequest

__all__ = ["VirtualAccountCreateParams"]


class VirtualAccountCreateParams(TypedDict, total=False):
    internal_account_id: Required[str]
    """The ID of the internal account that this virtual account is associated with."""

    name: Required[str]
    """The name of the virtual account."""

    account_details: Iterable[AccountDetailCreateParam]
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

    ledger_account: LedgerAccountCreateRequest
    """Specifies a ledger account object that will be created with the virtual account.

    The resulting ledger account is linked to the virtual account for auto-ledgering
    IPDs.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    routing_details: Iterable[RoutingDetailCreateParam]
    """An array of routing detail objects."""
