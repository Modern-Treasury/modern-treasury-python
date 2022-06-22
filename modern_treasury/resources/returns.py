# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.return_object import ReturnObject
from ..types.return_list_params import ReturnListParams
from ..types.return_create_params import ReturnCreateParams

__all__ = ["Returns", "AsyncReturns"]


class Returns(SyncAPIResource):
    def create(
        self,
        body: ReturnCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Create a return."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/returns",
            body=body,
            options=options,
            cast_to=ReturnObject,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Get a single return."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/returns/{id}",
            options=options,
            cast_to=ReturnObject,
        )

    def list(
        self,
        query: ReturnListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ReturnObject]:
        """Get a list of returns."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/returns",
            page=SyncPage[ReturnObject],
            options=options,
            model=ReturnObject,
        )


class AsyncReturns(AsyncAPIResource):
    async def create(
        self,
        body: ReturnCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Create a return."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/returns",
            body=body,
            options=options,
            cast_to=ReturnObject,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Get a single return."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/returns/{id}",
            options=options,
            cast_to=ReturnObject,
        )

    def list(
        self,
        query: ReturnListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ReturnObject, AsyncPage[ReturnObject]]:
        """Get a list of returns."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/returns",
            page=AsyncPage[ReturnObject],
            options=options,
            model=ReturnObject,
        )
