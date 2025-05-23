# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentActionCreateParams"]


class PaymentActionCreateParams(TypedDict, total=False):
    type: Required[str]
    """Required. The type of the payment action. Determines the action to be taken."""

    actionable_id: str
    """Optional. The ID of the associated actionable object."""

    actionable_type: str
    """Optional.

    The type of the associated actionable object. One of `payment_order`,
    `expected_payment`. Required if `actionable_id` is passed.
    """

    details: object
    """Optional. The specifc details of the payment action based on type."""

    internal_account_id: str
    """Optional.

    The ID of one of your organization's internal accounts. Required if
    `actionable_id` is not passed.
    """
