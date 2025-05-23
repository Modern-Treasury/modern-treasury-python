# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentActionUpdateParams"]


class PaymentActionUpdateParams(TypedDict, total=False):
    status: Required[Literal["pending", "processable", "processing", "sent", "failed", "cancelled"]]
    """Optional.

    Set the status of the payment action to `cancelled` to cancel the payment
    action. This will only work if the payment action is in a `pending` state.
    """
