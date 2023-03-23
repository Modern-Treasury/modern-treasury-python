# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..types import (
    AccountConnectionFlow,
    account_collection_flow_list_params,
    account_collection_flow_create_params,
    account_collection_flow_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["AccountCollectionFlows", "AsyncAccountCollectionFlows"]


class AccountCollectionFlows(SyncAPIResource):
    def create(
        self,
        *,
        counterparty_id: str,
        payment_types: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> AccountConnectionFlow:
        """
        create account_collection_flow

        Args:
          counterparty_id: Required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/account_collection_flows",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "payment_types": payment_types,
                },
                account_collection_flow_create_params.AccountCollectionFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountConnectionFlow,
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
    ) -> AccountConnectionFlow:
        """get account_collection_flow"""
        return self._get(
            f"/api/account_collection_flows/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountConnectionFlow,
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
    ) -> AccountConnectionFlow:
        """update account_collection_flow

        Args:
          status: Required.

        The updated status of the account collection flow. Can only be used to
              mark a flow as `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/api/account_collection_flows/{id}",
            body=maybe_transform(
                {"status": status}, account_collection_flow_update_params.AccountCollectionFlowUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountConnectionFlow,
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
    ) -> SyncPage[AccountConnectionFlow]:
        """
        list account_collection_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/account_collection_flows",
            page=SyncPage[AccountConnectionFlow],
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
                        "external_account_id": external_account_id,
                    },
                    account_collection_flow_list_params.AccountCollectionFlowListParams,
                ),
            ),
            model=AccountConnectionFlow,
        )


class AsyncAccountCollectionFlows(AsyncAPIResource):
    async def create(
        self,
        *,
        counterparty_id: str,
        payment_types: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> AccountConnectionFlow:
        """
        create account_collection_flow

        Args:
          counterparty_id: Required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/account_collection_flows",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "payment_types": payment_types,
                },
                account_collection_flow_create_params.AccountCollectionFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountConnectionFlow,
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
    ) -> AccountConnectionFlow:
        """get account_collection_flow"""
        return await self._get(
            f"/api/account_collection_flows/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountConnectionFlow,
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
    ) -> AccountConnectionFlow:
        """update account_collection_flow

        Args:
          status: Required.

        The updated status of the account collection flow. Can only be used to
              mark a flow as `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/api/account_collection_flows/{id}",
            body=maybe_transform(
                {"status": status}, account_collection_flow_update_params.AccountCollectionFlowUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountConnectionFlow,
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
    ) -> AsyncPaginator[AccountConnectionFlow, AsyncPage[AccountConnectionFlow]]:
        """
        list account_collection_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/account_collection_flows",
            page=AsyncPage[AccountConnectionFlow],
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
                        "external_account_id": external_account_id,
                    },
                    account_collection_flow_list_params.AccountCollectionFlowListParams,
                ),
            ),
            model=AccountConnectionFlow,
        )
