# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .external_account_type import ExternalAccountType
from .shared_params.address_request import AddressRequest

__all__ = ["ExternalAccountUpdateParams"]


class ExternalAccountUpdateParams(TypedDict, total=False):
    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    counterparty_id: Optional[str]

    metadata: Dict[str, str]
    """Additional data in the form of key-value pairs.

    Pairs can be removed by passing an empty string or `null` as the value.
    """

    name: Optional[str]
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    party_address: AddressRequest

    party_name: str
    """
    If this value isn't provided, it will be inherited from the counterparty's name.
    """

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""
