# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    ConnectionLegalEntity,
    connection_legal_entity_list_params,
    connection_legal_entity_create_params,
    connection_legal_entity_update_params,
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

__all__ = ["ConnectionLegalEntities", "AsyncConnectionLegalEntities"]


class ConnectionLegalEntities(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionLegalEntitiesWithRawResponse:
        return ConnectionLegalEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionLegalEntitiesWithStreamingResponse:
        return ConnectionLegalEntitiesWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_id: str,
        legal_entity: connection_legal_entity_create_params.LegalEntity | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ConnectionLegalEntity:
        """
        Create a connection legal entity.

        Args:
          connection_id: The ID of the connection.

          legal_entity: The legal entity.

          legal_entity_id: The ID of the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/connection_legal_entities",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "legal_entity": legal_entity,
                    "legal_entity_id": legal_entity_id,
                },
                connection_legal_entity_create_params.ConnectionLegalEntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ConnectionLegalEntity,
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
    ) -> ConnectionLegalEntity:
        """
        Get details on a single connection legal entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/connection_legal_entities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionLegalEntity,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["processing"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ConnectionLegalEntity:
        """
        Update a connection legal entity.

        Args:
          status: The status of the connection legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/connection_legal_entities/{id}",
            body=maybe_transform(
                {"status": status}, connection_legal_entity_update_params.ConnectionLegalEntityUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ConnectionLegalEntity,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["completed", "denied", "failed", "processing"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ConnectionLegalEntity]:
        """
        Get a list of all connection legal entities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/connection_legal_entities",
            page=SyncPage[ConnectionLegalEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "connection_id": connection_id,
                        "legal_entity_id": legal_entity_id,
                        "per_page": per_page,
                        "status": status,
                    },
                    connection_legal_entity_list_params.ConnectionLegalEntityListParams,
                ),
            ),
            model=ConnectionLegalEntity,
        )


class AsyncConnectionLegalEntities(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionLegalEntitiesWithRawResponse:
        return AsyncConnectionLegalEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionLegalEntitiesWithStreamingResponse:
        return AsyncConnectionLegalEntitiesWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_id: str,
        legal_entity: connection_legal_entity_create_params.LegalEntity | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ConnectionLegalEntity:
        """
        Create a connection legal entity.

        Args:
          connection_id: The ID of the connection.

          legal_entity: The legal entity.

          legal_entity_id: The ID of the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/connection_legal_entities",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "legal_entity": legal_entity,
                    "legal_entity_id": legal_entity_id,
                },
                connection_legal_entity_create_params.ConnectionLegalEntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ConnectionLegalEntity,
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
    ) -> ConnectionLegalEntity:
        """
        Get details on a single connection legal entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/connection_legal_entities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionLegalEntity,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["processing"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ConnectionLegalEntity:
        """
        Update a connection legal entity.

        Args:
          status: The status of the connection legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/connection_legal_entities/{id}",
            body=await async_maybe_transform(
                {"status": status}, connection_legal_entity_update_params.ConnectionLegalEntityUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ConnectionLegalEntity,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["completed", "denied", "failed", "processing"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ConnectionLegalEntity, AsyncPage[ConnectionLegalEntity]]:
        """
        Get a list of all connection legal entities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/connection_legal_entities",
            page=AsyncPage[ConnectionLegalEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "connection_id": connection_id,
                        "legal_entity_id": legal_entity_id,
                        "per_page": per_page,
                        "status": status,
                    },
                    connection_legal_entity_list_params.ConnectionLegalEntityListParams,
                ),
            ),
            model=ConnectionLegalEntity,
        )


class ConnectionLegalEntitiesWithRawResponse:
    def __init__(self, connection_legal_entities: ConnectionLegalEntities) -> None:
        self._connection_legal_entities = connection_legal_entities

        self.create = _legacy_response.to_raw_response_wrapper(
            connection_legal_entities.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            connection_legal_entities.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            connection_legal_entities.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            connection_legal_entities.list,
        )


class AsyncConnectionLegalEntitiesWithRawResponse:
    def __init__(self, connection_legal_entities: AsyncConnectionLegalEntities) -> None:
        self._connection_legal_entities = connection_legal_entities

        self.create = _legacy_response.async_to_raw_response_wrapper(
            connection_legal_entities.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            connection_legal_entities.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            connection_legal_entities.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            connection_legal_entities.list,
        )


class ConnectionLegalEntitiesWithStreamingResponse:
    def __init__(self, connection_legal_entities: ConnectionLegalEntities) -> None:
        self._connection_legal_entities = connection_legal_entities

        self.create = to_streamed_response_wrapper(
            connection_legal_entities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connection_legal_entities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connection_legal_entities.update,
        )
        self.list = to_streamed_response_wrapper(
            connection_legal_entities.list,
        )


class AsyncConnectionLegalEntitiesWithStreamingResponse:
    def __init__(self, connection_legal_entities: AsyncConnectionLegalEntities) -> None:
        self._connection_legal_entities = connection_legal_entities

        self.create = async_to_streamed_response_wrapper(
            connection_legal_entities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connection_legal_entities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connection_legal_entities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connection_legal_entities.list,
        )
