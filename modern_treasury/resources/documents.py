# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.document import Document
from ..types.document_list_params import DocumentListParams

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    def list(
        self,
        documentable_type: Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
        ],
        documentable_id: str,
        query: DocumentListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Document]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=SyncPage[Document],
            options=options,
            model=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    def list(
        self,
        documentable_type: Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
        ],
        documentable_id: str,
        query: DocumentListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncPage[Document]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=AsyncPage[Document],
            options=options,
            model=Document,
        )
