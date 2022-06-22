# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.line_item import LineItem
from ..types.line_item_list_params import LineItemListParams
from ..types.line_item_update_params import LineItemUpdateParams

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    def retrieve(
        self,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LineItem:
        """Get a single line item"""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            options=options,
            cast_to=LineItem,
        )

    def update(
        self,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        id: str,
        body: LineItemUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LineItem:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            body=body,
            options=options,
            cast_to=LineItem,
        )

    def list(
        self,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        query: LineItemListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LineItem]:
        """Get a list of line items"""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            f"/api/{itemizable_type}/{itemizable_id}/line_items",
            page=SyncPage[LineItem],
            options=options,
            model=LineItem,
        )


class AsyncLineItems(AsyncAPIResource):
    async def retrieve(
        self,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LineItem:
        """Get a single line item"""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            options=options,
            cast_to=LineItem,
        )

    async def update(
        self,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        id: str,
        body: LineItemUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LineItem:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            body=body,
            options=options,
            cast_to=LineItem,
        )

    def list(
        self,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        query: LineItemListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LineItem, AsyncPage[LineItem]]:
        """Get a list of line items"""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            f"/api/{itemizable_type}/{itemizable_id}/line_items",
            page=AsyncPage[LineItem],
            options=options,
            model=LineItem,
        )
