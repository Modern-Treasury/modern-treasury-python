# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import case_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from ..types.case import Case
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Cases", "AsyncCases"]


class Cases(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CasesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return CasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return CasesWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Case:
        """
        Get details on a single case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Case,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["open", "resolved"] | Omit = omit,
        subject_id: str | Omit = omit,
        subject_type: Literal["legal_entity"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Case]:
        """
        Get a list of cases.

        Args:
          status: The status of the case.

          subject_id: The ID of the object the case is about.

          subject_type: The type of the object the case is about.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/cases",
            page=SyncPage[Case],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "status": status,
                        "subject_id": subject_id,
                        "subject_type": subject_type,
                    },
                    case_list_params.CaseListParams,
                ),
            ),
            model=Case,
        )


class AsyncCases(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCasesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncCasesWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Case:
        """
        Get details on a single case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Case,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["open", "resolved"] | Omit = omit,
        subject_id: str | Omit = omit,
        subject_type: Literal["legal_entity"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Case, AsyncPage[Case]]:
        """
        Get a list of cases.

        Args:
          status: The status of the case.

          subject_id: The ID of the object the case is about.

          subject_type: The type of the object the case is about.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/cases",
            page=AsyncPage[Case],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "status": status,
                        "subject_id": subject_id,
                        "subject_type": subject_type,
                    },
                    case_list_params.CaseListParams,
                ),
            ),
            model=Case,
        )


class CasesWithRawResponse:
    def __init__(self, cases: Cases) -> None:
        self._cases = cases

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            cases.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            cases.list,
        )


class AsyncCasesWithRawResponse:
    def __init__(self, cases: AsyncCases) -> None:
        self._cases = cases

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            cases.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            cases.list,
        )


class CasesWithStreamingResponse:
    def __init__(self, cases: Cases) -> None:
        self._cases = cases

        self.retrieve = to_streamed_response_wrapper(
            cases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            cases.list,
        )


class AsyncCasesWithStreamingResponse:
    def __init__(self, cases: AsyncCases) -> None:
        self._cases = cases

        self.retrieve = async_to_streamed_response_wrapper(
            cases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            cases.list,
        )
