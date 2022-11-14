# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.connection import Connection

__all__ = ["Connections", "AsyncConnections"]


class Connections(SyncAPIResource):
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        vendor_customer_id: str | NotGiven = NOT_GIVEN,
        entity: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Connection]:
        """
        Get a list of all connections.

        Args:
          vendor_customer_id: An identifier assigned by the vendor to your organization.

          entity: A string code representing the vendor (i.e. bank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/connections",
            page=SyncPage[Connection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "vendor_customer_id": vendor_customer_id,
                    "entity": entity,
                },
            ),
            model=Connection,
        )


class AsyncConnections(AsyncAPIResource):
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        vendor_customer_id: str | NotGiven = NOT_GIVEN,
        entity: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Connection, AsyncPage[Connection]]:
        """
        Get a list of all connections.

        Args:
          vendor_customer_id: An identifier assigned by the vendor to your organization.

          entity: A string code representing the vendor (i.e. bank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/connections",
            page=AsyncPage[Connection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "vendor_customer_id": vendor_customer_id,
                    "entity": entity,
                },
            ),
            model=Connection,
        )
