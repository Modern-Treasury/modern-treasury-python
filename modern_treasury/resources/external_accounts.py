# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.external_account import ExternalAccount
from ..types.external_account_list_params import ExternalAccountListParams
from ..types.external_account_create_params import ExternalAccountCreateParams
from ..types.external_account_update_params import ExternalAccountUpdateParams
from ..types.external_account_verify_params import ExternalAccountVerifyParams
from ..types.external_account_complete_verification_params import (
    ExternalAccountCompleteVerificationParams,
)

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
    def create(
        self,
        body: ExternalAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/external_accounts",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/external_accounts/{id}",
            options=options,
            cast_to=ExternalAccount,
        )

    def update(
        self,
        id: str,
        body: ExternalAccountUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/external_accounts/{id}",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )

    def list(
        self,
        query: ExternalAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ExternalAccount]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/external_accounts",
            page=SyncPage[ExternalAccount],
            options=options,
            model=ExternalAccount,
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
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/external_accounts/{id}",
            options=options,
            cast_to=NoneType,
        )

    def complete_verification(
        self,
        id: str,
        body: ExternalAccountCompleteVerificationParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/api/external_accounts/{id}/complete_verification",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )

    def verify(
        self,
        id: str,
        body: ExternalAccountVerifyParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/api/external_accounts/{id}/verify",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )


class AsyncExternalAccounts(AsyncAPIResource):
    async def create(
        self,
        body: ExternalAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/external_accounts",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/external_accounts/{id}",
            options=options,
            cast_to=ExternalAccount,
        )

    async def update(
        self,
        id: str,
        body: ExternalAccountUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/external_accounts/{id}",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )

    def list(
        self,
        query: ExternalAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/api/external_accounts",
            page=AsyncPage[ExternalAccount],
            options=options,
            model=ExternalAccount,
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
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/external_accounts/{id}",
            options=options,
            cast_to=NoneType,
        )

    async def complete_verification(
        self,
        id: str,
        body: ExternalAccountCompleteVerificationParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/api/external_accounts/{id}/complete_verification",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )

    async def verify(
        self,
        id: str,
        body: ExternalAccountVerifyParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/api/external_accounts/{id}/verify",
            body=body,
            options=options,
            cast_to=ExternalAccount,
        )
