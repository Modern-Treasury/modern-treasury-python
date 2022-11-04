# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.connection import Connection
from ..types.connection_list_params import ConnectionListParams

__all__ = ["Connections", "AsyncConnections"]


class Connections(SyncAPIResource):
    def list(
        self,
        query: ConnectionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Connection]:
        """Get a list of all connections."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, ConnectionListParams))
        return self._get_api_list(
            "/api/connections",
            page=SyncPage[Connection],
            options=options,
            model=Connection,
        )


class AsyncConnections(AsyncAPIResource):
    def list(
        self,
        query: ConnectionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Connection, AsyncPage[Connection]]:
        """Get a list of all connections."""
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, ConnectionListParams))
        return self._get_api_list(
            "/api/connections",
            page=AsyncPage[Connection],
            options=options,
            model=Connection,
        )
