# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account_detail import AccountDetail

__all__ = ["AccountDetails", "AsyncAccountDetails"]


class AccountDetails(SyncAPIResource):
    def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        account_number: str,
        account_number_type: Literal["clabe", "iban", "other", "pan", "wallet_address"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
        """
        return self._post(
            f"/api/{accounts_type}/{account_id}/account_details",
            body={
                "account_number": account_number,
                "account_number_type": account_number_type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountDetail,
        )

    def retrieve(
        self,
        id: str,
        *,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountDetail:
        """Get a single account detail for a single internal or external account."""
        return self._get(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountDetail,
        )

    def list(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[AccountDetail]:
        """
        Get a list of account details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/account_details",
            page=SyncPage[AccountDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
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
    ) -> None:
        """Delete a single account detail for an external account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class AsyncAccountDetails(AsyncAPIResource):
    async def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        account_number: str,
        account_number_type: Literal["clabe", "iban", "other", "pan", "wallet_address"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
        """
        return await self._post(
            f"/api/{accounts_type}/{account_id}/account_details",
            body={
                "account_number": account_number,
                "account_number_type": account_number_type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountDetail,
        )

    async def retrieve(
        self,
        id: str,
        *,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountDetail:
        """Get a single account detail for a single internal or external account."""
        return await self._get(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountDetail,
        )

    def list(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[AccountDetail, AsyncPage[AccountDetail]]:
        """
        Get a list of account details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/account_details",
            page=AsyncPage[AccountDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
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
    ) -> None:
        """Delete a single account detail for an external account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )
