# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ExpectedPaymentListParams"]


class ExpectedPaymentListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str
    """Specify counterparty_id to see expected_payments for a specific account."""

    created_at_lower_bound: str
    """Used to return expected payments created after some datetime"""

    created_at_upper_bound: str
    """Used to return expected payments created before some datetime"""

    direction: Literal["credit", "debit"]
    """One of credit, debit"""

    internal_account_id: str
    """Specify internal_account_id to see expected_payments for a specific account."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    per_page: int

    status: Literal["archived", "reconciled", "unreconciled"]
    """One of unreconciled, reconciled, or archived."""

    type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "check",
        "cross_border",
        "eft",
        "interac",
        "provxchange",
        "rtp",
        "sen",
        "sepa",
        "signet",
        "wire",
    ]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp,sen,
    sepa, signet, wire
    """
