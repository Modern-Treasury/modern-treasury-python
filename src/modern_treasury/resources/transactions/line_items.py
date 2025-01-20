# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.transactions import line_item_list_params, line_item_create_params
from ...types.transactions.transaction_line_item import TransactionLineItem

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LineItemsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return LineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LineItemsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return LineItemsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        expected_payment_id: str,
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TransactionLineItem:
        """
        create transaction line items

        Args:
          amount: If a matching object exists in Modern Treasury, `amount` will be populated.
              Value in specified currency's smallest unit (taken from parent Transaction).

          expected_payment_id: The ID of the reconciled Expected Payment, otherwise `null`.

          transaction_id: The ID of the parent transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/transaction_line_items",
            body=maybe_transform(
                {
                    "amount": amount,
                    "expected_payment_id": expected_payment_id,
                    "transaction_id": transaction_id,
                },
                line_item_create_params.LineItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TransactionLineItem,
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
    ) -> None:
        """
        delete transaction line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/transaction_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncLineItems(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLineItemsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLineItemsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncLineItemsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        expected_payment_id: str,
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TransactionLineItem:
        """
        create transaction line items

        Args:
          amount: If a matching object exists in Modern Treasury, `amount` will be populated.
              Value in specified currency's smallest unit (taken from parent Transaction).

          expected_payment_id: The ID of the reconciled Expected Payment, otherwise `null`.

          transaction_id: The ID of the parent transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/transaction_line_items",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "expected_payment_id": expected_payment_id,
                    "transaction_id": transaction_id,
                },
                line_item_create_params.LineItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TransactionLineItem,
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
    ) -> None:
        """
        delete transaction line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/transaction_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class LineItemsWithRawResponse:
    def __init__(self, line_items: LineItems) -> None:
        self._line_items = line_items

        self.create = _legacy_response.to_raw_response_wrapper(
            line_items.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            line_items.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            line_items.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            line_items.delete,
        )


class AsyncLineItemsWithRawResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self._line_items = line_items

        self.create = _legacy_response.async_to_raw_response_wrapper(
            line_items.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            line_items.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            line_items.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            line_items.delete,
        )


class LineItemsWithStreamingResponse:
    def __init__(self, line_items: LineItems) -> None:
        self._line_items = line_items

        self.create = to_streamed_response_wrapper(
            line_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            line_items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            line_items.list,
        )
        self.delete = to_streamed_response_wrapper(
            line_items.delete,
        )


class AsyncLineItemsWithStreamingResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self._line_items = line_items

        self.create = async_to_streamed_response_wrapper(
            line_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            line_items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            line_items.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            line_items.delete,
        )
