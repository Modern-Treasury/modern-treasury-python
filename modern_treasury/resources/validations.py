# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options
from ..types.routing_number_lookup_request import RoutingNumberLookupRequest
from ..types.validation_validate_routing_number_params import (
    ValidationValidateRoutingNumberParams,
)

__all__ = ["Validations", "AsyncValidations"]


class Validations(SyncAPIResource):
    def validate_routing_number(
        self,
        query: ValidationValidateRoutingNumberParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> RoutingNumberLookupRequest:
        """
        Validates the routing number information supplied without creating a routing
        detail
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            "/api/validations/routing_numbers",
            options=options,
            cast_to=RoutingNumberLookupRequest,
        )


class AsyncValidations(AsyncAPIResource):
    async def validate_routing_number(
        self,
        query: ValidationValidateRoutingNumberParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> RoutingNumberLookupRequest:
        """
        Validates the routing number information supplied without creating a routing
        detail
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            "/api/validations/routing_numbers",
            options=options,
            cast_to=RoutingNumberLookupRequest,
        )
