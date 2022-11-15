# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction import Transaction

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Transaction:
        """Get details on a single transaction."""
        return self._get(
            f"/api/transactions/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )

    def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Transaction:
        """
        Update a single transaction.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/api/transactions/{id}",
            body={"metadata": metadata},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        posted: bool | NotGiven = NOT_GIVEN,
        as_of_date_start: str | NotGiven = NOT_GIVEN,
        as_of_date_end: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        payment_type: str | NotGiven = NOT_GIVEN,
        transactable_type: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Transaction]:
        """
        Get a list of all transactions.

        Args:
          internal_account_id: Specify `internal_account_id` if you wish to see transactions to/from a specific
              account.

          posted: Either `true` or `false`.

          as_of_date_start: Filters transactions with an `as_of_date` starting on or after the specified
              date (YYYY-MM-DD).

          as_of_date_end: Filters transactions with an `as_of_date` starting on or before the specified
              date (YYYY-MM-DD).

          description: Filters for transactions including the queried string in the description.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/transactions",
            page=SyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "internal_account_id": internal_account_id,
                    "virtual_account_id": virtual_account_id,
                    "posted": posted,
                    "as_of_date_start": as_of_date_start,
                    "as_of_date_end": as_of_date_end,
                    "direction": direction,
                    "counterparty_id": counterparty_id,
                    "payment_type": payment_type,
                    "transactable_type": transactable_type,
                    "description": description,
                    "metadata": metadata,
                },
            ),
            model=Transaction,
        )


class AsyncTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Transaction:
        """Get details on a single transaction."""
        return await self._get(
            f"/api/transactions/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )

    async def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Transaction:
        """
        Update a single transaction.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/api/transactions/{id}",
            body={"metadata": metadata},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        posted: bool | NotGiven = NOT_GIVEN,
        as_of_date_start: str | NotGiven = NOT_GIVEN,
        as_of_date_end: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        payment_type: str | NotGiven = NOT_GIVEN,
        transactable_type: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """
        Get a list of all transactions.

        Args:
          internal_account_id: Specify `internal_account_id` if you wish to see transactions to/from a specific
              account.

          posted: Either `true` or `false`.

          as_of_date_start: Filters transactions with an `as_of_date` starting on or after the specified
              date (YYYY-MM-DD).

          as_of_date_end: Filters transactions with an `as_of_date` starting on or before the specified
              date (YYYY-MM-DD).

          description: Filters for transactions including the queried string in the description.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/transactions",
            page=AsyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "internal_account_id": internal_account_id,
                    "virtual_account_id": virtual_account_id,
                    "posted": posted,
                    "as_of_date_start": as_of_date_start,
                    "as_of_date_end": as_of_date_end,
                    "direction": direction,
                    "counterparty_id": counterparty_id,
                    "payment_type": payment_type,
                    "transactable_type": transactable_type,
                    "description": description,
                    "metadata": metadata,
                },
            ),
            model=Transaction,
        )
