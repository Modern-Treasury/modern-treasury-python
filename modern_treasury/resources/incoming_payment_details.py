# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.incoming_payment_detail import IncomingPaymentDetail
from ..types.incoming_payment_detail_list_params import IncomingPaymentDetailListParams
from ..types.incoming_payment_detail_update_params import (
    IncomingPaymentDetailUpdateParams,
)
from ..types.incoming_payment_detail_create_async_params import (
    IncomingPaymentDetailCreateAsyncParams,
)

__all__ = ["IncomingPaymentDetails", "AsyncIncomingPaymentDetails"]


class IncomingPaymentDetails(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Get an existing Incoming Payment Detail."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/incoming_payment_details/{id}",
            options=options,
            cast_to=IncomingPaymentDetail,
        )

    def update(
        self,
        id: str,
        body: IncomingPaymentDetailUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Update an existing Incoming Payment Detail."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/incoming_payment_details/{id}",
            body=maybe_transform(body, IncomingPaymentDetailUpdateParams),
            options=options,
            cast_to=IncomingPaymentDetail,
        )

    def list(
        self,
        query: IncomingPaymentDetailListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[IncomingPaymentDetail]:
        """Get a list of Incoming Payment Details."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, IncomingPaymentDetailListParams)
        )
        return self._get_api_list(
            "/api/incoming_payment_details",
            page=SyncPage[IncomingPaymentDetail],
            options=options,
            model=IncomingPaymentDetail,
        )

    def create_async(
        self,
        body: IncomingPaymentDetailCreateAsyncParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Simulate Incoming Payment Detail"""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/simulations/incoming_payment_details/create_async",
            body=maybe_transform(body, IncomingPaymentDetailCreateAsyncParams),
            options=options,
            cast_to=NoneType,
        )


class AsyncIncomingPaymentDetails(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Get an existing Incoming Payment Detail."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/incoming_payment_details/{id}",
            options=options,
            cast_to=IncomingPaymentDetail,
        )

    async def update(
        self,
        id: str,
        body: IncomingPaymentDetailUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Update an existing Incoming Payment Detail."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/incoming_payment_details/{id}",
            body=maybe_transform(body, IncomingPaymentDetailUpdateParams),
            options=options,
            cast_to=IncomingPaymentDetail,
        )

    def list(
        self,
        query: IncomingPaymentDetailListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[IncomingPaymentDetail, AsyncPage[IncomingPaymentDetail]]:
        """Get a list of Incoming Payment Details."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, IncomingPaymentDetailListParams)
        )
        return self._get_api_list(
            "/api/incoming_payment_details",
            page=AsyncPage[IncomingPaymentDetail],
            options=options,
            model=IncomingPaymentDetail,
        )

    async def create_async(
        self,
        body: IncomingPaymentDetailCreateAsyncParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Simulate Incoming Payment Detail"""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/simulations/incoming_payment_details/create_async",
            body=maybe_transform(body, IncomingPaymentDetailCreateAsyncParams),
            options=options,
            cast_to=NoneType,
        )
