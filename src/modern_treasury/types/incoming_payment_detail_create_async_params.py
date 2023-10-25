# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .shared import Currency
from .._utils import PropertyInfo

__all__ = ["IncomingPaymentDetailCreateAsyncParams"]


class IncomingPaymentDetailCreateAsyncParams(TypedDict, total=False):
    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    as_of_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Defaults to today."""

    currency: Optional[Currency]
    """Defaults to the currency of the originating account."""

    description: Optional[str]
    """Defaults to a random description."""

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
