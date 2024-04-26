# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LineItemCreateParams"]


class LineItemCreateParams(TypedDict, total=False):
    amount: Required[int]
    """If a matching object exists in Modern Treasury, `amount` will be populated.

    Value in specified currency's smallest unit (taken from parent Transaction).
    """

    expected_payment_id: Required[str]
    """The ID of the reconciled Expected Payment, otherwise `null`."""

    transaction_id: Required[str]
    """The ID of the parent transaction."""
