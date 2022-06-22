# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.paper_item import PaperItem
from ..types.paper_item_list_params import PaperItemListParams

__all__ = ["PaperItems", "AsyncPaperItems"]


class PaperItems(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaperItem:
        """Get details on a single paper item."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/paper_items/{id}",
            options=options,
            cast_to=PaperItem,
        )

    def list(
        self,
        query: PaperItemListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[PaperItem]:
        """Get a list of all paper items."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/paper_items",
            page=SyncPage[PaperItem],
            options=options,
            model=PaperItem,
        )


class AsyncPaperItems(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaperItem:
        """Get details on a single paper item."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/paper_items/{id}",
            options=options,
            cast_to=PaperItem,
        )

    def list(
        self,
        query: PaperItemListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[PaperItem, AsyncPage[PaperItem]]:
        """Get a list of all paper items."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/paper_items",
            page=AsyncPage[PaperItem],
            options=options,
            model=PaperItem,
        )
