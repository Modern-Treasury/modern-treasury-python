# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from .. import _legacy_response
from ..types import (
    LedgerAccountCategory,
    ledger_account_category_list_params,
    ledger_account_category_create_params,
    ledger_account_category_update_params,
    ledger_account_category_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["LedgerAccountCategories", "AsyncLedgerAccountCategories"]


class LedgerAccountCategories(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerAccountCategoriesWithRawResponse:
        return LedgerAccountCategoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerAccountCategoriesWithStreamingResponse:
        return LedgerAccountCategoriesWithStreamingResponse(self)

    def create(
        self,
        *,
        currency: str,
        ledger_id: str,
        name: str,
        normal_balance: TransactionDirection,
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountCategory:
        """
        Create a ledger account category.

        Args:
          currency: The currency of the ledger account category.

          ledger_id: The id of the ledger that this account category belongs to.

          name: The name of the ledger account category.

          normal_balance: The normal balance of the ledger account category.

          currency_exponent: The currency exponent of the ledger account category.

          description: The description of the ledger account category.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_account_categories",
            body=maybe_transform(
                {
                    "currency": currency,
                    "ledger_id": ledger_id,
                    "name": name,
                    "normal_balance": normal_balance,
                    "currency_exponent": currency_exponent,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_category_create_params.LedgerAccountCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    def retrieve(
        self,
        id: str,
        *,
        balances: ledger_account_category_retrieve_params.Balances | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccountCategory:
        """
        Get the details on a single ledger account category.

        Args:
          balances: For example, if you want the balances as of a particular time (ISO8601), the
              encoded query string would be `balances%5Beffective_at%5D=2000-12-31T12:00:00Z`.
              The balances as of a time are inclusive of entries with that exact time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"balances": balances}, ledger_account_category_retrieve_params.LedgerAccountCategoryRetrieveParams
                ),
            ),
            cast_to=LedgerAccountCategory,
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
    ) -> LedgerAccountCategory:
        """
        Update the details of a ledger account category.

        Args:
          description: The description of the ledger account category.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: The name of the ledger account category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/ledger_account_categories/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                ledger_account_category_update_params.LedgerAccountCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        balances: ledger_account_category_list_params.Balances | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerAccountCategory]:
        """
        Get a list of ledger account categories.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          balances: For example, if you want the balances as of a particular time (ISO8601), the
              encoded query string would be `balances%5Beffective_at%5D=2000-12-31T12:00:00Z`.
              The balances as of a time are inclusive of entries with that exact time.

          ledger_account_id: Query categories which contain a ledger account directly or through child
              categories.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          parent_ledger_account_category_id: Query categories that are nested underneath a parent category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_account_categories",
            page=SyncPage[LedgerAccountCategory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "balances": balances,
                        "ledger_account_id": ledger_account_id,
                        "ledger_id": ledger_id,
                        "metadata": metadata,
                        "name": name,
                        "parent_ledger_account_category_id": parent_ledger_account_category_id,
                        "per_page": per_page,
                    },
                    ledger_account_category_list_params.LedgerAccountCategoryListParams,
                ),
            ),
            model=LedgerAccountCategory,
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
    ) -> LedgerAccountCategory:
        """
        Delete a ledger account category.

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
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    def add_ledger_account(
        self,
        ledger_account_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add a ledger account to a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ledger_account_id:
            raise ValueError(f"Expected a non-empty value for `ledger_account_id` but received {ledger_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def add_nested_category(
        self,
        sub_category_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add a ledger account category to a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not sub_category_id:
            raise ValueError(f"Expected a non-empty value for `sub_category_id` but received {sub_category_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def remove_ledger_account(
        self,
        ledger_account_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Remove a ledger account from a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ledger_account_id:
            raise ValueError(f"Expected a non-empty value for `ledger_account_id` but received {ledger_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def remove_nested_category(
        self,
        sub_category_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a ledger account category from a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not sub_category_id:
            raise ValueError(f"Expected a non-empty value for `sub_category_id` but received {sub_category_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncLedgerAccountCategories(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerAccountCategoriesWithRawResponse:
        return AsyncLedgerAccountCategoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerAccountCategoriesWithStreamingResponse:
        return AsyncLedgerAccountCategoriesWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency: str,
        ledger_id: str,
        name: str,
        normal_balance: TransactionDirection,
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerAccountCategory:
        """
        Create a ledger account category.

        Args:
          currency: The currency of the ledger account category.

          ledger_id: The id of the ledger that this account category belongs to.

          name: The name of the ledger account category.

          normal_balance: The normal balance of the ledger account category.

          currency_exponent: The currency exponent of the ledger account category.

          description: The description of the ledger account category.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_account_categories",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "ledger_id": ledger_id,
                    "name": name,
                    "normal_balance": normal_balance,
                    "currency_exponent": currency_exponent,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_category_create_params.LedgerAccountCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    async def retrieve(
        self,
        id: str,
        *,
        balances: ledger_account_category_retrieve_params.Balances | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerAccountCategory:
        """
        Get the details on a single ledger account category.

        Args:
          balances: For example, if you want the balances as of a particular time (ISO8601), the
              encoded query string would be `balances%5Beffective_at%5D=2000-12-31T12:00:00Z`.
              The balances as of a time are inclusive of entries with that exact time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"balances": balances}, ledger_account_category_retrieve_params.LedgerAccountCategoryRetrieveParams
                ),
            ),
            cast_to=LedgerAccountCategory,
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
    ) -> LedgerAccountCategory:
        """
        Update the details of a ledger account category.

        Args:
          description: The description of the ledger account category.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: The name of the ledger account category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/ledger_account_categories/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                ledger_account_category_update_params.LedgerAccountCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    def list(
        self,
        *,
        id: List[str] | NotGiven = NOT_GIVEN,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        balances: ledger_account_category_list_params.Balances | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerAccountCategory, AsyncPage[LedgerAccountCategory]]:
        """
        Get a list of ledger account categories.

        Args:
          id: If you have specific IDs to retrieve in bulk, you can pass them as query
              parameters delimited with `id[]=`, for example `?id[]=123&id[]=abc`.

          balances: For example, if you want the balances as of a particular time (ISO8601), the
              encoded query string would be `balances%5Beffective_at%5D=2000-12-31T12:00:00Z`.
              The balances as of a time are inclusive of entries with that exact time.

          ledger_account_id: Query categories which contain a ledger account directly or through child
              categories.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          parent_ledger_account_category_id: Query categories that are nested underneath a parent category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_account_categories",
            page=AsyncPage[LedgerAccountCategory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after_cursor": after_cursor,
                        "balances": balances,
                        "ledger_account_id": ledger_account_id,
                        "ledger_id": ledger_id,
                        "metadata": metadata,
                        "name": name,
                        "parent_ledger_account_category_id": parent_ledger_account_category_id,
                        "per_page": per_page,
                    },
                    ledger_account_category_list_params.LedgerAccountCategoryListParams,
                ),
            ),
            model=LedgerAccountCategory,
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
    ) -> LedgerAccountCategory:
        """
        Delete a ledger account category.

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
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    async def add_ledger_account(
        self,
        ledger_account_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add a ledger account to a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ledger_account_id:
            raise ValueError(f"Expected a non-empty value for `ledger_account_id` but received {ledger_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def add_nested_category(
        self,
        sub_category_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add a ledger account category to a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not sub_category_id:
            raise ValueError(f"Expected a non-empty value for `sub_category_id` but received {sub_category_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def remove_ledger_account(
        self,
        ledger_account_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Remove a ledger account from a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ledger_account_id:
            raise ValueError(f"Expected a non-empty value for `ledger_account_id` but received {ledger_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def remove_nested_category(
        self,
        sub_category_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a ledger account category from a ledger account category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not sub_category_id:
            raise ValueError(f"Expected a non-empty value for `sub_category_id` but received {sub_category_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class LedgerAccountCategoriesWithRawResponse:
    def __init__(self, ledger_account_categories: LedgerAccountCategories) -> None:
        self._ledger_account_categories = ledger_account_categories

        self.create = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.delete,
        )
        self.add_ledger_account = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.add_ledger_account,
        )
        self.add_nested_category = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.add_nested_category,
        )
        self.remove_ledger_account = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.remove_ledger_account,
        )
        self.remove_nested_category = _legacy_response.to_raw_response_wrapper(
            ledger_account_categories.remove_nested_category,
        )


class AsyncLedgerAccountCategoriesWithRawResponse:
    def __init__(self, ledger_account_categories: AsyncLedgerAccountCategories) -> None:
        self._ledger_account_categories = ledger_account_categories

        self.create = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.delete,
        )
        self.add_ledger_account = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.add_ledger_account,
        )
        self.add_nested_category = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.add_nested_category,
        )
        self.remove_ledger_account = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.remove_ledger_account,
        )
        self.remove_nested_category = _legacy_response.async_to_raw_response_wrapper(
            ledger_account_categories.remove_nested_category,
        )


