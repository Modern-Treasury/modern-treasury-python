# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.ledger_account_create_request import LedgerAccountCreateRequest

__all__ = ["VirtualAccountCreateParams", "AccountDetails", "AccountDetail", "RoutingDetails", "RoutingDetail"]


class VirtualAccountCreateParams(TypedDict, total=False):
    internal_account_id: Required[str]
    """The ID of the internal account that this virtual account is associated with."""

    name: Required[str]
    """The name of the virtual account."""

    account_details: Iterable[AccountDetail]
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

    ledger_account: LedgerAccountCreateRequest
    """Specifies a ledger account object that will be created with the virtual account.

    The resulting ledger account is linked to the virtual account for auto-ledgering
    IPDs.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    routing_details: Iterable[RoutingDetail]
    """An array of routing detail objects."""


class AccountDetail(TypedDict, total=False):
    account_number: Required[str]
    """The account number for the bank account."""

    account_number_type: Literal[
        "au_number",
        "base_address",
        "clabe",
        "ethereum_address",
        "hk_number",
        "iban",
        "id_number",
        "nz_number",
        "other",
        "pan",
        "polygon_address",
        "sg_number",
        "solana_address",
        "wallet_address",
    ]
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
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "il_bank_code",
            "in_ifsc",
            "jp_zengin_code",
            "mx_bank_identifier",
            "my_branch_code",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "sg_interbank_clearing_code",
            "swift",
            "za_national_clearing_code",
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
            "base",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "ethereum",
            "gb_fps",
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
    ]
    """
    If the routing detail is to be used for a specific payment type this field will
    be populated, otherwise null.
    """


RoutingDetails = RoutingDetail
"""This type is deprecated and will be removed in a future release.

Please use RoutingDetail instead.
"""
