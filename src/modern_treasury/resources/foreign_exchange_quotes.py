# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date, datetime

import httpx

from .. import _legacy_response
from ..types import (
    ForeignExchangeQuote,
    foreign_exchange_quote_list_params,
    foreign_exchange_quote_create_params,
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
from ..types.shared import Currency

__all__ = ["ForeignExchangeQuotes", "AsyncForeignExchangeQuotes"]


class ForeignExchangeQuotes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForeignExchangeQuotesWithRawResponse:
        return ForeignExchangeQuotesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForeignExchangeQuotesWithStreamingResponse:
        return ForeignExchangeQuotesWithStreamingResponse(self)

    def create(
        self,
        *,
        internal_account_id: str,
        target_currency: Optional[Currency],
        base_amount: int | NotGiven = NOT_GIVEN,
        base_currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        target_amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ForeignExchangeQuote:
        """
        create foreign_exchange_quote

        Args:
          internal_account_id: The ID for the `InternalAccount` this quote is associated with.

          target_currency: Currency to convert the `base_currency` to, often called the "buy" currency.

          base_amount: Amount in the lowest denomination of the `base_currency` to convert, often
              called the "sell" amount.

          base_currency: Currency to convert, often called the "sell" currency.

          effective_at: The timestamp until when the quoted rate is valid.

          target_amount: Amount in the lowest denomination of the `target_currency`, often called the
              "buy" amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/foreign_exchange_quotes",
            body=maybe_transform(
                {
                    "internal_account_id": internal_account_id,
                    "target_currency": target_currency,
                    "base_amount": base_amount,
                    "base_currency": base_currency,
                    "effective_at": effective_at,
                    "target_amount": target_amount,
                },
                foreign_exchange_quote_create_params.ForeignExchangeQuoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ForeignExchangeQuote,
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
    ) -> ForeignExchangeQuote:
        """
        get foreign_exchange_quote

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/foreign_exchange_quotes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForeignExchangeQuote,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        base_currency: str | NotGiven = NOT_GIVEN,
        effective_at_end: Union[str, date] | NotGiven = NOT_GIVEN,
        effective_at_start: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        target_currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ForeignExchangeQuote]:
        """
        list foreign_exchange_quotes

        Args:
          base_currency: Currency to convert, often called the "sell" currency.

          effective_at_end: An inclusive upper bound for searching effective_at

          effective_at_start: An inclusive lower bound for searching effective_at

          expires_at: The timestamp until which the quote must be booked by.

          internal_account_id: The ID for the `InternalAccount` this quote is associated with.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          target_currency: Currency to convert the `base_currency` to, often called the "buy" currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/foreign_exchange_quotes",
            page=SyncPage[ForeignExchangeQuote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "base_currency": base_currency,
                        "effective_at_end": effective_at_end,
                        "effective_at_start": effective_at_start,
                        "expires_at": expires_at,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "target_currency": target_currency,
                    },
                    foreign_exchange_quote_list_params.ForeignExchangeQuoteListParams,
                ),
            ),
            model=ForeignExchangeQuote,
        )


class AsyncForeignExchangeQuotes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForeignExchangeQuotesWithRawResponse:
        return AsyncForeignExchangeQuotesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForeignExchangeQuotesWithStreamingResponse:
        return AsyncForeignExchangeQuotesWithStreamingResponse(self)

    async def create(
        self,
        *,
        internal_account_id: str,
        target_currency: Optional[Currency],
        base_amount: int | NotGiven = NOT_GIVEN,
        base_currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        target_amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ForeignExchangeQuote:
        """
        create foreign_exchange_quote

        Args:
          internal_account_id: The ID for the `InternalAccount` this quote is associated with.

          target_currency: Currency to convert the `base_currency` to, often called the "buy" currency.

          base_amount: Amount in the lowest denomination of the `base_currency` to convert, often
              called the "sell" amount.

          base_currency: Currency to convert, often called the "sell" currency.

          effective_at: The timestamp until when the quoted rate is valid.

          target_amount: Amount in the lowest denomination of the `target_currency`, often called the
              "buy" amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/foreign_exchange_quotes",
            body=await async_maybe_transform(
                {
                    "internal_account_id": internal_account_id,
                    "target_currency": target_currency,
                    "base_amount": base_amount,
                    "base_currency": base_currency,
                    "effective_at": effective_at,
                    "target_amount": target_amount,
                },
                foreign_exchange_quote_create_params.ForeignExchangeQuoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ForeignExchangeQuote,
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
    ) -> ForeignExchangeQuote:
        """
        get foreign_exchange_quote

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/foreign_exchange_quotes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForeignExchangeQuote,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        base_currency: str | NotGiven = NOT_GIVEN,
        effective_at_end: Union[str, date] | NotGiven = NOT_GIVEN,
        effective_at_start: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        target_currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ForeignExchangeQuote, AsyncPage[ForeignExchangeQuote]]:
        """
        list foreign_exchange_quotes

        Args:
          base_currency: Currency to convert, often called the "sell" currency.

          effective_at_end: An inclusive upper bound for searching effective_at

          effective_at_start: An inclusive lower bound for searching effective_at

          expires_at: The timestamp until which the quote must be booked by.

          internal_account_id: The ID for the `InternalAccount` this quote is associated with.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          target_currency: Currency to convert the `base_currency` to, often called the "buy" currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/foreign_exchange_quotes",
            page=AsyncPage[ForeignExchangeQuote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "base_currency": base_currency,
                        "effective_at_end": effective_at_end,
                        "effective_at_start": effective_at_start,
                        "expires_at": expires_at,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "target_currency": target_currency,
                    },
                    foreign_exchange_quote_list_params.ForeignExchangeQuoteListParams,
                ),
            ),
            model=ForeignExchangeQuote,
        )


class ForeignExchangeQuotesWithRawResponse:
    def __init__(self, foreign_exchange_quotes: ForeignExchangeQuotes) -> None:
        self._foreign_exchange_quotes = foreign_exchange_quotes

        self.create = _legacy_response.to_raw_response_wrapper(
            foreign_exchange_quotes.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            foreign_exchange_quotes.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            foreign_exchange_quotes.list,
        )


class AsyncForeignExchangeQuotesWithRawResponse:
    def __init__(self, foreign_exchange_quotes: AsyncForeignExchangeQuotes) -> None:
        self._foreign_exchange_quotes = foreign_exchange_quotes

        self.create = _legacy_response.async_to_raw_response_wrapper(
            foreign_exchange_quotes.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            foreign_exchange_quotes.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            foreign_exchange_quotes.list,
        )


class ForeignExchangeQuotesWithStreamingResponse:
    def __init__(self, foreign_exchange_quotes: ForeignExchangeQuotes) -> None:
        self._foreign_exchange_quotes = foreign_exchange_quotes

        self.create = to_streamed_response_wrapper(
            foreign_exchange_quotes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            foreign_exchange_quotes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            foreign_exchange_quotes.list,
        )


class AsyncForeignExchangeQuotesWithStreamingResponse:
    def __init__(self, foreign_exchange_quotes: AsyncForeignExchangeQuotes) -> None:
        self._foreign_exchange_quotes = foreign_exchange_quotes

        self.create = async_to_streamed_response_wrapper(
            foreign_exchange_quotes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            foreign_exchange_quotes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            foreign_exchange_quotes.list,
        )
