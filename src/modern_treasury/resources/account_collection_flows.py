# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    AccountCollectionFlow,
    account_collection_flow_list_params,
    account_collection_flow_create_params,
    account_collection_flow_update_params,
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

__all__ = ["AccountCollectionFlows", "AsyncAccountCollectionFlows"]


class AccountCollectionFlows(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountCollectionFlowsWithRawResponse:
        return AccountCollectionFlowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountCollectionFlowsWithStreamingResponse:
        return AccountCollectionFlowsWithStreamingResponse(self)

    def create(
        self,
        *,
        counterparty_id: str,
        payment_types: List[str],
        receiving_countries: List[
            Literal[
                "USA",
                "AUS",
                "BEL",
                "CAN",
                "CHL",
                "CHN",
                "COL",
                "FRA",
                "DEU",
                "HKG",
                "IND",
                "IRL",
                "ITA",
                "MEX",
                "NLD",
                "PER",
                "ESP",
                "GBR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountCollectionFlow:
        """
        create account_collection_flow

        Args:
          counterparty_id: Required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/account_collection_flows",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "payment_types": payment_types,
                    "receiving_countries": receiving_countries,
                },
                account_collection_flow_create_params.AccountCollectionFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountCollectionFlow,
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
    ) -> AccountCollectionFlow:
        """
        get account_collection_flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/account_collection_flows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCollectionFlow,
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
    ) -> AccountCollectionFlow:
        """update account_collection_flow

        Args:
          status: Required.

        The updated status of the account collection flow. Can only be used to
              mark a flow as `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/account_collection_flows/{id}",
            body=maybe_transform(
                {"status": status}, account_collection_flow_update_params.AccountCollectionFlowUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountCollectionFlow,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        client_token: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[AccountCollectionFlow]:
        """
        list account_collection_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/account_collection_flows",
            page=SyncPage[AccountCollectionFlow],
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
                        "external_account_id": external_account_id,
                        "per_page": per_page,
                        "status": status,
                    },
                    account_collection_flow_list_params.AccountCollectionFlowListParams,
                ),
            ),
            model=AccountCollectionFlow,
        )


class AsyncAccountCollectionFlows(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountCollectionFlowsWithRawResponse:
        return AsyncAccountCollectionFlowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountCollectionFlowsWithStreamingResponse:
        return AsyncAccountCollectionFlowsWithStreamingResponse(self)

    async def create(
        self,
        *,
        counterparty_id: str,
        payment_types: List[str],
        receiving_countries: List[
            Literal[
                "USA",
                "AUS",
                "BEL",
                "CAN",
                "CHL",
                "CHN",
                "COL",
                "FRA",
                "DEU",
                "HKG",
                "IND",
                "IRL",
                "ITA",
                "MEX",
                "NLD",
                "PER",
                "ESP",
                "GBR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountCollectionFlow:
        """
        create account_collection_flow

        Args:
          counterparty_id: Required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/account_collection_flows",
            body=await async_maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "payment_types": payment_types,
                    "receiving_countries": receiving_countries,
                },
                account_collection_flow_create_params.AccountCollectionFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountCollectionFlow,
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
    ) -> AccountCollectionFlow:
        """
        get account_collection_flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/account_collection_flows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCollectionFlow,
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
    ) -> AccountCollectionFlow:
        """update account_collection_flow

        Args:
          status: Required.

        The updated status of the account collection flow. Can only be used to
              mark a flow as `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/account_collection_flows/{id}",
            body=await async_maybe_transform(
                {"status": status}, account_collection_flow_update_params.AccountCollectionFlowUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountCollectionFlow,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        client_token: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountCollectionFlow, AsyncPage[AccountCollectionFlow]]:
        """
        list account_collection_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/account_collection_flows",
            page=AsyncPage[AccountCollectionFlow],
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
                        "external_account_id": external_account_id,
                        "per_page": per_page,
                        "status": status,
                    },
                    account_collection_flow_list_params.AccountCollectionFlowListParams,
                ),
            ),
            model=AccountCollectionFlow,
        )


class AccountCollectionFlowsWithRawResponse:
    def __init__(self, account_collection_flows: AccountCollectionFlows) -> None:
        self._account_collection_flows = account_collection_flows

        self.create = _legacy_response.to_raw_response_wrapper(
            account_collection_flows.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            account_collection_flows.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            account_collection_flows.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            account_collection_flows.list,
        )


class AsyncAccountCollectionFlowsWithRawResponse:
    def __init__(self, account_collection_flows: AsyncAccountCollectionFlows) -> None:
        self._account_collection_flows = account_collection_flows

        self.create = _legacy_response.async_to_raw_response_wrapper(
            account_collection_flows.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            account_collection_flows.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            account_collection_flows.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            account_collection_flows.list,
        )


class AccountCollectionFlowsWithStreamingResponse:
    def __init__(self, account_collection_flows: AccountCollectionFlows) -> None:
        self._account_collection_flows = account_collection_flows

        self.create = to_streamed_response_wrapper(
            account_collection_flows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_collection_flows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            account_collection_flows.update,
        )
        self.list = to_streamed_response_wrapper(
            account_collection_flows.list,
        )


class AsyncAccountCollectionFlowsWithStreamingResponse:
    def __init__(self, account_collection_flows: AsyncAccountCollectionFlows) -> None:
        self._account_collection_flows = account_collection_flows

        self.create = async_to_streamed_response_wrapper(
            account_collection_flows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_collection_flows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            account_collection_flows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            account_collection_flows.list,
        )
