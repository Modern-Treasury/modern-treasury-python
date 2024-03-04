# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import typing_extensions
from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    LedgerAccountPayout,
    ledger_account_payout_list_params,
    ledger_account_payout_create_params,
    ledger_account_payout_update_params,
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

__all__ = ["LedgerAccountPayouts", "AsyncLedgerAccountPayouts"]


class LedgerAccountPayouts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerAccountPayoutsWithRawResponse:
        return LedgerAccountPayoutsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerAccountPayoutsWithStreamingResponse:
        return LedgerAccountPayoutsWithStreamingResponse(self)

    def create(
        self,
        *,
        funding_ledger_account_id: str,
        payout_ledger_account_id: str,
        allow_either_direction: Optional[bool] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at_upper_bound: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        skip_payout_ledger_transaction: Optional[bool] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["pending", "posted"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountPayout:
        """
        Create a ledger account payout.

        Args:
          funding_ledger_account_id: The id of the funding ledger account that sends to or receives funds from the
              payout ledger account.

          payout_ledger_account_id: The id of the payout ledger account whose ledger entries are queried against,
              and its balance is reduced as a result.

          allow_either_direction: If true, the payout amount and payout_entry_direction will bring the payout
              ledger account's balance closer to zero, even if the balance is negative.

          description: The description of the ledger account payout.

          effective_at_upper_bound: The exclusive upper bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account payout. The default value is the created_at
              timestamp of the ledger account payout.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          skip_payout_ledger_transaction: It is set to `false` by default. It should be set to `true` when migrating
              existing payouts.

          status: The status of the ledger account payout. It is set to `pending` by default. To
              post a ledger account payout at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_account_payouts",
            body=maybe_transform(
                {
                    "funding_ledger_account_id": funding_ledger_account_id,
                    "payout_ledger_account_id": payout_ledger_account_id,
                    "allow_either_direction": allow_either_direction,
                    "description": description,
                    "effective_at_upper_bound": effective_at_upper_bound,
                    "metadata": metadata,
                    "skip_payout_ledger_transaction": skip_payout_ledger_transaction,
                    "status": status,
                },
                ledger_account_payout_create_params.LedgerAccountPayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountPayout,
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
    ) -> LedgerAccountPayout:
        """
        Get details on a single ledger account payout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_account_payouts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountPayout,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["posted", "archived"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountPayout:
        """
        Update the details of a ledger account payout.

        Args:
          description: The description of the ledger account payout.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a pending ledger account payout, use `posted`. To archive a pending
              ledger transaction, use `archived`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/ledger_account_payouts/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_account_payout_update_params.LedgerAccountPayoutUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountPayout,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payout_entry_direction: str | NotGiven = NOT_GIVEN,
        payout_ledger_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerAccountPayout]:
        """
        Get a list of ledger account payouts.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_account_payouts",
            page=SyncPage[LedgerAccountPayout],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "metadata": metadata,
                        "payout_entry_direction": payout_entry_direction,
                        "payout_ledger_account_id": payout_ledger_account_id,
                        "per_page": per_page,
                    },
                    ledger_account_payout_list_params.LedgerAccountPayoutListParams,
                ),
            ),
            model=LedgerAccountPayout,
        )

    @typing_extensions.deprecated("use `retrieve` instead")
    def retireve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccountPayout:
        """
        Get details on a single ledger account payout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.retrieve(
            id=id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )


class AsyncLedgerAccountPayouts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerAccountPayoutsWithRawResponse:
        return AsyncLedgerAccountPayoutsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerAccountPayoutsWithStreamingResponse:
        return AsyncLedgerAccountPayoutsWithStreamingResponse(self)

    async def create(
        self,
        *,
        funding_ledger_account_id: str,
        payout_ledger_account_id: str,
        allow_either_direction: Optional[bool] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at_upper_bound: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        skip_payout_ledger_transaction: Optional[bool] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["pending", "posted"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountPayout:
        """
        Create a ledger account payout.

        Args:
          funding_ledger_account_id: The id of the funding ledger account that sends to or receives funds from the
              payout ledger account.

          payout_ledger_account_id: The id of the payout ledger account whose ledger entries are queried against,
              and its balance is reduced as a result.

          allow_either_direction: If true, the payout amount and payout_entry_direction will bring the payout
              ledger account's balance closer to zero, even if the balance is negative.

          description: The description of the ledger account payout.

          effective_at_upper_bound: The exclusive upper bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account payout. The default value is the created_at
              timestamp of the ledger account payout.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          skip_payout_ledger_transaction: It is set to `false` by default. It should be set to `true` when migrating
              existing payouts.

          status: The status of the ledger account payout. It is set to `pending` by default. To
              post a ledger account payout at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_account_payouts",
            body=await async_maybe_transform(
                {
                    "funding_ledger_account_id": funding_ledger_account_id,
                    "payout_ledger_account_id": payout_ledger_account_id,
                    "allow_either_direction": allow_either_direction,
                    "description": description,
                    "effective_at_upper_bound": effective_at_upper_bound,
                    "metadata": metadata,
                    "skip_payout_ledger_transaction": skip_payout_ledger_transaction,
                    "status": status,
                },
                ledger_account_payout_create_params.LedgerAccountPayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountPayout,
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
    ) -> LedgerAccountPayout:
        """
        Get details on a single ledger account payout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_account_payouts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountPayout,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["posted", "archived"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountPayout:
        """
        Update the details of a ledger account payout.

        Args:
          description: The description of the ledger account payout.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a pending ledger account payout, use `posted`. To archive a pending
              ledger transaction, use `archived`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/ledger_account_payouts/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_account_payout_update_params.LedgerAccountPayoutUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountPayout,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payout_entry_direction: str | NotGiven = NOT_GIVEN,
        payout_ledger_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerAccountPayout, AsyncPage[LedgerAccountPayout]]:
        """
        Get a list of ledger account payouts.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_account_payouts",
            page=AsyncPage[LedgerAccountPayout],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "metadata": metadata,
                        "payout_entry_direction": payout_entry_direction,
                        "payout_ledger_account_id": payout_ledger_account_id,
                        "per_page": per_page,
                    },
                    ledger_account_payout_list_params.LedgerAccountPayoutListParams,
                ),
            ),
            model=LedgerAccountPayout,
        )

    @typing_extensions.deprecated("use `retrieve` instead")
    async def retireve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccountPayout:
        """
        Get details on a single ledger account payout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.retrieve(
            id=id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )


