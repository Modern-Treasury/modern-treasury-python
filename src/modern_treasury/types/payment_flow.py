# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentFlow"]


class PaymentFlow(BaseModel):
    id: Optional[str] = None

    amount: Optional[int] = None
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    client_token: Optional[str] = None
    """The client token of the payment flow.

    This token can be used to embed a payment workflow in your client-side
    application.
    """

    counterparty_id: Optional[str] = None
    """The ID of a counterparty associated with the payment.

    As part of the payment workflow an external account will be associated with this
    counterparty.
    """

    created_at: Optional[datetime] = None

    currency: Optional[str] = None
    """The currency of the payment."""

    direction: Optional[Literal["credit", "debit"]] = None
    """Describes the direction money is flowing in the transaction.

    Can only be `debit`. A `debit` pulls money from someone else's account to your
    own.
    """

    due_date: Optional[date] = None
    """The due date for the flow.

    Can only be passed in when `effective_date_selection_enabled` is `true`.
    """

    effective_date_selection_enabled: Optional[bool] = None
    """
    When `true`, your end-user can schedule the payment `effective_date` while
    completing the pre-built UI.
    """

    existing_external_accounts_filter: Optional[Literal["verified"]] = None
    """
    When `verified` and `external_account_collection` is `enabled`, filters the list
    of external accounts your end-user can select to those with a
    `verification_status` of `verified`.
    """

    external_account_collection: Optional[Literal["disabled", "enabled"]] = None
    """
    When `enabled`, your end-user can select from an existing external account when
    completing the flow. When `disabled`, your end-user must add new payment details
    when completing the flow.
    """

    live_mode: Optional[bool] = None
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str] = None

    originating_account_id: Optional[str] = None
    """The ID of one of your organization's internal accounts."""

    payment_order_id: Optional[str] = None
    """If present, the ID of the payment order created using this flow."""

    receiving_account_id: Optional[str] = None
    """If present, the ID of the external account created using this flow."""

    selected_effective_date: Optional[date] = None
    """
    This field is set after your end-user selects a payment date while completing
    the pre-built UI. This field is always `null` unless
    `effective_date_selection_enabled` is `true`.
    """

    status: Optional[Literal["cancelled", "completed", "expired", "pending"]] = None
    """The current status of the payment flow.

    One of `pending`, `completed`, `expired`, or `cancelled`.
    """

    updated_at: Optional[datetime] = None
