# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    LedgerAccountSettlement,
    ledger_account_settlement_list_params,
    ledger_account_settlement_create_params,
    ledger_account_settlement_update_params,
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

__all__ = ["LedgerAccountSettlements", "AsyncLedgerAccountSettlements"]


class LedgerAccountSettlements(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerAccountSettlementsWithRawResponse:
        return LedgerAccountSettlementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerAccountSettlementsWithStreamingResponse:
        return LedgerAccountSettlementsWithStreamingResponse(self)

    def create(
        self,
        *,
        contra_ledger_account_id: str,
        settled_ledger_account_id: str,
        allow_either_direction: Optional[bool] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at_upper_bound: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        skip_settlement_ledger_transaction: Optional[bool] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["pending", "posted"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountSettlement:
        """
        Create a ledger account settlement.

        Args:
          contra_ledger_account_id: The id of the contra ledger account that sends to or receives funds from the
              settled ledger account.

          settled_ledger_account_id: The id of the settled ledger account whose ledger entries are queried against,
              and its balance is reduced as a result.

          allow_either_direction: If true, the settlement amount and settlement_entry_direction will bring the
              settlement ledger account's balance closer to zero, even if the balance is
              negative.

          description: The description of the ledger account settlement.

          effective_at_upper_bound: The exclusive upper bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account settlement. The default value is the
              created_at timestamp of the ledger account settlement.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          skip_settlement_ledger_transaction: It is set to `false` by default. It should be set to `true` when migrating
              existing settlements.

          status: The status of the ledger account settlement. It is set to `pending` by default.
              To post a ledger account settlement at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_account_settlements",
            body=maybe_transform(
                {
                    "contra_ledger_account_id": contra_ledger_account_id,
                    "settled_ledger_account_id": settled_ledger_account_id,
                    "allow_either_direction": allow_either_direction,
                    "description": description,
                    "effective_at_upper_bound": effective_at_upper_bound,
                    "metadata": metadata,
                    "skip_settlement_ledger_transaction": skip_settlement_ledger_transaction,
                    "status": status,
                },
                ledger_account_settlement_create_params.LedgerAccountSettlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountSettlement,
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
    ) -> LedgerAccountSettlement:
        """
        Get details on a single ledger account settlement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_account_settlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountSettlement,
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
    ) -> LedgerAccountSettlement:
        """
        Update the details of a ledger account settlement.

        Args:
          description: The description of the ledger account settlement.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a pending ledger account settlement, use `posted`. To archive a pending
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
            f"/api/ledger_account_settlements/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_account_settlement_update_params.LedgerAccountSettlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountSettlement,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        settled_ledger_account_id: str | NotGiven = NOT_GIVEN,
        settlement_entry_direction: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerAccountSettlement]:
        """
        Get a list of ledger account settlements.

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
            "/api/ledger_account_settlements",
            page=SyncPage[LedgerAccountSettlement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "ledger_transaction_id": ledger_transaction_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "settled_ledger_account_id": settled_ledger_account_id,
                        "settlement_entry_direction": settlement_entry_direction,
                    },
                    ledger_account_settlement_list_params.LedgerAccountSettlementListParams,
                ),
            ),
            model=LedgerAccountSettlement,
        )


class AsyncLedgerAccountSettlements(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerAccountSettlementsWithRawResponse:
        return AsyncLedgerAccountSettlementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerAccountSettlementsWithStreamingResponse:
        return AsyncLedgerAccountSettlementsWithStreamingResponse(self)

    async def create(
        self,
        *,
        contra_ledger_account_id: str,
        settled_ledger_account_id: str,
        allow_either_direction: Optional[bool] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at_upper_bound: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        skip_settlement_ledger_transaction: Optional[bool] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["pending", "posted"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountSettlement:
        """
        Create a ledger account settlement.

        Args:
          contra_ledger_account_id: The id of the contra ledger account that sends to or receives funds from the
              settled ledger account.

          settled_ledger_account_id: The id of the settled ledger account whose ledger entries are queried against,
              and its balance is reduced as a result.

          allow_either_direction: If true, the settlement amount and settlement_entry_direction will bring the
              settlement ledger account's balance closer to zero, even if the balance is
              negative.

          description: The description of the ledger account settlement.

          effective_at_upper_bound: The exclusive upper bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account settlement. The default value is the
              created_at timestamp of the ledger account settlement.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          skip_settlement_ledger_transaction: It is set to `false` by default. It should be set to `true` when migrating
              existing settlements.

          status: The status of the ledger account settlement. It is set to `pending` by default.
              To post a ledger account settlement at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_account_settlements",
            body=await async_maybe_transform(
                {
                    "contra_ledger_account_id": contra_ledger_account_id,
                    "settled_ledger_account_id": settled_ledger_account_id,
                    "allow_either_direction": allow_either_direction,
                    "description": description,
                    "effective_at_upper_bound": effective_at_upper_bound,
                    "metadata": metadata,
                    "skip_settlement_ledger_transaction": skip_settlement_ledger_transaction,
                    "status": status,
                },
                ledger_account_settlement_create_params.LedgerAccountSettlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountSettlement,
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
    ) -> LedgerAccountSettlement:
        """
        Get details on a single ledger account settlement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_account_settlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountSettlement,
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
    ) -> LedgerAccountSettlement:
        """
        Update the details of a ledger account settlement.

        Args:
          description: The description of the ledger account settlement.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a pending ledger account settlement, use `posted`. To archive a pending
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
            f"/api/ledger_account_settlements/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_account_settlement_update_params.LedgerAccountSettlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountSettlement,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        settled_ledger_account_id: str | NotGiven = NOT_GIVEN,
        settlement_entry_direction: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerAccountSettlement, AsyncPage[LedgerAccountSettlement]]:
        """
        Get a list of ledger account settlements.

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
            "/api/ledger_account_settlements",
            page=AsyncPage[LedgerAccountSettlement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "ledger_transaction_id": ledger_transaction_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "settled_ledger_account_id": settled_ledger_account_id,
                        "settlement_entry_direction": settlement_entry_direction,
                    },
                    ledger_account_settlement_list_params.LedgerAccountSettlementListParams,
                ),
            ),
            model=LedgerAccountSettlement,
        )


class LedgerAccountSettlementsWithRawResponse:
    def __init__(self, ledger_account_settlements: LedgerAccountSettlements) -> None:
        self._ledger_account_settlements = ledger_account_settlements

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_account_settlements.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_account_settlements.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            ledger_account_settlements.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_account_settlements.list,
        )


class AsyncLedgerAccountSettlementsWithRawResponse:
    def __init__(self, ledger_account_settlements: AsyncLedgerAccountSettlements) -> None:
        self._ledger_account_settlements = ledger_account_settlements

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_settlements.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_settlements.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_settlements.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_settlements.list,
        )


class LedgerAccountSettlementsWithStreamingResponse:
    def __init__(self, ledger_account_settlements: LedgerAccountSettlements) -> None:
        self._ledger_account_settlements = ledger_account_settlements

        self.create = to_streamed_response_wrapper(
            ledger_account_settlements.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_account_settlements.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ledger_account_settlements.update,
        )
        self.list = to_streamed_response_wrapper(
            ledger_account_settlements.list,
        )


class AsyncLedgerAccountSettlementsWithStreamingResponse:
    def __init__(self, ledger_account_settlements: AsyncLedgerAccountSettlements) -> None:
        self._ledger_account_settlements = ledger_account_settlements

        self.create = async_to_streamed_response_wrapper(
            ledger_account_settlements.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_account_settlements.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ledger_account_settlements.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_account_settlements.list,
        )
