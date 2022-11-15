# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from ..types import shared_params

__all__ = ["ExpectedPaymentUpdateParams"]


class ExpectedPaymentUpdateParams(TypedDict, total=False):
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

    counterparty_id: Optional[str]
    """The ID of the counterparty you expect for this payment."""

    currency: shared_params.Currency
    """Must conform to ISO 4217. Defaults to the currency of the internal account."""

    date_lower_bound: Optional[str]
    """The earliest date the payment may come in. Format: yyyy-mm-dd"""

    date_upper_bound: Optional[str]
    """The latest date the payment may come in. Format: yyyy-mm-dd"""

    description: Optional[str]
    """An optional description for internal use."""

    direction: Literal["credit", "debit"]
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: str
    """The ID of the Internal Account for the expected payment."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    remittance_information: Optional[str]
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    statement_descriptor: Optional[str]
    """The statement description you expect to see on the transaction.

    For ACH payments, this will be the full line item passed from the bank. For wire
    payments, this will be the OBI field on the wire. For check payments, this will
    be the memo field.
    """

    type: Optional[
        Literal[
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
    ]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet, wire.
    """
