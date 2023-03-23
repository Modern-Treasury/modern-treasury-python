# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentFlowCreateParams"]


class PaymentFlowCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Required.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000. Can be any integer up to 36 digits.
    """

    counterparty_id: Required[str]
    """Required.

    The ID of a counterparty associated with the payment. As part of the payment
    workflow an external account will be associated with this model.
    """

    currency: Required[str]
    """Required. The currency of the payment."""

    direction: Required[Literal["credit", "debit"]]
    """Required.

    Describes the direction money is flowing in the transaction. Can only be
    `debit`. A `debit` pulls money from someone else's account to your own.
    """

    originating_account_id: Required[str]
    """Required. The ID of one of your organization's internal accounts."""
