# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Mapping, Optional, cast, overload
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven, FileTypes
from .._utils import (
    extract_files,
    required_args,
    deepcopy_minimal,
    deprecated_positional_args,
)
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.document import Document
from ..types.document_list_params import DocumentListParams
from ..types.document_create_params import DocumentCreateParams

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    @overload
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
        *,
        document_type: str | NotGiven = NOT_GIVEN,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """
        Create a document.

        Args:
          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Create a document."""
        ...

    @required_args(["body"], ["file"])
    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("documentable_type")
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
        body: DocumentCreateParams | None = None,
        *,
        document_type: str | NotGiven = NOT_GIVEN,
        file: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """
        Create a document.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard DocumentCreateParams type.
            body = cast(
                Any,
                {
                    "document_type": document_type,
                    "file": file,
                },
            )

        body = deepcopy_minimal(body)
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Document,
        )

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("documentable_type", "documentable_id")
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Get an existing document."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/{documentable_type}/{documentable_id}/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Document,
        )

    @overload
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
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Document]:
        """
        Get a list of documents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Document]:
        """Get a list of documents."""
        ...

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("documentable_type")
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
        query: DocumentListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Document]:
        """
        Get a list of documents.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard DocumentListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=SyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    @overload
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
        *,
        document_type: str | NotGiven = NOT_GIVEN,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """
        Create a document.

        Args:
          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Create a document."""
        ...

    @required_args(["body"], ["file"])
    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("documentable_type")
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
        body: DocumentCreateParams | None = None,
        *,
        document_type: str | NotGiven = NOT_GIVEN,
        file: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """
        Create a document.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          document_type: A category given to the document, can be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard DocumentCreateParams type.
            body = cast(
                Any,
                {
                    "document_type": document_type,
                    "file": file,
                },
            )

        body = deepcopy_minimal(body)
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Document,
        )

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("documentable_type", "documentable_id")
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Document:
        """Get an existing document."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/{documentable_type}/{documentable_id}/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Document,
        )

    @overload
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
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncPage[Document]]:
        """
        Get a list of documents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncPage[Document]]:
        """Get a list of documents."""
        ...

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("documentable_type")
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
        query: DocumentListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncPage[Document]]:
        """
        Get a list of documents.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard DocumentListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            f"/api/{documentable_type}/{documentable_id}/documents",
            page=AsyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Document,
        )
