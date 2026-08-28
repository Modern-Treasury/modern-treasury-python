# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JournalSourceListParams"]


class JournalSourceListParams(TypedDict, total=False):
    journal_entry_id: str
    """The ID of the journal entry"""

    journal_report_id: str
    """The ID of the journal report"""

    page: int
    """Page number for pagination"""

    per_page: int
    """Number of items per page"""

    source_id: str
    """The ID of the source object"""

    source_type: str
    """The type of the source object"""
