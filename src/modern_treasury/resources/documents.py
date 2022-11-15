# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, deepcopy_minimal
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.document import Document

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    def create(
        self,
        documentable_id: str,
        *,
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
        document_type: str | NotGiven = NOT_GIVEN,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Document:
        """
        Create a document.

        Args:
          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        body = deepcopy_minimal(
            {
                "document_type": document_type,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return self._post(
            f"/api/{documentable_type}/{documentable_id}/documents",
            body=body,
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Document,
        )

    def retrieve(
        self,
        id: str,
        *,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Document:
        """Get an existing document."""
        return self._get(
            f"/api/{documentable_type}/{documentable_id}/documents/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Document,
        )

    def list(
        self,
        documentable_id: str,
        *,
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
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Document]:
        """
        Get a list of documents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=SyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    async def create(
        self,
        documentable_id: str,
        *,
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
        document_type: str | NotGiven = NOT_GIVEN,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Document:
        """
        Create a document.

        Args:
          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        body = deepcopy_minimal(
            {
                "document_type": document_type,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return await self._post(
            f"/api/{documentable_type}/{documentable_id}/documents",
            body=body,
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Document,
        )

    async def retrieve(
        self,
        id: str,
        *,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Document:
        """Get an existing document."""
        return await self._get(
            f"/api/{documentable_type}/{documentable_id}/documents/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Document,
        )

    def list(
        self,
        documentable_id: str,
        *,
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
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Document, AsyncPage[Document]]:
        """
        Get a list of documents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=AsyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=Document,
        )
