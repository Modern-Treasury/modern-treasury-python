# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Dict, Union, Optional, cast, overload

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction import Transaction
from ..types.transaction_list_params import TransactionListParams
from ..types.transaction_update_params import TransactionUpdateParams

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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Get details on a single transaction."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Transaction,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def update(
        self,
        id: str,
        body: TransactionUpdateParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Update a single transaction."""
        ...

    def update(
        self,
        id: str,
        body: TransactionUpdateParams | None = None,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """
        Update a single transaction.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionUpdateParams type.
            body = cast(Any, {"metadata": metadata})

        return self._patch(
            f"/api/transactions/{id}",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Transaction,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        ...

    @overload
    def list(
        self,
        query: TransactionListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """Get a list of all transactions."""
        ...

    def list(
        self,
        query: TransactionListParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """
        Get a list of all transactions.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionListParams type.
            query = cast(
                Any,
                {
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
            )

        return self._get_api_list(
            "/api/transactions",
            page=SyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Get details on a single transaction."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Transaction,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def update(
        self,
        id: str,
        body: TransactionUpdateParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Update a single transaction."""
        ...

    async def update(
        self,
        id: str,
        body: TransactionUpdateParams | None = None,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """
        Update a single transaction.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionUpdateParams type.
            body = cast(Any, {"metadata": metadata})

        return await self._patch(
            f"/api/transactions/{id}",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Transaction,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        ...

    @overload
    def list(
        self,
        query: TransactionListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """Get a list of all transactions."""
        ...

    def list(
        self,
        query: TransactionListParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """
        Get a list of all transactions.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionListParams type.
            query = cast(
                Any,
                {
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
            )

        return self._get_api_list(
            "/api/transactions",
            page=AsyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Transaction,
        )
