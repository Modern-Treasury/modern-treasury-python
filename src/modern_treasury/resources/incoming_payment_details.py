# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    IncomingPaymentDetail,
    incoming_payment_detail_list_params,
    incoming_payment_detail_update_params,
    incoming_payment_detail_create_async_params,
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
from ..types.shared import Currency, AsyncResponse, TransactionDirection

__all__ = ["IncomingPaymentDetails", "AsyncIncomingPaymentDetails"]


class IncomingPaymentDetails(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncomingPaymentDetailsWithRawResponse:
        return IncomingPaymentDetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncomingPaymentDetailsWithStreamingResponse:
        return IncomingPaymentDetailsWithStreamingResponse(self)

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
    ) -> IncomingPaymentDetail:
        """
        Get an existing Incoming Payment Detail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/incoming_payment_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IncomingPaymentDetail,
        )

    def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IncomingPaymentDetail:
        """
        Update an existing Incoming Payment Detail.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/incoming_payment_details/{id}",
            body=maybe_transform(
                {"metadata": metadata}, incoming_payment_detail_update_params.IncomingPaymentDetailUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IncomingPaymentDetail,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        as_of_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        direction: TransactionDirection | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["completed", "pending", "returned"] | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[IncomingPaymentDetail]:
        """
        Get a list of Incoming Payment Details.

        Args:
          as_of_date_end: Filters incoming payment details with an as_of_date starting on or before the
              specified date (YYYY-MM-DD).

          as_of_date_start: Filters incoming payment details with an as_of_date starting on or after the
              specified date (YYYY-MM-DD).

          direction: One of `credit` or `debit`.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: The current status of the incoming payment order. One of `pending`, `completed`,
              or `returned`.

          type: One of: `ach`, `book`, `check`, `eft`, `interac`, `rtp`, `sepa`, `signet`, or
              `wire`.

          virtual_account_id: If the incoming payment detail is in a virtual account, the ID of the Virtual
              Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/incoming_payment_details",
            page=SyncPage[IncomingPaymentDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date_end": as_of_date_end,
                        "as_of_date_start": as_of_date_start,
                        "direction": direction,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                        "virtual_account_id": virtual_account_id,
                    },
                    incoming_payment_detail_list_params.IncomingPaymentDetailListParams,
                ),
            ),
            model=IncomingPaymentDetail,
        )

    def create_async(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        as_of_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AsyncResponse:
        """
        Simulate Incoming Payment Detail

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          as_of_date: Defaults to today.

          currency: Defaults to the currency of the originating account.

          description: Defaults to a random description.

          direction: One of `credit`, `debit`.

          internal_account_id: The ID of one of your internal accounts.

          type: One of `ach`, `wire`, `check`.

          virtual_account_id: An optional parameter to associate the incoming payment detail to a virtual
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/simulations/incoming_payment_details/create_async",
            body=maybe_transform(
                {
                    "amount": amount,
                    "as_of_date": as_of_date,
                    "currency": currency,
                    "description": description,
                    "direction": direction,
                    "internal_account_id": internal_account_id,
                    "type": type,
                    "virtual_account_id": virtual_account_id,
                },
                incoming_payment_detail_create_async_params.IncomingPaymentDetailCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AsyncResponse,
        )


class AsyncIncomingPaymentDetails(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncomingPaymentDetailsWithRawResponse:
        return AsyncIncomingPaymentDetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncomingPaymentDetailsWithStreamingResponse:
        return AsyncIncomingPaymentDetailsWithStreamingResponse(self)

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
    ) -> IncomingPaymentDetail:
        """
        Get an existing Incoming Payment Detail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/incoming_payment_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IncomingPaymentDetail,
        )

    async def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IncomingPaymentDetail:
        """
        Update an existing Incoming Payment Detail.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/incoming_payment_details/{id}",
            body=await async_maybe_transform(
                {"metadata": metadata}, incoming_payment_detail_update_params.IncomingPaymentDetailUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IncomingPaymentDetail,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        as_of_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        direction: TransactionDirection | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["completed", "pending", "returned"] | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IncomingPaymentDetail, AsyncPage[IncomingPaymentDetail]]:
        """
        Get a list of Incoming Payment Details.

        Args:
          as_of_date_end: Filters incoming payment details with an as_of_date starting on or before the
              specified date (YYYY-MM-DD).

          as_of_date_start: Filters incoming payment details with an as_of_date starting on or after the
              specified date (YYYY-MM-DD).

          direction: One of `credit` or `debit`.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: The current status of the incoming payment order. One of `pending`, `completed`,
              or `returned`.

          type: One of: `ach`, `book`, `check`, `eft`, `interac`, `rtp`, `sepa`, `signet`, or
              `wire`.

          virtual_account_id: If the incoming payment detail is in a virtual account, the ID of the Virtual
              Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/incoming_payment_details",
            page=AsyncPage[IncomingPaymentDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date_end": as_of_date_end,
                        "as_of_date_start": as_of_date_start,
                        "direction": direction,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                        "virtual_account_id": virtual_account_id,
                    },
                    incoming_payment_detail_list_params.IncomingPaymentDetailListParams,
                ),
            ),
            model=IncomingPaymentDetail,
        )

    async def create_async(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        as_of_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AsyncResponse:
        """
        Simulate Incoming Payment Detail

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          as_of_date: Defaults to today.

          currency: Defaults to the currency of the originating account.

          description: Defaults to a random description.

          direction: One of `credit`, `debit`.

          internal_account_id: The ID of one of your internal accounts.

          type: One of `ach`, `wire`, `check`.

          virtual_account_id: An optional parameter to associate the incoming payment detail to a virtual
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/simulations/incoming_payment_details/create_async",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "as_of_date": as_of_date,
                    "currency": currency,
                    "description": description,
                    "direction": direction,
                    "internal_account_id": internal_account_id,
                    "type": type,
                    "virtual_account_id": virtual_account_id,
                },
                incoming_payment_detail_create_async_params.IncomingPaymentDetailCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AsyncResponse,
        )


