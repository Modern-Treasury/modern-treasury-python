# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Query, Headers, Timeout, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared import AccountDetail
from ..types.account_detail_list_params import AccountDetailListParams
from ..types.account_detail_create_params import AccountDetailCreateParams

__all__ = ["AccountDetails", "AsyncAccountDetails"]


class AccountDetails(SyncAPIResource):
    def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: AccountDetailCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountDetail:
        """Create an account detail for an external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/api/{accounts_type}/{account_id}/account_details",
            body=maybe_transform(body, AccountDetailCreateParams),
            options=options,
            cast_to=AccountDetail,
        )

    def retrieve(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountDetail:
        """Get a single account detail for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=options,
            cast_to=AccountDetail,
        )

    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: AccountDetailListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[AccountDetail]:
        """Get a list of account details for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, AccountDetailListParams))
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/account_details",
            page=SyncPage[AccountDetail],
            options=options,
            model=AccountDetail,
        )

    def delete(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a single account detail for an external account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=options,
            cast_to=NoneType,
        )


class AsyncAccountDetails(AsyncAPIResource):
    async def create(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        body: AccountDetailCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountDetail:
        """Create an account detail for an external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/api/{accounts_type}/{account_id}/account_details",
            body=maybe_transform(body, AccountDetailCreateParams),
            options=options,
            cast_to=AccountDetail,
        )

    async def retrieve(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountDetail:
        """Get a single account detail for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=options,
            cast_to=AccountDetail,
        )

    def list(
        self,
        accounts_type: Literal["external_accounts", "internal_accounts"],
        account_id: str,
        query: AccountDetailListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[AccountDetail, AsyncPage[AccountDetail]]:
        """Get a list of account details for a single internal or external account."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, AccountDetailListParams))
        return self._get_api_list(
            f"/api/{accounts_type}/{account_id}/account_details",
            page=AsyncPage[AccountDetail],
            options=options,
            model=AccountDetail,
        )

    async def delete(
        self,
        accounts_type: Literal["external_accounts"],
        account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a single account detail for an external account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/{accounts_type}/{account_id}/account_details/{id}",
            options=options,
            cast_to=NoneType,
        )
