# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ledger_account_category import LedgerAccountCategory
from ..types.ledger_account_category_list_params import LedgerAccountCategoryListParams
from ..types.ledger_account_category_create_params import (
    LedgerAccountCategoryCreateParams,
)
from ..types.ledger_account_category_update_params import (
    LedgerAccountCategoryUpdateParams,
)

__all__ = ["LedgerAccountCategories", "AsyncLedgerAccountCategories"]


class LedgerAccountCategories(SyncAPIResource):
    def create(
        self,
        body: LedgerAccountCategoryCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Create a ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/api/ledger_account_categories",
            body=maybe_transform(body, LedgerAccountCategoryCreateParams),
            options=options,
            cast_to=LedgerAccountCategory,
        )

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Get the details on a single ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/ledger_account_categories/{id}",
            options=options,
            cast_to=LedgerAccountCategory,
        )

    def update(
        self,
        id: str,
        body: LedgerAccountCategoryUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Update the details of a ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/api/ledger_account_categories/{id}",
            body=maybe_transform(body, LedgerAccountCategoryUpdateParams),
            options=options,
            cast_to=LedgerAccountCategory,
        )

    def list(
        self,
        query: LedgerAccountCategoryListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LedgerAccountCategory]:
        """Get a list of ledger account categories."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, LedgerAccountCategoryListParams)
        )
        return self._get_api_list(
            "/api/ledger_account_categories",
            page=SyncPage[LedgerAccountCategory],
            options=options,
            model=LedgerAccountCategory,
        )

    def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Delete a ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/ledger_account_categories/{id}",
            options=options,
            cast_to=LedgerAccountCategory,
        )

    def add_ledger_account(
        self,
        id: str,
        ledger_account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Add a ledger account category to an account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._put(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=options,
            cast_to=NoneType,
        )

    def add_nested_category(
        self,
        id: str,
        sub_category_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Add a ledger account category to a ledger account category."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._put(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=options,
            cast_to=NoneType,
        )

    def remove_ledger_account(
        self,
        id: str,
        ledger_account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a ledger account category from an account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=options,
            cast_to=NoneType,
        )

    def remove_nested_category(
        self,
        id: str,
        sub_category_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a ledger account category from a ledger account category."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return self._delete(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=options,
            cast_to=NoneType,
        )


class AsyncLedgerAccountCategories(AsyncAPIResource):
    async def create(
        self,
        body: LedgerAccountCategoryCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Create a ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/api/ledger_account_categories",
            body=maybe_transform(body, LedgerAccountCategoryCreateParams),
            options=options,
            cast_to=LedgerAccountCategory,
        )

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Get the details on a single ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/ledger_account_categories/{id}",
            options=options,
            cast_to=LedgerAccountCategory,
        )

    async def update(
        self,
        id: str,
        body: LedgerAccountCategoryUpdateParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Update the details of a ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/api/ledger_account_categories/{id}",
            body=maybe_transform(body, LedgerAccountCategoryUpdateParams),
            options=options,
            cast_to=LedgerAccountCategory,
        )

    def list(
        self,
        query: LedgerAccountCategoryListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerAccountCategory, AsyncPage[LedgerAccountCategory]]:
        """Get a list of ledger account categories."""
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, LedgerAccountCategoryListParams)
        )
        return self._get_api_list(
            "/api/ledger_account_categories",
            page=AsyncPage[LedgerAccountCategory],
            options=options,
            model=LedgerAccountCategory,
        )

    async def delete(
        self,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> LedgerAccountCategory:
        """Delete a ledger account category."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/ledger_account_categories/{id}",
            options=options,
            cast_to=LedgerAccountCategory,
        )

    async def add_ledger_account(
        self,
        id: str,
        ledger_account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Add a ledger account category to an account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._put(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=options,
            cast_to=NoneType,
        )

    async def add_nested_category(
        self,
        id: str,
        sub_category_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Add a ledger account category to a ledger account category."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._put(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=options,
            cast_to=NoneType,
        )

    async def remove_ledger_account(
        self,
        id: str,
        ledger_account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a ledger account category from an account."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}",
            options=options,
            cast_to=NoneType,
        )

    async def remove_nested_category(
        self,
        id: str,
        sub_category_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Delete a ledger account category from a ledger account category."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._delete(
            f"/api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}",
            options=options,
            cast_to=NoneType,
        )
