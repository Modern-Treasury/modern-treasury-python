# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PaymentRequestSimulateParams"]


class PaymentRequestSimulateParams(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    internal_account_id: Required[str]

    requesting_account_number: Required[str]

    requesting_party_name: Required[str]

    requesting_routing_number: Required[str]

    description: Optional[str]
    """An optional description for internal use."""
