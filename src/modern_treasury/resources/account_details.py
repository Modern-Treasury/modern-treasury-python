# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import AccountDetail, account_detail_list_params, account_detail_create_params
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
from ..types.shared import AccountsType

__all__ = ["AccountDetails", "AsyncAccountDetails"]


class AccountDetails(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountDetailsWithRawResponse:
        return AccountDetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountDetailsWithStreamingResponse:
        return AccountDetailsWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        account_number: str,
        account_number_type: Literal["clabe", "hk_number", "iban", "other", "pan", "wallet_address"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountDetail:
        """
        Create an account detail for an external account.

        Args:
          account_number: The account number for the bank account.

          account_number_type: One of `iban`, `clabe`, `wallet_address`, or `other`. Use `other` if the bank
              account number is in a generic format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/api/{accounts_type}/{account_id}/account_details",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "account_number_type": account_number_type,
                },
                account_detail_create_params.AccountDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountDetail,
        )

    def retrieve(
        self,
        id: str,
        *,
        accounts_type: AccountsType,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountDetail:
        """
        Get a single account detail for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountDetail,
        )

    def list(
        self,
        account_id: str,
        *,
        accounts_type: AccountsType,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[AccountDetail]:
        """
        Get a list of account details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/account_details",
            page=SyncPage[AccountDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                    },
                    account_detail_list_params.AccountDetailListParams,
                ),
            ),
            model=AccountDetail,
        )

    def delete(
        self,
        id: str,
        *,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a single account detail for an external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncAccountDetails(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountDetailsWithRawResponse:
        return AsyncAccountDetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountDetailsWithStreamingResponse:
        return AsyncAccountDetailsWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        account_number: str,
        account_number_type: Literal["clabe", "hk_number", "iban", "other", "pan", "wallet_address"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountDetail:
        """
        Create an account detail for an external account.

        Args:
          account_number: The account number for the bank account.

          account_number_type: One of `iban`, `clabe`, `wallet_address`, or `other`. Use `other` if the bank
              account number is in a generic format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/api/{accounts_type}/{account_id}/account_details",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "account_number_type": account_number_type,
                },
                account_detail_create_params.AccountDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountDetail,
        )

    async def retrieve(
        self,
        id: str,
        *,
        accounts_type: AccountsType,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountDetail:
        """
        Get a single account detail for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountDetail,
        )

    def list(
        self,
        account_id: str,
        *,
        accounts_type: AccountsType,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountDetail, AsyncPage[AccountDetail]]:
        """
        Get a list of account details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/account_details",
            page=AsyncPage[AccountDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                    },
                    account_detail_list_params.AccountDetailListParams,
                ),
            ),
            model=AccountDetail,
        )

    async def delete(
        self,
        id: str,
        *,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a single account detail for an external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not accounts_type:
            raise ValueError(f"Expected a non-empty value for `accounts_type` but received {accounts_type!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AccountDetailsWithRawResponse:
    def __init__(self, account_details: AccountDetails) -> None:
        self._account_details = account_details

        self.create = _legacy_response.to_raw_response_wrapper(
            account_details.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            account_details.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            account_details.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            account_details.delete,
        )


class AsyncAccountDetailsWithRawResponse:
    def __init__(self, account_details: AsyncAccountDetails) -> None:
        self._account_details = account_details

        self.create = _legacy_response.async_to_raw_response_wrapper(
            account_details.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            account_details.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            account_details.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            account_details.delete,
        )


class AccountDetailsWithStreamingResponse:
    def __init__(self, account_details: AccountDetails) -> None:
        self._account_details = account_details

        self.create = to_streamed_response_wrapper(
            account_details.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_details.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            account_details.list,
        )
        self.delete = to_streamed_response_wrapper(
            account_details.delete,
        )


class AsyncAccountDetailsWithStreamingResponse:
    def __init__(self, account_details: AsyncAccountDetails) -> None:
        self._account_details = account_details

        self.create = async_to_streamed_response_wrapper(
            account_details.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_details.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            account_details.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            account_details.delete,
        )
