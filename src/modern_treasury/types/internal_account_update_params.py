# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .shared_params.address_request import AddressRequest

__all__ = ["InternalAccountUpdateParams"]


class InternalAccountUpdateParams(TypedDict, total=False):
    allowed_ach_debit_company_ids: Optional[SequenceNotStr[str]]
    """The ACH Company IDs allowed to debit this account.

    `null` allows every company. An empty array allows none. Debits from any other
    company are returned with code R10. Only applicable to debitable accounts under
    a Modern Treasury PSP connection.
    """

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

    party_type: Optional[Literal["individual", "business"]]
    """Either individual or business.

    Inherits from associated LegalEntity legal_entity_type, if one exists.
    """

    status: Literal["pending_closure"]
    """Requests closure of the internal account.

    The resulting status may be `closed` for vendors that close synchronously.
    """
