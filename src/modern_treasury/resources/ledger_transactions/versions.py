# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Dict, Union, Optional
from datetime import datetime

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ledger_transactions import LedgerTransactionVersion, version_list_params

__all__ = ["Versions", "AsyncVersions"]


class Versions(SyncAPIResource):
    def list(
        self,
        id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        version: Dict[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[LedgerTransactionVersion]:
        """
        Get a list of ledger transaction versions.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created_at timestamp. For example, for all dates after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              version. For example, for all versions after 2, use version%5Bgt%5D=2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/ledger_transactions/{id}/versions",
            page=SyncPage[LedgerTransactionVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "created_at": created_at,
                        "version": version,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            model=LedgerTransactionVersion,
        )

    def versions(
        self,
        id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        version: Dict[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[LedgerTransactionVersion]:
        """
        Get a list of ledger transaction versions.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created_at timestamp. For example, for all dates after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              version. For example, for all versions after 2, use version%5Bgt%5D=2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        warnings.warn("This method has been deprecated and will be removed soon.", DeprecationWarning, stacklevel=2)
        return self.list(
            id=id,
            after_cursor=after_cursor,
            per_page=per_page,
            created_at=created_at,
            version=version,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )


class AsyncVersions(AsyncAPIResource):
    def list(
        self,
        id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        version: Dict[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[LedgerTransactionVersion, AsyncPage[LedgerTransactionVersion]]:
        """
        Get a list of ledger transaction versions.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created_at timestamp. For example, for all dates after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              version. For example, for all versions after 2, use version%5Bgt%5D=2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/ledger_transactions/{id}/versions",
            page=AsyncPage[LedgerTransactionVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "created_at": created_at,
                        "version": version,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            model=LedgerTransactionVersion,
        )

    def versions(
        self,
        id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Dict[str, Union[str, datetime]] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        version: Dict[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[LedgerTransactionVersion, AsyncPage[LedgerTransactionVersion]]:
        """
        Get a list of ledger transaction versions.

        Args:
          created_at: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              created_at timestamp. For example, for all dates after Jan 1 2000 12:00 UTC, use
              created_at%5Bgt%5D=2000-01-01T12:00:00Z.

          version: Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to filter by the
              version. For example, for all versions after 2, use version%5Bgt%5D=2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        warnings.warn("This method has been deprecated and will be removed soon.", DeprecationWarning, stacklevel=2)
        return self.list(
            id=id,
            after_cursor=after_cursor,
            per_page=per_page,
            created_at=created_at,
            version=version,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
