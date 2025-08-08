# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .ledger_entry_create_request import LedgerEntryCreateRequest

__all__ = ["LedgerTransactionCreateRequest"]


class LedgerTransactionCreateRequest(BaseModel):
    ledger_entries: List[LedgerEntryCreateRequest]
    """An array of ledger entry objects."""

    description: Optional[str] = None
    """An optional description for internal use."""

    effective_at: Optional[datetime] = None
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    effective_date: Optional[date] = None
    """
    The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
    purposes.
    """

    external_id: Optional[str] = None
    """A unique string to represent the ledger transaction.

    Only one pending or posted ledger transaction may have this ID in the ledger.
    """

    ledgerable_id: Optional[str] = None
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the id will be populated here, otherwise null.
    """

    ledgerable_type: Optional[
        Literal["expected_payment", "incoming_payment_detail", "payment_order", "return", "reversal"]
    ] = None
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the type will be populated here, otherwise null. This can be one of
    payment_order, incoming_payment_detail, expected_payment, return, or reversal.
    """

    metadata: Optional[Dict[str, str]] = None
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Optional[Literal["archived", "pending", "posted"]] = None
    """To post a ledger transaction at creation, use `posted`."""
