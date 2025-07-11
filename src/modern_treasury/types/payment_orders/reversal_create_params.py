# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.ledger_transaction_create_request import LedgerTransactionCreateRequest

__all__ = ["ReversalCreateParams"]


class ReversalCreateParams(TypedDict, total=False):
    reason: Required[
        Literal[
            "duplicate",
            "incorrect_amount",
            "incorrect_receiving_account",
            "date_earlier_than_intended",
            "date_later_than_intended",
        ]
    ]
    """The reason for the reversal.

    Must be one of `duplicate`, `incorrect_amount`, `incorrect_receiving_account`,
    `date_earlier_than_intended`, `date_later_than_intended`.
    """

    ledger_transaction: LedgerTransactionCreateRequest
    """Specifies a ledger transaction object that will be created with the reversal.

    If the ledger transaction cannot be created, then the reversal creation will
    fail. The resulting ledger transaction will mirror the status of the reversal.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """
