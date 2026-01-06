# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .transaction_create_param import TransactionCreateParam
from .transaction_update_param import TransactionUpdateParam
from .payment_order_update_param import PaymentOrderUpdateParam
from .expected_payment_create_param import ExpectedPaymentCreateParam
from .expected_payment_update_param import ExpectedPaymentUpdateParam
from .ledger_transaction_update_param import LedgerTransactionUpdateParam
from .payment_order_async_create_param import PaymentOrderAsyncCreateParam
from .shared_params.ledger_account_create_request import LedgerAccountCreateRequest
from .shared_params.ledger_transaction_create_request import LedgerTransactionCreateRequest

__all__ = [
    "BulkRequestCreateParams",
    "Resources",
    "Resource",
    "ResourcesID",
    "ResourceID",
    "ResourcesPaymentOrderUpdateRequestWithID",
    "ResourcePaymentOrderUpdateRequestWithID",
    "ResourcesExpectedPaymentUpdateRequestWithID",
    "ResourceExpectedPaymentUpdateRequestWithID",
    "ResourcesTransactionUpdateRequestWithID",
    "ResourceTransactionUpdateRequestWithID",
    "ResourcesLedgerTransactionUpdateRequestWithID",
    "ResourceLedgerTransactionUpdateRequestWithID",
]


class BulkRequestCreateParams(TypedDict, total=False):
    action_type: Required[Literal["create", "update", "delete"]]
    """One of create, or update."""

    resource_type: Required[
        Literal[
            "payment_order",
            "ledger_account",
            "ledger_transaction",
            "expected_payment",
            "transaction",
            "transaction_line_item",
            "entity_link",
        ]
    ]
    """One of payment_order, expected_payment, or ledger_transaction."""

    resources: Required[Iterable[Resource]]
    """
    An array of objects where each object contains the input params for a single
    `action_type` request on a `resource_type` resource
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class ResourceID(TypedDict, total=False):
    id: str


ResourcesID = ResourceID
"""This type is deprecated and will be removed in a future release.

Please use ResourceID instead.
"""


class ResourcePaymentOrderUpdateRequestWithID(PaymentOrderUpdateParam, total=False):
    id: str


ResourcesPaymentOrderUpdateRequestWithID = ResourcePaymentOrderUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithID instead.
"""


class ResourceExpectedPaymentUpdateRequestWithID(ExpectedPaymentUpdateParam, total=False):
    id: str


ResourcesExpectedPaymentUpdateRequestWithID = ResourceExpectedPaymentUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceExpectedPaymentUpdateRequestWithID instead.
"""


class ResourceTransactionUpdateRequestWithID(TransactionUpdateParam, total=False):
    id: str


ResourcesTransactionUpdateRequestWithID = ResourceTransactionUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceTransactionUpdateRequestWithID instead.
"""


class ResourceLedgerTransactionUpdateRequestWithID(LedgerTransactionUpdateParam, total=False):
    id: str


ResourcesLedgerTransactionUpdateRequestWithID = ResourceLedgerTransactionUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceLedgerTransactionUpdateRequestWithID instead.
"""

Resource: TypeAlias = Union[
    PaymentOrderAsyncCreateParam,
    ExpectedPaymentCreateParam,
    LedgerTransactionCreateRequest,
    LedgerAccountCreateRequest,
    TransactionCreateParam,
    ResourceID,
    ResourcePaymentOrderUpdateRequestWithID,
    ResourceExpectedPaymentUpdateRequestWithID,
    ResourceTransactionUpdateRequestWithID,
    ResourceLedgerTransactionUpdateRequestWithID,
]

Resources = Resource
"""This type is deprecated and will be removed in a future release.

Please use Resource instead.
"""
