# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.invoices import InvoiceLineItem, line_item_list_params, line_item_create_params, line_item_update_params

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LineItemsWithRawResponse:
        return LineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LineItemsWithStreamingResponse:
        return LineItemsWithStreamingResponse(self)

    def create(
        self,
        invoice_id: str,
        *,
        name: str,
        unit_amount: int,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        unit_amount_decimal: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        create invoice_line_item

        Args:
          name: The name of the line item, typically a product or SKU name.

          unit_amount: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit.

          description: An optional free-form description of the line item.

          direction: Either `debit` or `credit`. `debit` indicates that a client owes the business
              money and increases the invoice's `total_amount` due. `credit` has the opposite
              intention and effect.

          quantity: The number of units of a product or service that this line item is for. Must be
              a whole number. Defaults to 1 if not provided.

          unit_amount_decimal: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit. Accepts decimal strings with
              up to 12 decimals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            f"/api/invoices/{invoice_id}/invoice_line_items",
            body=maybe_transform(
                {
                    "name": name,
                    "unit_amount": unit_amount,
                    "description": description,
                    "direction": direction,
                    "quantity": quantity,
                    "unit_amount_decimal": unit_amount_decimal,
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
            cast_to=InvoiceLineItem,
        )

    def retrieve(
        self,
        id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceLineItem:
        """
        get invoice_line_item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceLineItem,
        )

    def update(
        self,
        id: str,
        *,
        invoice_id: str,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        unit_amount: int | NotGiven = NOT_GIVEN,
        unit_amount_decimal: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        update invoice_line_item

        Args:
          description: An optional free-form description of the line item.

          direction: Either `debit` or `credit`. `debit` indicates that a client owes the business
              money and increases the invoice's `total_amount` due. `credit` has the opposite
              intention and effect.

          name: The name of the line item, typically a product or SKU name.

          quantity: The number of units of a product or service that this line item is for. Must be
              a whole number. Defaults to 1 if not provided.

          unit_amount: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit.

          unit_amount_decimal: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit. Accepts decimal strings with
              up to 12 decimals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "direction": direction,
                    "name": name,
                    "quantity": quantity,
                    "unit_amount": unit_amount,
                    "unit_amount_decimal": unit_amount_decimal,
                },
                line_item_update_params.LineItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InvoiceLineItem,
        )

    def list(
        self,
        invoice_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InvoiceLineItem]:
        """
        list invoice_line_items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get_api_list(
            f"/api/invoices/{invoice_id}/invoice_line_items",
            page=SyncPage[InvoiceLineItem],
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
            model=InvoiceLineItem,
        )

    def delete(
        self,
        id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        delete invoice_line_item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InvoiceLineItem,
        )


class AsyncLineItems(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLineItemsWithRawResponse:
        return AsyncLineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLineItemsWithStreamingResponse:
        return AsyncLineItemsWithStreamingResponse(self)

    async def create(
        self,
        invoice_id: str,
        *,
        name: str,
        unit_amount: int,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        unit_amount_decimal: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        create invoice_line_item

        Args:
          name: The name of the line item, typically a product or SKU name.

          unit_amount: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit.

          description: An optional free-form description of the line item.

          direction: Either `debit` or `credit`. `debit` indicates that a client owes the business
              money and increases the invoice's `total_amount` due. `credit` has the opposite
              intention and effect.

          quantity: The number of units of a product or service that this line item is for. Must be
              a whole number. Defaults to 1 if not provided.

          unit_amount_decimal: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit. Accepts decimal strings with
              up to 12 decimals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            f"/api/invoices/{invoice_id}/invoice_line_items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "unit_amount": unit_amount,
                    "description": description,
                    "direction": direction,
                    "quantity": quantity,
                    "unit_amount_decimal": unit_amount_decimal,
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
            cast_to=InvoiceLineItem,
        )

    async def retrieve(
        self,
        id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceLineItem:
        """
        get invoice_line_item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceLineItem,
        )

    async def update(
        self,
        id: str,
        *,
        invoice_id: str,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        unit_amount: int | NotGiven = NOT_GIVEN,
        unit_amount_decimal: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        update invoice_line_item

        Args:
          description: An optional free-form description of the line item.

          direction: Either `debit` or `credit`. `debit` indicates that a client owes the business
              money and increases the invoice's `total_amount` due. `credit` has the opposite
              intention and effect.

          name: The name of the line item, typically a product or SKU name.

          quantity: The number of units of a product or service that this line item is for. Must be
              a whole number. Defaults to 1 if not provided.

          unit_amount: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit.

          unit_amount_decimal: The cost per unit of the product or service that this line item is for,
              specified in the invoice currency's smallest unit. Accepts decimal strings with
              up to 12 decimals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "direction": direction,
                    "name": name,
                    "quantity": quantity,
                    "unit_amount": unit_amount,
                    "unit_amount_decimal": unit_amount_decimal,
                },
                line_item_update_params.LineItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InvoiceLineItem,
        )

    def list(
        self,
        invoice_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InvoiceLineItem, AsyncPage[InvoiceLineItem]]:
        """
        list invoice_line_items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get_api_list(
            f"/api/invoices/{invoice_id}/invoice_line_items",
            page=AsyncPage[InvoiceLineItem],
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
            model=InvoiceLineItem,
        )

    async def delete(
        self,
        id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        delete invoice_line_item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InvoiceLineItem,
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
        self.update = _legacy_response.to_raw_response_wrapper(
            line_items.update,
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
        self.update = _legacy_response.async_to_raw_response_wrapper(
            line_items.update,
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
        self.update = to_streamed_response_wrapper(
            line_items.update,
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
        self.update = async_to_streamed_response_wrapper(
            line_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            line_items.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            line_items.delete,
        )
