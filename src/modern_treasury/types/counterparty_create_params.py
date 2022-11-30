# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "AccountsPartyAddress",
    "AccountsAccountDetails",
    "AccountsRoutingDetails",
    "AccountsContactDetails",
    "Accounts",
    "Accounting",
    "CounterpartyCreateParams",
]


class AccountsPartyAddress(TypedDict, total=False):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str]

    line2: Optional[str]

    locality: Optional[str]
    """Locality or City."""

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""


class AccountsAccountDetails(TypedDict, total=False):
    account_number: Required[str]

    account_number_type: Literal["iban", "clabe", "wallet_address", "pan", "other"]


class AccountsRoutingDetails(TypedDict, total=False):
    routing_number: Required[str]

    routing_number_type: Required[
        Literal["aba", "swift", "au_bsb", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "br_codigo"]
    ]

    payment_type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "check",
        "eft",
        "cross_border",
        "interac",
        "provxchange",
        "rtp",
        "sen",
        "sepa",
        "signet",
        "wire",
    ]


class AccountsContactDetails(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number"]


class Accounts(TypedDict, total=False):
    account_details: List[AccountsAccountDetails]

    account_type: Literal["cash", "checking", "loan", "non_resident", "other", "overdraft", "savings"]
    """Can be `checking`, `savings` or `other`."""

    contact_details: List[AccountsContactDetails]

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    party_address: AccountsPartyAddress
    """Required if receiving wire payments."""

    party_identifier: str

    party_name: str
    """
    If this value isn't provided, it will be inherited from the counterparty's name.
    """

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""

    plaid_processor_token: str
    """
    If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
    you can pass the processor token in this field.
    """

    routing_details: List[AccountsRoutingDetails]


class Accounting(TypedDict, total=False):
    type: Literal["customer", "vendor"]
    """An optional type to auto-sync the counterparty to your ledger.

    Either `customer` or `vendor`.
    """


class CounterpartyCreateParams(TypedDict, total=False):
    name: Required[Optional[str]]
    """A human friendly name for this counterparty."""

    accounting: Accounting

    accounts: List[Accounts]
    """The accounts for this counterparty."""

    email: Optional[str]
    """The counterparty's email."""

    ledger_type: Literal["customer", "vendor"]
    """An optional type to auto-sync the counterparty to your ledger.

    Either `customer` or `vendor`.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    send_remittance_advice: bool
    """
    Send an email to the counterparty whenever an associated payment order is sent
    to the bank.
    """

    taxpayer_identifier: str
    """Either a valid SSN or EIN."""
