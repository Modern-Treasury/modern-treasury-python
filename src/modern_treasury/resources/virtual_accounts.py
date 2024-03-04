# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from .. import _legacy_response
from ..types import (
    VirtualAccount,
    virtual_account_list_params,
    virtual_account_create_params,
    virtual_account_update_params,
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

__all__ = ["VirtualAccounts", "AsyncVirtualAccounts"]


class VirtualAccounts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VirtualAccountsWithRawResponse:
        return VirtualAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualAccountsWithStreamingResponse:
        return VirtualAccountsWithStreamingResponse(self)

    def create(
        self,
        *,
        internal_account_id: str,
        name: str,
        account_details: Iterable[virtual_account_create_params.AccountDetail] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        credit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        debit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ledger_account: virtual_account_create_params.LedgerAccount | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        routing_details: Iterable[virtual_account_create_params.RoutingDetail] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VirtualAccount:
        """
        create virtual_account

        Args:
          internal_account_id: The ID of the internal account that this virtual account is associated with.

          name: The name of the virtual account.

          account_details: An array of account detail objects.

          counterparty_id: The ID of the counterparty that the virtual account belongs to.

          credit_ledger_account_id: The ID of a credit normal ledger account. When money leaves the virtual account,
              this ledger account will be credited. Must be accompanied by a
              debit_ledger_account_id if present.

          debit_ledger_account_id: The ID of a debit normal ledger account. When money enters the virtual account,
              this ledger account will be debited. Must be accompanied by a
              credit_ledger_account_id if present.

          description: An optional description for internal use.

          ledger_account: Specifies a ledger account object that will be created with the virtual account.
              The resulting ledger account is linked to the virtual account for auto-ledgering
              IPDs.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          routing_details: An array of routing detail objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/virtual_accounts",
            body=maybe_transform(
                {
                    "internal_account_id": internal_account_id,
                    "name": name,
                    "account_details": account_details,
                    "counterparty_id": counterparty_id,
                    "credit_ledger_account_id": credit_ledger_account_id,
                    "debit_ledger_account_id": debit_ledger_account_id,
                    "description": description,
                    "ledger_account": ledger_account,
                    "metadata": metadata,
                    "routing_details": routing_details,
                },
                virtual_account_create_params.VirtualAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualAccount:
        """
        get virtual_account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/virtual_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualAccount,
        )

    def update(
        self,
        id: str,
        *,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VirtualAccount:
        """
        update virtual_account

        Args:
          ledger_account_id: The ledger account that you'd like to link to the virtual account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/virtual_accounts/{id}",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "ledger_account_id": ledger_account_id,
                    "metadata": metadata,
                    "name": name,
                },
                virtual_account_update_params.VirtualAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VirtualAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/virtual_accounts",
            page=SyncPage[VirtualAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                    },
                    virtual_account_list_params.VirtualAccountListParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VirtualAccount:
        """
        delete virtual_account

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
            f"/api/virtual_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VirtualAccount,
        )


class AsyncVirtualAccounts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVirtualAccountsWithRawResponse:
        return AsyncVirtualAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualAccountsWithStreamingResponse:
        return AsyncVirtualAccountsWithStreamingResponse(self)

    async def create(
        self,
        *,
        internal_account_id: str,
        name: str,
        account_details: Iterable[virtual_account_create_params.AccountDetail] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        credit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        debit_ledger_account_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ledger_account: virtual_account_create_params.LedgerAccount | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        routing_details: Iterable[virtual_account_create_params.RoutingDetail] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VirtualAccount:
        """
        create virtual_account

        Args:
          internal_account_id: The ID of the internal account that this virtual account is associated with.

          name: The name of the virtual account.

          account_details: An array of account detail objects.

          counterparty_id: The ID of the counterparty that the virtual account belongs to.

          credit_ledger_account_id: The ID of a credit normal ledger account. When money leaves the virtual account,
              this ledger account will be credited. Must be accompanied by a
              debit_ledger_account_id if present.

          debit_ledger_account_id: The ID of a debit normal ledger account. When money enters the virtual account,
              this ledger account will be debited. Must be accompanied by a
              credit_ledger_account_id if present.

          description: An optional description for internal use.

          ledger_account: Specifies a ledger account object that will be created with the virtual account.
              The resulting ledger account is linked to the virtual account for auto-ledgering
              IPDs.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          routing_details: An array of routing detail objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/virtual_accounts",
            body=await async_maybe_transform(
                {
                    "internal_account_id": internal_account_id,
                    "name": name,
                    "account_details": account_details,
                    "counterparty_id": counterparty_id,
                    "credit_ledger_account_id": credit_ledger_account_id,
                    "debit_ledger_account_id": debit_ledger_account_id,
                    "description": description,
                    "ledger_account": ledger_account,
                    "metadata": metadata,
                    "routing_details": routing_details,
                },
                virtual_account_create_params.VirtualAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualAccount:
        """
        get virtual_account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/virtual_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualAccount,
        )

    async def update(
        self,
        id: str,
        *,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VirtualAccount:
        """
        update virtual_account

        Args:
          ledger_account_id: The ledger account that you'd like to link to the virtual account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/virtual_accounts/{id}",
            body=await async_maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "ledger_account_id": ledger_account_id,
                    "metadata": metadata,
                    "name": name,
                },
                virtual_account_update_params.VirtualAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VirtualAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/virtual_accounts",
            page=AsyncPage[VirtualAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                    },
                    virtual_account_list_params.VirtualAccountListParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VirtualAccount:
        """
        delete virtual_account

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
            f"/api/virtual_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VirtualAccount,
        )


class VirtualAccountsWithRawResponse:
    def __init__(self, virtual_accounts: VirtualAccounts) -> None:
        self._virtual_accounts = virtual_accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            virtual_accounts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            virtual_accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            virtual_accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            virtual_accounts.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            virtual_accounts.delete,
        )


class AsyncVirtualAccountsWithRawResponse:
    def __init__(self, virtual_accounts: AsyncVirtualAccounts) -> None:
        self._virtual_accounts = virtual_accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            virtual_accounts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            virtual_accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            virtual_accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            virtual_accounts.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            virtual_accounts.delete,
        )


class VirtualAccountsWithStreamingResponse:
    def __init__(self, virtual_accounts: VirtualAccounts) -> None:
        self._virtual_accounts = virtual_accounts

        self.create = to_streamed_response_wrapper(
            virtual_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            virtual_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            virtual_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            virtual_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            virtual_accounts.delete,
        )


class AsyncVirtualAccountsWithStreamingResponse:
    def __init__(self, virtual_accounts: AsyncVirtualAccounts) -> None:
        self._virtual_accounts = virtual_accounts

        self.create = async_to_streamed_response_wrapper(
            virtual_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            virtual_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            virtual_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            virtual_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            virtual_accounts.delete,
        )
