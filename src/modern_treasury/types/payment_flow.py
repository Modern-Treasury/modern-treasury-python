# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentFlow"]


class PaymentFlow(BaseModel):
    id: Optional[str]

    amount: Optional[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    client_token: Optional[str]
    """The client token of the payment flow.

    This token can be used to embed a payment workflow in your client-side
    application.
    """

    counterparty_id: Optional[str]
    """The ID of a counterparty associated with the payment.

    As part of the payment workflow an external account will be associated with this
    counterparty.
    """

    created_at: Optional[datetime]

    currency: Optional[str]
    """The currency of the payment."""

    direction: Optional[Literal["credit", "debit"]]
    """Describes the direction money is flowing in the transaction.

    Can only be `debit`. A `debit` pulls money from someone else's account to your
    own.
    """

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str]

    originating_account_id: Optional[str]
    """The ID of one of your organization's internal accounts."""

    payment_order_id: Optional[str]
    """If present, the ID of the payment order created using this flow."""

    receiving_account_id: Optional[str]
    """If present, the ID of the external account created using this flow."""

    status: Optional[Literal["cancelled", "completed", "expired", "pending"]]
    """The current status of the payment flow.

    One of `pending`, `completed`, `expired`, or `cancelled`.
    """

    updated_at: Optional[datetime]
