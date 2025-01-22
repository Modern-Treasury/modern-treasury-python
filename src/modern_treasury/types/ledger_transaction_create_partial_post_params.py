# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LedgerTransactionCreatePartialPostParams", "PostedLedgerEntries", "PostedLedgerEntry"]


class LedgerTransactionCreatePartialPostParams(TypedDict, total=False):
    posted_ledger_entries: Required[Iterable[PostedLedgerEntry]]
    """An array of ledger entry objects to be set on the posted ledger transaction.

    There must be one entry for each of the existing entries with a lesser amount
    than the existing entry.
    """

    description: str
    """An optional free-form description for the posted ledger transaction.

    Maximum of 1000 characters allowed.
    """

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (IS08601 format) at which the posted ledger transaction happened
    for reporting purposes.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class PostedLedgerEntry(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    direction: Required[Literal["credit", "debit"]]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_id: Required[str]
    """The ledger account that this ledger entry is associated with."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


PostedLedgerEntries = PostedLedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use PostedLedgerEntry instead.
"""
