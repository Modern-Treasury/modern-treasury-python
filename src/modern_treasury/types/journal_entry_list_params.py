# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JournalEntryListParams"]


class JournalEntryListParams(TypedDict, total=False):
    journal_report_id: Required[str]
    """The ID of the journal report"""

    page: int
    """Page number for pagination"""

    per_page: int
    """Number of items per page"""
