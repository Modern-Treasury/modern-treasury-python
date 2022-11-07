# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload
from typing_extensions import Literal

from ..types import shared
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NoneType, NotGiven
from .._utils import required_args, deprecated_positional_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.routing_detail_list_params import RoutingDetailListParams
from ..types.routing_detail_create_params import RoutingDetailCreateParams

__all__ = ["RoutingDetails", "AsyncRoutingDetails"]


class RoutingDetails(SyncAPIResource):
    @overload
    def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        *,
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
                "eft",
                "global_pay",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
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
        ...

    @overload
    def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: RoutingDetailCreateParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
        """Create a routing detail for a single external account."""
        ...

    @required_args(["body"], ["routing_number", "routing_number_type"])
    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type")
    def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: RoutingDetailCreateParams | None = None,
        *,
        routing_number: str | NotGiven = NOT_GIVEN,
        routing_number_type: Literal[
            "aba", "au_bsb", "br_codigo", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "swift"
        ]
        | NotGiven = NOT_GIVEN,
        payment_type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "eft",
                "global_pay",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
        """
        Create a routing detail for a single external account.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          routing_number: The routing number of the bank.

          routing_number_type: One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`.

          payment_type: If the routing detail is to be used for a specific payment type this field will
              be populated, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard RoutingDetailCreateParams type.
            body = cast(
                Any,
                {
                    "routing_number": routing_number,
                    "routing_number_type": routing_number_type,
                    "payment_type": payment_type,
                },
            )

        return self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=shared.RoutingDetail,
        )

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type", "account_id")
    def retrieve(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
        """Get a single routing detail for a single internal or external account."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=shared.RoutingDetail,
        )

    @overload
    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[shared.RoutingDetail]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: RoutingDetailListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[shared.RoutingDetail]:
        """Get a list of routing details for a single internal or external account."""
        ...

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type")
    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: RoutingDetailListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[shared.RoutingDetail]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard RoutingDetailListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=SyncPage[shared.RoutingDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=shared.RoutingDetail,
        )

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type", "account_id")
    def delete(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a routing detail for a single external account."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=NoneType,
        )


class AsyncRoutingDetails(AsyncAPIResource):
    @overload
    async def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        *,
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
                "eft",
                "global_pay",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
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
        ...

    @overload
    async def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: RoutingDetailCreateParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
        """Create a routing detail for a single external account."""
        ...

    @required_args(["body"], ["routing_number", "routing_number_type"])
    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type")
    async def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: RoutingDetailCreateParams | None = None,
        *,
        routing_number: str | NotGiven = NOT_GIVEN,
        routing_number_type: Literal[
            "aba", "au_bsb", "br_codigo", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "swift"
        ]
        | NotGiven = NOT_GIVEN,
        payment_type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "eft",
                "global_pay",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
        """
        Create a routing detail for a single external account.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          routing_number: The routing number of the bank.

          routing_number_type: One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`.

          payment_type: If the routing detail is to be used for a specific payment type this field will
              be populated, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard RoutingDetailCreateParams type.
            body = cast(
                Any,
                {
                    "routing_number": routing_number,
                    "routing_number_type": routing_number_type,
                    "payment_type": payment_type,
                },
            )

        return await self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=shared.RoutingDetail,
        )

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type", "account_id")
    async def retrieve(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> shared.RoutingDetail:
        """Get a single routing detail for a single internal or external account."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=shared.RoutingDetail,
        )

    @overload
    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[shared.RoutingDetail, AsyncPage[shared.RoutingDetail]]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: RoutingDetailListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[shared.RoutingDetail, AsyncPage[shared.RoutingDetail]]:
        """Get a list of routing details for a single internal or external account."""
        ...

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type")
    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: RoutingDetailListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[shared.RoutingDetail, AsyncPage[shared.RoutingDetail]]:
        """
        Get a list of routing details for a single internal or external account.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard RoutingDetailListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=AsyncPage[shared.RoutingDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=shared.RoutingDetail,
        )

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("accounts_type", "account_id")
    async def delete(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a routing detail for a single external account."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=NoneType,
        )
