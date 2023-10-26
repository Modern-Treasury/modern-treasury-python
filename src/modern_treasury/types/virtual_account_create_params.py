# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VirtualAccountCreateParams", "AccountDetails", "AccountDetail", "RoutingDetails", "RoutingDetail"]


class VirtualAccountCreateParams(TypedDict, total=False):
    internal_account_id: Required[str]
    """The ID of the internal account that this virtual account is associated with."""

    name: Required[str]
    """The name of the virtual account."""

    account_details: List[AccountDetail]
    """An array of account detail objects."""

    counterparty_id: str
    """The ID of the counterparty that the virtual account belongs to."""

    credit_ledger_account_id: str
    """The ID of a credit normal ledger account.

    When money leaves the virtual account, this ledger account will be credited.
    Must be accompanied by a debit_ledger_account_id if present.
    """

    debit_ledger_account_id: str
    """The ID of a debit normal ledger account.

    When money enters the virtual account, this ledger account will be debited. Must
    be accompanied by a credit_ledger_account_id if present.
    """

    description: str
    """An optional description for internal use."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    routing_details: List[RoutingDetail]
    """An array of routing detail objects."""


class AccountDetail(TypedDict, total=False):
    account_number: Required[str]
    """The account number for the bank account."""

    account_number_type: Literal["clabe", "iban", "other", "pan", "wallet_address"]
    """One of `iban`, `clabe`, `wallet_address`, or `other`.

    Use `other` if the bank account number is in a generic format.
    """


AccountDetails = AccountDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountDetail instead.
"""


class RoutingDetail(TypedDict, total=False):
    routing_number: Required[str]
    """The routing number of the bank."""

    routing_number_type: Required[
        Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "nz_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ]
    ]
    """The type of routing number.

    See https://docs.moderntreasury.com/platform/reference/routing-detail-object for
    more details.
    """

    payment_type: Optional[
        Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "eft",
            "interac",
            "masav",
            "neft",
            "nics",
            "nz_becs",
            "provxchange",
            "rtp",
            "se_bankgirot",
            "sen",
            "sepa",
            "sg_giro",
            "sic",
            "signet",
            "wire",
            "zengin",
        ]
    ]
    """
    If the routing detail is to be used for a specific payment type this field will
    be populated, otherwise null.
    """


RoutingDetails = RoutingDetail
"""This type is deprecated and will be removed in a future release.

Please use RoutingDetail instead.
"""
