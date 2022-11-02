# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ledger_entry import LedgerEntry
from ..types.ledger_entry_list_params import LedgerEntryListParams

__all__ = ["LedgerEntries", "AsyncLedgerEntries"]


class LedgerEntries(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerEntry:
        """Get details on a single ledger entry."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/ledger_entries/{id}",
            options=options,
            cast_to=LedgerEntry,
        )

    def list(
        self,
        query: LedgerEntryListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LedgerEntry]:
        """Get a list of all ledger entries."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LedgerEntryListParams))
        return self._get_api_list(
            "/api/ledger_entries",
            page=SyncPage[LedgerEntry],
            options=options,
            model=LedgerEntry,
        )


class AsyncLedgerEntries(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerEntry:
        """Get details on a single ledger entry."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/ledger_entries/{id}",
            options=options,
            cast_to=LedgerEntry,
        )

    def list(
        self,
        query: LedgerEntryListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerEntry, AsyncPage[LedgerEntry]]:
        """Get a list of all ledger entries."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LedgerEntryListParams))
        return self._get_api_list(
            "/api/ledger_entries",
            page=AsyncPage[LedgerEntry],
            options=options,
            model=LedgerEntry,
        )
