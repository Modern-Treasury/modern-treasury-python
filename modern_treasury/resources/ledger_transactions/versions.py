# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union

from ..._types import NOT_GIVEN, Headers, Timeout, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ledger_transactions.version_versions_params import VersionVersionsParams
from ...types.ledger_transactions.ledger_transaction_version import (
    LedgerTransactionVersion,
)

__all__ = ["Versions", "AsyncVersions"]


class Versions(SyncAPIResource):
    def versions(
        self,
        id: str,
        query: VersionVersionsParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LedgerTransactionVersion]:
        """Get a list of ledger transaction versions."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, VersionVersionsParams))
        return self._get_api_list(
            f"/api/ledger_transactions/{id}/versions",
            page=SyncPage[LedgerTransactionVersion],
            options=options,
            model=LedgerTransactionVersion,
        )


class AsyncVersions(AsyncAPIResource):
    def versions(
        self,
        id: str,
        query: VersionVersionsParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerTransactionVersion, AsyncPage[LedgerTransactionVersion]]:
        """Get a list of ledger transaction versions."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, VersionVersionsParams))
        return self._get_api_list(
            f"/api/ledger_transactions/{id}/versions",
            page=AsyncPage[LedgerTransactionVersion],
            options=options,
            model=LedgerTransactionVersion,
        )
