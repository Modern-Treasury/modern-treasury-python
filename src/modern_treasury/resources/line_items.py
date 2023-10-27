# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from ..types import LineItem, line_item_list_params, line_item_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import ModernTreasury, AsyncModernTreasury

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    with_raw_response: LineItemsWithRawResponse

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = LineItemsWithRawResponse(self)

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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LineItem:
        """
        Get a single line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LineItem]:
        """
        Get a list of line items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
    with_raw_response: AsyncLineItemsWithRawResponse

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncLineItemsWithRawResponse(self)

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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LineItem:
        """
        Get a single line item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        return await self._patch(
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LineItem, AsyncPage[LineItem]]:
        """
        Get a list of line items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        self.retrieve = to_raw_response_wrapper(
            line_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            line_items.update,
        )
        self.list = to_raw_response_wrapper(
            line_items.list,
        )


class AsyncLineItemsWithRawResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            line_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            line_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            line_items.list,
        )
