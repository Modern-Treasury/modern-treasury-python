# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NoneType, NotGiven
from ..._utils import extract_files
from .reversals import Reversals, AsyncReversals
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payment_order import PaymentOrder
from ...types.payment_order_list_params import PaymentOrderListParams
from ...types.payment_order_create_params import PaymentOrderCreateParams
from ...types.payment_order_update_params import PaymentOrderUpdateParams
from ...types.payment_order_create_async_params import PaymentOrderCreateAsyncParams

if TYPE_CHECKING:
    from ..._client import ModernTreasury, AsyncModernTreasury

__all__ = ["PaymentOrders", "AsyncPaymentOrders"]


class PaymentOrders(SyncAPIResource):
    reversals: Reversals

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.reversals = Reversals(client)

    def create(
        self,
        body: PaymentOrderCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaymentOrder:
        """Create a new Payment Order"""
        # Make a copy of the input so that our internal mutations (extracting files)
        # don't incidentally mutate the user's dictionary.
        body = body.copy()
        files = extract_files(body, paths=[["documents", "<array>", "file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/payment_orders",
            body=body,
            files=files,
            options=options,
            cast_to=PaymentOrder,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaymentOrder:
        """Get details on a single payment order"""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/payment_orders/{id}",
            options=options,
            cast_to=PaymentOrder,
        )

    def update(
        self,
        id: str,
        body: PaymentOrderUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaymentOrder:
        """Update a payment order"""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/payment_orders/{id}",
            body=body,
            options=options,
            cast_to=PaymentOrder,
        )

    def list(
        self,
        query: PaymentOrderListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[PaymentOrder]:
        """Get a list of all payment orders"""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/payment_orders",
            page=SyncPage[PaymentOrder],
            options=options,
            model=PaymentOrder,
        )

    def create_async(
        self,
        body: PaymentOrderCreateAsyncParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Create a new payment order asynchronously"""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/payment_orders/create_async",
            body=body,
            options=options,
            cast_to=NoneType,
        )


class AsyncPaymentOrders(AsyncAPIResource):
    reversals: AsyncReversals

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.reversals = AsyncReversals(client)

    async def create(
        self,
        body: PaymentOrderCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaymentOrder:
        """Create a new Payment Order"""
        # Make a copy of the input so that our internal mutations (extracting files)
        # don't incidentally mutate the user's dictionary.
        body = body.copy()
        files = extract_files(body, paths=[["documents", "<array>", "file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/payment_orders",
            body=body,
            files=files,
            options=options,
            cast_to=PaymentOrder,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaymentOrder:
        """Get details on a single payment order"""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/payment_orders/{id}",
            options=options,
            cast_to=PaymentOrder,
        )

    async def update(
        self,
        id: str,
        body: PaymentOrderUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PaymentOrder:
        """Update a payment order"""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/payment_orders/{id}",
            body=body,
            options=options,
            cast_to=PaymentOrder,
        )

    def list(
        self,
        query: PaymentOrderListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[PaymentOrder, AsyncPage[PaymentOrder]]:
        """Get a list of all payment orders"""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/payment_orders",
            page=AsyncPage[PaymentOrder],
            options=options,
            model=PaymentOrder,
        )

    async def create_async(
        self,
        body: PaymentOrderCreateAsyncParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Create a new payment order asynchronously"""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/payment_orders/create_async",
            body=body,
            options=options,
            cast_to=NoneType,
        )
