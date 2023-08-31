# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LedgerTransactionCreateReversalParams"]


class LedgerTransactionCreateReversalParams(TypedDict, total=False):
    description: str
    """An optional free-form description for the reversal ledger transaction.

    Maximum of 1000 characters allowed.
    """

    effective_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    The timestamp (ISO8601 format) at which the reversal ledger transaction happened
    for reporting purposes. It defaults to the `effective_at` of the original ledger
    transaction if not provided.
    """

    external_id: str
    """Must be unique within the ledger."""

    ledgerable_id: str
    """
    Specify this if you'd like to link the reversal ledger transaction to a Payment
    object like Return or Reversal.
    """

    ledgerable_type: Literal[
        "counterparty",
        "expected_payment",
        "incoming_payment_detail",
        "internal_account",
        "line_item",
        "paper_item",
        "payment_order",
        "payment_order_attempt",
        "return",
        "reversal",
    ]
    """
    Specify this if you'd like to link the reversal ledger transaction to a Payment
    object like Return or Reversal.
    """

    metadata: Dict[str, str]
    """
    Additional data to be added to the reversal ledger transaction as key-value
    pairs. Both the key and value must be strings.
    """

    status: Literal["archived", "pending", "posted"]
    """Status of the reversal ledger transaction.

    It defaults to `posted` if not provided.
    """
