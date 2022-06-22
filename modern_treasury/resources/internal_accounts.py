# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.internal_account import InternalAccount
from ..types.internal_account_list_params import InternalAccountListParams
from ..types.internal_account_create_params import InternalAccountCreateParams
from ..types.internal_account_update_params import InternalAccountUpdateParams

__all__ = ["InternalAccounts", "AsyncInternalAccounts"]


class InternalAccounts(SyncAPIResource):
    def create(
        self,
        body: InternalAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/internal_accounts",
            body=body,
            options=options,
            cast_to=InternalAccount,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/internal_accounts/{id}",
            options=options,
            cast_to=InternalAccount,
        )

    def update(
        self,
        id: str,
        body: InternalAccountUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/internal_accounts/{id}",
            body=body,
            options=options,
            cast_to=InternalAccount,
        )

    def list(
        self,
        query: InternalAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[InternalAccount]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/internal_accounts",
            page=SyncPage[InternalAccount],
            options=options,
            model=InternalAccount,
        )


class AsyncInternalAccounts(AsyncAPIResource):
    async def create(
        self,
        body: InternalAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/internal_accounts",
            body=body,
            options=options,
            cast_to=InternalAccount,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/internal_accounts/{id}",
            options=options,
            cast_to=InternalAccount,
        )

    async def update(
        self,
        id: str,
        body: InternalAccountUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/internal_accounts/{id}",
            body=body,
            options=options,
            cast_to=InternalAccount,
        )

    def list(
        self,
        query: InternalAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[InternalAccount, AsyncPage[InternalAccount]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/internal_accounts",
            page=AsyncPage[InternalAccount],
            options=options,
            model=InternalAccount,
        )
