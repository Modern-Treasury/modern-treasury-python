# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .transaction_create_request_param import TransactionCreateRequestParam
from .transaction_update_request_param import TransactionUpdateRequestParam
from .payment_order_update_request_param import PaymentOrderUpdateRequestParam
from .ledger_account_update_request_param import LedgerAccountUpdateRequestParam
from .expected_payment_create_request_param import ExpectedPaymentCreateRequestParam
from .expected_payment_update_request_param import ExpectedPaymentUpdateRequestParam
from .ledger_transaction_update_request_param import LedgerTransactionUpdateRequestParam
from .payment_order_async_create_request_param import PaymentOrderAsyncCreateRequestParam
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
    "ResourcesLedgerAccountUpdateRequestWithID",
    "ResourceLedgerAccountUpdateRequestWithID",
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


class ResourcePaymentOrderUpdateRequestWithID(PaymentOrderUpdateRequestParam, total=False):
    id: str


ResourcesPaymentOrderUpdateRequestWithID = ResourcePaymentOrderUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithID instead.
"""


class ResourceExpectedPaymentUpdateRequestWithID(ExpectedPaymentUpdateRequestParam, total=False):
    id: str


ResourcesExpectedPaymentUpdateRequestWithID = ResourceExpectedPaymentUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceExpectedPaymentUpdateRequestWithID instead.
"""


class ResourceTransactionUpdateRequestWithID(TransactionUpdateRequestParam, total=False):
    id: str


ResourcesTransactionUpdateRequestWithID = ResourceTransactionUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceTransactionUpdateRequestWithID instead.
"""


class ResourceLedgerTransactionUpdateRequestWithID(LedgerTransactionUpdateRequestParam, total=False):
    id: str


ResourcesLedgerTransactionUpdateRequestWithID = ResourceLedgerTransactionUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceLedgerTransactionUpdateRequestWithID instead.
"""


class ResourceLedgerAccountUpdateRequestWithID(LedgerAccountUpdateRequestParam, total=False):
    id: str


ResourcesLedgerAccountUpdateRequestWithID = ResourceLedgerAccountUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceLedgerAccountUpdateRequestWithID instead.
"""

Resource: TypeAlias = Union[
    PaymentOrderAsyncCreateRequestParam,
    ExpectedPaymentCreateRequestParam,
    LedgerTransactionCreateRequest,
    LedgerAccountCreateRequest,
    TransactionCreateRequestParam,
    ResourceID,
    ResourcePaymentOrderUpdateRequestWithID,
    ResourceExpectedPaymentUpdateRequestWithID,
    ResourceTransactionUpdateRequestWithID,
    ResourceLedgerTransactionUpdateRequestWithID,
    ResourceLedgerAccountUpdateRequestWithID,
]

Resources = Resource
"""This type is deprecated and will be removed in a future release.

Please use Resource instead.
"""
