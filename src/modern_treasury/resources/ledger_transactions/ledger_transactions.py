# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import (
    LedgerTransaction,
    ledger_transaction_list_params,
    ledger_transaction_create_params,
    ledger_transaction_update_params,
    ledger_transaction_create_reversal_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .versions import (
    Versions,
    AsyncVersions,
    VersionsWithRawResponse,
    AsyncVersionsWithRawResponse,
    VersionsWithStreamingResponse,
    AsyncVersionsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["LedgerTransactions", "AsyncLedgerTransactions"]


class LedgerTransactions(SyncAPIResource):
    @cached_property
    def versions(self) -> Versions:
        return Versions(self._client)

    @cached_property
    def with_raw_response(self) -> LedgerTransactionsWithRawResponse:
        return LedgerTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerTransactionsWithStreamingResponse:
        return LedgerTransactionsWithStreamingResponse(self)

    def create(
        self,
        *,
        ledger_entries: Iterable[ledger_transaction_create_params.LedgerEntry],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerTransaction:
        """
        Create a ledger transaction.

        Args:
          ledger_entries: An array of ledger entry objects.

          description: An optional description for internal use.

          effective_at: The timestamp (ISO8601 format) at which the ledger transaction happened for
              reporting purposes.

          effective_date: The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
              purposes.

          external_id: A unique string to represent the ledger transaction. Only one pending or posted
              ledger transaction may have this ID in the ledger.

          ledgerable_id: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the id will be populated here, otherwise null.

          ledgerable_type: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the type will be populated here, otherwise null. This can be one of
              payment_order, incoming_payment_detail, expected_payment, return, or reversal.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a ledger transaction at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_transactions",
            body=maybe_transform(
                {
                    "ledger_entries": ledger_entries,
                    "description": description,
                    "effective_at": effective_at,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "ledgerable_id": ledgerable_id,
                    "ledgerable_type": ledgerable_type,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_transaction_create_params.LedgerTransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerTransaction,
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
    ) -> LedgerTransaction:
        """
        Get details on a single ledger transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerTransaction,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ledger_entries: Iterable[ledger_transaction_update_params.LedgerEntry] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerTransaction:
        """
        Update the details of a ledger transaction.

        Args:
          description: An optional description for internal use.

          effective_at: The timestamp (ISO8601 format) at which the ledger transaction happened for
              reporting purposes.

          ledger_entries: An array of ledger entry objects.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a ledger transaction at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/ledger_transactions/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "effective_at": effective_at,
                    "ledger_entries": ledger_entries,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_transaction_update_params.LedgerTransactionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerTransaction,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_account_payout_id: str | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        order_by: ledger_transaction_list_params.OrderBy | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        posted_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        reverses_ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerTransaction]:
        """
        Get a list of ledger transactions.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          effective_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by
              effective at. For example, for all transactions after Jan 1 2000, use
              effective_at%5Bgt%5D=2000-01-01T00:00:00:00.000Z.

          effective_date: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by
              effective date. For example, for all dates after Jan 1 2000, use
              effective_date%5Bgt%5D=2000-01-01.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          order_by: Order by `created_at` or `effective_at` in `asc` or `desc` order. For example,
              to order by `effective_at asc`, use `order_by%5Beffective_at%5D=asc`. Ordering
              by only one field at a time is supported.

          posted_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              posted_at%5Bgt%5D=2000-01-01T12:00:00Z.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_transactions",
            page=SyncPage[LedgerTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "effective_at": effective_at,
                        "effective_date": effective_date,
                        "external_id": external_id,
                        "ledger_account_category_id": ledger_account_category_id,
                        "ledger_account_id": ledger_account_id,
                        "ledger_account_payout_id": ledger_account_payout_id,
                        "ledger_account_settlement_id": ledger_account_settlement_id,
                        "ledger_id": ledger_id,
                        "ledgerable_id": ledgerable_id,
                        "ledgerable_type": ledgerable_type,
                        "metadata": metadata,
                        "order_by": order_by,
                        "per_page": per_page,
                        "posted_at": posted_at,
                        "reverses_ledger_transaction_id": reverses_ledger_transaction_id,
                        "status": status,
                        "updated_at": updated_at,
                    },
                    ledger_transaction_list_params.LedgerTransactionListParams,
                ),
            ),
            model=LedgerTransaction,
        )

    def create_reversal(
        self,
        id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerTransaction:
        """
        Create a ledger transaction reversal.

        Args:
          description: An optional free-form description for the reversal ledger transaction. Maximum
              of 1000 characters allowed.

          effective_at: The timestamp (ISO8601 format) at which the reversal ledger transaction happened
              for reporting purposes. It defaults to the `effective_at` of the original ledger
              transaction if not provided.

          external_id: Must be unique within the ledger.

          ledgerable_id: Specify this if you'd like to link the reversal ledger transaction to a Payment
              object like Return or Reversal.

          ledgerable_type: Specify this if you'd like to link the reversal ledger transaction to a Payment
              object like Return or Reversal.

          metadata: Additional data to be added to the reversal ledger transaction as key-value
              pairs. Both the key and value must be strings.

          status: Status of the reversal ledger transaction. It defaults to `posted` if not
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/ledger_transactions/{id}/reversal",
            body=maybe_transform(
                {
                    "description": description,
                    "effective_at": effective_at,
                    "external_id": external_id,
                    "ledgerable_id": ledgerable_id,
                    "ledgerable_type": ledgerable_type,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_transaction_create_reversal_params.LedgerTransactionCreateReversalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerTransaction,
        )


class AsyncLedgerTransactions(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersions:
        return AsyncVersions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLedgerTransactionsWithRawResponse:
        return AsyncLedgerTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerTransactionsWithStreamingResponse:
        return AsyncLedgerTransactionsWithStreamingResponse(self)

    async def create(
        self,
        *,
        ledger_entries: Iterable[ledger_transaction_create_params.LedgerEntry],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerTransaction:
        """
        Create a ledger transaction.

        Args:
          ledger_entries: An array of ledger entry objects.

          description: An optional description for internal use.

          effective_at: The timestamp (ISO8601 format) at which the ledger transaction happened for
              reporting purposes.

          effective_date: The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
              purposes.

          external_id: A unique string to represent the ledger transaction. Only one pending or posted
              ledger transaction may have this ID in the ledger.

          ledgerable_id: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the id will be populated here, otherwise null.

          ledgerable_type: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the type will be populated here, otherwise null. This can be one of
              payment_order, incoming_payment_detail, expected_payment, return, or reversal.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a ledger transaction at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_transactions",
            body=await async_maybe_transform(
                {
                    "ledger_entries": ledger_entries,
                    "description": description,
                    "effective_at": effective_at,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "ledgerable_id": ledgerable_id,
                    "ledgerable_type": ledgerable_type,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_transaction_create_params.LedgerTransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerTransaction,
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
    ) -> LedgerTransaction:
        """
        Get details on a single ledger transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerTransaction,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ledger_entries: Iterable[ledger_transaction_update_params.LedgerEntry] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerTransaction:
        """
        Update the details of a ledger transaction.

        Args:
          description: An optional description for internal use.

          effective_at: The timestamp (ISO8601 format) at which the ledger transaction happened for
              reporting purposes.

          ledger_entries: An array of ledger entry objects.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          status: To post a ledger transaction at creation, use `posted`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/ledger_transactions/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "effective_at": effective_at,
                    "ledger_entries": ledger_entries,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_transaction_update_params.LedgerTransactionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerTransaction,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        effective_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_account_payout_id: str | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        order_by: ledger_transaction_list_params.OrderBy | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        posted_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        reverses_ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerTransaction, AsyncPage[LedgerTransaction]]:
        """
        Get a list of ledger transactions.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          effective_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by
              effective at. For example, for all transactions after Jan 1 2000, use
              effective_at%5Bgt%5D=2000-01-01T00:00:00:00.000Z.

          effective_date: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by
              effective date. For example, for all dates after Jan 1 2000, use
              effective_date%5Bgt%5D=2000-01-01.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          order_by: Order by `created_at` or `effective_at` in `asc` or `desc` order. For example,
              to order by `effective_at asc`, use `order_by%5Beffective_at%5D=asc`. Ordering
              by only one field at a time is supported.

          posted_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              posted_at%5Bgt%5D=2000-01-01T12:00:00Z.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_transactions",
            page=AsyncPage[LedgerTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "effective_at": effective_at,
                        "effective_date": effective_date,
                        "external_id": external_id,
                        "ledger_account_category_id": ledger_account_category_id,
                        "ledger_account_id": ledger_account_id,
                        "ledger_account_payout_id": ledger_account_payout_id,
                        "ledger_account_settlement_id": ledger_account_settlement_id,
                        "ledger_id": ledger_id,
                        "ledgerable_id": ledgerable_id,
                        "ledgerable_type": ledgerable_type,
                        "metadata": metadata,
                        "order_by": order_by,
                        "per_page": per_page,
                        "posted_at": posted_at,
                        "reverses_ledger_transaction_id": reverses_ledger_transaction_id,
                        "status": status,
                        "updated_at": updated_at,
                    },
                    ledger_transaction_list_params.LedgerTransactionListParams,
                ),
            ),
            model=LedgerTransaction,
        )

    async def create_reversal(
        self,
        id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerTransaction:
        """
        Create a ledger transaction reversal.

        Args:
          description: An optional free-form description for the reversal ledger transaction. Maximum
              of 1000 characters allowed.

          effective_at: The timestamp (ISO8601 format) at which the reversal ledger transaction happened
              for reporting purposes. It defaults to the `effective_at` of the original ledger
              transaction if not provided.

          external_id: Must be unique within the ledger.

          ledgerable_id: Specify this if you'd like to link the reversal ledger transaction to a Payment
              object like Return or Reversal.

          ledgerable_type: Specify this if you'd like to link the reversal ledger transaction to a Payment
              object like Return or Reversal.

          metadata: Additional data to be added to the reversal ledger transaction as key-value
              pairs. Both the key and value must be strings.

          status: Status of the reversal ledger transaction. It defaults to `posted` if not
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/ledger_transactions/{id}/reversal",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "effective_at": effective_at,
                    "external_id": external_id,
                    "ledgerable_id": ledgerable_id,
                    "ledgerable_type": ledgerable_type,
                    "metadata": metadata,
                    "status": status,
                },
                ledger_transaction_create_reversal_params.LedgerTransactionCreateReversalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerTransaction,
        )


