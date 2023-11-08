# File generated from our OpenAPI spec by Stainless.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["InvoiceLineItem"]


class InvoiceLineItem(BaseModel):
    id: str

    amount: int
    """
    The total amount for this line item specified in the invoice currency's smallest
    unit.
    """

    created_at: datetime

    description: str
    """An optional free-form description of the line item."""

    direction: str
    """Either `debit` or `credit`.

    `debit` indicates that a client owes the business money and increases the
    invoice's `total_amount` due. `credit` has the opposite intention and effect.
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    name: str
    """The name of the line item, typically a product or SKU name."""

    object: str

    quantity: int
    """The number of units of a product or service that this line item is for.

    Must be a whole number. Defaults to 1 if not provided.
    """

    unit_amount: int
    """
    The cost per unit of the product or service that this line item is for,
    specified in the invoice currency's smallest unit.
    """

    unit_amount_decimal: str
    """
    The cost per unit of the product or service that this line item is for,
    specified in the invoice currency's smallest unit. Accepts decimal strings with
    up to 12 decimals
    """

    updated_at: datetime
