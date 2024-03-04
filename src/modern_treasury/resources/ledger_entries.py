# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    LedgerEntry,
    ledger_entry_list_params,
    ledger_entry_update_params,
    ledger_entry_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.shared import TransactionDirection

__all__ = ["LedgerEntries", "AsyncLedgerEntries"]


class LedgerEntries(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerEntriesWithRawResponse:
        return LedgerEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerEntriesWithStreamingResponse:
        return LedgerEntriesWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        show_balances: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerEntry:
        """
        Get details on a single ledger entry.

        Args:
          show_balances: If true, response will include the balances attached to the ledger entry. If
              there is no balance available, null will be returned instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"show_balances": show_balances}, ledger_entry_retrieve_params.LedgerEntryRetrieveParams
                ),
            ),
            cast_to=LedgerEntry,
        )

    def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerEntry:
        """
        Update the details of a ledger entry.

        Args:
          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/ledger_entries/{id}",
            body=maybe_transform({"metadata": metadata}, ledger_entry_update_params.LedgerEntryUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerEntry,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_lock_version: int | NotGiven = NOT_GIVEN,
        direction: TransactionDirection | NotGiven = NOT_GIVEN,
        effective_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, Union[str, date]] | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_account_lock_version: Dict[str, int] | NotGiven = NOT_GIVEN,
        ledger_account_payout_id: str | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: str | NotGiven = NOT_GIVEN,
        ledger_account_statement_id: str | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        order_by: ledger_entry_list_params.OrderBy | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        show_balances: bool | NotGiven = NOT_GIVEN,
        show_deleted: bool | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerEntry]:
        """
        Get a list of all ledger entries.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          as_of_lock_version: Shows all ledger entries that were present on a ledger account at a particular
              `lock_version`. You must also specify `ledger_account_id`.

          direction: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          effective_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              transaction's effective time. Format ISO8601

          effective_date: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              transaction's effective date. Format YYYY-MM-DD

          ledger_account_category_id: Get all ledger entries that match the direction specified. One of `credit`,
              `debit`.

          ledger_account_lock_version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              lock_version of a ledger account. For example, for all entries created at or
              before before lock_version 1000 of a ledger account, use
              `ledger_account_lock_version%5Blte%5D=1000`.

          ledger_account_statement_id: Get all ledger entries that are included in the ledger account statement.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          order_by: Order by `created_at` or `effective_at` in `asc` or `desc` order. For example,
              to order by `effective_at asc`, use `order_by%5Beffective_at%5D=asc`. Ordering
              by only one field at a time is supported.

          show_balances: If true, response will include the balances attached to the ledger entry. If
              there is no balance available, null will be returned instead.

          show_deleted: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          status: Get all ledger entries that match the status specified. One of `pending`,
              `posted`, or `archived`.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_entries",
            page=SyncPage[LedgerEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "as_of_lock_version": as_of_lock_version,
                        "direction": direction,
                        "effective_at": effective_at,
                        "effective_date": effective_date,
                        "ledger_account_category_id": ledger_account_category_id,
                        "ledger_account_id": ledger_account_id,
                        "ledger_account_lock_version": ledger_account_lock_version,
                        "ledger_account_payout_id": ledger_account_payout_id,
                        "ledger_account_settlement_id": ledger_account_settlement_id,
                        "ledger_account_statement_id": ledger_account_statement_id,
                        "ledger_transaction_id": ledger_transaction_id,
                        "metadata": metadata,
                        "order_by": order_by,
                        "per_page": per_page,
                        "show_balances": show_balances,
                        "show_deleted": show_deleted,
                        "status": status,
                        "updated_at": updated_at,
                    },
                    ledger_entry_list_params.LedgerEntryListParams,
                ),
            ),
            model=LedgerEntry,
        )


class AsyncLedgerEntries(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerEntriesWithRawResponse:
        return AsyncLedgerEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerEntriesWithStreamingResponse:
        return AsyncLedgerEntriesWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        show_balances: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerEntry:
        """
        Get details on a single ledger entry.

        Args:
          show_balances: If true, response will include the balances attached to the ledger entry. If
              there is no balance available, null will be returned instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"show_balances": show_balances}, ledger_entry_retrieve_params.LedgerEntryRetrieveParams
                ),
            ),
            cast_to=LedgerEntry,
        )

    async def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerEntry:
        """
        Update the details of a ledger entry.

        Args:
          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/ledger_entries/{id}",
            body=await async_maybe_transform(
                {"metadata": metadata}, ledger_entry_update_params.LedgerEntryUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerEntry,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_lock_version: int | NotGiven = NOT_GIVEN,
        direction: TransactionDirection | NotGiven = NOT_GIVEN,
        effective_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, Union[str, date]] | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_account_lock_version: Dict[str, int] | NotGiven = NOT_GIVEN,
        ledger_account_payout_id: str | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: str | NotGiven = NOT_GIVEN,
        ledger_account_statement_id: str | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        order_by: ledger_entry_list_params.OrderBy | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        show_balances: bool | NotGiven = NOT_GIVEN,
        show_deleted: bool | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerEntry, AsyncPage[LedgerEntry]]:
        """
        Get a list of all ledger entries.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          as_of_lock_version: Shows all ledger entries that were present on a ledger account at a particular
              `lock_version`. You must also specify `ledger_account_id`.

          direction: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          effective_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              transaction's effective time. Format ISO8601

          effective_date: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              transaction's effective date. Format YYYY-MM-DD

          ledger_account_category_id: Get all ledger entries that match the direction specified. One of `credit`,
              `debit`.

          ledger_account_lock_version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              lock_version of a ledger account. For example, for all entries created at or
              before before lock_version 1000 of a ledger account, use
              `ledger_account_lock_version%5Blte%5D=1000`.

          ledger_account_statement_id: Get all ledger entries that are included in the ledger account statement.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          order_by: Order by `created_at` or `effective_at` in `asc` or `desc` order. For example,
              to order by `effective_at asc`, use `order_by%5Beffective_at%5D=asc`. Ordering
              by only one field at a time is supported.

          show_balances: If true, response will include the balances attached to the ledger entry. If
              there is no balance available, null will be returned instead.

          show_deleted: If true, response will include ledger entries that were deleted. When you update
              a ledger transaction to specify a new set of entries, the previous entries are
              deleted.

          status: Get all ledger entries that match the status specified. One of `pending`,
              `posted`, or `archived`.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_entries",
            page=AsyncPage[LedgerEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "as_of_lock_version": as_of_lock_version,
                        "direction": direction,
                        "effective_at": effective_at,
                        "effective_date": effective_date,
                        "ledger_account_category_id": ledger_account_category_id,
                        "ledger_account_id": ledger_account_id,
                        "ledger_account_lock_version": ledger_account_lock_version,
                        "ledger_account_payout_id": ledger_account_payout_id,
                        "ledger_account_settlement_id": ledger_account_settlement_id,
                        "ledger_account_statement_id": ledger_account_statement_id,
                        "ledger_transaction_id": ledger_transaction_id,
                        "metadata": metadata,
                        "order_by": order_by,
                        "per_page": per_page,
                        "show_balances": show_balances,
                        "show_deleted": show_deleted,
                        "status": status,
                        "updated_at": updated_at,
                    },
                    ledger_entry_list_params.LedgerEntryListParams,
                ),
            ),
            model=LedgerEntry,
        )


class LedgerEntriesWithRawResponse:
    def __init__(self, ledger_entries: LedgerEntries) -> None:
        self._ledger_entries = ledger_entries

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_entries.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            ledger_entries.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_entries.list,
        )


class AsyncLedgerEntriesWithRawResponse:
    def __init__(self, ledger_entries: AsyncLedgerEntries) -> None:
        self._ledger_entries = ledger_entries

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_entries.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            ledger_entries.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_entries.list,
        )


class LedgerEntriesWithStreamingResponse:
    def __init__(self, ledger_entries: LedgerEntries) -> None:
        self._ledger_entries = ledger_entries

        self.retrieve = to_streamed_response_wrapper(
            ledger_entries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ledger_entries.update,
        )
        self.list = to_streamed_response_wrapper(
            ledger_entries.list,
        )


class AsyncLedgerEntriesWithStreamingResponse:
    def __init__(self, ledger_entries: AsyncLedgerEntries) -> None:
        self._ledger_entries = ledger_entries

        self.retrieve = async_to_streamed_response_wrapper(
            ledger_entries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ledger_entries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_entries.list,
        )
