# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.internal_accounts.balance_report import BalanceReport
from ...types.internal_accounts.balance_report_list_params import (
    BalanceReportListParams,
)

__all__ = ["BalanceReports", "AsyncBalanceReports"]


class BalanceReports(SyncAPIResource):
    def retrieve(
        self,
        internal_account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> BalanceReport:
        """Get a single balance report for a given internal account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=options,
            cast_to=BalanceReport,
        )

    def list(
        self,
        internal_account_id: str,
        query: BalanceReportListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[BalanceReport]:
        """Get all balance reports for a given internal account."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, BalanceReportListParams))
        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=SyncPage[BalanceReport],
            options=options,
            model=BalanceReport,
        )


class AsyncBalanceReports(AsyncAPIResource):
    async def retrieve(
        self,
        internal_account_id: str,
        id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> BalanceReport:
        """Get a single balance report for a given internal account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=options,
            cast_to=BalanceReport,
        )

    def list(
        self,
        internal_account_id: str,
        query: BalanceReportListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[BalanceReport, AsyncPage[BalanceReport]]:
        """Get all balance reports for a given internal account."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, BalanceReportListParams))
        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=AsyncPage[BalanceReport],
            options=options,
            model=BalanceReport,
        )
