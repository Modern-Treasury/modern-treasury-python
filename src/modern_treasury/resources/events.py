# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import datetime

from ..types import Event, event_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import ModernTreasury, AsyncModernTreasury

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    with_raw_response: EventsWithRawResponse

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = EventsWithRawResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        get event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/events/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        event_name: str | NotGiven = NOT_GIVEN,
        event_time_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_time_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resource: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Event]:
        """
        list events

        Args:
          event_time_end: An inclusive upper bound for when the event occurred

          event_time_start: An inclusive lower bound for when the event occurred

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/events",
            page=SyncPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "entity_id": entity_id,
                        "event_name": event_name,
                        "event_time_end": event_time_end,
                        "event_time_start": event_time_start,
                        "per_page": per_page,
                        "resource": resource,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )


class AsyncEvents(AsyncAPIResource):
    with_raw_response: AsyncEventsWithRawResponse

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncEventsWithRawResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        get event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/events/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        event_name: str | NotGiven = NOT_GIVEN,
        event_time_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_time_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resource: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Event, AsyncPage[Event]]:
        """
        list events

        Args:
          event_time_end: An inclusive upper bound for when the event occurred

          event_time_start: An inclusive lower bound for when the event occurred

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/events",
            page=AsyncPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "entity_id": entity_id,
                        "event_name": event_name,
                        "event_time_end": event_time_end,
                        "event_time_start": event_time_start,
                        "per_page": per_page,
                        "resource": resource,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )


class EventsWithRawResponse:
    def __init__(self, events: Events) -> None:
        self.retrieve = to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )


class AsyncEventsWithRawResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )
