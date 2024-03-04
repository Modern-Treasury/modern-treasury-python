# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date

import httpx

from ... import _legacy_response
from ...types import (
    Transaction,
    transaction_list_params,
    transaction_create_params,
    transaction_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .line_items import (
    LineItems,
    AsyncLineItems,
    LineItemsWithRawResponse,
    AsyncLineItemsWithRawResponse,
    LineItemsWithStreamingResponse,
    AsyncLineItemsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    @cached_property
    def line_items(self) -> LineItems:
        return LineItems(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionsWithRawResponse:
        return TransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsWithStreamingResponse:
        return TransactionsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        as_of_date: Union[str, date, None],
        direction: str,
        internal_account_id: str,
        vendor_code: str,
        vendor_code_type: str,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        posted: bool | NotGiven = NOT_GIVEN,
        vendor_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """create transaction

        Args:
          amount: Value in specified currency's smallest unit.

        e.g. $10 would be represented
              as 1000.

          as_of_date: The date on which the transaction occurred.

          direction: Either `credit` or `debit`.

          internal_account_id: The ID of the relevant Internal Account.

          vendor_code: When applicable, the bank-given code that determines the transaction's category.
              For most banks this is the BAI2/BTRS transaction code.

          vendor_code_type: The type of `vendor_code` being reported. Can be one of `bai2`, `bankprov`,
              `bnk_dev`, `cleartouch`, `currencycloud`, `cross_river`, `dc_bank`, `dwolla`,
              `evolve`, `goldman_sachs`, `iso20022`, `jpmc`, `mx`, `signet`, `silvergate`,
              `swift`, `us_bank`, or others.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          posted: This field will be `true` if the transaction has posted to the account.

          vendor_description: The transaction detail text that often appears in on your bank statement and in
              your banking portal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/transactions",
            body=maybe_transform(
                {
                    "amount": amount,
                    "as_of_date": as_of_date,
                    "direction": direction,
                    "internal_account_id": internal_account_id,
                    "vendor_code": vendor_code,
                    "vendor_code_type": vendor_code_type,
                    "metadata": metadata,
                    "posted": posted,
                    "vendor_description": vendor_description,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
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
    ) -> Transaction:
        """
        Get details on a single transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    ) -> None:
        """
        delete transaction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncTransactions(AsyncAPIResource):
    @cached_property
    def line_items(self) -> AsyncLineItems:
        return AsyncLineItems(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionsWithRawResponse:
        return AsyncTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsWithStreamingResponse:
        return AsyncTransactionsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        as_of_date: Union[str, date, None],
        direction: str,
        internal_account_id: str,
        vendor_code: str,
        vendor_code_type: str,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        posted: bool | NotGiven = NOT_GIVEN,
        vendor_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """create transaction

        Args:
          amount: Value in specified currency's smallest unit.

        e.g. $10 would be represented
              as 1000.

          as_of_date: The date on which the transaction occurred.

          direction: Either `credit` or `debit`.

          internal_account_id: The ID of the relevant Internal Account.

          vendor_code: When applicable, the bank-given code that determines the transaction's category.
              For most banks this is the BAI2/BTRS transaction code.

          vendor_code_type: The type of `vendor_code` being reported. Can be one of `bai2`, `bankprov`,
              `bnk_dev`, `cleartouch`, `currencycloud`, `cross_river`, `dc_bank`, `dwolla`,
              `evolve`, `goldman_sachs`, `iso20022`, `jpmc`, `mx`, `signet`, `silvergate`,
              `swift`, `us_bank`, or others.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          posted: This field will be `true` if the transaction has posted to the account.

          vendor_description: The transaction detail text that often appears in on your bank statement and in
              your banking portal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/transactions",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "as_of_date": as_of_date,
                    "direction": direction,
                    "internal_account_id": internal_account_id,
                    "vendor_code": vendor_code,
                    "vendor_code_type": vendor_code_type,
                    "metadata": metadata,
                    "posted": posted,
                    "vendor_description": vendor_description,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
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
    ) -> Transaction:
        """
        Get details on a single transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/transactions/{id}",
            body=await async_maybe_transform({"metadata": metadata}, transaction_update_params.TransactionUpdateParams),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    ) -> None:
        """
        delete transaction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class TransactionsWithRawResponse:
    def __init__(self, transactions: Transactions) -> None:
        self._transactions = transactions

        self.create = _legacy_response.to_raw_response_wrapper(
            transactions.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            transactions.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            transactions.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            transactions.delete,
        )

    @cached_property
    def line_items(self) -> LineItemsWithRawResponse:
        return LineItemsWithRawResponse(self._transactions.line_items)


class AsyncTransactionsWithRawResponse:
    def __init__(self, transactions: AsyncTransactions) -> None:
        self._transactions = transactions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            transactions.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            transactions.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            transactions.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            transactions.delete,
        )

    @cached_property
    def line_items(self) -> AsyncLineItemsWithRawResponse:
        return AsyncLineItemsWithRawResponse(self._transactions.line_items)


class TransactionsWithStreamingResponse:
    def __init__(self, transactions: Transactions) -> None:
        self._transactions = transactions

        self.create = to_streamed_response_wrapper(
            transactions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            transactions.update,
        )
        self.list = to_streamed_response_wrapper(
            transactions.list,
        )
        self.delete = to_streamed_response_wrapper(
            transactions.delete,
        )

    @cached_property
    def line_items(self) -> LineItemsWithStreamingResponse:
        return LineItemsWithStreamingResponse(self._transactions.line_items)


class AsyncTransactionsWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactions) -> None:
        self._transactions = transactions

        self.create = async_to_streamed_response_wrapper(
            transactions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            transactions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            transactions.delete,
        )

    @cached_property
    def line_items(self) -> AsyncLineItemsWithStreamingResponse:
        return AsyncLineItemsWithStreamingResponse(self._transactions.line_items)
