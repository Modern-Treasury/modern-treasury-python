# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

__all__ = ["PaymentFlowUpdateParams"]

class PaymentFlowUpdateParams(TypedDict, total=False):
    status: Required[Literal["cancelled"]]
    """Required.

    The updated status of the payment flow. Can only be used to mark a flow as
    `cancelled`.
    """