# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    PaymentFlow,
    payment_flow_list_params,
    payment_flow_create_params,
    payment_flow_update_params,
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

__all__ = ["PaymentFlows", "AsyncPaymentFlows"]


class PaymentFlows(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentFlowsWithRawResponse:
        return PaymentFlowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentFlowsWithStreamingResponse:
        return PaymentFlowsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        counterparty_id: str,
        currency: str,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentFlow:
        """create payment_flow

        Args:
          amount: Required.

        Value in specified currency's smallest unit. e.g. $10 would be
              represented as 1000. Can be any integer up to 36 digits.

          counterparty_id: Required. The ID of a counterparty associated with the payment. As part of the
              payment workflow an external account will be associated with this model.

          currency: Required. The currency of the payment.

          direction: Required. Describes the direction money is flowing in the transaction. Can only
              be `debit`. A `debit` pulls money from someone else's account to your own.

          originating_account_id: Required. The ID of one of your organization's internal accounts.

          due_date: Optional. Can only be passed in when `effective_date_selection_enabled` is
              `true`. When set, the due date is shown to your end-user in the pre-built UI as
              they are selecting a payment `effective_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/payment_flows",
            body=maybe_transform(
                {
                    "amount": amount,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "direction": direction,
                    "originating_account_id": originating_account_id,
                    "due_date": due_date,
                },
                payment_flow_create_params.PaymentFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentFlow,
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
    ) -> PaymentFlow:
        """
        get payment_flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/payment_flows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlow,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentFlow:
        """update payment_flow

        Args:
          status: Required.

        The updated status of the payment flow. Can only be used to mark a
              flow as `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/payment_flows/{id}",
            body=maybe_transform({"status": status}, payment_flow_update_params.PaymentFlowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentFlow,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        client_token: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_order_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PaymentFlow]:
        """
        list payment_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_flows",
            page=SyncPage[PaymentFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "client_token": client_token,
                        "counterparty_id": counterparty_id,
                        "originating_account_id": originating_account_id,
                        "payment_order_id": payment_order_id,
                        "per_page": per_page,
                        "receiving_account_id": receiving_account_id,
                        "status": status,
                    },
                    payment_flow_list_params.PaymentFlowListParams,
                ),
            ),
            model=PaymentFlow,
        )


class AsyncPaymentFlows(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentFlowsWithRawResponse:
        return AsyncPaymentFlowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentFlowsWithStreamingResponse:
        return AsyncPaymentFlowsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        counterparty_id: str,
        currency: str,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentFlow:
        """create payment_flow

        Args:
          amount: Required.

        Value in specified currency's smallest unit. e.g. $10 would be
              represented as 1000. Can be any integer up to 36 digits.

          counterparty_id: Required. The ID of a counterparty associated with the payment. As part of the
              payment workflow an external account will be associated with this model.

          currency: Required. The currency of the payment.

          direction: Required. Describes the direction money is flowing in the transaction. Can only
              be `debit`. A `debit` pulls money from someone else's account to your own.

          originating_account_id: Required. The ID of one of your organization's internal accounts.

          due_date: Optional. Can only be passed in when `effective_date_selection_enabled` is
              `true`. When set, the due date is shown to your end-user in the pre-built UI as
              they are selecting a payment `effective_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/payment_flows",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "direction": direction,
                    "originating_account_id": originating_account_id,
                    "due_date": due_date,
                },
                payment_flow_create_params.PaymentFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentFlow,
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
    ) -> PaymentFlow:
        """
        get payment_flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/payment_flows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlow,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentFlow:
        """update payment_flow

        Args:
          status: Required.

        The updated status of the payment flow. Can only be used to mark a
              flow as `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/payment_flows/{id}",
            body=await async_maybe_transform({"status": status}, payment_flow_update_params.PaymentFlowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentFlow,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        client_token: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_order_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PaymentFlow, AsyncPage[PaymentFlow]]:
        """
        list payment_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_flows",
            page=AsyncPage[PaymentFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "client_token": client_token,
                        "counterparty_id": counterparty_id,
                        "originating_account_id": originating_account_id,
                        "payment_order_id": payment_order_id,
                        "per_page": per_page,
                        "receiving_account_id": receiving_account_id,
                        "status": status,
                    },
                    payment_flow_list_params.PaymentFlowListParams,
                ),
            ),
            model=PaymentFlow,
        )


class PaymentFlowsWithRawResponse:
    def __init__(self, payment_flows: PaymentFlows) -> None:
        self._payment_flows = payment_flows

        self.create = _legacy_response.to_raw_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            payment_flows.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            payment_flows.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            payment_flows.list,
        )


class AsyncPaymentFlowsWithRawResponse:
    def __init__(self, payment_flows: AsyncPaymentFlows) -> None:
        self._payment_flows = payment_flows

        self.create = _legacy_response.async_to_raw_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            payment_flows.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            payment_flows.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            payment_flows.list,
        )


class PaymentFlowsWithStreamingResponse:
    def __init__(self, payment_flows: PaymentFlows) -> None:
        self._payment_flows = payment_flows

        self.create = to_streamed_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_flows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            payment_flows.update,
        )
        self.list = to_streamed_response_wrapper(
            payment_flows.list,
        )


class AsyncPaymentFlowsWithStreamingResponse:
    def __init__(self, payment_flows: AsyncPaymentFlows) -> None:
        self._payment_flows = payment_flows

        self.create = async_to_streamed_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_flows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            payment_flows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_flows.list,
        )
