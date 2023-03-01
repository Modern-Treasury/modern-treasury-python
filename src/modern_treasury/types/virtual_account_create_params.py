# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VirtualAccountCreateParams", "AccountDetail", "RoutingDetail", "RoutingDetailBankAddress"]


class AccountDetail(TypedDict, total=False):
    account_number_safe: Required[str]
    """The last 4 digits of the account_number."""

    account_number_type: Required[Literal["clabe", "iban", "other", "pan", "wallet_address"]]
    """One of `iban`, `clabe`, `wallet_address`, or `other`.

    Use `other` if the bank account number is in a generic format.
    """

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]]

    id: Required[str]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    account_number: str
    """The account number for the bank account."""


AccountDetail = AccountDetail
"""This type is deprecated and will be removed in a future release.

Please use AccountDetail instead.
"""


class RoutingDetailBankAddress(TypedDict, total=False):
    country: Required[Optional[str]]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    id: Required[str]

    line1: Required[Optional[str]]

    line2: Required[Optional[str]]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Required[Optional[str]]
    """Locality or City."""

    object: Required[str]

    postal_code: Required[Optional[str]]
    """The postal code of the address."""

    region: Required[Optional[str]]
    """Region or State."""

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


RoutingDetailBankAddress = RoutingDetailBankAddress
"""This type is deprecated and will be removed in a future release.

Please use RoutingDetailBankAddress instead.
"""


class RoutingDetail(TypedDict, total=False):
    bank_address: Required[Optional[RoutingDetailBankAddress]]

    bank_name: Required[str]
    """The name of the bank."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]]

    id: Required[str]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    payment_type: Required[
        Optional[
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
                "masav",
                "neft",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
    ]
    """
    If the routing detail is to be used for a specific payment type this field will
    be populated, otherwise null.
    """

    routing_number: Required[str]
    """The routing number of the bank."""

    routing_number_type: Required[
        Literal["aba", "au_bsb", "br_codigo", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "swift"]
    ]
    """One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`."""

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


RoutingDetail = RoutingDetail
"""This type is deprecated and will be removed in a future release.

Please use RoutingDetail instead.
"""


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
