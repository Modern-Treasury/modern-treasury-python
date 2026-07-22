# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional, Dict

from .shared.currency import Currency

from .shared.transaction_direction import TransactionDirection

__all__ = ["InternalAccountListParams"]

class InternalAccountListParams(TypedDict, total=False):
    after_cursor: Optional[str]

    counterparty_id: str
    """Only return internal accounts associated with this counterparty."""

    currency: Currency
    """Only return internal accounts with this currency."""

    external_id: str
    """An optional user-defined 180 character unique identifier."""

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

    payment_type: Literal["ach", "au_becs", "bacs", "book", "card", "chats", "check", "cross_border", "dk_nets", "eft", "gb_fps", "masav", "mx_ccen", "neft", "nics", "nz_becs", "pl_elixir", "rtp", "se_bankgirot", "sepa", "sg_giro", "sic", "stablecoin", "wire", "zengin"]
    """Only return internal accounts that can make this type of payment."""

    per_page: int

    status: Literal["active", "pending_activation", "suspended", "pending_closure", "closed"]
    """Only return internal accounts with this status."""