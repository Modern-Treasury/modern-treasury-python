# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import LineItem, line_item_list_params, line_item_update_params
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
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LineItem:
        """
        Get a single line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not itemizable_type:
            raise ValueError(f"Expected a non-empty value for `itemizable_type` but received {itemizable_type!r}")
        if not itemizable_id:
            raise ValueError(f"Expected a non-empty value for `itemizable_id` but received {itemizable_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LineItem,
        )

    def update(
        self,
        id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LineItem:
        """
        update line item

        Args:
          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not itemizable_type:
            raise ValueError(f"Expected a non-empty value for `itemizable_type` but received {itemizable_type!r}")
        if not itemizable_id:
            raise ValueError(f"Expected a non-empty value for `itemizable_id` but received {itemizable_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            body=maybe_transform({"metadata": metadata}, line_item_update_params.LineItemUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LineItem,
        )

    def list(
        self,
        itemizable_id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LineItem]:
        """
        Get a list of line items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not itemizable_type:
            raise ValueError(f"Expected a non-empty value for `itemizable_type` but received {itemizable_type!r}")
        if not itemizable_id:
            raise ValueError(f"Expected a non-empty value for `itemizable_id` but received {itemizable_id!r}")
        return self._get_api_list(
            f"/api/{itemizable_type}/{itemizable_id}/line_items",
            page=SyncPage[LineItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                    },
                    line_item_list_params.LineItemListParams,
                ),
            ),
            model=LineItem,
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
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LineItem:
        """
        Get a single line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not itemizable_type:
            raise ValueError(f"Expected a non-empty value for `itemizable_type` but received {itemizable_type!r}")
        if not itemizable_id:
            raise ValueError(f"Expected a non-empty value for `itemizable_id` but received {itemizable_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LineItem,
        )

    async def update(
        self,
        id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LineItem:
        """
        update line item

        Args:
          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not itemizable_type:
            raise ValueError(f"Expected a non-empty value for `itemizable_type` but received {itemizable_type!r}")
        if not itemizable_id:
            raise ValueError(f"Expected a non-empty value for `itemizable_id` but received {itemizable_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            body=await async_maybe_transform({"metadata": metadata}, line_item_update_params.LineItemUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LineItem,
        )

    def list(
        self,
        itemizable_id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LineItem, AsyncPage[LineItem]]:
        """
        Get a list of line items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not itemizable_type:
            raise ValueError(f"Expected a non-empty value for `itemizable_type` but received {itemizable_type!r}")
        if not itemizable_id:
            raise ValueError(f"Expected a non-empty value for `itemizable_id` but received {itemizable_id!r}")
        return self._get_api_list(
            f"/api/{itemizable_type}/{itemizable_id}/line_items",
            page=AsyncPage[LineItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                    },
                    line_item_list_params.LineItemListParams,
                ),
            ),
            model=LineItem,
        )


class LineItemsWithRawResponse:
    def __init__(self, line_items: LineItems) -> None:
        self._line_items = line_items

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            line_items.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            line_items.update,
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
        self.update = _legacy_response.async_to_raw_response_wrapper(
            line_items.update,
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
        self.update = to_streamed_response_wrapper(
            line_items.update,
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
        self.update = async_to_streamed_response_wrapper(
            line_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            line_items.list,
        )
