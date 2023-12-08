# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .shared import TransactionDirection
from .._utils import PropertyInfo

__all__ = ["ExpectedPaymentListParams"]


class ExpectedPaymentListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str
    """Specify counterparty_id to see expected_payments for a specific account."""

    created_at_lower_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Used to return expected payments created after some datetime"""

    created_at_upper_bound: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Used to return expected payments created before some datetime"""

    direction: TransactionDirection
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

    status: Literal["archived", "partially_reconciled", "reconciled", "unreconciled"]
    """One of unreconciled, reconciled, or archived."""

    type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "chats",
        "check",
        "cross_border",
        "dk_nets",
        "eft",
        "hu_ics",
        "interac",
        "masav",
        "mx_ccen",
        "neft",
        "nics",
        "nz_becs",
        "pl_elixir",
        "provxchange",
        "ro_sent",
        "rtp",
        "se_bankgirot",
        "sen",
        "sepa",
        "sg_giro",
        "sic",
        "signet",
        "sknbi",
        "wire",
        "zengin",
    ]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp,sen,
    sepa, signet, wire
    """
