# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction import Transaction
from ..types.transaction_list_params import TransactionListParams
from ..types.transaction_update_params import TransactionUpdateParams

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Get details on a single transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/transactions/{id}",
            options=options,
            cast_to=Transaction,
        )

    def update(
        self,
        id: str,
        body: TransactionUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Update a single transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/transactions/{id}",
            body=body,
            options=options,
            cast_to=Transaction,
        )

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """Get a list of all transactions."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/transactions",
            page=SyncPage[Transaction],
            options=options,
            model=Transaction,
        )


class AsyncTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Get details on a single transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/transactions/{id}",
            options=options,
            cast_to=Transaction,
        )

    async def update(
        self,
        id: str,
        body: TransactionUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Update a single transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/transactions/{id}",
            body=body,
            options=options,
            cast_to=Transaction,
        )

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """Get a list of all transactions."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/transactions",
            page=AsyncPage[Transaction],
            options=options,
            model=Transaction,
        )
