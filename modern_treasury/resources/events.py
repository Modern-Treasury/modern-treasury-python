# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.event import Event
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_list_params import EventListParams

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Event:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/events/{id}",
            options=options,
            cast_to=Event,
        )

    def list(
        self,
        query: EventListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Event]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/events",
            page=SyncPage[Event],
            options=options,
            model=Event,
        )


class AsyncEvents(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Event:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/events/{id}",
            options=options,
            cast_to=Event,
        )

    def list(
        self,
        query: EventListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Event, AsyncPage[Event]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/events",
            page=AsyncPage[Event],
            options=options,
            model=Event,
        )
