# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["VirtualAccountSettingCreateParams"]


class VirtualAccountSettingCreateParams(TypedDict, total=False):
    allocation_type: Required[str]
    """The method used to allocate virtual account numbers."""

    internal_account_id: Required[str]
    """The ID of the internal account for the virtual account setting."""

    allocation_identifier: Optional[str]
    """
    The prefix, suffix, or bank-assigned identifier for the virtual account numbers.
    """

    allocation_length: Optional[int]
    """The total length of generated virtual account numbers."""

    allocation_range_end: Optional[str]
    """The inclusive end of the virtual account number range."""

    allocation_range_start: Optional[str]
    """The inclusive start of the virtual account number range."""

    external_id: Optional[str]
    """A user-defined identifier for the virtual account setting."""

    generated_allocation_identifier_length: Optional[int]
    """The length of a generated virtual account setting prefix."""
