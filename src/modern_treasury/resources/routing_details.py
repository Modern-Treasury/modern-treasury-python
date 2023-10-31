# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from typing_extensions import Literal

from ..types import (
    RoutingDetail,
    routing_detail_list_params,
    routing_detail_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared import AccountsType

if TYPE_CHECKING:
    from .._client import ModernTreasury, AsyncModernTreasury

__all__ = ["RoutingDetails", "AsyncRoutingDetails"]


class RoutingDetails(SyncAPIResource):
    with_raw_response: RoutingDetailsWithRawResponse

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = RoutingDetailsWithRawResponse(self)

    def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        routing_number: str,
        routing_number_type: Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "nz_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ],
        payment_type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "chats",
                "check",
                "cross_border",
                "eft",
                "interac",
                "masav",
                "neft",
                "nics",
                "nz_becs",
                "provxchange",
                "rtp",
                "se_bankgirot",
                "sen",
                "sepa",
                "sg_giro",
                "sic",
                "signet",
                "wire",
                "zengin",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RoutingDetail:
        """
        Create a routing detail for a single external account.

        Args:
          routing_number: The routing number of the bank.

          routing_number_type: The type of routing number. See
              https://docs.moderntreasury.com/platform/reference/routing-detail-object for
              more details.

          payment_type: If the routing detail is to be used for a specific payment type this field will
              be populated, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body=maybe_transform(
                {
                    "routing_number": routing_number,
                    "routing_number_type": routing_number_type,
                    "payment_type": payment_type,
                },
                routing_detail_create_params.RoutingDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RoutingDetail,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoutingDetail:
        """
        Get a single routing detail for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingDetail,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[RoutingDetail]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=SyncPage[RoutingDetail],
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
                    routing_detail_list_params.RoutingDetailListParams,
                ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a routing detail for a single external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncRoutingDetails(AsyncAPIResource):
    with_raw_response: AsyncRoutingDetailsWithRawResponse

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncRoutingDetailsWithRawResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        accounts_type: Literal["external_accounts"],
        routing_number: str,
        routing_number_type: Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "nz_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ],
        payment_type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "chats",
                "check",
                "cross_border",
                "eft",
                "interac",
                "masav",
                "neft",
                "nics",
                "nz_becs",
                "provxchange",
                "rtp",
                "se_bankgirot",
                "sen",
                "sepa",
                "sg_giro",
                "sic",
                "signet",
                "wire",
                "zengin",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RoutingDetail:
        """
        Create a routing detail for a single external account.

        Args:
          routing_number: The routing number of the bank.

          routing_number_type: The type of routing number. See
              https://docs.moderntreasury.com/platform/reference/routing-detail-object for
              more details.

          payment_type: If the routing detail is to be used for a specific payment type this field will
              be populated, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body=maybe_transform(
                {
                    "routing_number": routing_number,
                    "routing_number_type": routing_number_type,
                    "payment_type": payment_type,
                },
                routing_detail_create_params.RoutingDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RoutingDetail,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoutingDetail:
        """
        Get a single routing detail for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingDetail,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RoutingDetail, AsyncPage[RoutingDetail]]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=AsyncPage[RoutingDetail],
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
                    routing_detail_list_params.RoutingDetailListParams,
                ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a routing detail for a single external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class RoutingDetailsWithRawResponse:
    def __init__(self, routing_details: RoutingDetails) -> None:
        self.create = to_raw_response_wrapper(
            routing_details.create,
        )
        self.retrieve = to_raw_response_wrapper(
            routing_details.retrieve,
        )
        self.list = to_raw_response_wrapper(
            routing_details.list,
        )
        self.delete = to_raw_response_wrapper(
            routing_details.delete,
        )


class AsyncRoutingDetailsWithRawResponse:
    def __init__(self, routing_details: AsyncRoutingDetails) -> None:
        self.create = async_to_raw_response_wrapper(
            routing_details.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            routing_details.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            routing_details.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routing_details.delete,
        )
