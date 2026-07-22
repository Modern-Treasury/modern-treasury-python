# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Optional, Union, Dict

from datetime import datetime

from .._utils import PropertyInfo

from .shared.transaction_direction import TransactionDirection

__all__ = ["ExpectedPaymentListParams"]

class ExpectedPaymentListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str
    """Specify counterparty_id to see expected_payments for a specific account."""

    created_at_lower_bound: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Used to return expected payments created after some datetime"""

    created_at_upper_bound: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Used to return expected payments created before some datetime"""

    direction: TransactionDirection
    """One of credit, debit"""

    external_id: str

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

    type: Literal["ach", "au_becs", "bacs", "book", "card", "chats", "check", "cross_border", "dk_nets", "eft", "gb_fps", "masav", "mx_ccen", "neft", "nics", "nz_becs", "pl_elixir", "rtp", "se_bankgirot", "sepa", "sg_giro", "sic", "stablecoin", "wire", "zengin"]
    """One of: ach, au_becs, bacs, book, check, eft, rtp, sepa, wire"""

    updated_at_lower_bound: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Used to return expected payments updated after some datetime"""

    updated_at_upper_bound: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Used to return expected payments updated before some datetime"""