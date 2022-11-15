from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import ModernTreasury, AsyncModernTreasury


class SyncAPIResource:
    _client: ModernTreasury

    def __init__(self, client: ModernTreasury) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list


class AsyncAPIResource:
    _client: AsyncModernTreasury

    def __init__(self, client: AsyncModernTreasury) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list
