# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from ..types import (
    LedgerAccountCategory,
    ledger_account_category_list_params,
    ledger_account_category_create_params,
    ledger_account_category_update_params,
    ledger_account_category_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["LedgerAccountCategories", "AsyncLedgerAccountCategories"]


class LedgerAccountCategories(SyncAPIResource):
    def create(
        self,
        *,
        currency: str,
        ledger_id: str,
        name: str,
        normal_balance: Literal["credit", "debit"],
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_account_categories",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "currency": currency,
                    "currency_exponent": currency_exponent,
                    "ledger_id": ledger_id,
                    "normal_balance": normal_balance,
                },
                ledger_account_category_create_params.LedgerAccountCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
    ) -> LedgerAccountCategory:
        """
        Get the details on a single ledger account category.

        Args:
          balances: For example, if you want the balances as of a particular effective date
              (YYYY-MM-DD), the encoded query string would be
              balances%5Bas_of_date%5D=2000-12-31. The balances as of a date are inclusive of
              entries with that exact date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get(
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/api/ledger_account_categories/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_category_update_params.LedgerAccountCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> SyncPage[LedgerAccountCategory]:
        """
        Get a list of ledger account categories.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          parent_ledger_account_category_id: Query categories that are nested underneath a parent category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_account_categories",
            page=SyncPage[LedgerAccountCategory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "metadata": metadata,
                        "name": name,
                        "ledger_id": ledger_id,
                        "parent_ledger_account_category_id": parent_ledger_account_category_id,
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
        idempotency_key: str | None = None,
    ) -> LedgerAccountCategory:
        """Delete a ledger account category."""
        return self._delete(
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Add a ledger account category to an account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Add a ledger account category to a ledger account category."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Delete a ledger account category from an account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Delete a ledger account category from a ledger account category."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncLedgerAccountCategories(AsyncAPIResource):
    async def create(
        self,
        *,
        currency: str,
        ledger_id: str,
        name: str,
        normal_balance: Literal["credit", "debit"],
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_account_categories",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "currency": currency,
                    "currency_exponent": currency_exponent,
                    "ledger_id": ledger_id,
                    "normal_balance": normal_balance,
                },
                ledger_account_category_create_params.LedgerAccountCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
    ) -> LedgerAccountCategory:
        """
        Get the details on a single ledger account category.

        Args:
          balances: For example, if you want the balances as of a particular effective date
              (YYYY-MM-DD), the encoded query string would be
              balances%5Bas_of_date%5D=2000-12-31. The balances as of a date are inclusive of
              entries with that exact date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._get(
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/api/ledger_account_categories/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_category_update_params.LedgerAccountCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccountCategory,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[LedgerAccountCategory, AsyncPage[LedgerAccountCategory]]:
        """
        Get a list of ledger account categories.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          parent_ledger_account_category_id: Query categories that are nested underneath a parent category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_account_categories",
            page=AsyncPage[LedgerAccountCategory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "metadata": metadata,
                        "name": name,
                        "ledger_id": ledger_id,
                        "parent_ledger_account_category_id": parent_ledger_account_category_id,
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
        idempotency_key: str | None = None,
    ) -> LedgerAccountCategory:
        """Delete a ledger account category."""
        return await self._delete(
            f"/api/ledger_account_categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Add a ledger account category to an account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Add a ledger account category to a ledger account category."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Delete a ledger account category from an account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
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
        idempotency_key: str | None = None,
    ) -> None:
        """Delete a ledger account category from a ledger account category."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )
