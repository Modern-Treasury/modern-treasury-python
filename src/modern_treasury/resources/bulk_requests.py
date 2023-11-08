# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

import httpx

from ..types import BulkRequest, bulk_request_list_params, bulk_request_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import ModernTreasury, AsyncModernTreasury

__all__ = ["BulkRequests", "AsyncBulkRequests"]


class BulkRequests(SyncAPIResource):
    with_raw_response: BulkRequestsWithRawResponse

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = BulkRequestsWithRawResponse(self)

    def create(
        self,
        *,
        action_type: Literal["create", "update"],
        resource_type: Literal["payment_order", "ledger_transaction", "expected_payment"],
        resources: List[bulk_request_create_params.Resource],
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BulkRequest:
        """
        create bulk_request

        Args:
          action_type: One of create, or update.

          resource_type: One of payment_order, expected_payment, or ledger_transaction.

          resources: An array of objects where each object contains the input params for a single
              `action_type` request on a `resource_type` resource

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/bulk_requests",
            body=maybe_transform(
                {
                    "action_type": action_type,
                    "resource_type": resource_type,
                    "resources": resources,
                    "metadata": metadata,
                },
                bulk_request_create_params.BulkRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BulkRequest,
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
    ) -> BulkRequest:
        """
        get bulk_request

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/bulk_requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRequest,
        )

    def list(
        self,
        *,
        action_type: Literal["create", "update"] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resource_type: Literal["payment_order", "ledger_transaction", "expected_payment"] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "processing", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BulkRequest]:
        """
        list bulk_requests

        Args:
          action_type: One of create, or update.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          resource_type: One of payment_order, expected_payment, or ledger_transaction.

          status: One of pending, processing, or completed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/bulk_requests",
            page=SyncPage[BulkRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_type": action_type,
                        "after_cursor": after_cursor,
                        "metadata": metadata,
                        "per_page": per_page,
                        "resource_type": resource_type,
                        "status": status,
                    },
                    bulk_request_list_params.BulkRequestListParams,
                ),
            ),
            model=BulkRequest,
        )


class AsyncBulkRequests(AsyncAPIResource):
    with_raw_response: AsyncBulkRequestsWithRawResponse

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncBulkRequestsWithRawResponse(self)

    async def create(
        self,
        *,
        action_type: Literal["create", "update"],
        resource_type: Literal["payment_order", "ledger_transaction", "expected_payment"],
        resources: List[bulk_request_create_params.Resource],
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BulkRequest:
        """
        create bulk_request

        Args:
          action_type: One of create, or update.

          resource_type: One of payment_order, expected_payment, or ledger_transaction.

          resources: An array of objects where each object contains the input params for a single
              `action_type` request on a `resource_type` resource

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/bulk_requests",
            body=maybe_transform(
                {
                    "action_type": action_type,
                    "resource_type": resource_type,
                    "resources": resources,
                    "metadata": metadata,
                },
                bulk_request_create_params.BulkRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BulkRequest,
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
    ) -> BulkRequest:
        """
        get bulk_request

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/bulk_requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRequest,
        )

    def list(
        self,
        *,
        action_type: Literal["create", "update"] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resource_type: Literal["payment_order", "ledger_transaction", "expected_payment"] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "processing", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BulkRequest, AsyncPage[BulkRequest]]:
        """
        list bulk_requests

        Args:
          action_type: One of create, or update.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          resource_type: One of payment_order, expected_payment, or ledger_transaction.

          status: One of pending, processing, or completed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/bulk_requests",
            page=AsyncPage[BulkRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_type": action_type,
                        "after_cursor": after_cursor,
                        "metadata": metadata,
                        "per_page": per_page,
                        "resource_type": resource_type,
                        "status": status,
                    },
                    bulk_request_list_params.BulkRequestListParams,
                ),
            ),
            model=BulkRequest,
        )


class BulkRequestsWithRawResponse:
    def __init__(self, bulk_requests: BulkRequests) -> None:
        self.create = to_raw_response_wrapper(
            bulk_requests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bulk_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bulk_requests.list,
        )


class AsyncBulkRequestsWithRawResponse:
    def __init__(self, bulk_requests: AsyncBulkRequests) -> None:
        self.create = async_to_raw_response_wrapper(
            bulk_requests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bulk_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bulk_requests.list,
        )
