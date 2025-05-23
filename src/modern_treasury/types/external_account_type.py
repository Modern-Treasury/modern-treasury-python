# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ExternalAccountType"]

ExternalAccountType: TypeAlias = Literal[
    "base_wallet",
    "cash",
    "checking",
    "crypto_wallet",
    "ethereum_wallet",
    "general_ledger",
    "loan",
    "non_resident",
    "other",
    "overdraft",
    "polygon_wallet",
    "savings",
    "solana_wallet",
]