class LedgerAccountCategoriesWithStreamingResponse:
    def __init__(self, ledger_account_categories: LedgerAccountCategories) -> None:
        self._ledger_account_categories = ledger_account_categories

        self.create = to_streamed_response_wrapper(
            ledger_account_categories.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_account_categories.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ledger_account_categories.update,
        )
        self.list = to_streamed_response_wrapper(
            ledger_account_categories.list,
        )
        self.delete = to_streamed_response_wrapper(
            ledger_account_categories.delete,
        )
        self.add_ledger_account = to_streamed_response_wrapper(
            ledger_account_categories.add_ledger_account,
        )
        self.add_nested_category = to_streamed_response_wrapper(
            ledger_account_categories.add_nested_category,
        )
        self.remove_ledger_account = to_streamed_response_wrapper(
            ledger_account_categories.remove_ledger_account,
        )
        self.remove_nested_category = to_streamed_response_wrapper(
            ledger_account_categories.remove_nested_category,
        )


class AsyncLedgerAccountCategoriesWithStreamingResponse:
    def __init__(self, ledger_account_categories: AsyncLedgerAccountCategories) -> None:
        self._ledger_account_categories = ledger_account_categories

        self.create = async_to_streamed_response_wrapper(
            ledger_account_categories.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_account_categories.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ledger_account_categories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_account_categories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ledger_account_categories.delete,
        )
        self.add_ledger_account = async_to_streamed_response_wrapper(
            ledger_account_categories.add_ledger_account,
        )
        self.add_nested_category = async_to_streamed_response_wrapper(
            ledger_account_categories.add_nested_category,
        )
        self.remove_ledger_account = async_to_streamed_response_wrapper(
            ledger_account_categories.remove_ledger_account,
        )
        self.remove_nested_category = async_to_streamed_response_wrapper(
            ledger_account_categories.remove_nested_category,
        )
