# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ledger import Ledger
from ..types.ledger_list_params import LedgerListParams
from ..types.ledger_create_params import LedgerCreateParams
from ..types.ledger_update_params import LedgerUpdateParams

__all__ = ["Ledgers", "AsyncLedgers"]


class Ledgers(SyncAPIResource):
    def create(
        self,
        body: LedgerCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Create a ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/ledgers",
            body=maybe_transform(body, LedgerCreateParams),
            options=options,
            cast_to=Ledger,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Get details on a single ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/ledgers/{id}",
            options=options,
            cast_to=Ledger,
        )

    def update(
        self,
        id: str,
        body: LedgerUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Update the details of a ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/ledgers/{id}",
            body=maybe_transform(body, LedgerUpdateParams),
            options=options,
            cast_to=Ledger,
        )

    def list(
        self,
        query: LedgerListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Ledger]:
        """Get a list of ledgers."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LedgerListParams))
        return self._get_api_list(
            "/api/ledgers",
            page=SyncPage[Ledger],
            options=options,
            model=Ledger,
        )

    def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Delete a ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/ledgers/{id}",
            options=options,
            cast_to=Ledger,
        )


class AsyncLedgers(AsyncAPIResource):
    async def create(
        self,
        body: LedgerCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Create a ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/ledgers",
            body=maybe_transform(body, LedgerCreateParams),
            options=options,
            cast_to=Ledger,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Get details on a single ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/ledgers/{id}",
            options=options,
            cast_to=Ledger,
        )

    async def update(
        self,
        id: str,
        body: LedgerUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Update the details of a ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/ledgers/{id}",
            body=maybe_transform(body, LedgerUpdateParams),
            options=options,
            cast_to=Ledger,
        )

    def list(
        self,
        query: LedgerListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Ledger, AsyncPage[Ledger]]:
        """Get a list of ledgers."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LedgerListParams))
        return self._get_api_list(
            "/api/ledgers",
            page=AsyncPage[Ledger],
            options=options,
            model=Ledger,
        )

    async def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Ledger:
        """Delete a ledger."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/ledgers/{id}",
            options=options,
            cast_to=Ledger,
        )
