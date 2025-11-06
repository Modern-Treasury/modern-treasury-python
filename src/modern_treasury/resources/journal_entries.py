# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import journal_entry_list_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options

__all__ = ["JournalEntries", "AsyncJournalEntries"]


class JournalEntries(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JournalEntriesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return JournalEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JournalEntriesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return JournalEntriesWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve a specific journal entry

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/journal_entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        journal_report_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve a list of journal entries

        Args:
          journal_report_id: The ID of the journal report

          page: Page number for pagination

          per_page: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/journal_entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "journal_report_id": journal_report_id,
                        "page": page,
                        "per_page": per_page,
                    },
                    journal_entry_list_params.JournalEntryListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncJournalEntries(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJournalEntriesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJournalEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJournalEntriesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncJournalEntriesWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve a specific journal entry

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/journal_entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        journal_report_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve a list of journal entries

        Args:
          journal_report_id: The ID of the journal report

          page: Page number for pagination

          per_page: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/journal_entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "journal_report_id": journal_report_id,
                        "page": page,
                        "per_page": per_page,
                    },
                    journal_entry_list_params.JournalEntryListParams,
                ),
            ),
            cast_to=NoneType,
        )


class JournalEntriesWithRawResponse:
    def __init__(self, journal_entries: JournalEntries) -> None:
        self._journal_entries = journal_entries

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            journal_entries.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            journal_entries.list,
        )


class AsyncJournalEntriesWithRawResponse:
    def __init__(self, journal_entries: AsyncJournalEntries) -> None:
        self._journal_entries = journal_entries

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            journal_entries.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            journal_entries.list,
        )


class JournalEntriesWithStreamingResponse:
    def __init__(self, journal_entries: JournalEntries) -> None:
        self._journal_entries = journal_entries

        self.retrieve = to_streamed_response_wrapper(
            journal_entries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            journal_entries.list,
        )


class AsyncJournalEntriesWithStreamingResponse:
    def __init__(self, journal_entries: AsyncJournalEntries) -> None:
        self._journal_entries = journal_entries

        self.retrieve = async_to_streamed_response_wrapper(
            journal_entries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            journal_entries.list,
        )
