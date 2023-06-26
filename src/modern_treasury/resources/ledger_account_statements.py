# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional

from ..types import (
    LedgerAccountStatementCreateResponse,
    LedgerAccountStatementRetrieveResponse,
    ledger_account_statement_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["LedgerAccountStatements", "AsyncLedgerAccountStatements"]


class LedgerAccountStatements(SyncAPIResource):
    def create(
        self,
        *,
        effective_at_lower_bound: str,
        effective_at_upper_bound: str,
        ledger_account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccountStatementRetrieveResponse:
        """
        Get details on a single ledger account statement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/ledger_account_statements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountStatementRetrieveResponse,
        )


class AsyncLedgerAccountStatements(AsyncAPIResource):
    async def create(
        self,
        *,
        effective_at_lower_bound: str,
        effective_at_upper_bound: str,
        ledger_account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccountStatementRetrieveResponse:
        """
        Get details on a single ledger account statement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/ledger_account_statements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountStatementRetrieveResponse,
        )
