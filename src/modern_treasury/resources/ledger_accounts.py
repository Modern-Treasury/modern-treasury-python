# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import (
    LedgerAccount,
    ledger_account_list_params,
    ledger_account_create_params,
    ledger_account_update_params,
    ledger_account_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["LedgerAccounts", "AsyncLedgerAccounts"]


class LedgerAccounts(SyncAPIResource):
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
    ) -> LedgerAccount:
        """
        Create a ledger account.

        Args:
          currency: The currency of the ledger account.

          ledger_id: The id of the ledger that this account belongs to.

          name: The name of the ledger account.

          normal_balance: The normal balance of the ledger account.

          currency_exponent: The currency exponent of the ledger account.

          description: The description of the ledger account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledger_accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "normal_balance": normal_balance,
                    "ledger_id": ledger_id,
                    "currency": currency,
                    "currency_exponent": currency_exponent,
                    "metadata": metadata,
                },
                ledger_account_create_params.LedgerAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    def retrieve(
        self,
        id: str,
        *,
        balances: ledger_account_retrieve_params.Balances | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccount:
        """
        Get details on a single ledger account.

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
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {"balances": balances}, ledger_account_retrieve_params.LedgerAccountRetrieveParams
                ),
            ),
            cast_to=LedgerAccount,
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
    ) -> LedgerAccount:
        """
        Update the details of a ledger account.

        Args:
          description: The description of the ledger account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: The name of the ledger account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/api/ledger_accounts/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_update_params.LedgerAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        balances: ledger_account_list_params.Balances | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[LedgerAccount]:
        """
        Get a list of ledger accounts.

        Args:
          balances: For example, if you want the balances as of a particular effective date
              (YYYY-MM-DD), the encoded query string would be
              balances%5Bas_of_date%5D=2000-12-31. The balances as of a date are inclusive of
              entries with that exact date.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_accounts",
            page=SyncPage[LedgerAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "metadata": metadata,
                        "id": id,
                        "name": name,
                        "ledger_id": ledger_id,
                        "balances": balances,
                        "updated_at": updated_at,
                        "ledger_account_category_id": ledger_account_category_id,
                    },
                    ledger_account_list_params.LedgerAccountListParams,
                ),
            ),
            model=LedgerAccount,
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
    ) -> LedgerAccount:
        """Delete a ledger account."""
        return self._delete(
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )


class AsyncLedgerAccounts(AsyncAPIResource):
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
    ) -> LedgerAccount:
        """
        Create a ledger account.

        Args:
          currency: The currency of the ledger account.

          ledger_id: The id of the ledger that this account belongs to.

          name: The name of the ledger account.

          normal_balance: The normal balance of the ledger account.

          currency_exponent: The currency exponent of the ledger account.

          description: The description of the ledger account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledger_accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "normal_balance": normal_balance,
                    "ledger_id": ledger_id,
                    "currency": currency,
                    "currency_exponent": currency_exponent,
                    "metadata": metadata,
                },
                ledger_account_create_params.LedgerAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    async def retrieve(
        self,
        id: str,
        *,
        balances: ledger_account_retrieve_params.Balances | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccount:
        """
        Get details on a single ledger account.

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
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {"balances": balances}, ledger_account_retrieve_params.LedgerAccountRetrieveParams
                ),
            ),
            cast_to=LedgerAccount,
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
    ) -> LedgerAccount:
        """
        Update the details of a ledger account.

        Args:
          description: The description of the ledger account.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: The name of the ledger account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/api/ledger_accounts/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                },
                ledger_account_update_params.LedgerAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        balances: ledger_account_list_params.Balances | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[LedgerAccount, AsyncPage[LedgerAccount]]:
        """
        Get a list of ledger accounts.

        Args:
          balances: For example, if you want the balances as of a particular effective date
              (YYYY-MM-DD), the encoded query string would be
              balances%5Bas_of_date%5D=2000-12-31. The balances as of a date are inclusive of
              entries with that exact date.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          updated_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_accounts",
            page=AsyncPage[LedgerAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "metadata": metadata,
                        "id": id,
                        "name": name,
                        "ledger_id": ledger_id,
                        "balances": balances,
                        "updated_at": updated_at,
                        "ledger_account_category_id": ledger_account_category_id,
                    },
                    ledger_account_list_params.LedgerAccountListParams,
                ),
            ),
            model=LedgerAccount,
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
    ) -> LedgerAccount:
        """Delete a ledger account."""
        return await self._delete(
            f"/api/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerAccount,
        )
