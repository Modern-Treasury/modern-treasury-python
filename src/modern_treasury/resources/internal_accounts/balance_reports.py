# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.internal_accounts import BalanceReport, balance_report_list_params, balance_report_create_params

__all__ = ["BalanceReports", "AsyncBalanceReports"]


class BalanceReports(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalanceReportsWithRawResponse:
        return BalanceReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceReportsWithStreamingResponse:
        return BalanceReportsWithStreamingResponse(self)

    def create(
        self,
        internal_account_id: str,
        *,
        as_of_date: Union[str, date],
        as_of_time: str,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"],
        balances: Iterable[balance_report_create_params.Balance],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BalanceReport:
        """
        create balance reports

        Args:
          as_of_date: The date of the balance report in local time.

          as_of_time: The time (24-hour clock) of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

          balances: An array of `Balance` objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        return self._post(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            body=maybe_transform(
                {
                    "as_of_date": as_of_date,
                    "as_of_time": as_of_time,
                    "balance_report_type": balance_report_type,
                    "balances": balances,
                },
                balance_report_create_params.BalanceReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BalanceReport,
        )

    def retrieve(
        self,
        id: str,
        *,
        internal_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceReport:
        """
        Get a single balance report for a given internal account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceReport,
        )

    def list(
        self,
        internal_account_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Union[str, date] | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BalanceReport]:
        """
        Get all balance reports for a given internal account.

        Args:
          as_of_date: The date of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=SyncPage[BalanceReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date": as_of_date,
                        "balance_report_type": balance_report_type,
                        "per_page": per_page,
                    },
                    balance_report_list_params.BalanceReportListParams,
                ),
            ),
            model=BalanceReport,
        )

    def delete(
        self,
        id: str,
        *,
        internal_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes a given balance report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncBalanceReports(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalanceReportsWithRawResponse:
        return AsyncBalanceReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceReportsWithStreamingResponse:
        return AsyncBalanceReportsWithStreamingResponse(self)

    async def create(
        self,
        internal_account_id: str,
        *,
        as_of_date: Union[str, date],
        as_of_time: str,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"],
        balances: Iterable[balance_report_create_params.Balance],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BalanceReport:
        """
        create balance reports

        Args:
          as_of_date: The date of the balance report in local time.

          as_of_time: The time (24-hour clock) of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

          balances: An array of `Balance` objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        return await self._post(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            body=await async_maybe_transform(
                {
                    "as_of_date": as_of_date,
                    "as_of_time": as_of_time,
                    "balance_report_type": balance_report_type,
                    "balances": balances,
                },
                balance_report_create_params.BalanceReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BalanceReport,
        )

    async def retrieve(
        self,
        id: str,
        *,
        internal_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceReport:
        """
        Get a single balance report for a given internal account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceReport,
        )

    def list(
        self,
        internal_account_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Union[str, date] | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BalanceReport, AsyncPage[BalanceReport]]:
        """
        Get all balance reports for a given internal account.

        Args:
          as_of_date: The date of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=AsyncPage[BalanceReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date": as_of_date,
                        "balance_report_type": balance_report_type,
                        "per_page": per_page,
                    },
                    balance_report_list_params.BalanceReportListParams,
                ),
            ),
            model=BalanceReport,
        )

    async def delete(
        self,
        id: str,
        *,
        internal_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes a given balance report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class BalanceReportsWithRawResponse:
    def __init__(self, balance_reports: BalanceReports) -> None:
        self._balance_reports = balance_reports

        self.create = _legacy_response.to_raw_response_wrapper(
            balance_reports.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            balance_reports.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            balance_reports.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            balance_reports.delete,
        )


class AsyncBalanceReportsWithRawResponse:
    def __init__(self, balance_reports: AsyncBalanceReports) -> None:
        self._balance_reports = balance_reports

        self.create = _legacy_response.async_to_raw_response_wrapper(
            balance_reports.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            balance_reports.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            balance_reports.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            balance_reports.delete,
        )


class BalanceReportsWithStreamingResponse:
    def __init__(self, balance_reports: BalanceReports) -> None:
        self._balance_reports = balance_reports

        self.create = to_streamed_response_wrapper(
            balance_reports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            balance_reports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            balance_reports.list,
        )
        self.delete = to_streamed_response_wrapper(
            balance_reports.delete,
        )


class AsyncBalanceReportsWithStreamingResponse:
    def __init__(self, balance_reports: AsyncBalanceReports) -> None:
        self._balance_reports = balance_reports

        self.create = async_to_streamed_response_wrapper(
            balance_reports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            balance_reports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            balance_reports.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            balance_reports.delete,
        )
