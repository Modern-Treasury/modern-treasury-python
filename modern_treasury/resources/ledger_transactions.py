# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ledger_transaction import LedgerTransaction
from ..types.ledger_transaction_list_params import LedgerTransactionListParams
from ..types.ledger_transaction_create_params import LedgerTransactionCreateParams
from ..types.ledger_transaction_update_params import LedgerTransactionUpdateParams

__all__ = ["LedgerTransactions", "AsyncLedgerTransactions"]


class LedgerTransactions(SyncAPIResource):
    def create(
        self,
        body: LedgerTransactionCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerTransaction:
        """Create a ledger transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/ledger_transactions",
            body=maybe_transform(body, LedgerTransactionCreateParams),
            options=options,
            cast_to=LedgerTransaction,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerTransaction:
        """Get details on a single ledger transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/ledger_transactions/{id}",
            options=options,
            cast_to=LedgerTransaction,
        )

    def update(
        self,
        id: str,
        body: LedgerTransactionUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerTransaction:
        """Update the details of a ledger transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/ledger_transactions/{id}",
            body=maybe_transform(body, LedgerTransactionUpdateParams),
            options=options,
            cast_to=LedgerTransaction,
        )

    def list(
        self,
        query: LedgerTransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LedgerTransaction]:
        """Get a list of ledger transactions."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, LedgerTransactionListParams)
        )
        return self._get_api_list(
            "/api/ledger_transactions",
            page=SyncPage[LedgerTransaction],
            options=options,
            model=LedgerTransaction,
        )


class AsyncLedgerTransactions(AsyncAPIResource):
    async def create(
        self,
        body: LedgerTransactionCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerTransaction:
        """Create a ledger transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/ledger_transactions",
            body=maybe_transform(body, LedgerTransactionCreateParams),
            options=options,
            cast_to=LedgerTransaction,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerTransaction:
        """Get details on a single ledger transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/ledger_transactions/{id}",
            options=options,
            cast_to=LedgerTransaction,
        )

    async def update(
        self,
        id: str,
        body: LedgerTransactionUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerTransaction:
        """Update the details of a ledger transaction."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/ledger_transactions/{id}",
            body=maybe_transform(body, LedgerTransactionUpdateParams),
            options=options,
            cast_to=LedgerTransaction,
        )

    def list(
        self,
        query: LedgerTransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerTransaction, AsyncPage[LedgerTransaction]]:
        """Get a list of ledger transactions."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, LedgerTransactionListParams)
        )
        return self._get_api_list(
            "/api/ledger_transactions",
            page=AsyncPage[LedgerTransaction],
            options=options,
            model=LedgerTransaction,
        )
