# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    payment_request_list_params,
    payment_request_update_params,
    payment_request_simulate_params,
    payment_request_cancel_simulation_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.payment_request import PaymentRequest

__all__ = ["PaymentRequests", "AsyncPaymentRequests"]


class PaymentRequests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentRequestsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return PaymentRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentRequestsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return PaymentRequestsWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Gets an incoming wire drawdown request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/payment_requests/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["approved", "declined"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentRequest:
        """
        Approves or declines a pending wire drawdown request.

        Args:
          status: Approve the request and create a wire payment order, or decline the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/api/payment_requests/{id}", id=id),
            body=maybe_transform({"status": status}, payment_request_update_params.PaymentRequestUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentRequest,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        after_cursor: Optional[str] | Omit = omit,
        created_at_end: Union[str, datetime] | Omit = omit,
        created_at_start: Union[str, datetime] | Omit = omit,
        internal_account_id: str | Omit = omit,
        payment_type: Literal["wire"] | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["approved", "cancelled", "declined", "pending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PaymentRequest]:
        """
        Lists incoming wire drawdown requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_requests",
            page=SyncPage[PaymentRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "internal_account_id": internal_account_id,
                        "payment_type": payment_type,
                        "per_page": per_page,
                        "status": status,
                    },
                    payment_request_list_params.PaymentRequestListParams,
                ),
            ),
            model=PaymentRequest,
        )

    def cancel_simulation(
        self,
        id: str,
        *,
        status: Literal["cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentRequest:
        """
        Simulates cancellation of a pending wire drawdown request in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/api/simulations/payment_requests/{id}", id=id),
            body=maybe_transform(
                {"status": status}, payment_request_cancel_simulation_params.PaymentRequestCancelSimulationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentRequest,
        )

    def simulate(
        self,
        *,
        amount: int,
        internal_account_id: str,
        requesting_account_number: str,
        requesting_party_name: str,
        requesting_routing_number: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentRequest:
        """
        Simulates receiving a wire drawdown request in sandbox.

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          description: An optional description for internal use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/simulations/payment_requests",
            body=maybe_transform(
                {
                    "amount": amount,
                    "internal_account_id": internal_account_id,
                    "requesting_account_number": requesting_account_number,
                    "requesting_party_name": requesting_party_name,
                    "requesting_routing_number": requesting_routing_number,
                    "description": description,
                },
                payment_request_simulate_params.PaymentRequestSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentRequest,
        )


class AsyncPaymentRequests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentRequestsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentRequestsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncPaymentRequestsWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Gets an incoming wire drawdown request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/payment_requests/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["approved", "declined"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentRequest:
        """
        Approves or declines a pending wire drawdown request.

        Args:
          status: Approve the request and create a wire payment order, or decline the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/api/payment_requests/{id}", id=id),
            body=await async_maybe_transform(
                {"status": status}, payment_request_update_params.PaymentRequestUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentRequest,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        after_cursor: Optional[str] | Omit = omit,
        created_at_end: Union[str, datetime] | Omit = omit,
        created_at_start: Union[str, datetime] | Omit = omit,
        internal_account_id: str | Omit = omit,
        payment_type: Literal["wire"] | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["approved", "cancelled", "declined", "pending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentRequest, AsyncPage[PaymentRequest]]:
        """
        Lists incoming wire drawdown requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_requests",
            page=AsyncPage[PaymentRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "internal_account_id": internal_account_id,
                        "payment_type": payment_type,
                        "per_page": per_page,
                        "status": status,
                    },
                    payment_request_list_params.PaymentRequestListParams,
                ),
            ),
            model=PaymentRequest,
        )

    async def cancel_simulation(
        self,
        id: str,
        *,
        status: Literal["cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentRequest:
        """
        Simulates cancellation of a pending wire drawdown request in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/api/simulations/payment_requests/{id}", id=id),
            body=await async_maybe_transform(
                {"status": status}, payment_request_cancel_simulation_params.PaymentRequestCancelSimulationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentRequest,
        )

    async def simulate(
        self,
        *,
        amount: int,
        internal_account_id: str,
        requesting_account_number: str,
        requesting_party_name: str,
        requesting_routing_number: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentRequest:
        """
        Simulates receiving a wire drawdown request in sandbox.

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          description: An optional description for internal use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/simulations/payment_requests",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "internal_account_id": internal_account_id,
                    "requesting_account_number": requesting_account_number,
                    "requesting_party_name": requesting_party_name,
                    "requesting_routing_number": requesting_routing_number,
                    "description": description,
                },
                payment_request_simulate_params.PaymentRequestSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentRequest,
        )


class PaymentRequestsWithRawResponse:
    def __init__(self, payment_requests: PaymentRequests) -> None:
        self._payment_requests = payment_requests

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            payment_requests.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            payment_requests.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            payment_requests.list,
        )
        self.cancel_simulation = _legacy_response.to_raw_response_wrapper(
            payment_requests.cancel_simulation,
        )
        self.simulate = _legacy_response.to_raw_response_wrapper(
            payment_requests.simulate,
        )


class AsyncPaymentRequestsWithRawResponse:
    def __init__(self, payment_requests: AsyncPaymentRequests) -> None:
        self._payment_requests = payment_requests

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            payment_requests.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            payment_requests.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            payment_requests.list,
        )
        self.cancel_simulation = _legacy_response.async_to_raw_response_wrapper(
            payment_requests.cancel_simulation,
        )
        self.simulate = _legacy_response.async_to_raw_response_wrapper(
            payment_requests.simulate,
        )


class PaymentRequestsWithStreamingResponse:
    def __init__(self, payment_requests: PaymentRequests) -> None:
        self._payment_requests = payment_requests

        self.retrieve = to_streamed_response_wrapper(
            payment_requests.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            payment_requests.update,
        )
        self.list = to_streamed_response_wrapper(
            payment_requests.list,
        )
        self.cancel_simulation = to_streamed_response_wrapper(
            payment_requests.cancel_simulation,
        )
        self.simulate = to_streamed_response_wrapper(
            payment_requests.simulate,
        )


class AsyncPaymentRequestsWithStreamingResponse:
    def __init__(self, payment_requests: AsyncPaymentRequests) -> None:
        self._payment_requests = payment_requests

        self.retrieve = async_to_streamed_response_wrapper(
            payment_requests.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            payment_requests.update,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_requests.list,
        )
        self.cancel_simulation = async_to_streamed_response_wrapper(
            payment_requests.cancel_simulation,
        )
        self.simulate = async_to_streamed_response_wrapper(
            payment_requests.simulate,
        )
