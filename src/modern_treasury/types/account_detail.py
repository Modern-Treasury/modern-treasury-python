# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountDetail"]


class AccountDetail(BaseModel):
    id: str

    account_number_safe: str
    """The last 4 digits of the account_number."""

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

    created_at: datetime

    discarded_at: Optional[datetime] = None

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: datetime

    account_number: Optional[str] = None
    """The account number for the bank account."""
