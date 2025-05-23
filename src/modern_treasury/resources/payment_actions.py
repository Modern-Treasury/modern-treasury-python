# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import payment_action_list_params, payment_action_create_params, payment_action_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.payment_action_list_response import PaymentActionListResponse
from ..types.payment_action_create_response import PaymentActionCreateResponse
from ..types.payment_action_update_response import PaymentActionUpdateResponse
from ..types.payment_action_retrieve_response import PaymentActionRetrieveResponse

__all__ = ["PaymentActions", "AsyncPaymentActions"]


class PaymentActions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentActionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return PaymentActionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentActionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return PaymentActionsWithStreamingResponse(self)

    def create(
        self,
        *,
        type: str,
        actionable_id: str | NotGiven = NOT_GIVEN,
        actionable_type: str | NotGiven = NOT_GIVEN,
        details: object | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentActionCreateResponse:
        """Create a payment action.

        Args:
          type: Required.

        The type of the payment action. Determines the action to be taken.

          actionable_id: Optional. The ID of the associated actionable object.

          actionable_type: Optional. The type of the associated actionable object. One of `payment_order`,
              `expected_payment`. Required if `actionable_id` is passed.

          details: Optional. The specifc details of the payment action based on type.

          internal_account_id: Optional. The ID of one of your organization's internal accounts. Required if
              `actionable_id` is not passed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/payment_actions",
            body=maybe_transform(
                {
                    "type": type,
                    "actionable_id": actionable_id,
                    "actionable_type": actionable_type,
                    "details": details,
                    "internal_account_id": internal_account_id,
                },
                payment_action_create_params.PaymentActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentActionCreateResponse,
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
    ) -> PaymentActionRetrieveResponse:
        """
        Get details on a single payment action.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/payment_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentActionRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["pending", "processable", "processing", "sent", "failed", "cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentActionUpdateResponse:
        """Update a single payment action.

        Args:
          status: Optional.

        Set the status of the payment action to `cancelled` to cancel the
              payment action. This will only work if the payment action is in a `pending`
              state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/payment_actions/{id}",
            body=maybe_transform({"status": status}, payment_action_update_params.PaymentActionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentActionUpdateResponse,
        )

    def list(
        self,
        *,
        actionable_id: str | NotGiven = NOT_GIVEN,
        actionable_type: str | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: payment_action_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["pending", "processable", "processing", "sent", "failed", "cancelled"] | NotGiven = NOT_GIVEN,
        type: Literal["stop", "issue"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PaymentActionListResponse]:
        """
        Get a list of all payment actions.

        Args:
          actionable_id: The ID of the associated actionable object.

          actionable_type: The type of the associated actionable object. One of `payment_order`,
              `expected_payment`.

          created_at: Filter by `created_at` using comparison operators like `gt` (>), `gte` (>=),
              `lt` (<), `lte` (<=), or `eq` (=) to filter by the created at timestamp. For
              example, `created_at[gte]=2024-01-01T00:00:00Z`

          internal_account_id: The ID of one of your internal accounts.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: Filter by payment actions of a specific status.

          type: The type of payment action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_actions",
            page=SyncPage[PaymentActionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actionable_id": actionable_id,
                        "actionable_type": actionable_type,
                        "after_cursor": after_cursor,
                        "created_at": created_at,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                    },
                    payment_action_list_params.PaymentActionListParams,
                ),
            ),
            model=PaymentActionListResponse,
        )


class AsyncPaymentActions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentActionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentActionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentActionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncPaymentActionsWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: str,
        actionable_id: str | NotGiven = NOT_GIVEN,
        actionable_type: str | NotGiven = NOT_GIVEN,
        details: object | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentActionCreateResponse:
        """Create a payment action.

        Args:
          type: Required.

        The type of the payment action. Determines the action to be taken.

          actionable_id: Optional. The ID of the associated actionable object.

          actionable_type: Optional. The type of the associated actionable object. One of `payment_order`,
              `expected_payment`. Required if `actionable_id` is passed.

          details: Optional. The specifc details of the payment action based on type.

          internal_account_id: Optional. The ID of one of your organization's internal accounts. Required if
              `actionable_id` is not passed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/payment_actions",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "actionable_id": actionable_id,
                    "actionable_type": actionable_type,
                    "details": details,
                    "internal_account_id": internal_account_id,
                },
                payment_action_create_params.PaymentActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentActionCreateResponse,
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
    ) -> PaymentActionRetrieveResponse:
        """
        Get details on a single payment action.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/payment_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentActionRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["pending", "processable", "processing", "sent", "failed", "cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentActionUpdateResponse:
        """Update a single payment action.

        Args:
          status: Optional.

        Set the status of the payment action to `cancelled` to cancel the
              payment action. This will only work if the payment action is in a `pending`
              state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/payment_actions/{id}",
            body=await async_maybe_transform(
                {"status": status}, payment_action_update_params.PaymentActionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentActionUpdateResponse,
        )

    def list(
        self,
        *,
        actionable_id: str | NotGiven = NOT_GIVEN,
        actionable_type: str | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: payment_action_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["pending", "processable", "processing", "sent", "failed", "cancelled"] | NotGiven = NOT_GIVEN,
        type: Literal["stop", "issue"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PaymentActionListResponse, AsyncPage[PaymentActionListResponse]]:
        """
        Get a list of all payment actions.

        Args:
          actionable_id: The ID of the associated actionable object.

          actionable_type: The type of the associated actionable object. One of `payment_order`,
              `expected_payment`.

          created_at: Filter by `created_at` using comparison operators like `gt` (>), `gte` (>=),
              `lt` (<), `lte` (<=), or `eq` (=) to filter by the created at timestamp. For
              example, `created_at[gte]=2024-01-01T00:00:00Z`

          internal_account_id: The ID of one of your internal accounts.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: Filter by payment actions of a specific status.

          type: The type of payment action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_actions",
            page=AsyncPage[PaymentActionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actionable_id": actionable_id,
                        "actionable_type": actionable_type,
                        "after_cursor": after_cursor,
                        "created_at": created_at,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                    },
                    payment_action_list_params.PaymentActionListParams,
                ),
            ),
            model=PaymentActionListResponse,
        )


class PaymentActionsWithRawResponse:
    def __init__(self, payment_actions: PaymentActions) -> None:
        self._payment_actions = payment_actions

        self.create = _legacy_response.to_raw_response_wrapper(
            payment_actions.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            payment_actions.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            payment_actions.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            payment_actions.list,
        )


class AsyncPaymentActionsWithRawResponse:
    def __init__(self, payment_actions: AsyncPaymentActions) -> None:
        self._payment_actions = payment_actions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            payment_actions.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            payment_actions.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            payment_actions.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            payment_actions.list,
        )


class PaymentActionsWithStreamingResponse:
    def __init__(self, payment_actions: PaymentActions) -> None:
        self._payment_actions = payment_actions

        self.create = to_streamed_response_wrapper(
            payment_actions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_actions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            payment_actions.update,
        )
        self.list = to_streamed_response_wrapper(
            payment_actions.list,
        )


class AsyncPaymentActionsWithStreamingResponse:
    def __init__(self, payment_actions: AsyncPaymentActions) -> None:
        self._payment_actions = payment_actions

        self.create = async_to_streamed_response_wrapper(
            payment_actions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_actions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            payment_actions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_actions.list,
        )
