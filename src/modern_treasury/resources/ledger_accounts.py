# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    LedgerAccount,
    ledger_account_list_params,
    ledger_account_create_params,
    ledger_account_update_params,
    ledger_account_retrieve_params,
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
from ..types.shared import TransactionDirection

__all__ = ["LedgerAccounts", "AsyncLedgerAccounts"]


class LedgerAccounts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerAccountsWithRawResponse:
        return LedgerAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerAccountsWithStreamingResponse:
        return LedgerAccountsWithStreamingResponse(self)

    def create(
        self,
        *,
        currency: str,
        ledger_id: str,
        name: str,
        normal_balance: TransactionDirection,
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_account_category_ids: List[str] | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal["external_account", "internal_account", "virtual_account"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccount:
        """
        Create a ledger account.

        Args:
          currency: The currency of the ledger account.

          ledger_id: The id of the ledger that this account belongs to.

          name: The name of the ledger account.

          normal_balance: The normal balance of the ledger account.

          currency_exponent: The currency exponent of the ledger account.

          description: The description of the ledger account.

          ledger_account_category_ids: The array of ledger account category ids that this ledger account should be a
              child of.

          ledgerable_id: If the ledger account links to another object in Modern Treasury, the id will be
              populated here, otherwise null.

          ledgerable_type: If the ledger account links to another object in Modern Treasury, the type will
              be populated here, otherwise null. The value is one of internal_account or
              external_account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_accounts",
            body=maybe_transform(
                {
                    "currency": currency,
                    "ledger_id": ledger_id,
                    "name": name,
                    "normal_balance": normal_balance,
                    "currency_exponent": currency_exponent,
                    "description": description,
                    "ledger_account_category_ids": ledger_account_category_ids,
                    "ledgerable_id": ledgerable_id,
                    "ledgerable_type": ledgerable_type,
                    "metadata": metadata,
                },
                ledger_account_create_params.LedgerAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    def retrieve(
        self,
        id: str,
        *,
        balances: ledger_account_retrieve_params.Balances | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccount:
        """
        Get details on a single ledger account.

        Args:
          balances: Use `balances[effective_at_lower_bound]` and
              `balances[effective_at_upper_bound]` to get the balances change between the two
              timestamps. The lower bound is inclusive while the upper bound is exclusive of
              the provided timestamps. If no value is supplied the balances will be retrieved
              not including that bound. Use `balances[as_of_lock_version]` to retrieve a
              balance as of a specific Ledger Account `lock_version`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"balances": balances}, ledger_account_retrieve_params.LedgerAccountRetrieveParams
                ),
            ),
            cast_to=LedgerAccount,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccount:
        """
        Update the details of a ledger account.

        Args:
          description: The description of the ledger account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: The name of the ledger account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/ledger_accounts/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                ledger_account_update_params.LedgerAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        available_balance_amount: ledger_account_list_params.AvailableBalanceAmount | NotGiven = NOT_GIVEN,
        balances: ledger_account_list_params.Balances | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pending_balance_amount: ledger_account_list_params.PendingBalanceAmount | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        posted_balance_amount: ledger_account_list_params.PostedBalanceAmount | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerAccount]:
        """
        Get a list of ledger accounts.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          available_balance_amount: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
              filter by balance amount.

          balances: Use `balances[effective_at_lower_bound]` and
              `balances[effective_at_upper_bound]` to get the balances change between the two
              timestamps. The lower bound is inclusive while the upper bound is exclusive of
              the provided timestamps. If no value is supplied the balances will be retrieved
              not including that bound.

          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          pending_balance_amount: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
              filter by balance amount.

          posted_balance_amount: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
              filter by balance amount.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              updated at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_accounts",
            page=SyncPage[LedgerAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "available_balance_amount": available_balance_amount,
                        "balances": balances,
                        "created_at": created_at,
                        "currency": currency,
                        "ledger_account_category_id": ledger_account_category_id,
                        "ledger_id": ledger_id,
                        "metadata": metadata,
                        "name": name,
                        "pending_balance_amount": pending_balance_amount,
                        "per_page": per_page,
                        "posted_balance_amount": posted_balance_amount,
                        "updated_at": updated_at,
                    },
                    ledger_account_list_params.LedgerAccountListParams,
                ),
            ),
            model=LedgerAccount,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccount:
        """
        Delete a ledger account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )


class AsyncLedgerAccounts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerAccountsWithRawResponse:
        return AsyncLedgerAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerAccountsWithStreamingResponse:
        return AsyncLedgerAccountsWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency: str,
        ledger_id: str,
        name: str,
        normal_balance: TransactionDirection,
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_account_category_ids: List[str] | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal["external_account", "internal_account", "virtual_account"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccount:
        """
        Create a ledger account.

        Args:
          currency: The currency of the ledger account.

          ledger_id: The id of the ledger that this account belongs to.

          name: The name of the ledger account.

          normal_balance: The normal balance of the ledger account.

          currency_exponent: The currency exponent of the ledger account.

          description: The description of the ledger account.

          ledger_account_category_ids: The array of ledger account category ids that this ledger account should be a
              child of.

          ledgerable_id: If the ledger account links to another object in Modern Treasury, the id will be
              populated here, otherwise null.

          ledgerable_type: If the ledger account links to another object in Modern Treasury, the type will
              be populated here, otherwise null. The value is one of internal_account or
              external_account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_accounts",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "ledger_id": ledger_id,
                    "name": name,
                    "normal_balance": normal_balance,
                    "currency_exponent": currency_exponent,
                    "description": description,
                    "ledger_account_category_ids": ledger_account_category_ids,
                    "ledgerable_id": ledgerable_id,
                    "ledgerable_type": ledgerable_type,
                    "metadata": metadata,
                },
                ledger_account_create_params.LedgerAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    async def retrieve(
        self,
        id: str,
        *,
        balances: ledger_account_retrieve_params.Balances | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccount:
        """
        Get details on a single ledger account.

        Args:
          balances: Use `balances[effective_at_lower_bound]` and
              `balances[effective_at_upper_bound]` to get the balances change between the two
              timestamps. The lower bound is inclusive while the upper bound is exclusive of
              the provided timestamps. If no value is supplied the balances will be retrieved
              not including that bound. Use `balances[as_of_lock_version]` to retrieve a
              balance as of a specific Ledger Account `lock_version`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"balances": balances}, ledger_account_retrieve_params.LedgerAccountRetrieveParams
                ),
            ),
            cast_to=LedgerAccount,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccount:
        """
        Update the details of a ledger account.

        Args:
          description: The description of the ledger account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: The name of the ledger account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/ledger_accounts/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                ledger_account_update_params.LedgerAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        available_balance_amount: ledger_account_list_params.AvailableBalanceAmount | NotGiven = NOT_GIVEN,
        balances: ledger_account_list_params.Balances | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pending_balance_amount: ledger_account_list_params.PendingBalanceAmount | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        posted_balance_amount: ledger_account_list_params.PostedBalanceAmount | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerAccount, AsyncPage[LedgerAccount]]:
        """
        Get a list of ledger accounts.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          available_balance_amount: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
              filter by balance amount.

          balances: Use `balances[effective_at_lower_bound]` and
              `balances[effective_at_upper_bound]` to get the balances change between the two
              timestamps. The lower bound is inclusive while the upper bound is exclusive of
              the provided timestamps. If no value is supplied the balances will be retrieved
              not including that bound.

          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          pending_balance_amount: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
              filter by balance amount.

          posted_balance_amount: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), `eq` (=), or `not_eq` (!=) to
              filter by balance amount.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              updated at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_accounts",
            page=AsyncPage[LedgerAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "available_balance_amount": available_balance_amount,
                        "balances": balances,
                        "created_at": created_at,
                        "currency": currency,
                        "ledger_account_category_id": ledger_account_category_id,
                        "ledger_id": ledger_id,
                        "metadata": metadata,
                        "name": name,
                        "pending_balance_amount": pending_balance_amount,
                        "per_page": per_page,
                        "posted_balance_amount": posted_balance_amount,
                        "updated_at": updated_at,
                    },
                    ledger_account_list_params.LedgerAccountListParams,
                ),
            ),
            model=LedgerAccount,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccount:
        """
        Delete a ledger account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )


class LedgerAccountsWithRawResponse:
    def __init__(self, ledger_accounts: LedgerAccounts) -> None:
        self._ledger_accounts = ledger_accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_accounts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            ledger_accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_accounts.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            ledger_accounts.delete,
        )


class AsyncLedgerAccountsWithRawResponse:
    def __init__(self, ledger_accounts: AsyncLedgerAccounts) -> None:
        self._ledger_accounts = ledger_accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_accounts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            ledger_accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_accounts.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            ledger_accounts.delete,
        )


class LedgerAccountsWithStreamingResponse:
    def __init__(self, ledger_accounts: LedgerAccounts) -> None:
        self._ledger_accounts = ledger_accounts

        self.create = to_streamed_response_wrapper(
            ledger_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ledger_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            ledger_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            ledger_accounts.delete,
        )


class AsyncLedgerAccountsWithStreamingResponse:
    def __init__(self, ledger_accounts: AsyncLedgerAccounts) -> None:
        self._ledger_accounts = ledger_accounts

        self.create = async_to_streamed_response_wrapper(
            ledger_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ledger_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ledger_accounts.delete,
        )
