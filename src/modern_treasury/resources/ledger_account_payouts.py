# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from ..types import LedgerAccountPayout
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["LedgerAccountPayouts", "AsyncLedgerAccountPayouts"]


class LedgerAccountPayouts(SyncAPIResource):
    def create(
        self,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["pending", "posted"]] | NotGiven = NOT_GIVEN,
        payout_ledger_account_id: str,
        funding_ledger_account_id: str,
        effective_at_upper_bound: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccountPayout:
        """
        Create a ledger account payout.

        Args:
          description: The description of the ledger account payout.

          status: The status of the ledger account payout. It is set to `pending` by default. To
              post a ledger account payout at creation, use `posted`.

          payout_ledger_account_id: The id of the payout ledger account whose ledger entries are queried against,
              and its balance is reduced as a result.

          funding_ledger_account_id: The id of the funding ledger account that sends to or receives funds from the
              payout ledger account.

          effective_at_upper_bound: The maximum effective_at timestamp of the ledger entries to be included in the
              ledger account payout. The default value is the created_at timestamp of the
              ledger account payout.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/api/ledger_account_payouts",
            body={
                "description": description,
                "status": status,
                "payout_ledger_account_id": payout_ledger_account_id,
                "funding_ledger_account_id": funding_ledger_account_id,
                "effective_at_upper_bound": effective_at_upper_bound,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerAccountPayout,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["posted", "archived"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccountPayout:
        """
        Update the details of a ledger account payout.

        Args:
          description: The description of the ledger account payout.

          status: To post a pending ledger account payout, use `posted`. To archive a pending
              ledger transaction, use `archived`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/api/ledger_account_payouts/{id}",
            body={
                "description": description,
                "status": status,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerAccountPayout,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        payout_ledger_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[LedgerAccountPayout]:
        """
        Get a list of ledger account payouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_account_payouts",
            page=SyncPage[LedgerAccountPayout],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "payout_ledger_account_id": payout_ledger_account_id,
                },
            ),
            model=LedgerAccountPayout,
        )

    def retireve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccountPayout:
        """Get details on a single ledger account payout."""
        return self._get(
            f"/api/ledger_account_payouts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerAccountPayout,
        )


class AsyncLedgerAccountPayouts(AsyncAPIResource):
    async def create(
        self,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["pending", "posted"]] | NotGiven = NOT_GIVEN,
        payout_ledger_account_id: str,
        funding_ledger_account_id: str,
        effective_at_upper_bound: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccountPayout:
        """
        Create a ledger account payout.

        Args:
          description: The description of the ledger account payout.

          status: The status of the ledger account payout. It is set to `pending` by default. To
              post a ledger account payout at creation, use `posted`.

          payout_ledger_account_id: The id of the payout ledger account whose ledger entries are queried against,
              and its balance is reduced as a result.

          funding_ledger_account_id: The id of the funding ledger account that sends to or receives funds from the
              payout ledger account.

          effective_at_upper_bound: The maximum effective_at timestamp of the ledger entries to be included in the
              ledger account payout. The default value is the created_at timestamp of the
              ledger account payout.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/api/ledger_account_payouts",
            body={
                "description": description,
                "status": status,
                "payout_ledger_account_id": payout_ledger_account_id,
                "funding_ledger_account_id": funding_ledger_account_id,
                "effective_at_upper_bound": effective_at_upper_bound,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerAccountPayout,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["posted", "archived"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccountPayout:
        """
        Update the details of a ledger account payout.

        Args:
          description: The description of the ledger account payout.

          status: To post a pending ledger account payout, use `posted`. To archive a pending
              ledger transaction, use `archived`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/api/ledger_account_payouts/{id}",
            body={
                "description": description,
                "status": status,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerAccountPayout,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        payout_ledger_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[LedgerAccountPayout, AsyncPage[LedgerAccountPayout]]:
        """
        Get a list of ledger account payouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/ledger_account_payouts",
            page=AsyncPage[LedgerAccountPayout],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "payout_ledger_account_id": payout_ledger_account_id,
                },
            ),
            model=LedgerAccountPayout,
        )

    async def retireve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LedgerAccountPayout:
        """Get details on a single ledger account payout."""
        return await self._get(
            f"/api/ledger_account_payouts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LedgerAccountPayout,
        )