class LedgerAccountPayoutsWithRawResponse:
    def __init__(self, ledger_account_payouts: LedgerAccountPayouts) -> None:
        self._ledger_account_payouts = ledger_account_payouts

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_account_payouts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_account_payouts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            ledger_account_payouts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_account_payouts.list,
        )
        self.retireve = (  # pyright: ignore[reportDeprecated]
            _legacy_response.to_raw_response_wrapper(
                ledger_account_payouts.retireve  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncLedgerAccountPayoutsWithRawResponse:
    def __init__(self, ledger_account_payouts: AsyncLedgerAccountPayouts) -> None:
        self._ledger_account_payouts = ledger_account_payouts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_payouts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_payouts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_payouts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_payouts.list,
        )
        self.retireve = (  # pyright: ignore[reportDeprecated]
            _legacy_response.async_to_raw_response_wrapper(
                ledger_account_payouts.retireve  # pyright: ignore[reportDeprecated],
            )
        )


class LedgerAccountPayoutsWithStreamingResponse:
    def __init__(self, ledger_account_payouts: LedgerAccountPayouts) -> None:
        self._ledger_account_payouts = ledger_account_payouts

        self.create = to_streamed_response_wrapper(
            ledger_account_payouts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_account_payouts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ledger_account_payouts.update,
        )
        self.list = to_streamed_response_wrapper(
            ledger_account_payouts.list,
        )
        self.retireve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                ledger_account_payouts.retireve  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncLedgerAccountPayoutsWithStreamingResponse:
    def __init__(self, ledger_account_payouts: AsyncLedgerAccountPayouts) -> None:
        self._ledger_account_payouts = ledger_account_payouts

        self.create = async_to_streamed_response_wrapper(
            ledger_account_payouts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_account_payouts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ledger_account_payouts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_account_payouts.list,
        )
        self.retireve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                ledger_account_payouts.retireve  # pyright: ignore[reportDeprecated],
            )
        )
