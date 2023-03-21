# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..types import (
    PaymentFlow,
    payment_flow_list_params,
    payment_flow_create_params,
    payment_flow_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["PaymentFlows", "AsyncPaymentFlows"]


class PaymentFlows(SyncAPIResource):
    def create(
        self,
        *,
        amount: int,
        counterparty_id: str,
        currency: str,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/payment_flows",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "direction": direction,
                    "counterparty_id": counterparty_id,
                    "originating_account_id": originating_account_id,
                },
                payment_flow_create_params.PaymentFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
    ) -> PaymentFlow:
        """get payment_flow"""
        return self._get(
            f"/api/payment_flows/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/api/payment_flows/{id}",
            body=maybe_transform({"status": status}, payment_flow_update_params.PaymentFlowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
    ) -> SyncPage[PaymentFlow]:
        """
        list payment_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/payment_flows",
            page=SyncPage[PaymentFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "client_token": client_token,
                        "status": status,
                        "counterparty_id": counterparty_id,
                        "receiving_account_id": receiving_account_id,
                        "originating_account_id": originating_account_id,
                        "payment_order_id": payment_order_id,
                    },
                    payment_flow_list_params.PaymentFlowListParams,
                ),
            ),
            model=PaymentFlow,
        )


class AsyncPaymentFlows(AsyncAPIResource):
    async def create(
        self,
        *,
        amount: int,
        counterparty_id: str,
        currency: str,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/payment_flows",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "direction": direction,
                    "counterparty_id": counterparty_id,
                    "originating_account_id": originating_account_id,
                },
                payment_flow_create_params.PaymentFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
    ) -> PaymentFlow:
        """get payment_flow"""
        return await self._get(
            f"/api/payment_flows/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/api/payment_flows/{id}",
            body=maybe_transform({"status": status}, payment_flow_update_params.PaymentFlowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
    ) -> AsyncPaginator[PaymentFlow, AsyncPage[PaymentFlow]]:
        """
        list payment_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/payment_flows",
            page=AsyncPage[PaymentFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "client_token": client_token,
                        "status": status,
                        "counterparty_id": counterparty_id,
                        "receiving_account_id": receiving_account_id,
                        "originating_account_id": originating_account_id,
                        "payment_order_id": payment_order_id,
                    },
                    payment_flow_list_params.PaymentFlowListParams,
                ),
            ),
            model=PaymentFlow,
        )
