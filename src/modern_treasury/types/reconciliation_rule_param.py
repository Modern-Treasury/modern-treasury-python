# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.currency import Currency

__all__ = ["ReconciliationRuleParam"]


class ReconciliationRuleParam(TypedDict, total=False):
    amount_lower_bound: Required[int]
    """The lowest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_upper_bound: Required[int]
    """The highest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    direction: Required[Literal["credit", "debit"]]
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: Required[str]
    """The ID of the Internal Account for the expected payment"""

    counterparty_id: Optional[str]
    """The ID of the counterparty you expect for this payment"""

    currency: Currency
    """Must conform to ISO 4217. Defaults to the currency of the internal account"""

    custom_identifiers: Optional[Dict[str, str]]
    """A hash of custom identifiers for this payment"""

    date_lower_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The earliest date the payment may come in. Format is yyyy-mm-dd"""

    date_upper_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The latest date the payment may come in. Format is yyyy-mm-dd"""

    type: Optional[
        Literal[
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
    ]
    """
    One of ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet wire
    """
