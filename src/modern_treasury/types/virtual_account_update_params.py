# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .shared_params.address_request import AddressRequest

__all__ = ["VirtualAccountUpdateParams"]


class VirtualAccountUpdateParams(TypedDict, total=False):
    counterparty_id: str

    ledger_account_id: str
    """The ledger account that you'd like to link to the virtual account."""

    metadata: Dict[str, str]

    name: Optional[str]

    party_address: AddressRequest
    """The address of the owner of the virtual account.

    Omit to leave it unchanged; pass all fields blank to clear it, after which the
    internal account's party address is used.
    """
