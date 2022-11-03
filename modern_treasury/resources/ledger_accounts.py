# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ledger_account import LedgerAccount
from ..types.ledger_account_list_params import LedgerAccountListParams
from ..types.ledger_account_create_params import LedgerAccountCreateParams
from ..types.ledger_account_update_params import LedgerAccountUpdateParams
from ..types.ledger_account_retrieve_params import LedgerAccountRetrieveParams

__all__ = ["LedgerAccounts", "AsyncLedgerAccounts"]


class LedgerAccounts(SyncAPIResource):
    def create(
        self,
        body: LedgerAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccount:
        """Create a ledger account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/ledger_accounts",
            body=maybe_transform(body, LedgerAccountCreateParams),
            options=options,
            cast_to=LedgerAccount,
        )

    def retrieve(
        self,
        id: str,
        query: LedgerAccountRetrieveParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> LedgerAccount:
        """Get details on a single ledger account."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, LedgerAccountRetrieveParams)
        )
        return self._get(
            f"/api/ledger_accounts/{id}",
            options=options,
            cast_to=LedgerAccount,
        )

    def update(
        self,
        id: str,
        body: LedgerAccountUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccount:
        """Update the details of a ledger account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/ledger_accounts/{id}",
            body=maybe_transform(body, LedgerAccountUpdateParams),
            options=options,
            cast_to=LedgerAccount,
        )

    def list(
        self,
        query: LedgerAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LedgerAccount]:
        """Get a list of ledger accounts."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LedgerAccountListParams))
        return self._get_api_list(
            "/api/ledger_accounts",
            page=SyncPage[LedgerAccount],
            options=options,
            model=LedgerAccount,
        )

    def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccount:
        """Delete a ledger account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/ledger_accounts/{id}",
            options=options,
            cast_to=LedgerAccount,
        )


class AsyncLedgerAccounts(AsyncAPIResource):
    async def create(
        self,
        body: LedgerAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccount:
        """Create a ledger account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/ledger_accounts",
            body=maybe_transform(body, LedgerAccountCreateParams),
            options=options,
            cast_to=LedgerAccount,
        )

    async def retrieve(
        self,
        id: str,
        query: LedgerAccountRetrieveParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> LedgerAccount:
        """Get details on a single ledger account."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, LedgerAccountRetrieveParams)
        )
        return await self._get(
            f"/api/ledger_accounts/{id}",
            options=options,
            cast_to=LedgerAccount,
        )

    async def update(
        self,
        id: str,
        body: LedgerAccountUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccount:
        """Update the details of a ledger account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/ledger_accounts/{id}",
            body=maybe_transform(body, LedgerAccountUpdateParams),
            options=options,
            cast_to=LedgerAccount,
        )

    def list(
        self,
        query: LedgerAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerAccount, AsyncPage[LedgerAccount]]:
        """Get a list of ledger accounts."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LedgerAccountListParams))
        return self._get_api_list(
            "/api/ledger_accounts",
            page=AsyncPage[LedgerAccount],
            options=options,
            model=LedgerAccount,
        )

    async def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccount:
        """Delete a ledger account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/ledger_accounts/{id}",
            options=options,
            cast_to=LedgerAccount,
        )
