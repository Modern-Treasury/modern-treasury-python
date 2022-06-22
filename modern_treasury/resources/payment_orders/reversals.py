# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union

from ..._types import NOT_GIVEN, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payment_orders.reversal import Reversal
from ...types.payment_orders.reversal_list_params import ReversalListParams

__all__ = ["Reversals", "AsyncReversals"]


class Reversals(SyncAPIResource):
    def list(
        self,
        payment_order_id: str,
        query: ReversalListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Reversal]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=SyncPage[Reversal],
            options=options,
            model=Reversal,
        )


class AsyncReversals(AsyncAPIResource):
    def list(
        self,
        payment_order_id: str,
        query: ReversalListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Reversal, AsyncPage[Reversal]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=AsyncPage[Reversal],
            options=options,
            model=Reversal,
        )
