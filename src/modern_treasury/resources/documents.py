# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import Document, document_list_params, document_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsWithRawResponse:
        return DocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsWithStreamingResponse:
        return DocumentsWithStreamingResponse(self)

    def create(
        self,
        *,
        documentable_id: str,
        documentable_type: Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "incoming_payment_details",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
            "decisions",
            "connections",
        ],
        file: FileTypes,
        document_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Document:
        """
        Create a document.

        Args:
          documentable_id: The unique identifier for the associated object.

          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "documentable_id": documentable_id,
                "documentable_type": documentable_type,
                "file": file,
                "document_type": document_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/documents",
            body=maybe_transform(body, document_create_params.DocumentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Document,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Get an existing document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        documentable_id: str | NotGiven = NOT_GIVEN,
        documentable_type: Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "incoming_payment_details",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
            "decisions",
            "connections",
        ]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Document]:
        """
        Get a list of documents.

        Args:
          documentable_id: The unique identifier for the associated object.

          documentable_type: The type of the associated object. Currently can be one of `payment_order`,
              `transaction`, `paper_item`, `expected_payment`, `counterparty`, `organization`,
              `case`, `internal_account`, `decision`, or `external_account`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/documents",
            page=SyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "documentable_id": documentable_id,
                        "documentable_type": documentable_type,
                        "per_page": per_page,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsWithRawResponse:
        return AsyncDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsWithStreamingResponse:
        return AsyncDocumentsWithStreamingResponse(self)

    async def create(
        self,
        *,
        documentable_id: str,
        documentable_type: Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "incoming_payment_details",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
            "decisions",
            "connections",
        ],
        file: FileTypes,
        document_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Document:
        """
        Create a document.

        Args:
          documentable_id: The unique identifier for the associated object.

          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "documentable_id": documentable_id,
                "documentable_type": documentable_type,
                "file": file,
                "document_type": document_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/documents",
            body=await async_maybe_transform(body, document_create_params.DocumentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Document,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Get an existing document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        documentable_id: str | NotGiven = NOT_GIVEN,
        documentable_type: Literal[
            "cases",
            "counterparties",
            "expected_payments",
            "external_accounts",
            "incoming_payment_details",
            "internal_accounts",
            "organizations",
            "paper_items",
            "payment_orders",
            "transactions",
            "decisions",
            "connections",
        ]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncPage[Document]]:
        """
        Get a list of documents.

        Args:
          documentable_id: The unique identifier for the associated object.

          documentable_type: The type of the associated object. Currently can be one of `payment_order`,
              `transaction`, `paper_item`, `expected_payment`, `counterparty`, `organization`,
              `case`, `internal_account`, `decision`, or `external_account`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/documents",
            page=AsyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "documentable_id": documentable_id,
                        "documentable_type": documentable_type,
                        "per_page": per_page,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )


class DocumentsWithRawResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.create = _legacy_response.to_raw_response_wrapper(
            documents.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            documents.list,
        )


class AsyncDocumentsWithRawResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.create = _legacy_response.async_to_raw_response_wrapper(
            documents.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            documents.list,
        )


class DocumentsWithStreamingResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.create = to_streamed_response_wrapper(
            documents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            documents.list,
        )


class AsyncDocumentsWithStreamingResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.create = async_to_streamed_response_wrapper(
            documents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
