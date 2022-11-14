# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from ..._utils import deprecated_positional_args
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.internal_accounts.balance_report import BalanceReport
from ...types.internal_accounts.balance_report_list_params import (
    BalanceReportListParams,
)

__all__ = ["BalanceReports", "AsyncBalanceReports"]


class BalanceReports(SyncAPIResource):

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("internal_account_id")
    def retrieve(
        self,
        internal_account_id: str,
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
    ) -> BalanceReport:
        """Get a single balance report for a given internal account."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=BalanceReport,
        )

    @overload
    def list(
        self,
        internal_account_id: str,
        *,
        as_of_date: str | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
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
        """
        ...

    @overload
    def list(
        self,
        internal_account_id: str,
        query: BalanceReportListParams = {},
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
    ) -> SyncPage[BalanceReport]:
        """Get all balance reports for a given internal account."""
        ...

    def list(
        self,
        internal_account_id: str,
        query: BalanceReportListParams | None = None,
        *,
        as_of_date: str | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
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
    ) -> SyncPage[BalanceReport]:
        """
        Get all balance reports for a given internal account.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          as_of_date: The date of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

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
            # with the standard BalanceReportListParams type.
            query = cast(
                Any,
                {
                    "as_of_date": as_of_date,
                    "balance_report_type": balance_report_type,
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=SyncPage[BalanceReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=BalanceReport,
        )


class AsyncBalanceReports(AsyncAPIResource):

    # These parameters are deprecated as positional to make it impossible to get the order wrong.
    # In the future you will have to pass them as named arguments
    @deprecated_positional_args("internal_account_id")
    async def retrieve(
        self,
        internal_account_id: str,
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
    ) -> BalanceReport:
        """Get a single balance report for a given internal account."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=BalanceReport,
        )

    @overload
    def list(
        self,
        internal_account_id: str,
        *,
        as_of_date: str | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
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
        """
        ...

    @overload
    def list(
        self,
        internal_account_id: str,
        query: BalanceReportListParams = {},
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
    ) -> AsyncPaginator[BalanceReport, AsyncPage[BalanceReport]]:
        """Get all balance reports for a given internal account."""
        ...

    def list(
        self,
        internal_account_id: str,
        query: BalanceReportListParams | None = None,
        *,
        as_of_date: str | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[BalanceReport, AsyncPage[BalanceReport]]:
        """
        Get all balance reports for a given internal account.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          as_of_date: The date of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

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
            # with the standard BalanceReportListParams type.
            query = cast(
                Any,
                {
                    "as_of_date": as_of_date,
                    "balance_report_type": balance_report_type,
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            )

        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=AsyncPage[BalanceReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=BalanceReport,
        )
