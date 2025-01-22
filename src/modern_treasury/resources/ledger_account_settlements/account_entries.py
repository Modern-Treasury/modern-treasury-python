# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.ledger_account_settlements import account_entry_delete_params, account_entry_update_params

__all__ = ["AccountEntries", "AsyncAccountEntries"]


class AccountEntries(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountEntriesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AccountEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountEntriesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AccountEntriesWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        ledger_entry_ids: Optional[List[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add ledger entries to a draft ledger account settlement.

        Args:
          ledger_entry_ids: The ids of the ledger entries that are to be added or removed from the ledger
              account settlement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/api/ledger_account_settlements/{id}/ledger_entries",
            body=maybe_transform(
                {"ledger_entry_ids": ledger_entry_ids}, account_entry_update_params.AccountEntryUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        id: str,
        *,
        ledger_entry_ids: Optional[Iterable[object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Remove ledger entries from a draft ledger account settlement.

        Args:
          ledger_entry_ids: The ids of the ledger entries that are to be added or removed from the ledger
              account settlement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/ledger_account_settlements/{id}/ledger_entries",
            body=maybe_transform(
                {"ledger_entry_ids": ledger_entry_ids}, account_entry_delete_params.AccountEntryDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncAccountEntries(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountEntriesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountEntriesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncAccountEntriesWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        ledger_entry_ids: Optional[List[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add ledger entries to a draft ledger account settlement.

        Args:
          ledger_entry_ids: The ids of the ledger entries that are to be added or removed from the ledger
              account settlement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/api/ledger_account_settlements/{id}/ledger_entries",
            body=await async_maybe_transform(
                {"ledger_entry_ids": ledger_entry_ids}, account_entry_update_params.AccountEntryUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        id: str,
        *,
        ledger_entry_ids: Optional[Iterable[object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Remove ledger entries from a draft ledger account settlement.

        Args:
          ledger_entry_ids: The ids of the ledger entries that are to be added or removed from the ledger
              account settlement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/ledger_account_settlements/{id}/ledger_entries",
            body=await async_maybe_transform(
                {"ledger_entry_ids": ledger_entry_ids}, account_entry_delete_params.AccountEntryDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AccountEntriesWithRawResponse:
    def __init__(self, account_entries: AccountEntries) -> None:
        self._account_entries = account_entries

        self.update = _legacy_response.to_raw_response_wrapper(
            account_entries.update,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            account_entries.delete,
        )


class AsyncAccountEntriesWithRawResponse:
    def __init__(self, account_entries: AsyncAccountEntries) -> None:
        self._account_entries = account_entries

        self.update = _legacy_response.async_to_raw_response_wrapper(
            account_entries.update,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            account_entries.delete,
        )


class AccountEntriesWithStreamingResponse:
    def __init__(self, account_entries: AccountEntries) -> None:
        self._account_entries = account_entries

        self.update = to_streamed_response_wrapper(
            account_entries.update,
        )
        self.delete = to_streamed_response_wrapper(
            account_entries.delete,
        )


class AsyncAccountEntriesWithStreamingResponse:
    def __init__(self, account_entries: AsyncAccountEntries) -> None:
        self._account_entries = account_entries

        self.update = async_to_streamed_response_wrapper(
            account_entries.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            account_entries.delete,
        )
