# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["LedgerEventHandlerVariable", "Query"]


class Query(BaseModel):
    field: str
    """The LHS of the conditional."""

    operator: str
    """What the operator between the `field` and `value` is."""

    value: str
    """The RHS of the conditional."""


class LedgerEventHandlerVariable(BaseModel):
    query: Query

    type: str
    """The type of object this variable is.

    Currently, only "ledger_account" is supported.
    """
