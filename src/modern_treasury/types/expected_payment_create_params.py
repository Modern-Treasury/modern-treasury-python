# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..types import shared_params
from .._utils import PropertyInfo
from .expected_payment_type import ExpectedPaymentType

__all__ = ["ExpectedPaymentCreateParams", "LineItems", "LineItem"]


class ExpectedPaymentCreateParams(TypedDict, total=False):
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

    direction: Required[shared_params.TransactionDirection]
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: Required[str]
    """The ID of the Internal Account for the expected payment."""

    counterparty_id: Optional[str]
    """The ID of the counterparty you expect for this payment."""

    currency: Optional[shared_params.Currency]
    """Must conform to ISO 4217. Defaults to the currency of the internal account."""

    date_lower_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The earliest date the payment may come in. Format: yyyy-mm-dd"""

    date_upper_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The latest date the payment may come in. Format: yyyy-mm-dd"""

    description: Optional[str]
    """An optional description for internal use."""

    line_items: List[LineItem]

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    reconciliation_filters: Optional[object]
    """The reconciliation filters you have for this payment."""

    reconciliation_groups: Optional[object]
    """The reconciliation groups you have for this payment."""

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

    type: Optional[ExpectedPaymentType]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet, wire.
    """


class LineItem(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    description: Optional[str]
    """A free-form description of the line item."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


LineItems = LineItem
"""This type is deprecated and will be removed in a future release.

Please use LineItem instead.
"""
