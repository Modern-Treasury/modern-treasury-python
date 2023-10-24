# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LedgerEventHandlerVariableParam", "Query"]


class Query(TypedDict, total=False):
    field: Required[str]
    """The LHS of the conditional."""

    operator: Required[str]
    """What the operator between the `field` and `value` is."""

    value: Required[str]
    """The RHS of the conditional."""


class LedgerEventHandlerVariableParam(TypedDict, total=False):
    query: Required[Query]

    type: Required[str]
    """The type of object this variable is.

    Currently, only "ledger_account" is supported.
    """
