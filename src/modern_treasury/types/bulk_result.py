# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .transaction import Transaction
from .ledger_account import LedgerAccount
from .expected_payment import ExpectedPayment
from .ledger_transaction import LedgerTransaction

__all__ = ["BulkResult", "Entity", "EntityBulkError", "EntityBulkErrorRequestErrors", "EntityBulkErrorRequestError"]


class EntityBulkErrorRequestError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None

    parameter: Optional[str] = None


EntityBulkErrorRequestErrors = EntityBulkErrorRequestError
"""This type is deprecated and will be removed in a future release.

Please use EntityBulkErrorRequestError instead.
"""


class EntityBulkError(BaseModel):
    id: str

    created_at: datetime

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    request_errors: List[EntityBulkErrorRequestError]

    updated_at: datetime


Entity: TypeAlias = Union[
    "PaymentOrder", ExpectedPayment, LedgerTransaction, LedgerAccount, Transaction, EntityBulkError
]


class BulkResult(BaseModel):
    id: str

    created_at: datetime

    entity: Entity
    """An object with type as indicated by `entity_type`.

    This is the result object that is generated by performing the requested action
    on the provided input `request_params`.
    """

    entity_id: str
    """Unique identifier for the result entity object."""

    entity_type: Literal[
        "payment_order",
        "ledger_account",
        "ledger_transaction",
        "expected_payment",
        "transaction",
        "entity_link",
        "transaction_line_item",
        "bulk_error",
    ]
    """The type of the result entity object.

    For a successful bulk result, this is the same as the `resource_type` of the
    bulk request. For a failed bulk result, this is always bulk_error
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    request_id: str
    """Unique identifier for the request that created this bulk result.

    This is the ID of the bulk request when `request_type` is bulk_request
    """

    request_params: Optional[Dict[str, str]] = None
    """
    An optional object that contains the provided input params for the request that
    created this result. This is an item in the `resources` array for the
    bulk_request
    """

    request_type: Literal["bulk_request"]
    """The type of the request that created this result.

    bulk_request is the only supported `request_type`
    """

    status: Literal["pending", "successful", "failed"]
    """One of successful or failed."""

    updated_at: datetime


from .payment_order import PaymentOrder
