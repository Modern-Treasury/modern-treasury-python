# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional

from ..types import virtual_account_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.virtual_account import VirtualAccount

__all__ = ["VirtualAccounts", "AsyncVirtualAccounts"]


class VirtualAccounts(SyncAPIResource):
    def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        internal_account_id: str,
        account_details: List[virtual_account_create_params.AccountDetails] | NotGiven = NOT_GIVEN,
        routing_details: List[virtual_account_create_params.RoutingDetails] | NotGiven = NOT_GIVEN,
        debit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        credit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> VirtualAccount:
        """
        Args:
          name: The name of the virtual account.

          description: An optional description for internal use.

          counterparty_id: The ID of the counterparty that the virtual account belongs to.

          internal_account_id: The ID of the internal account that this virtual account is associated with.

          account_details: An array of account detail objects.

          routing_details: An array of routing detail objects.

          debit_ledger_account_id: The ID of a debit normal ledger account. When money enters the virtual account,
              this ledger account will be debited. Must be accompanied by a
              credit_ledger_account_id if present.

          credit_ledger_account_id: The ID of a credit normal ledger account. When money leaves the virtual account,
              this ledger account will be credited. Must be accompanied by a
              debit_ledger_account_id if present.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/api/virtual_accounts",
            body={
                "name": name,
                "description": description,
                "counterparty_id": counterparty_id,
                "internal_account_id": internal_account_id,
                "account_details": account_details,
                "routing_details": routing_details,
                "debit_ledger_account_id": debit_ledger_account_id,
                "credit_ledger_account_id": credit_ledger_account_id,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=VirtualAccount,
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
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/virtual_accounts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> VirtualAccount:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/api/virtual_accounts/{id}",
            body={
                "name": name,
                "counterparty_id": counterparty_id,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=VirtualAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[VirtualAccount]:
        """
        Get a list of virtual accounts.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/virtual_accounts",
            page=SyncPage[VirtualAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "internal_account_id": internal_account_id,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                },
            ),
            model=VirtualAccount,
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
    ) -> VirtualAccount:
        return self._delete(
            f"/api/virtual_accounts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=VirtualAccount,
        )


class AsyncVirtualAccounts(AsyncAPIResource):
    async def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        internal_account_id: str,
        account_details: List[virtual_account_create_params.AccountDetails] | NotGiven = NOT_GIVEN,
        routing_details: List[virtual_account_create_params.RoutingDetails] | NotGiven = NOT_GIVEN,
        debit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        credit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> VirtualAccount:
        """
        Args:
          name: The name of the virtual account.

          description: An optional description for internal use.

          counterparty_id: The ID of the counterparty that the virtual account belongs to.

          internal_account_id: The ID of the internal account that this virtual account is associated with.

          account_details: An array of account detail objects.

          routing_details: An array of routing detail objects.

          debit_ledger_account_id: The ID of a debit normal ledger account. When money enters the virtual account,
              this ledger account will be debited. Must be accompanied by a
              credit_ledger_account_id if present.

          credit_ledger_account_id: The ID of a credit normal ledger account. When money leaves the virtual account,
              this ledger account will be credited. Must be accompanied by a
              debit_ledger_account_id if present.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/api/virtual_accounts",
            body={
                "name": name,
                "description": description,
                "counterparty_id": counterparty_id,
                "internal_account_id": internal_account_id,
                "account_details": account_details,
                "routing_details": routing_details,
                "debit_ledger_account_id": debit_ledger_account_id,
                "credit_ledger_account_id": credit_ledger_account_id,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=VirtualAccount,
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
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/virtual_accounts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> VirtualAccount:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/api/virtual_accounts/{id}",
            body={
                "name": name,
                "counterparty_id": counterparty_id,
                "metadata": metadata,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=VirtualAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[VirtualAccount, AsyncPage[VirtualAccount]]:
        """
        Get a list of virtual accounts.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/virtual_accounts",
            page=AsyncPage[VirtualAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "internal_account_id": internal_account_id,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                },
            ),
            model=VirtualAccount,
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
    ) -> VirtualAccount:
        return await self._delete(
            f"/api/virtual_accounts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=VirtualAccount,
        )
