# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from datetime import date

from ...types import Transaction, transaction_list_params, transaction_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .line_items import LineItems, AsyncLineItems
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import ModernTreasury, AsyncModernTreasury

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    line_items: LineItems

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.line_items = LineItems(client)

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
    ) -> Transaction:
        """
        Get details on a single transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """
        Update a single transaction.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/api/transactions/{id}",
            body=maybe_transform({"metadata": metadata}, transaction_update_params.TransactionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        as_of_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_type: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        posted: bool | NotGiven = NOT_GIVEN,
        transactable_type: str | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """
        Get a list of all transactions.

        Args:
          as_of_date_end: Filters transactions with an `as_of_date` starting on or before the specified
              date (YYYY-MM-DD).

          as_of_date_start: Filters transactions with an `as_of_date` starting on or after the specified
              date (YYYY-MM-DD).

          description: Filters for transactions including the queried string in the description.

          internal_account_id: Specify `internal_account_id` if you wish to see transactions to/from a specific
              account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          posted: Either `true` or `false`.

          vendor_id: Filters for transactions including the queried vendor id (an identifier given to
              transactions by the bank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/transactions",
            page=SyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date_end": as_of_date_end,
                        "as_of_date_start": as_of_date_start,
                        "counterparty_id": counterparty_id,
                        "description": description,
                        "direction": direction,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "payment_type": payment_type,
                        "per_page": per_page,
                        "posted": posted,
                        "transactable_type": transactable_type,
                        "vendor_id": vendor_id,
                        "virtual_account_id": virtual_account_id,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=Transaction,
        )


class AsyncTransactions(AsyncAPIResource):
    line_items: AsyncLineItems

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.line_items = AsyncLineItems(client)

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
    ) -> Transaction:
        """
        Get details on a single transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """
        Update a single transaction.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/api/transactions/{id}",
            body=maybe_transform({"metadata": metadata}, transaction_update_params.TransactionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        as_of_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_type: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        posted: bool | NotGiven = NOT_GIVEN,
        transactable_type: str | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """
        Get a list of all transactions.

        Args:
          as_of_date_end: Filters transactions with an `as_of_date` starting on or before the specified
              date (YYYY-MM-DD).

          as_of_date_start: Filters transactions with an `as_of_date` starting on or after the specified
              date (YYYY-MM-DD).

          description: Filters for transactions including the queried string in the description.

          internal_account_id: Specify `internal_account_id` if you wish to see transactions to/from a specific
              account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          posted: Either `true` or `false`.

          vendor_id: Filters for transactions including the queried vendor id (an identifier given to
              transactions by the bank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/transactions",
            page=AsyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date_end": as_of_date_end,
                        "as_of_date_start": as_of_date_start,
                        "counterparty_id": counterparty_id,
                        "description": description,
                        "direction": direction,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "payment_type": payment_type,
                        "per_page": per_page,
                        "posted": posted,
                        "transactable_type": transactable_type,
                        "vendor_id": vendor_id,
                        "virtual_account_id": virtual_account_id,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=Transaction,
        )
