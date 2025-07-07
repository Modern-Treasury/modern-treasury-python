# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InternalAccountUpdateAccountCapabilityParams"]


class InternalAccountUpdateAccountCapabilityParams(TypedDict, total=False):
    internal_account_id: Required[str]

    identifier: Required[str]
    """
    A unique reference assigned by your bank for tracking and recognizing payment
    files. It is important this is formatted exactly how the bank assigned it.
    """
