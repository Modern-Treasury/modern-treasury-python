# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.routing_detail import RoutingDetail

__all__ = ["RoutingDetails", "AsyncRoutingDetails"]


class RoutingDetails(SyncAPIResource):
    def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        routing_number: str,
        routing_number_type: Literal[
            "aba", "au_bsb", "br_codigo", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "swift"
        ],
        payment_type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "cross_border",
                "eft",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> RoutingDetail:
        """
        Create a routing detail for a single external account.

        Args:
          routing_number: The routing number of the bank.

          routing_number_type: One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`.

          payment_type: If the routing detail is to be used for a specific payment type this field will
              be populated, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body={
                "routing_number": routing_number,
                "routing_number_type": routing_number_type,
                "payment_type": payment_type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=RoutingDetail,
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
    ) -> RoutingDetail:
        """Get a single routing detail for a single internal or external account."""
        return self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=RoutingDetail,
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
    ) -> SyncPage[RoutingDetail]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=SyncPage[RoutingDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=RoutingDetail,
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
        """Delete a routing detail for a single external account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class AsyncRoutingDetails(AsyncAPIResource):
    async def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        routing_number: str,
        routing_number_type: Literal[
            "aba", "au_bsb", "br_codigo", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "swift"
        ],
        payment_type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "cross_border",
                "eft",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> RoutingDetail:
        """
        Create a routing detail for a single external account.

        Args:
          routing_number: The routing number of the bank.

          routing_number_type: One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`.

          payment_type: If the routing detail is to be used for a specific payment type this field will
              be populated, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body={
                "routing_number": routing_number,
                "routing_number_type": routing_number_type,
                "payment_type": payment_type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=RoutingDetail,
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
    ) -> RoutingDetail:
        """Get a single routing detail for a single internal or external account."""
        return await self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=RoutingDetail,
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
    ) -> AsyncPaginator[RoutingDetail, AsyncPage[RoutingDetail]]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=AsyncPage[RoutingDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=RoutingDetail,
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
        """Delete a routing detail for a single external account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )
