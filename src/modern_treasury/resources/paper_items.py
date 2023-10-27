# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import date

from ..types import PaperItem, paper_item_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import ModernTreasury, AsyncModernTreasury

__all__ = ["PaperItems", "AsyncPaperItems"]


class PaperItems(SyncAPIResource):
    with_raw_response: PaperItemsWithRawResponse

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = PaperItemsWithRawResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PaperItem:
        """
        Get details on a single paper item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/paper_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperItem,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        deposit_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        deposit_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        lockbox_number: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PaperItem]:
        """
        Get a list of all paper items.

        Args:
          deposit_date_end: Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date

          deposit_date_start: Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date

          lockbox_number: Specify `lockbox_number` if you wish to see paper items that are associated with
              a specific lockbox number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/paper_items",
            page=SyncPage[PaperItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "deposit_date_end": deposit_date_end,
                        "deposit_date_start": deposit_date_start,
                        "lockbox_number": lockbox_number,
                        "per_page": per_page,
                    },
                    paper_item_list_params.PaperItemListParams,
                ),
            ),
            model=PaperItem,
        )


class AsyncPaperItems(AsyncAPIResource):
    with_raw_response: AsyncPaperItemsWithRawResponse

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncPaperItemsWithRawResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PaperItem:
        """
        Get details on a single paper item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/paper_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperItem,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        deposit_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        deposit_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        lockbox_number: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PaperItem, AsyncPage[PaperItem]]:
        """
        Get a list of all paper items.

        Args:
          deposit_date_end: Specify an inclusive end date (YYYY-MM-DD) when filtering by deposit_date

          deposit_date_start: Specify an inclusive start date (YYYY-MM-DD) when filtering by deposit_date

          lockbox_number: Specify `lockbox_number` if you wish to see paper items that are associated with
              a specific lockbox number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/paper_items",
            page=AsyncPage[PaperItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "deposit_date_end": deposit_date_end,
                        "deposit_date_start": deposit_date_start,
                        "lockbox_number": lockbox_number,
                        "per_page": per_page,
                    },
                    paper_item_list_params.PaperItemListParams,
                ),
            ),
            model=PaperItem,
        )


class PaperItemsWithRawResponse:
    def __init__(self, paper_items: PaperItems) -> None:
        self.retrieve = to_raw_response_wrapper(
            paper_items.retrieve,
        )
        self.list = to_raw_response_wrapper(
            paper_items.list,
        )


class AsyncPaperItemsWithRawResponse:
    def __init__(self, paper_items: AsyncPaperItems) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            paper_items.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            paper_items.list,
        )
