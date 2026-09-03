# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .shared_params.address_request import AddressRequest

__all__ = ["InternalAccountUpdateParams"]


class InternalAccountUpdateParams(TypedDict, total=False):
    contra_ledger_account_id: str
    """The Contra Ledger Account associated to this account."""

    counterparty_id: str
    """The Counterparty associated to this account."""

    external_id: Optional[str]
    """An optional user-defined 180 character unique identifier."""

    ledger_account_id: str
    """The Ledger Account associated to this account."""

    metadata: Dict[str, str]
    """Additional data in the form of key-value pairs.

    Pairs can be removed by passing an empty string or `null` as the value.
    """

    name: str
    """The nickname for the internal account."""

    parent_account_id: str
    """The parent internal account for this account."""

    party_address: AddressRequest
    """The address associated with the owner of the internal account.

    Updating this value does not guarantee that the new address matches the address
    on record with the account's bank; you are responsible for verifying that the
    address is accurate.
    """

    status: Literal["pending_closure"]
    """Requests closure of the internal account.

    The resulting status may be `closed` for vendors that close synchronously.
    """
