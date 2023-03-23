# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PaymentFlowListParams"]


class PaymentFlowListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    client_token: str

    counterparty_id: str

    originating_account_id: str

    payment_order_id: str

    per_page: int

    receiving_account_id: str

    status: str
