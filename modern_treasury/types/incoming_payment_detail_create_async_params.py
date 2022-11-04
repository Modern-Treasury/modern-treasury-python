# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..types import shared_params

__all__ = ["IncomingPaymentDetailCreateAsyncParams"]


class IncomingPaymentDetailCreateAsyncParams(TypedDict, total=False):
    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: Optional[str]
    """Defaults to today."""

    currency: shared_params.Currency
    """Defaults to the currency of the originating account."""

    direction: Literal["credit", "debit"]
    """One of `credit`, `debit`."""

    internal_account_id: str
    """The ID of one of your internal accounts."""

    type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"]
    """One of `ach`, `wire`, `check`."""

    virtual_account_id: Optional[str]
    """
    An optional parameter to associate the incoming payment detail to a virtual
    account.
    """
