# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ledger_entry import LedgerEntry

__all__ = ["LedgerEntries", "AsyncLedgerEntries"]


class LedgerEntries(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerEntry:
        """Get details on a single ledger entry."""
        return self._get(
            f"/api/ledger_entries/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerEntry,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_account_lock_version: Dict[str, int] | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        show_deleted: bool | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[LedgerEntry]:
        """
        Get a list of all ledger entries.

        Args:
          effective_date: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              transaction's effective date. Format YYYY-MM-DD

          effective_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              transaction's effective time. Format ISO8601

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          ledger_account_lock_version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              lock_version of a ledger account. For example, for all entries created at or
              before before lock_version 1000 of a ledger account, use
              ledger_account_lock_version%5Blte%5D=1000

          ledger_account_category_id: Get all ledger entries that match the direction specified. One of `credit`,
              `debit`.

          show_deleted: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          direction: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_entries",
            page=SyncPage[LedgerEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "ledger_account_id": ledger_account_id,
                    "ledger_transaction_id": ledger_transaction_id,
                    "effective_date": effective_date,
                    "effective_at": effective_at,
                    "updated_at": updated_at,
                    "ledger_account_lock_version": ledger_account_lock_version,
                    "ledger_account_category_id": ledger_account_category_id,
                    "show_deleted": show_deleted,
                    "direction": direction,
                },
            ),
            model=LedgerEntry,
        )


class AsyncLedgerEntries(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerEntry:
        """Get details on a single ledger entry."""
        return await self._get(
            f"/api/ledger_entries/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerEntry,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_account_lock_version: Dict[str, int] | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        show_deleted: bool | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[LedgerEntry, AsyncPage[LedgerEntry]]:
        """
        Get a list of all ledger entries.

        Args:
          effective_date: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              transaction's effective date. Format YYYY-MM-DD

          effective_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              transaction's effective time. Format ISO8601

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          ledger_account_lock_version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              lock_version of a ledger account. For example, for all entries created at or
              before before lock_version 1000 of a ledger account, use
              ledger_account_lock_version%5Blte%5D=1000

          ledger_account_category_id: Get all ledger entries that match the direction specified. One of `credit`,
              `debit`.

          show_deleted: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          direction: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_entries",
            page=AsyncPage[LedgerEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "ledger_account_id": ledger_account_id,
                    "ledger_transaction_id": ledger_transaction_id,
                    "effective_date": effective_date,
                    "effective_at": effective_at,
                    "updated_at": updated_at,
                    "ledger_account_lock_version": ledger_account_lock_version,
                    "ledger_account_category_id": ledger_account_category_id,
                    "show_deleted": show_deleted,
                    "direction": direction,
                },
            ),
            model=LedgerEntry,
        )
