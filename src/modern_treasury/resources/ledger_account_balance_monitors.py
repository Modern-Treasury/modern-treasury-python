# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from .. import _legacy_response
from ..types import (
    LedgerAccountBalanceMonitor,
    ledger_account_balance_monitor_list_params,
    ledger_account_balance_monitor_create_params,
    ledger_account_balance_monitor_update_params,
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

__all__ = ["LedgerAccountBalanceMonitors", "AsyncLedgerAccountBalanceMonitors"]


class LedgerAccountBalanceMonitors(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerAccountBalanceMonitorsWithRawResponse:
        return LedgerAccountBalanceMonitorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerAccountBalanceMonitorsWithStreamingResponse:
        return LedgerAccountBalanceMonitorsWithStreamingResponse(self)

    def create(
        self,
        *,
        alert_condition: ledger_account_balance_monitor_create_params.AlertCondition,
        ledger_account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountBalanceMonitor:
        """
        Create a ledger account balance monitor.

        Args:
          alert_condition: Describes the condition that must be satisfied for the monitor to be triggered.

          ledger_account_id: The ledger account associated with this balance monitor.

          description: An optional, free-form description for internal use.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_account_balance_monitors",
            body=maybe_transform(
                {
                    "alert_condition": alert_condition,
                    "ledger_account_id": ledger_account_id,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_balance_monitor_create_params.LedgerAccountBalanceMonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountBalanceMonitor,
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
    ) -> LedgerAccountBalanceMonitor:
        """
        Get details on a single ledger account balance monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_account_balance_monitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountBalanceMonitor,
        )

    def update(
        self,
        id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountBalanceMonitor:
        """
        Update a ledger account balance monitor.

        Args:
          description: An optional, free-form description for internal use.

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
            f"/api/ledger_account_balance_monitors/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_balance_monitor_update_params.LedgerAccountBalanceMonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountBalanceMonitor,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerAccountBalanceMonitor]:
        """
        Get a list of ledger account balance monitors.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          ledger_account_id: Query the balance monitors for a single ledger account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_account_balance_monitors",
            page=SyncPage[LedgerAccountBalanceMonitor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "ledger_account_id": ledger_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                    },
                    ledger_account_balance_monitor_list_params.LedgerAccountBalanceMonitorListParams,
                ),
            ),
            model=LedgerAccountBalanceMonitor,
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
    ) -> LedgerAccountBalanceMonitor:
        """
        Delete a ledger account balance monitor.

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
            f"/api/ledger_account_balance_monitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountBalanceMonitor,
        )


class AsyncLedgerAccountBalanceMonitors(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerAccountBalanceMonitorsWithRawResponse:
        return AsyncLedgerAccountBalanceMonitorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerAccountBalanceMonitorsWithStreamingResponse:
        return AsyncLedgerAccountBalanceMonitorsWithStreamingResponse(self)

    async def create(
        self,
        *,
        alert_condition: ledger_account_balance_monitor_create_params.AlertCondition,
        ledger_account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountBalanceMonitor:
        """
        Create a ledger account balance monitor.

        Args:
          alert_condition: Describes the condition that must be satisfied for the monitor to be triggered.

          ledger_account_id: The ledger account associated with this balance monitor.

          description: An optional, free-form description for internal use.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_account_balance_monitors",
            body=await async_maybe_transform(
                {
                    "alert_condition": alert_condition,
                    "ledger_account_id": ledger_account_id,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_balance_monitor_create_params.LedgerAccountBalanceMonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountBalanceMonitor,
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
    ) -> LedgerAccountBalanceMonitor:
        """
        Get details on a single ledger account balance monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_account_balance_monitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountBalanceMonitor,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountBalanceMonitor:
        """
        Update a ledger account balance monitor.

        Args:
          description: An optional, free-form description for internal use.

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
            f"/api/ledger_account_balance_monitors/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_balance_monitor_update_params.LedgerAccountBalanceMonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountBalanceMonitor,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerAccountBalanceMonitor, AsyncPage[LedgerAccountBalanceMonitor]]:
        """
        Get a list of ledger account balance monitors.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          ledger_account_id: Query the balance monitors for a single ledger account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_account_balance_monitors",
            page=AsyncPage[LedgerAccountBalanceMonitor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "ledger_account_id": ledger_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                    },
                    ledger_account_balance_monitor_list_params.LedgerAccountBalanceMonitorListParams,
                ),
            ),
            model=LedgerAccountBalanceMonitor,
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
    ) -> LedgerAccountBalanceMonitor:
        """
        Delete a ledger account balance monitor.

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
            f"/api/ledger_account_balance_monitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountBalanceMonitor,
        )


class LedgerAccountBalanceMonitorsWithRawResponse:
    def __init__(self, ledger_account_balance_monitors: LedgerAccountBalanceMonitors) -> None:
        self._ledger_account_balance_monitors = ledger_account_balance_monitors

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_account_balance_monitors.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_account_balance_monitors.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            ledger_account_balance_monitors.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_account_balance_monitors.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            ledger_account_balance_monitors.delete,
        )


class AsyncLedgerAccountBalanceMonitorsWithRawResponse:
    def __init__(self, ledger_account_balance_monitors: AsyncLedgerAccountBalanceMonitors) -> None:
        self._ledger_account_balance_monitors = ledger_account_balance_monitors

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_balance_monitors.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_balance_monitors.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_balance_monitors.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_balance_monitors.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_balance_monitors.delete,
        )


class LedgerAccountBalanceMonitorsWithStreamingResponse:
    def __init__(self, ledger_account_balance_monitors: LedgerAccountBalanceMonitors) -> None:
        self._ledger_account_balance_monitors = ledger_account_balance_monitors

        self.create = to_streamed_response_wrapper(
            ledger_account_balance_monitors.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_account_balance_monitors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ledger_account_balance_monitors.update,
        )
        self.list = to_streamed_response_wrapper(
            ledger_account_balance_monitors.list,
        )
        self.delete = to_streamed_response_wrapper(
            ledger_account_balance_monitors.delete,
        )


class AsyncLedgerAccountBalanceMonitorsWithStreamingResponse:
    def __init__(self, ledger_account_balance_monitors: AsyncLedgerAccountBalanceMonitors) -> None:
        self._ledger_account_balance_monitors = ledger_account_balance_monitors

        self.create = async_to_streamed_response_wrapper(
            ledger_account_balance_monitors.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_account_balance_monitors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ledger_account_balance_monitors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_account_balance_monitors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ledger_account_balance_monitors.delete,
        )
