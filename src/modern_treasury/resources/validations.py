# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import (
    RoutingNumberLookupRequest,
    validation_validate_routing_number_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Validations", "AsyncValidations"]


class Validations(SyncAPIResource):
    def validate_routing_number(
        self,
        *,
        routing_number: str,
        routing_number_type: Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "gb_sort_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "se_bankgiro_clearing_code",
            "swift",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoutingNumberLookupRequest:
        """
        Validates the routing number information supplied without creating a routing
        detail

        Args:
          routing_number: The routing number that is being validated.

          routing_number_type: One of `aba`, `au_bsb`, `br_codigo`, `ca_cpa`, `cnaps`, `gb_sort_code`,
              `in_ifsc`, `my_branch_code`, `se_bankgiro_clearing_code`, or `swift`. In sandbox
              mode we currently only support `aba` and `swift` with routing numbers
              '123456789' and 'GRINUST0XXX' respectively.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/validations/routing_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "routing_number": routing_number,
                        "routing_number_type": routing_number_type,
                    },
                    validation_validate_routing_number_params.ValidationValidateRoutingNumberParams,
                ),
            ),
            cast_to=RoutingNumberLookupRequest,
        )


class AsyncValidations(AsyncAPIResource):
    async def validate_routing_number(
        self,
        *,
        routing_number: str,
        routing_number_type: Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "gb_sort_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "se_bankgiro_clearing_code",
            "swift",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoutingNumberLookupRequest:
        """
        Validates the routing number information supplied without creating a routing
        detail

        Args:
          routing_number: The routing number that is being validated.

          routing_number_type: One of `aba`, `au_bsb`, `br_codigo`, `ca_cpa`, `cnaps`, `gb_sort_code`,
              `in_ifsc`, `my_branch_code`, `se_bankgiro_clearing_code`, or `swift`. In sandbox
              mode we currently only support `aba` and `swift` with routing numbers
              '123456789' and 'GRINUST0XXX' respectively.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/validations/routing_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "routing_number": routing_number,
                        "routing_number_type": routing_number_type,
                    },
                    validation_validate_routing_number_params.ValidationValidateRoutingNumberParams,
                ),
            ),
            cast_to=RoutingNumberLookupRequest,
        )
