# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["LineItemUpdateParams"]


class LineItemUpdateParams(TypedDict, total=False):
    invoice_id: Required[str]

    description: str
    """An optional free-form description of the line item."""

    direction: str
    """Either `debit` or `credit`.

    `debit` indicates that a client owes the business money and increases the
    invoice's `total_amount` due. `credit` has the opposite intention and effect.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """The name of the line item, typically a product or SKU name."""

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
