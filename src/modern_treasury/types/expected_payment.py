# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .reconciliation_rule import ReconciliationRule
from .expected_payment_type import ExpectedPaymentType

__all__ = ["ExpectedPayment"]


class ExpectedPayment(BaseModel):
    id: str

    amount_lower_bound: Optional[int] = None
    """The lowest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_reconciled: Optional[int] = None
    """The amount reconciled for this expected payment.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_reconciled_direction: Optional[Literal["credit", "debit"]] = None
    """One of credit or debit.

    Indicates whether amount_reconciled is a credit or debit amount.
    """

    amount_unreconciled: Optional[int] = None
    """The amount that remains unreconciled for this expected payment.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_unreconciled_direction: Optional[Literal["credit", "debit"]] = None
    """One of credit or debit.

    Indicates whether amount_unreconciled is a credit or debit amount.
    """

    amount_upper_bound: Optional[int] = None
    """The highest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    counterparty_id: Optional[str] = None
    """The ID of the counterparty you expect for this payment."""

    created_at: datetime

    currency: Optional[
        Literal[
            "AED",
            "AFN",
            "ALL",
            "AMD",
            "ANG",
            "AOA",
            "ARS",
            "AUD",
            "AWG",
            "AZN",
            "BAM",
            "BBD",
            "BCH",
            "BDT",
            "BGN",
            "BHD",
            "BIF",
            "BMD",
            "BND",
            "BOB",
            "BRL",
            "BSD",
            "BTC",
            "BTN",
            "BWP",
            "BYN",
            "BYR",
            "BZD",
            "CAD",
            "CDF",
            "CHF",
            "CLF",
            "CLP",
            "CNH",
            "CNY",
            "COP",
            "CRC",
            "CUC",
            "CUP",
            "CVE",
            "CZK",
            "DJF",
            "DKK",
            "DOP",
            "DZD",
            "EEK",
            "EGP",
            "ERN",
            "ETB",
            "ETH",
            "EUR",
            "EURC",
            "FJD",
            "FKP",
            "GBP",
            "GBX",
            "GEL",
            "GGP",
            "GHS",
            "GIP",
            "GMD",
            "GNF",
            "GTQ",
            "GYD",
            "HKD",
            "HNL",
            "HRK",
            "HTG",
            "HUF",
            "IDR",
            "ILS",
            "IMP",
            "INR",
            "IQD",
            "IRR",
            "ISK",
            "JEP",
            "JMD",
            "JOD",
            "JPY",
            "KES",
            "KGS",
            "KHR",
            "KMF",
            "KPW",
            "KRW",
            "KWD",
            "KYD",
            "KZT",
            "LAK",
            "LBP",
            "LKR",
            "LRD",
            "LSL",
            "LTL",
            "LVL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRO",
            "MRU",
            "MTL",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MYR",
            "MZN",
            "NAD",
            "NGN",
            "NIO",
            "NOK",
            "NPR",
            "NZD",
            "OMR",
            "OP",
            "PAB",
            "PEN",
            "PGK",
            "PHP",
            "PKR",
            "PLN",
            "PYG",
            "PYUSD",
            "QAR",
            "RON",
            "RSD",
            "RUB",
            "RWF",
            "SAR",
            "SBD",
            "SCR",
            "SDG",
            "SEK",
            "SGD",
            "SHP",
            "SKK",
            "SLE",
            "SLL",
            "SOS",
            "SRD",
            "SSP",
            "STD",
            "STN",
            "SVC",
            "SYP",
            "SZL",
            "THB",
            "TJS",
            "TMM",
            "TMT",
            "TND",
            "TOP",
            "TRY",
            "TTD",
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "USDC",
            "USDG",
            "USDT",
            "UYU",
            "UZS",
            "VEF",
            "VES",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XAG",
            "XAU",
            "XBA",
            "XBB",
            "XBC",
            "XBD",
            "XCD",
            "XCG",
            "XDR",
            "XFU",
            "XOF",
            "XPD",
            "XPF",
            "XPT",
            "XTS",
            "YER",
            "ZAR",
            "ZMK",
            "ZMW",
            "ZWD",
            "ZWG",
            "ZWL",
            "ZWN",
            "ZWR",
        ]
    ] = None

    date_lower_bound: Optional[date] = None
    """The earliest date the payment may come in. Format: yyyy-mm-dd"""

    date_upper_bound: Optional[date] = None
    """The latest date the payment may come in. Format: yyyy-mm-dd"""

    description: Optional[str] = None
    """An optional description for internal use."""

    direction: Optional[Literal["credit", "debit"]] = None
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    external_id: Optional[str] = None
    """An optional user-defined 180 character unique identifier."""

    internal_account_id: Optional[str] = None
    """The ID of the Internal Account for the expected payment."""

    ledger_transaction_id: Optional[str] = None
    """The ID of the ledger transaction linked to the expected payment."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    object: str

    reconciliation_filters: Optional[builtins.object] = None
    """The reconciliation filters you have for this payment."""

    reconciliation_groups: Optional[builtins.object] = None
    """The reconciliation groups you have for this payment."""

    reconciliation_method: Optional[Literal["automatic", "manual"]] = None
    """
    One of manual if this expected payment was manually reconciled in the dashboard,
    automatic if it was automatically reconciled by Modern Treasury, or null if it
    is unreconciled.
    """

    reconciliation_rule_variables: List[ReconciliationRule]
    """An array of reconciliation rule variables for this payment."""

    remittance_information: Optional[str] = None
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    statement_descriptor: Optional[str] = None
    """The statement description you expect to see on the transaction.

    For ACH payments, this will be the full line item passed from the bank. For wire
    payments, this will be the OBI field on the wire. For check payments, this will
    be the memo field.
    """

    status: Literal["archived", "partially_reconciled", "reconciled", "unreconciled"]
    """One of unreconciled, partially_reconciled, reconciled, or archived."""

    transaction_id: Optional[str] = None
    """The ID of the Transaction this expected payment object has been matched to."""

    transaction_line_item_id: Optional[str] = None
    """The ID of the Transaction Line Item this expected payment has been matched to."""

    type: Optional[ExpectedPaymentType] = None
    """One of: ach, au_becs, bacs, book, check, eft, rtp, sepa, wire."""

    updated_at: datetime
