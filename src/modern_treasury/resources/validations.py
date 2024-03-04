# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import RoutingNumberLookupRequest, validation_validate_routing_number_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["Validations", "AsyncValidations"]


class Validations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidationsWithRawResponse:
        return ValidationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidationsWithStreamingResponse:
        return ValidationsWithStreamingResponse(self)

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
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "in_ifsc",
            "jp_zengin_code",
            "mx_bank_identifier",
            "my_branch_code",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingNumberLookupRequest:
        """
        Validates the routing number information supplied without creating a routing
        detail

        Args:
          routing_number: The routing number that is being validated.

          routing_number_type: The type of routing number. See
              https://docs.moderntreasury.com/platform/reference/routing-detail-object for
              more details. In sandbox mode we currently only support `aba` and `swift` with
              routing numbers '123456789' and 'GRINUST0XXX' respectively.

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
    @cached_property
    def with_raw_response(self) -> AsyncValidationsWithRawResponse:
        return AsyncValidationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidationsWithStreamingResponse:
        return AsyncValidationsWithStreamingResponse(self)

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
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "in_ifsc",
            "jp_zengin_code",
            "mx_bank_identifier",
            "my_branch_code",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingNumberLookupRequest:
        """
        Validates the routing number information supplied without creating a routing
        detail

        Args:
          routing_number: The routing number that is being validated.

          routing_number_type: The type of routing number. See
              https://docs.moderntreasury.com/platform/reference/routing-detail-object for
              more details. In sandbox mode we currently only support `aba` and `swift` with
              routing numbers '123456789' and 'GRINUST0XXX' respectively.

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
                query=await async_maybe_transform(
                    {
                        "routing_number": routing_number,
                        "routing_number_type": routing_number_type,
                    },
                    validation_validate_routing_number_params.ValidationValidateRoutingNumberParams,
                ),
            ),
            cast_to=RoutingNumberLookupRequest,
        )


class ValidationsWithRawResponse:
    def __init__(self, validations: Validations) -> None:
        self._validations = validations

        self.validate_routing_number = _legacy_response.to_raw_response_wrapper(
            validations.validate_routing_number,
        )


class AsyncValidationsWithRawResponse:
    def __init__(self, validations: AsyncValidations) -> None:
        self._validations = validations

        self.validate_routing_number = _legacy_response.async_to_raw_response_wrapper(
            validations.validate_routing_number,
        )


class ValidationsWithStreamingResponse:
    def __init__(self, validations: Validations) -> None:
        self._validations = validations

        self.validate_routing_number = to_streamed_response_wrapper(
            validations.validate_routing_number,
        )


class AsyncValidationsWithStreamingResponse:
    def __init__(self, validations: AsyncValidations) -> None:
        self._validations = validations

        self.validate_routing_number = async_to_streamed_response_wrapper(
            validations.validate_routing_number,
        )
