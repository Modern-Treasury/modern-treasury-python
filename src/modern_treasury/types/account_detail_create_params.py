# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountDetailCreateParams"]


class AccountDetailCreateParams(TypedDict, total=False):
    accounts_type: Required[Literal["external_accounts"]]

    account_number: Required[str]
    """The account number for the bank account."""

    account_number_type: Literal["clabe", "hk_number", "iban", "other", "pan", "wallet_address"]
    """One of `iban`, `clabe`, `wallet_address`, or `other`.

    Use `other` if the bank account number is in a generic format.
    """
