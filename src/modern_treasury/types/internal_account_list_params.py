# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .shared.currency import Currency
from .shared.transaction_direction import TransactionDirection

__all__ = ["InternalAccountListParams"]


class InternalAccountListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str
    """Only return internal accounts associated with this counterparty."""

    currency: Currency
    """Only return internal accounts with this currency."""

    legal_entity_id: str
    """Only return internal accounts associated with this legal entity."""

    metadata: Dict[str, str]
    """
    For example, if you want to query for records with metadata key `Type` and value
    `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
    parameters.
    """

    payment_direction: TransactionDirection
    """Only return internal accounts that can originate payments with this direction."""

    payment_type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "base",
        "book",
        "card",
        "chats",
        "check",
        "cross_border",
        "dk_nets",
        "eft",
        "ethereum",
        "hu_ics",
        "interac",
        "masav",
        "mx_ccen",
        "neft",
        "nics",
        "nz_becs",
        "pl_elixir",
        "polygon",
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
        "solana",
        "wire",
        "zengin",
    ]
    """Only return internal accounts that can make this type of payment."""

    per_page: int
