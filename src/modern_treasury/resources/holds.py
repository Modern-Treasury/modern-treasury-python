# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import hold_list_params, hold_create_params, hold_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.hold_list_response import HoldListResponse
from ..types.hold_create_response import HoldCreateResponse
from ..types.hold_update_response import HoldUpdateResponse
from ..types.hold_retrieve_response import HoldRetrieveResponse

__all__ = ["Holds", "AsyncHolds"]


class Holds(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return HoldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return HoldsWithStreamingResponse(self)

    def create(
        self,
        *,
        status: Literal["active"],
        target_id: str,
        target_type: Literal["payment_order"],
        metadata: Optional[Dict[str, str]] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> HoldCreateResponse:
        """
        Create a new hold

        Args:
          status: The status of the hold

          target_id: The ID of the target to hold

          target_type: The type of target to hold

          metadata: Additional metadata for the hold

          reason: The reason for the hold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/holds",
            body=maybe_transform(
                {
                    "status": status,
                    "target_id": target_id,
                    "target_type": target_type,
                    "metadata": metadata,
                    "reason": reason,
                },
                hold_create_params.HoldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=HoldCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HoldRetrieveResponse:
        """
        Get a specific hold

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/holds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HoldRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["resolved"],
        resolution: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> HoldUpdateResponse:
        """
        Update a hold

        Args:
          status: The new status of the hold

          resolution: The resolution of the hold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/holds/{id}",
            body=maybe_transform(
                {
                    "status": status,
                    "resolution": resolution,
                },
                hold_update_params.HoldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=HoldUpdateResponse,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        per_page: int | Omit = omit,
        status: Optional[Literal["active", "resolved"]] | Omit = omit,
        target_id: Optional[str] | Omit = omit,
        target_type: Optional[Literal["payment_order"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[HoldListResponse]:
        """
        Get a list of holds.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: Translation missing: en.openapi.descriptions.payment_order.query_params.status

          target_id:
              Translation missing:
              en.openapi.descriptions.payment_order.query_params.target_id

          target_type:
              Translation missing:
              en.openapi.descriptions.payment_order.query_params.target_type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/holds",
            page=SyncPage[HoldListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "target_id": target_id,
                        "target_type": target_type,
                    },
                    hold_list_params.HoldListParams,
                ),
            ),
            model=HoldListResponse,
        )


class AsyncHolds(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncHoldsWithStreamingResponse(self)

    async def create(
        self,
        *,
        status: Literal["active"],
        target_id: str,
        target_type: Literal["payment_order"],
        metadata: Optional[Dict[str, str]] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> HoldCreateResponse:
        """
        Create a new hold

        Args:
          status: The status of the hold

          target_id: The ID of the target to hold

          target_type: The type of target to hold

          metadata: Additional metadata for the hold

          reason: The reason for the hold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/holds",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "target_id": target_id,
                    "target_type": target_type,
                    "metadata": metadata,
                    "reason": reason,
                },
                hold_create_params.HoldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=HoldCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HoldRetrieveResponse:
        """
        Get a specific hold

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/holds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HoldRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["resolved"],
        resolution: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> HoldUpdateResponse:
        """
        Update a hold

        Args:
          status: The new status of the hold

          resolution: The resolution of the hold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/holds/{id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "resolution": resolution,
                },
                hold_update_params.HoldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=HoldUpdateResponse,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        per_page: int | Omit = omit,
        status: Optional[Literal["active", "resolved"]] | Omit = omit,
        target_id: Optional[str] | Omit = omit,
        target_type: Optional[Literal["payment_order"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[HoldListResponse, AsyncPage[HoldListResponse]]:
        """
        Get a list of holds.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: Translation missing: en.openapi.descriptions.payment_order.query_params.status

          target_id:
              Translation missing:
              en.openapi.descriptions.payment_order.query_params.target_id

          target_type:
              Translation missing:
              en.openapi.descriptions.payment_order.query_params.target_type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/holds",
            page=AsyncPage[HoldListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "target_id": target_id,
                        "target_type": target_type,
                    },
                    hold_list_params.HoldListParams,
                ),
            ),
            model=HoldListResponse,
        )


class HoldsWithRawResponse:
    def __init__(self, holds: Holds) -> None:
        self._holds = holds

        self.create = _legacy_response.to_raw_response_wrapper(
            holds.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            holds.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            holds.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            holds.list,
        )


class AsyncHoldsWithRawResponse:
    def __init__(self, holds: AsyncHolds) -> None:
        self._holds = holds

        self.create = _legacy_response.async_to_raw_response_wrapper(
            holds.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            holds.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            holds.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            holds.list,
        )


class HoldsWithStreamingResponse:
    def __init__(self, holds: Holds) -> None:
        self._holds = holds

        self.create = to_streamed_response_wrapper(
            holds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            holds.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            holds.update,
        )
        self.list = to_streamed_response_wrapper(
            holds.list,
        )


class AsyncHoldsWithStreamingResponse:
    def __init__(self, holds: AsyncHolds) -> None:
        self._holds = holds

        self.create = async_to_streamed_response_wrapper(
            holds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            holds.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            holds.update,
        )
        self.list = async_to_streamed_response_wrapper(
            holds.list,
        )
