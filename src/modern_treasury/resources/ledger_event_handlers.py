# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import (
    LedgerEventHandler,
    LedgerEventHandlerVariableParam,
    ledger_event_handler_list_params,
    ledger_event_handler_create_params,
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

__all__ = ["LedgerEventHandlers", "AsyncLedgerEventHandlers"]


class LedgerEventHandlers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerEventHandlersWithRawResponse:
        return LedgerEventHandlersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerEventHandlersWithStreamingResponse:
        return LedgerEventHandlersWithStreamingResponse(self)

    def create(
        self,
        *,
        ledger_transaction_template: ledger_event_handler_create_params.LedgerTransactionTemplate,
        name: str,
        conditions: Optional[ledger_event_handler_create_params.Conditions] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        variables: Optional[Dict[str, LedgerEventHandlerVariableParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerEventHandler:
        """
        create ledger_event_handler

        Args:
          name: Name of the ledger event handler.

          description: An optional description.

          ledger_id: The id of the ledger that this account belongs to.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_event_handlers",
            body=maybe_transform(
                {
                    "ledger_transaction_template": ledger_transaction_template,
                    "name": name,
                    "conditions": conditions,
                    "description": description,
                    "ledger_id": ledger_id,
                    "metadata": metadata,
                    "variables": variables,
                },
                ledger_event_handler_create_params.LedgerEventHandlerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerEventHandler,
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
    ) -> LedgerEventHandler:
        """
        Get details on a single ledger event handler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_event_handlers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerEventHandler,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerEventHandler]:
        """
        Get a list of ledger event handlers.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_event_handlers",
            page=SyncPage[LedgerEventHandler],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at": created_at,
                        "metadata": metadata,
                        "name": name,
                        "per_page": per_page,
                    },
                    ledger_event_handler_list_params.LedgerEventHandlerListParams,
                ),
            ),
            model=LedgerEventHandler,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerEventHandler:
        """
        Archive a ledger event handler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/ledger_event_handlers/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerEventHandler,
        )


class AsyncLedgerEventHandlers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerEventHandlersWithRawResponse:
        return AsyncLedgerEventHandlersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerEventHandlersWithStreamingResponse:
        return AsyncLedgerEventHandlersWithStreamingResponse(self)

    async def create(
        self,
        *,
        ledger_transaction_template: ledger_event_handler_create_params.LedgerTransactionTemplate,
        name: str,
        conditions: Optional[ledger_event_handler_create_params.Conditions] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        variables: Optional[Dict[str, LedgerEventHandlerVariableParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerEventHandler:
        """
        create ledger_event_handler

        Args:
          name: Name of the ledger event handler.

          description: An optional description.

          ledger_id: The id of the ledger that this account belongs to.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_event_handlers",
            body=await async_maybe_transform(
                {
                    "ledger_transaction_template": ledger_transaction_template,
                    "name": name,
                    "conditions": conditions,
                    "description": description,
                    "ledger_id": ledger_id,
                    "metadata": metadata,
                    "variables": variables,
                },
                ledger_event_handler_create_params.LedgerEventHandlerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerEventHandler,
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
    ) -> LedgerEventHandler:
        """
        Get details on a single ledger event handler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_event_handlers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerEventHandler,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerEventHandler, AsyncPage[LedgerEventHandler]]:
        """
        Get a list of ledger event handlers.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_event_handlers",
            page=AsyncPage[LedgerEventHandler],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at": created_at,
                        "metadata": metadata,
                        "name": name,
                        "per_page": per_page,
                    },
                    ledger_event_handler_list_params.LedgerEventHandlerListParams,
                ),
            ),
            model=LedgerEventHandler,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerEventHandler:
        """
        Archive a ledger event handler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/ledger_event_handlers/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerEventHandler,
        )


class LedgerEventHandlersWithRawResponse:
    def __init__(self, ledger_event_handlers: LedgerEventHandlers) -> None:
        self._ledger_event_handlers = ledger_event_handlers

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_event_handlers.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_event_handlers.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_event_handlers.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            ledger_event_handlers.delete,
        )


class AsyncLedgerEventHandlersWithRawResponse:
    def __init__(self, ledger_event_handlers: AsyncLedgerEventHandlers) -> None:
        self._ledger_event_handlers = ledger_event_handlers

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_event_handlers.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_event_handlers.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_event_handlers.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            ledger_event_handlers.delete,
        )


class LedgerEventHandlersWithStreamingResponse:
    def __init__(self, ledger_event_handlers: LedgerEventHandlers) -> None:
        self._ledger_event_handlers = ledger_event_handlers

        self.create = to_streamed_response_wrapper(
            ledger_event_handlers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_event_handlers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ledger_event_handlers.list,
        )
        self.delete = to_streamed_response_wrapper(
            ledger_event_handlers.delete,
        )


class AsyncLedgerEventHandlersWithStreamingResponse:
    def __init__(self, ledger_event_handlers: AsyncLedgerEventHandlers) -> None:
        self._ledger_event_handlers = ledger_event_handlers

        self.create = async_to_streamed_response_wrapper(
            ledger_event_handlers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_event_handlers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_event_handlers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ledger_event_handlers.delete,
        )
