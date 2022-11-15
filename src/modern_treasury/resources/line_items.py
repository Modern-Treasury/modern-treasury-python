# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.line_item import LineItem

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LineItem:
        """Get a single line item"""
        return self._get(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LineItem,
        )

    def update(
        self,
        id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LineItem:
        """Args:
          metadata: Additional data represented as key-value pairs.

        Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            body={"metadata": metadata},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LineItem,
        )

    def list(
        self,
        itemizable_id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[LineItem]:
        """
        Get a list of line items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{itemizable_type}/{itemizable_id}/line_items",
            page=SyncPage[LineItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=LineItem,
        )


class AsyncLineItems(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LineItem:
        """Get a single line item"""
        return await self._get(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LineItem,
        )

    async def update(
        self,
        id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        itemizable_id: str,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LineItem:
        """Args:
          metadata: Additional data represented as key-value pairs.

        Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/api/{itemizable_type}/{itemizable_id}/line_items/{id}",
            body={"metadata": metadata},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=LineItem,
        )

    def list(
        self,
        itemizable_id: str,
        *,
        itemizable_type: Literal["expected_payments", "payment_orders"],
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[LineItem, AsyncPage[LineItem]]:
        """
        Get a list of line items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/{itemizable_type}/{itemizable_id}/line_items",
            page=AsyncPage[LineItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=LineItem,
        )
