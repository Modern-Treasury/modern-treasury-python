# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.counterparty import Counterparty
from ..types.counterparty_list_params import CounterpartyListParams
from ..types.counterparty_create_params import CounterpartyCreateParams
from ..types.counterparty_update_params import CounterpartyUpdateParams
from ..types.counterparty_collect_account_params import CounterpartyCollectAccountParams
from ..types.counterparty_collect_account_response import (
    CounterpartyCollectAccountResponse,
)

__all__ = ["Counterparties", "AsyncCounterparties"]


class Counterparties(SyncAPIResource):
    def create(
        self,
        body: CounterpartyCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Counterparty:
        """Create a new counterparty."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/counterparties",
            body=body,
            options=options,
            cast_to=Counterparty,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Counterparty:
        """Get details on a single counterparty."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/counterparties/{id}",
            options=options,
            cast_to=Counterparty,
        )

    def update(
        self,
        id: str,
        body: CounterpartyUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Counterparty:
        """Updates a given counterparty with new information."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/counterparties/{id}",
            body=body,
            options=options,
            cast_to=Counterparty,
        )

    def list(
        self,
        query: CounterpartyListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Counterparty]:
        """Get a paginated list of all counterparties."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/counterparties",
            page=SyncPage[Counterparty],
            options=options,
            model=Counterparty,
        )

    def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Deletes a given counterparty."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/counterparties/{id}",
            options=options,
            cast_to=NoneType,
        )

    def collect_account(
        self,
        id: str,
        body: CounterpartyCollectAccountParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CounterpartyCollectAccountResponse:
        """Send an email requesting account details."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/api/counterparties/{id}/collect_account",
            body=body,
            options=options,
            cast_to=CounterpartyCollectAccountResponse,
        )


class AsyncCounterparties(AsyncAPIResource):
    async def create(
        self,
        body: CounterpartyCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Counterparty:
        """Create a new counterparty."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/counterparties",
            body=body,
            options=options,
            cast_to=Counterparty,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Counterparty:
        """Get details on a single counterparty."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/counterparties/{id}",
            options=options,
            cast_to=Counterparty,
        )

    async def update(
        self,
        id: str,
        body: CounterpartyUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Counterparty:
        """Updates a given counterparty with new information."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/counterparties/{id}",
            body=body,
            options=options,
            cast_to=Counterparty,
        )

    def list(
        self,
        query: CounterpartyListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Counterparty, AsyncPage[Counterparty]]:
        """Get a paginated list of all counterparties."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/counterparties",
            page=AsyncPage[Counterparty],
            options=options,
            model=Counterparty,
        )

    async def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Deletes a given counterparty."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/counterparties/{id}",
            options=options,
            cast_to=NoneType,
        )

    async def collect_account(
        self,
        id: str,
        body: CounterpartyCollectAccountParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CounterpartyCollectAccountResponse:
        """Send an email requesting account details."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/api/counterparties/{id}/collect_account",
            body=body,
            options=options,
            cast_to=CounterpartyCollectAccountResponse,
        )
