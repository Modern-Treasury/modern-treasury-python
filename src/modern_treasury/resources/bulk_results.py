# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import BulkResult, bulk_result_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["BulkResults", "AsyncBulkResults"]


class BulkResults(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResultsWithRawResponse:
        return BulkResultsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResultsWithStreamingResponse:
        return BulkResultsWithStreamingResponse(self)

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
    ) -> BulkResult:
        """
        get bulk_result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/bulk_results/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkResult,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        entity_type: Literal["payment_order", "ledger_transaction", "expected_payment", "bulk_error"]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        request_type: Literal["bulk_request"] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "successful", "failed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BulkResult]:
        """
        list bulk_results

        Args:
          entity_id: Unique identifier for the result entity object.

          entity_type: The type of the request that created this result. bulk_request is the only
              supported `request_type`

          request_id: Unique identifier for the request that created this bulk result. This is the ID
              of the bulk request when `request_type` is bulk_request

          request_type: The type of the request that created this result. bulk_request is the only
              supported `request_type`

          status: One of successful or failed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/bulk_results",
            page=SyncPage[BulkResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "entity_id": entity_id,
                        "entity_type": entity_type,
                        "per_page": per_page,
                        "request_id": request_id,
                        "request_type": request_type,
                        "status": status,
                    },
                    bulk_result_list_params.BulkResultListParams,
                ),
            ),
            model=BulkResult,
        )


class AsyncBulkResults(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResultsWithRawResponse:
        return AsyncBulkResultsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResultsWithStreamingResponse:
        return AsyncBulkResultsWithStreamingResponse(self)

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
    ) -> BulkResult:
        """
        get bulk_result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/bulk_results/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkResult,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        entity_type: Literal["payment_order", "ledger_transaction", "expected_payment", "bulk_error"]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        request_type: Literal["bulk_request"] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "successful", "failed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BulkResult, AsyncPage[BulkResult]]:
        """
        list bulk_results

        Args:
          entity_id: Unique identifier for the result entity object.

          entity_type: The type of the request that created this result. bulk_request is the only
              supported `request_type`

          request_id: Unique identifier for the request that created this bulk result. This is the ID
              of the bulk request when `request_type` is bulk_request

          request_type: The type of the request that created this result. bulk_request is the only
              supported `request_type`

          status: One of successful or failed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/bulk_results",
            page=AsyncPage[BulkResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "entity_id": entity_id,
                        "entity_type": entity_type,
                        "per_page": per_page,
                        "request_id": request_id,
                        "request_type": request_type,
                        "status": status,
                    },
                    bulk_result_list_params.BulkResultListParams,
                ),
            ),
            model=BulkResult,
        )


class BulkResultsWithRawResponse:
    def __init__(self, bulk_results: BulkResults) -> None:
        self._bulk_results = bulk_results

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            bulk_results.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            bulk_results.list,
        )


class AsyncBulkResultsWithRawResponse:
    def __init__(self, bulk_results: AsyncBulkResults) -> None:
        self._bulk_results = bulk_results

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            bulk_results.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            bulk_results.list,
        )


class BulkResultsWithStreamingResponse:
    def __init__(self, bulk_results: BulkResults) -> None:
        self._bulk_results = bulk_results

        self.retrieve = to_streamed_response_wrapper(
            bulk_results.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bulk_results.list,
        )


class AsyncBulkResultsWithStreamingResponse:
    def __init__(self, bulk_results: AsyncBulkResults) -> None:
        self._bulk_results = bulk_results

        self.retrieve = async_to_streamed_response_wrapper(
            bulk_results.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bulk_results.list,
        )
