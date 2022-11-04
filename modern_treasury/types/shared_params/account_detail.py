# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountDetail"]


class AccountDetail(TypedDict, total=False):
    account_number: Required[str]
    """The account number for the bank account."""

    account_number_type: Required[Literal["clabe", "iban", "other", "pan", "wallet_address"]]
    """One of `iban`, `clabe`, `wallet_address`, or `other`.

    Use `other` if the bank account number is in a generic format.
    """

    created_at: Required[str]

    discarded_at: Required[Optional[str]]

    id: Required[str]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    updated_at: Required[str]
