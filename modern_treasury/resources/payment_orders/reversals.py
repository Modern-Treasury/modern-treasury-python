# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payment_orders.reversal import Reversal
from ...types.payment_orders.reversal_list_params import ReversalListParams
from ...types.payment_orders.reversal_create_params import ReversalCreateParams

__all__ = ["Reversals", "AsyncReversals"]


class Reversals(SyncAPIResource):
    def create(
        self,
        payment_order_id: str,
        body: ReversalCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Reversal:
        """Create a reversal for a payment order."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/api/payment_orders/{payment_order_id}/reversals",
            body=maybe_transform(body, ReversalCreateParams),
            options=options,
            cast_to=Reversal,
        )

    def retrieve(
        self,
        payment_order_id: str,
        reversal_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Reversal:
        """Get details on a single reversal of a payment order."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/payment_orders/{payment_order_id}/reversals/{reversal_id}",
            options=options,
            cast_to=Reversal,
        )

    def list(
        self,
        payment_order_id: str,
        query: ReversalListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Reversal]:
        """Get a list of all reversals of a payment order."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, ReversalListParams))
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=SyncPage[Reversal],
            options=options,
            model=Reversal,
        )


class AsyncReversals(AsyncAPIResource):
    async def create(
        self,
        payment_order_id: str,
        body: ReversalCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Reversal:
        """Create a reversal for a payment order."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/api/payment_orders/{payment_order_id}/reversals",
            body=maybe_transform(body, ReversalCreateParams),
            options=options,
            cast_to=Reversal,
        )

    async def retrieve(
        self,
        payment_order_id: str,
        reversal_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Reversal:
        """Get details on a single reversal of a payment order."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/payment_orders/{payment_order_id}/reversals/{reversal_id}",
            options=options,
            cast_to=Reversal,
        )

    def list(
        self,
        payment_order_id: str,
        query: ReversalListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Reversal, AsyncPage[Reversal]]:
        """Get a list of all reversals of a payment order."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, ReversalListParams))
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=AsyncPage[Reversal],
            options=options,
            model=Reversal,
        )
