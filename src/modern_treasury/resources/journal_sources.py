# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import journal_source_list_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options

__all__ = ["JournalSources", "AsyncJournalSources"]


class JournalSources(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JournalSourcesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return JournalSourcesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JournalSourcesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return JournalSourcesWithStreamingResponse(self)

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
        Retrieve a specific journal source

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
            path_template("/api/journal_sources/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        journal_entry_id: str | Omit = omit,
        journal_report_id: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        source_id: str | Omit = omit,
        source_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve a list of journal sources

        Args:
          journal_entry_id: The ID of the journal entry

          journal_report_id: The ID of the journal report

          page: Page number for pagination

          per_page: Number of items per page

          source_id: The ID of the source object

          source_type: The type of the source object

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/journal_sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "journal_entry_id": journal_entry_id,
                        "journal_report_id": journal_report_id,
                        "page": page,
                        "per_page": per_page,
                        "source_id": source_id,
                        "source_type": source_type,
                    },
                    journal_source_list_params.JournalSourceListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncJournalSources(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJournalSourcesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJournalSourcesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJournalSourcesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncJournalSourcesWithStreamingResponse(self)

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
        Retrieve a specific journal source

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
            path_template("/api/journal_sources/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        journal_entry_id: str | Omit = omit,
        journal_report_id: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        source_id: str | Omit = omit,
        source_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve a list of journal sources

        Args:
          journal_entry_id: The ID of the journal entry

          journal_report_id: The ID of the journal report

          page: Page number for pagination

          per_page: Number of items per page

          source_id: The ID of the source object

          source_type: The type of the source object

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/journal_sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "journal_entry_id": journal_entry_id,
                        "journal_report_id": journal_report_id,
                        "page": page,
                        "per_page": per_page,
                        "source_id": source_id,
                        "source_type": source_type,
                    },
                    journal_source_list_params.JournalSourceListParams,
                ),
            ),
            cast_to=NoneType,
        )


class JournalSourcesWithRawResponse:
    def __init__(self, journal_sources: JournalSources) -> None:
        self._journal_sources = journal_sources

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            journal_sources.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            journal_sources.list,
        )


class AsyncJournalSourcesWithRawResponse:
    def __init__(self, journal_sources: AsyncJournalSources) -> None:
        self._journal_sources = journal_sources

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            journal_sources.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            journal_sources.list,
        )


class JournalSourcesWithStreamingResponse:
    def __init__(self, journal_sources: JournalSources) -> None:
        self._journal_sources = journal_sources

        self.retrieve = to_streamed_response_wrapper(
            journal_sources.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            journal_sources.list,
        )


class AsyncJournalSourcesWithStreamingResponse:
    def __init__(self, journal_sources: AsyncJournalSources) -> None:
        self._journal_sources = journal_sources

        self.retrieve = async_to_streamed_response_wrapper(
            journal_sources.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            journal_sources.list,
        )