class LedgerTransactionsWithRawResponse:
    def __init__(self, ledger_transactions: LedgerTransactions) -> None:
        self._ledger_transactions = ledger_transactions

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_transactions.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_transactions.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            ledger_transactions.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_transactions.list,
        )
        self.create_reversal = _legacy_response.to_raw_response_wrapper(
            ledger_transactions.create_reversal,
        )

    @cached_property
    def versions(self) -> VersionsWithRawResponse:
        return VersionsWithRawResponse(self._ledger_transactions.versions)


class AsyncLedgerTransactionsWithRawResponse:
    def __init__(self, ledger_transactions: AsyncLedgerTransactions) -> None:
        self._ledger_transactions = ledger_transactions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_transactions.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_transactions.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            ledger_transactions.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_transactions.list,
        )
        self.create_reversal = _legacy_response.async_to_raw_response_wrapper(
            ledger_transactions.create_reversal,
        )

    @cached_property
    def versions(self) -> AsyncVersionsWithRawResponse:
        return AsyncVersionsWithRawResponse(self._ledger_transactions.versions)


class LedgerTransactionsWithStreamingResponse:
    def __init__(self, ledger_transactions: LedgerTransactions) -> None:
        self._ledger_transactions = ledger_transactions

        self.create = to_streamed_response_wrapper(
            ledger_transactions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_transactions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ledger_transactions.update,
        )
        self.list = to_streamed_response_wrapper(
            ledger_transactions.list,
        )
        self.create_reversal = to_streamed_response_wrapper(
            ledger_transactions.create_reversal,
        )

    @cached_property
    def versions(self) -> VersionsWithStreamingResponse:
        return VersionsWithStreamingResponse(self._ledger_transactions.versions)


class AsyncLedgerTransactionsWithStreamingResponse:
    def __init__(self, ledger_transactions: AsyncLedgerTransactions) -> None:
        self._ledger_transactions = ledger_transactions

        self.create = async_to_streamed_response_wrapper(
            ledger_transactions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_transactions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ledger_transactions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_transactions.list,
        )
        self.create_reversal = async_to_streamed_response_wrapper(
            ledger_transactions.create_reversal,
        )

    @cached_property
    def versions(self) -> AsyncVersionsWithStreamingResponse:
        return AsyncVersionsWithStreamingResponse(self._ledger_transactions.versions)
