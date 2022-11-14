# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.event import Event
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Event:
        return self._get(
            f"/api/events/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Event,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        event_time_start: str | NotGiven = NOT_GIVEN,
        event_time_end: str | NotGiven = NOT_GIVEN,
        resource: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        event_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Event]:
        """
        Args:
          event_time_start: An inclusive lower bound for when the event occurred

          event_time_end: An inclusive upper bound for when the event occurred

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/events",
            page=SyncPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "event_time_start": event_time_start,
                    "event_time_end": event_time_end,
                    "resource": resource,
                    "entity_id": entity_id,
                    "event_name": event_name,
                },
            ),
            model=Event,
        )


class AsyncEvents(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Event:
        return await self._get(
            f"/api/events/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Event,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        event_time_start: str | NotGiven = NOT_GIVEN,
        event_time_end: str | NotGiven = NOT_GIVEN,
        resource: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        event_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Event, AsyncPage[Event]]:
        """
        Args:
          event_time_start: An inclusive lower bound for when the event occurred

          event_time_end: An inclusive upper bound for when the event occurred

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/events",
            page=AsyncPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "event_time_start": event_time_start,
                    "event_time_end": event_time_end,
                    "resource": resource,
                    "entity_id": entity_id,
                    "event_name": event_name,
                },
            ),
            model=Event,
        )
