# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["ReconciliationRule"]


class ReconciliationRule(BaseModel):
    amount_lower_bound: int
    """The lowest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_upper_bound: int
    """The highest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    direction: Literal["credit", "debit"]
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: str
    """The ID of the Internal Account for the expected payment"""

    counterparty_id: Optional[str] = None
    """The ID of the counterparty you expect for this payment"""

    currency: Optional[Currency] = None
    """Must conform to ISO 4217. Defaults to the currency of the internal account"""

    custom_identifiers: Optional[Dict[str, str]] = None
    """A hash of custom identifiers for this payment"""

    date_lower_bound: Optional[date] = None
    """The earliest date the payment may come in. Format is yyyy-mm-dd"""

    date_upper_bound: Optional[date] = None
    """The latest date the payment may come in. Format is yyyy-mm-dd"""

    type: Optional[
        Literal[
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
    ] = None
    """
    One of ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet wire
    """
