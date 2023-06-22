# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime

from ...types import shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.invoices import (
    InvoiceLineItem,
    line_item_list_params,
    line_item_create_params,
    line_item_update_params,
)

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    def create(
        self,
        invoice_id: str,
        *,
        name: str,
        unit_amount: int,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/api/invoices/{invoice_id}/invoice_line_items",
            body=maybe_transform(
                {
                    "name": name,
                    "unit_amount": unit_amount,
                    "description": description,
                    "direction": direction,
                    "quantity": quantity,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceLineItem:
        """
        get invoice_line_item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        contact_details: List[line_item_update_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[line_item_update_params.CounterpartyBillingAddress]
        | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[line_item_update_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: shared_params.Currency | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[line_item_update_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        update invoice_line_item

        Args:
          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_id: The ID of the counterparty receiving the invoice.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          due_date: A future date by when the invoice needs to be paid.

          invoicer_address: The invoice issuer's business address.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            body=maybe_transform(
                {
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_id": counterparty_id,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "due_date": due_date,
                    "invoicer_address": invoicer_address,
                    "originating_account_id": originating_account_id,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InvoiceLineItem]:
        """
        list invoice_line_items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def create(
        self,
        invoice_id: str,
        *,
        name: str,
        unit_amount: int,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/api/invoices/{invoice_id}/invoice_line_items",
            body=maybe_transform(
                {
                    "name": name,
                    "unit_amount": unit_amount,
                    "description": description,
                    "direction": direction,
                    "quantity": quantity,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceLineItem:
        """
        get invoice_line_item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        contact_details: List[line_item_update_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[line_item_update_params.CounterpartyBillingAddress]
        | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[line_item_update_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: shared_params.Currency | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[line_item_update_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItem:
        """
        update invoice_line_item

        Args:
          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_id: The ID of the counterparty receiving the invoice.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          due_date: A future date by when the invoice needs to be paid.

          invoicer_address: The invoice issuer's business address.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/api/invoices/{invoice_id}/invoice_line_items/{id}",
            body=maybe_transform(
                {
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_id": counterparty_id,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "due_date": due_date,
                    "invoicer_address": invoicer_address,
                    "originating_account_id": originating_account_id,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InvoiceLineItem, AsyncPage[InvoiceLineItem]]:
        """
        list invoice_line_items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
