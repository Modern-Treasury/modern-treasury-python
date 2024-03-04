# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import (
    LedgerAccountStatementCreateResponse,
    LedgerAccountStatementRetrieveResponse,
    ledger_account_statement_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["LedgerAccountStatements", "AsyncLedgerAccountStatements"]


class LedgerAccountStatements(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerAccountStatementsWithRawResponse:
        return LedgerAccountStatementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerAccountStatementsWithStreamingResponse:
        return LedgerAccountStatementsWithStreamingResponse(self)

    def create(
        self,
        *,
        effective_at_lower_bound: Union[str, datetime],
        effective_at_upper_bound: Union[str, datetime],
        ledger_account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountStatementCreateResponse:
        """
        Create a ledger account statement.

        Args:
          effective_at_lower_bound: The inclusive lower bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account statement.

          effective_at_upper_bound: The exclusive upper bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account statement.

          ledger_account_id: The id of the ledger account whose ledger entries are queried against, and its
              balances are computed as a result.

          description: The description of the ledger account statement.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_account_statements",
            body=maybe_transform(
                {
                    "effective_at_lower_bound": effective_at_lower_bound,
                    "effective_at_upper_bound": effective_at_upper_bound,
                    "ledger_account_id": ledger_account_id,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_statement_create_params.LedgerAccountStatementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountStatementCreateResponse,
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
    ) -> LedgerAccountStatementRetrieveResponse:
        """
        Get details on a single ledger account statement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_account_statements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountStatementRetrieveResponse,
        )


class AsyncLedgerAccountStatements(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerAccountStatementsWithRawResponse:
        return AsyncLedgerAccountStatementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerAccountStatementsWithStreamingResponse:
        return AsyncLedgerAccountStatementsWithStreamingResponse(self)

    async def create(
        self,
        *,
        effective_at_lower_bound: Union[str, datetime],
        effective_at_upper_bound: Union[str, datetime],
        ledger_account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountStatementCreateResponse:
        """
        Create a ledger account statement.

        Args:
          effective_at_lower_bound: The inclusive lower bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account statement.

          effective_at_upper_bound: The exclusive upper bound of the effective_at timestamp of the ledger entries to
              be included in the ledger account statement.

          ledger_account_id: The id of the ledger account whose ledger entries are queried against, and its
              balances are computed as a result.

          description: The description of the ledger account statement.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_account_statements",
            body=await async_maybe_transform(
                {
                    "effective_at_lower_bound": effective_at_lower_bound,
                    "effective_at_upper_bound": effective_at_upper_bound,
                    "ledger_account_id": ledger_account_id,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_statement_create_params.LedgerAccountStatementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountStatementCreateResponse,
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
    ) -> LedgerAccountStatementRetrieveResponse:
        """
        Get details on a single ledger account statement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_account_statements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountStatementRetrieveResponse,
        )


class LedgerAccountStatementsWithRawResponse:
    def __init__(self, ledger_account_statements: LedgerAccountStatements) -> None:
        self._ledger_account_statements = ledger_account_statements

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_account_statements.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_account_statements.retrieve,
        )


class AsyncLedgerAccountStatementsWithRawResponse:
    def __init__(self, ledger_account_statements: AsyncLedgerAccountStatements) -> None:
        self._ledger_account_statements = ledger_account_statements

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_statements.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_statements.retrieve,
        )


class LedgerAccountStatementsWithStreamingResponse:
    def __init__(self, ledger_account_statements: LedgerAccountStatements) -> None:
        self._ledger_account_statements = ledger_account_statements

        self.create = to_streamed_response_wrapper(
            ledger_account_statements.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_account_statements.retrieve,
        )


class AsyncLedgerAccountStatementsWithStreamingResponse:
    def __init__(self, ledger_account_statements: AsyncLedgerAccountStatements) -> None:
        self._ledger_account_statements = ledger_account_statements

        self.create = async_to_streamed_response_wrapper(
            ledger_account_statements.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_account_statements.retrieve,
        )
