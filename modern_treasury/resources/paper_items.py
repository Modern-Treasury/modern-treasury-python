# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.paper_item import PaperItem
from ..types.paper_item_list_params import PaperItemListParams

__all__ = ["PaperItems", "AsyncPaperItems"]


class PaperItems(SyncAPIResource):
    def retrieve(
        self,
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
    ) -> PaperItem:
        """Get details on a single paper item."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/paper_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=PaperItem,
        )

    @overload
    def list(
        self,
        *,
        lockbox_number: str | NotGiven = NOT_GIVEN,
        deposit_date_start: str | NotGiven = NOT_GIVEN,
        deposit_date_end: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncPage[PaperItem]:
        """
        Get a list of all paper items.

        Args:
          lockbox_number: Specify `lockbox_number` if you wish to see paper items that are associated with
              a specific lockbox number.

          deposit_date_start: Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date

          deposit_date_end: Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: PaperItemListParams = {},
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
    ) -> SyncPage[PaperItem]:
        """Get a list of all paper items."""
        ...

    def list(
        self,
        query: PaperItemListParams | None = None,
        *,
        lockbox_number: str | NotGiven = NOT_GIVEN,
        deposit_date_start: str | NotGiven = NOT_GIVEN,
        deposit_date_end: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncPage[PaperItem]:
        """
        Get a list of all paper items.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          lockbox_number: Specify `lockbox_number` if you wish to see paper items that are associated with
              a specific lockbox number.

          deposit_date_start: Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date

          deposit_date_end: Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date

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
            # with the standard PaperItemListParams type.
            query = cast(
                Any,
                {
                    "lockbox_number": lockbox_number,
                    "deposit_date_start": deposit_date_start,
                    "deposit_date_end": deposit_date_end,
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            "/api/paper_items",
            page=SyncPage[PaperItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=PaperItem,
        )


class AsyncPaperItems(AsyncAPIResource):
    async def retrieve(
        self,
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
    ) -> PaperItem:
        """Get details on a single paper item."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/paper_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=PaperItem,
        )

    @overload
    def list(
        self,
        *,
        lockbox_number: str | NotGiven = NOT_GIVEN,
        deposit_date_start: str | NotGiven = NOT_GIVEN,
        deposit_date_end: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[PaperItem, AsyncPage[PaperItem]]:
        """
        Get a list of all paper items.

        Args:
          lockbox_number: Specify `lockbox_number` if you wish to see paper items that are associated with
              a specific lockbox number.

          deposit_date_start: Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date

          deposit_date_end: Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: PaperItemListParams = {},
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
    ) -> AsyncPaginator[PaperItem, AsyncPage[PaperItem]]:
        """Get a list of all paper items."""
        ...

    def list(
        self,
        query: PaperItemListParams | None = None,
        *,
        lockbox_number: str | NotGiven = NOT_GIVEN,
        deposit_date_start: str | NotGiven = NOT_GIVEN,
        deposit_date_end: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[PaperItem, AsyncPage[PaperItem]]:
        """
        Get a list of all paper items.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          lockbox_number: Specify `lockbox_number` if you wish to see paper items that are associated with
              a specific lockbox number.

          deposit_date_start: Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date

          deposit_date_end: Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date

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
            # with the standard PaperItemListParams type.
            query = cast(
                Any,
                {
                    "lockbox_number": lockbox_number,
                    "deposit_date_start": deposit_date_start,
                    "deposit_date_end": deposit_date_end,
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            "/api/paper_items",
            page=AsyncPage[PaperItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=PaperItem,
        )
