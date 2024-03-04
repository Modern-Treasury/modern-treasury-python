# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .. import _legacy_response
from ..types import LedgerableEvent, ledgerable_event_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["LedgerableEvents", "AsyncLedgerableEvents"]


class LedgerableEvents(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerableEventsWithRawResponse:
        return LedgerableEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerableEventsWithStreamingResponse:
        return LedgerableEventsWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        custom_data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerableEvent:
        """
        Create a ledgerable event.

        Args:
          name: Name of the ledgerable event.

          custom_data: Additionally data to be used by the Ledger Event Handler.

          description: Description of the ledgerable event.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledgerable_events",
            body=maybe_transform(
                {
                    "name": name,
                    "custom_data": custom_data,
                    "description": description,
                    "metadata": metadata,
                },
                ledgerable_event_create_params.LedgerableEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerableEvent,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerableEvent:
        """
        Get details on a single ledgerable event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledgerable_events/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerableEvent,
        )


class AsyncLedgerableEvents(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerableEventsWithRawResponse:
        return AsyncLedgerableEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerableEventsWithStreamingResponse:
        return AsyncLedgerableEventsWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        custom_data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerableEvent:
        """
        Create a ledgerable event.

        Args:
          name: Name of the ledgerable event.

          custom_data: Additionally data to be used by the Ledger Event Handler.

          description: Description of the ledgerable event.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledgerable_events",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "custom_data": custom_data,
                    "description": description,
                    "metadata": metadata,
                },
                ledgerable_event_create_params.LedgerableEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerableEvent,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerableEvent:
        """
        Get details on a single ledgerable event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledgerable_events/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerableEvent,
        )


class LedgerableEventsWithRawResponse:
    def __init__(self, ledgerable_events: LedgerableEvents) -> None:
        self._ledgerable_events = ledgerable_events

        self.create = _legacy_response.to_raw_response_wrapper(
            ledgerable_events.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledgerable_events.retrieve,
        )


class AsyncLedgerableEventsWithRawResponse:
    def __init__(self, ledgerable_events: AsyncLedgerableEvents) -> None:
        self._ledgerable_events = ledgerable_events

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledgerable_events.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledgerable_events.retrieve,
        )


class LedgerableEventsWithStreamingResponse:
    def __init__(self, ledgerable_events: LedgerableEvents) -> None:
        self._ledgerable_events = ledgerable_events

        self.create = to_streamed_response_wrapper(
            ledgerable_events.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledgerable_events.retrieve,
        )


class AsyncLedgerableEventsWithStreamingResponse:
    def __init__(self, ledgerable_events: AsyncLedgerableEvents) -> None:
        self._ledgerable_events = ledgerable_events

        self.create = async_to_streamed_response_wrapper(
            ledgerable_events.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledgerable_events.retrieve,
        )
