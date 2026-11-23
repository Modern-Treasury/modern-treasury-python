# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentRequestUpdateParams"]


class PaymentRequestUpdateParams(TypedDict, total=False):
    status: Required[Literal["approved", "declined"]]
    """Approve the request and create a wire payment order, or decline the request."""
