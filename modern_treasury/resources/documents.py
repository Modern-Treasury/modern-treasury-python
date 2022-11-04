# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import extract_files, maybe_transform, deepcopy_minimal
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.document import Document
from ..types.document_list_params import DocumentListParams
from ..types.document_create_params import DocumentCreateParams

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    def create(
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
        body: DocumentCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Create a document."""
        # Make a copy of the input so that our internal mutations (extracting files)
        # don't incidentally mutate the user's dictionary.
        body = deepcopy_minimal(body)
        files = extract_files(body, paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/api/{documentable_type}/{documentable_id}/documents",
            body=maybe_transform(body, DocumentCreateParams),
            files=files,
            options=options,
            cast_to=Document,
        )

    def retrieve(
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
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Get an existing document."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/{documentable_type}/{documentable_id}/documents/{id}",
            options=options,
            cast_to=Document,
        )

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
        """Get a list of documents."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, DocumentListParams))
        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=SyncPage[Document],
            options=options,
            model=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    async def create(
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
        body: DocumentCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Create a document."""
        # Make a copy of the input so that our internal mutations (extracting files)
        # don't incidentally mutate the user's dictionary.
        body = deepcopy_minimal(body)
        files = extract_files(body, paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/api/{documentable_type}/{documentable_id}/documents",
            body=maybe_transform(body, DocumentCreateParams),
            files=files,
            options=options,
            cast_to=Document,
        )

    async def retrieve(
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
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Get an existing document."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/{documentable_type}/{documentable_id}/documents/{id}",
            options=options,
            cast_to=Document,
        )

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
        """Get a list of documents."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, DocumentListParams))
        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=AsyncPage[Document],
            options=options,
            model=Document,
        )
