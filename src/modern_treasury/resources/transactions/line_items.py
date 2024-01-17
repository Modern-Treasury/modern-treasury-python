# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.transactions import TransactionLineItem, line_item_list_params

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LineItemsWithRawResponse:
        return LineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LineItemsWithStreamingResponse:
        return LineItemsWithStreamingResponse(self)

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
    ) -> TransactionLineItem:
        """
        get transaction line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/transaction_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLineItem,
        )

    def list(
        self,
        *,
        id: Dict[str, str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: Optional[Literal["originating", "receiving"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TransactionLineItem]:
        """
        list transaction_line_items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/transaction_line_items",
            page=SyncPage[TransactionLineItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "transaction_id": transaction_id,
                        "type": type,
                    },
                    line_item_list_params.LineItemListParams,
                ),
            ),
            model=TransactionLineItem,
        )


class AsyncLineItems(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLineItemsWithRawResponse:
        return AsyncLineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLineItemsWithStreamingResponse:
        return AsyncLineItemsWithStreamingResponse(self)

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
    ) -> TransactionLineItem:
        """
        get transaction line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/transaction_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLineItem,
        )

    def list(
        self,
        *,
        id: Dict[str, str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: Optional[Literal["originating", "receiving"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TransactionLineItem, AsyncPage[TransactionLineItem]]:
        """
        list transaction_line_items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/transaction_line_items",
            page=AsyncPage[TransactionLineItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "transaction_id": transaction_id,
                        "type": type,
                    },
                    line_item_list_params.LineItemListParams,
                ),
            ),
            model=TransactionLineItem,
        )


class LineItemsWithRawResponse:
    def __init__(self, line_items: LineItems) -> None:
        self._line_items = line_items

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            line_items.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            line_items.list,
        )


class AsyncLineItemsWithRawResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self._line_items = line_items

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            line_items.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            line_items.list,
        )


class LineItemsWithStreamingResponse:
    def __init__(self, line_items: LineItems) -> None:
        self._line_items = line_items

        self.retrieve = to_streamed_response_wrapper(
            line_items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            line_items.list,
        )


class AsyncLineItemsWithStreamingResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self._line_items = line_items

        self.retrieve = async_to_streamed_response_wrapper(
            line_items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            line_items.list,
        )
