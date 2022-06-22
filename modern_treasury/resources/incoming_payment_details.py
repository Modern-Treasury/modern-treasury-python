# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.incoming_payment_detail import IncomingPaymentDetail
from ..types.incoming_payment_detail_list_params import IncomingPaymentDetailListParams
from ..types.incoming_payment_detail_update_params import (
    IncomingPaymentDetailUpdateParams,
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
            body=body,
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
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/incoming_payment_details",
            page=SyncPage[IncomingPaymentDetail],
            options=options,
            model=IncomingPaymentDetail,
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
            body=body,
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
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/incoming_payment_details",
            page=AsyncPage[IncomingPaymentDetail],
            options=options,
            model=IncomingPaymentDetail,
        )
