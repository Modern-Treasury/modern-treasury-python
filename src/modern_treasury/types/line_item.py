# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.accounting import Accounting

__all__ = ["LineItem"]


class LineItem(BaseModel):
    id: str

    accounting: Accounting

    accounting_category_id: Optional[str] = None
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    accounting_ledger_class_id: Optional[str] = None
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    created_at: datetime

    description: Optional[str] = None
    """A free-form description of the line item."""

    itemizable_id: str
    """The ID of the payment order or expected payment."""

    itemizable_type: Literal["ExpectedPayment", "PaymentOrder"]
    """One of `payment_orders` or `expected_payments`."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    object: str

    updated_at: datetime
