# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ExternalAccountType"]

ExternalAccountType: TypeAlias = Literal[
    "cash", "checking", "general_ledger", "loan", "non_resident", "other", "overdraft", "savings"
]
