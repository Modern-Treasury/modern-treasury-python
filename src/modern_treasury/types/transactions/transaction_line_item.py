# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransactionLineItem"]


class TransactionLineItem(BaseModel):
    id: str

    amount: int
    """If a matching object exists in Modern Treasury, `amount` will be populated.

    Value in specified currency's smallest unit (taken from parent Transaction).
    """

    counterparty_id: Optional[str] = None
    """The ID for the counterparty for this transaction line item."""

    created_at: datetime

    description: str
    """
    If no matching object is found, `description` will be a free-form text field
    describing the line item. This field may contain personally identifiable
    information (PII) and is not included in API responses by default. Learn more
    about changing your settings at
    https://docs.moderntreasury.com/reference/personally-identifiable-information.
    """

    discarded_at: Optional[datetime] = None

    expected_payment_id: Optional[str] = None
    """The ID of the reconciled Expected Payment, otherwise `null`."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment, or false
    if it exists in the test environment.
    """

    object: str

    reconcilable: bool
    """
    Describes whether this line item should be counted towards the corresponding
    transaction’s reconciliation.
    """

    transactable_id: Optional[str] = None
    """
    If a matching object exists in Modern Treasury, the ID will be populated here,
    otherwise `null`.
    """

    transactable_type: Optional[
        Literal["incoming_payment_detail", "paper_item", "payment_order", "payment_order_attempt", "return", "reversal"]
    ] = None
    """
    If a matching object exists in Modern Treasury, the type will be populated here,
    otherwise `null`.
    """

    transaction_id: str
    """The ID of the parent transaction."""

    type: Literal["originating", "receiving"]
    """
    Indicates whether the line item is `originating` or `receiving` (see
    https://www.moderntreasury.com/journal/beginners-guide-to-ach for more).
    """

    updated_at: datetime
