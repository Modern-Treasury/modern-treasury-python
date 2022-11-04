# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Query, Headers, Timeout, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared import RoutingDetail
from ..types.routing_detail_list_params import RoutingDetailListParams
from ..types.routing_detail_create_params import RoutingDetailCreateParams

__all__ = ["RoutingDetails", "AsyncRoutingDetails"]


class RoutingDetails(SyncAPIResource):
    def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: RoutingDetailCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RoutingDetail:
        """Create a routing detail for a single external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body=maybe_transform(body, RoutingDetailCreateParams),
            options=options,
            cast_to=RoutingDetail,
        )

    def retrieve(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RoutingDetail:
        """Get a single routing detail for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=options,
            cast_to=RoutingDetail,
        )

    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: RoutingDetailListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[RoutingDetail]:
        """Get a list of routing details for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, RoutingDetailListParams))
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=SyncPage[RoutingDetail],
            options=options,
            model=RoutingDetail,
        )

    def delete(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a routing detail for a single external account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=options,
            cast_to=NoneType,
        )


class AsyncRoutingDetails(AsyncAPIResource):
    async def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: RoutingDetailCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RoutingDetail:
        """Create a routing detail for a single external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/api/{accounts_type}/{account_id}/routing_details",
            body=maybe_transform(body, RoutingDetailCreateParams),
            options=options,
            cast_to=RoutingDetail,
        )

    async def retrieve(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RoutingDetail:
        """Get a single routing detail for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=options,
            cast_to=RoutingDetail,
        )

    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: RoutingDetailListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[RoutingDetail, AsyncPage[RoutingDetail]]:
        """Get a list of routing details for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, RoutingDetailListParams))
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/routing_details",
            page=AsyncPage[RoutingDetail],
            options=options,
            model=RoutingDetail,
        )

    async def delete(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a routing detail for a single external account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/{accounts_type}/{account_id}/routing_details/{id}",
            options=options,
            cast_to=NoneType,
        )