class IncomingPaymentDetailsWithRawResponse:
    def __init__(self, incoming_payment_details: IncomingPaymentDetails) -> None:
        self._incoming_payment_details = incoming_payment_details

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            incoming_payment_details.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            incoming_payment_details.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            incoming_payment_details.list,
        )
        self.create_async = _legacy_response.to_raw_response_wrapper(
            incoming_payment_details.create_async,
        )


class AsyncIncomingPaymentDetailsWithRawResponse:
    def __init__(self, incoming_payment_details: AsyncIncomingPaymentDetails) -> None:
        self._incoming_payment_details = incoming_payment_details

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            incoming_payment_details.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            incoming_payment_details.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            incoming_payment_details.list,
        )
        self.create_async = _legacy_response.async_to_raw_response_wrapper(
            incoming_payment_details.create_async,
        )


class IncomingPaymentDetailsWithStreamingResponse:
    def __init__(self, incoming_payment_details: IncomingPaymentDetails) -> None:
        self._incoming_payment_details = incoming_payment_details

        self.retrieve = to_streamed_response_wrapper(
            incoming_payment_details.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            incoming_payment_details.update,
        )
        self.list = to_streamed_response_wrapper(
            incoming_payment_details.list,
        )
        self.create_async = to_streamed_response_wrapper(
            incoming_payment_details.create_async,
        )


class AsyncIncomingPaymentDetailsWithStreamingResponse:
    def __init__(self, incoming_payment_details: AsyncIncomingPaymentDetails) -> None:
        self._incoming_payment_details = incoming_payment_details

        self.retrieve = async_to_streamed_response_wrapper(
            incoming_payment_details.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            incoming_payment_details.update,
        )
        self.list = async_to_streamed_response_wrapper(
            incoming_payment_details.list,
        )
        self.create_async = async_to_streamed_response_wrapper(
            incoming_payment_details.create_async,
        )
