# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.currency import Currency
from .expected_payment_type import ExpectedPaymentType
from .reconciliation_rule_param import ReconciliationRuleParam

__all__ = ["ExpectedPaymentUpdateParams"]


class ExpectedPaymentUpdateParams(TypedDict, total=False):
    amount_lower_bound: Optional[int]
    """The lowest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_upper_bound: Optional[int]
    """The highest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    counterparty_id: Optional[str]
    """The ID of the counterparty you expect for this payment."""

    currency: Optional[Currency]
    """Must conform to ISO 4217. Defaults to the currency of the internal account."""

    date_lower_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The earliest date the payment may come in. Format: yyyy-mm-dd"""

    date_upper_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The latest date the payment may come in. Format: yyyy-mm-dd"""

    description: Optional[str]
    """An optional description for internal use."""

    direction: Optional[Literal["credit", "debit"]]
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: Optional[str]
    """The ID of the Internal Account for the expected payment."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    reconciliation_filters: Optional[object]
    """The reconciliation filters you have for this payment."""

    reconciliation_groups: Optional[object]
    """The reconciliation groups you have for this payment."""

    reconciliation_rule_variables: Optional[Iterable[ReconciliationRuleParam]]
    """An array of reconciliation rule variables for this payment."""

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

    status: Optional[Literal["reconciled"]]
    """
    The Expected Payment's status can be updated from partially_reconciled to
    reconciled.
    """

    type: Optional[ExpectedPaymentType]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet, wire.
    """
