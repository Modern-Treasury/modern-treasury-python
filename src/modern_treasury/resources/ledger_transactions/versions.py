# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.ledger_transactions import LedgerTransactionVersion, version_list_params

__all__ = ["Versions", "AsyncVersions"]


class Versions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsWithRawResponse:
        return VersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsWithStreamingResponse:
        return VersionsWithStreamingResponse(self)

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        ledger_account_statement_id: str | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        version: Dict[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LedgerTransactionVersion]:
        """
        Get a list of ledger transaction versions.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created_at timestamp. For example, for all dates after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          ledger_account_statement_id: Get all ledger transaction versions that are included in the ledger account
              statement.

          ledger_transaction_id: Get all the ledger transaction versions corresponding to the ID of a ledger
              transaction.

          version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              version. For example, for all versions after 2, use version%5Bgt%5D=2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_transaction_versions",
            page=SyncPage[LedgerTransactionVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at": created_at,
                        "ledger_account_statement_id": ledger_account_statement_id,
                        "ledger_transaction_id": ledger_transaction_id,
                        "per_page": per_page,
                        "version": version,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            model=LedgerTransactionVersion,
        )


class AsyncVersions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsWithRawResponse:
        return AsyncVersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsWithStreamingResponse:
        return AsyncVersionsWithStreamingResponse(self)

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        ledger_account_statement_id: str | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        version: Dict[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerTransactionVersion, AsyncPage[LedgerTransactionVersion]]:
        """
        Get a list of ledger transaction versions.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created_at timestamp. For example, for all dates after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          ledger_account_statement_id: Get all ledger transaction versions that are included in the ledger account
              statement.

          ledger_transaction_id: Get all the ledger transaction versions corresponding to the ID of a ledger
              transaction.

          version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              version. For example, for all versions after 2, use version%5Bgt%5D=2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/ledger_transaction_versions",
            page=AsyncPage[LedgerTransactionVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at": created_at,
                        "ledger_account_statement_id": ledger_account_statement_id,
                        "ledger_transaction_id": ledger_transaction_id,
                        "per_page": per_page,
                        "version": version,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            model=LedgerTransactionVersion,
        )


class VersionsWithRawResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.list = _legacy_response.to_raw_response_wrapper(
            versions.list,
        )


class AsyncVersionsWithRawResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.list = _legacy_response.async_to_raw_response_wrapper(
            versions.list,
        )


class VersionsWithStreamingResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.list = to_streamed_response_wrapper(
            versions.list,
        )


class AsyncVersionsWithStreamingResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
