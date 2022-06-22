# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.expected_payment import ExpectedPayment
from ..types.expected_payment_list_params import ExpectedPaymentListParams
from ..types.expected_payment_create_params import ExpectedPaymentCreateParams
from ..types.expected_payment_update_params import ExpectedPaymentUpdateParams

__all__ = ["ExpectedPayments", "AsyncExpectedPayments"]


class ExpectedPayments(SyncAPIResource):
    def create(
        self,
        body: ExpectedPaymentCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/expected_payments",
            body=body,
            options=options,
            cast_to=ExpectedPayment,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/expected_payments/{id}",
            options=options,
            cast_to=ExpectedPayment,
        )

    def update(
        self,
        id: str,
        body: ExpectedPaymentUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/expected_payments/{id}",
            body=body,
            options=options,
            cast_to=ExpectedPayment,
        )

    def list(
        self,
        query: ExpectedPaymentListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ExpectedPayment]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/expected_payments",
            page=SyncPage[ExpectedPayment],
            options=options,
            model=ExpectedPayment,
        )

    def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/expected_payments/{id}",
            options=options,
            cast_to=ExpectedPayment,
        )


class AsyncExpectedPayments(AsyncAPIResource):
    async def create(
        self,
        body: ExpectedPaymentCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/expected_payments",
            body=body,
            options=options,
            cast_to=ExpectedPayment,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/expected_payments/{id}",
            options=options,
            cast_to=ExpectedPayment,
        )

    async def update(
        self,
        id: str,
        body: ExpectedPaymentUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/expected_payments/{id}",
            body=body,
            options=options,
            cast_to=ExpectedPayment,
        )

    def list(
        self,
        query: ExpectedPaymentListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ExpectedPayment, AsyncPage[ExpectedPayment]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/expected_payments",
            page=AsyncPage[ExpectedPayment],
            options=options,
            model=ExpectedPayment,
        )

    async def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExpectedPayment:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/expected_payments/{id}",
            options=options,
            cast_to=ExpectedPayment,
        )
