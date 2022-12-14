# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.event import Event

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEvents:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.events.retrieve(
            "string",
        )
        assert isinstance(resource, Event)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.events.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.events.list(
            after_cursor="string",
            per_page=0,
            event_time_start="2019-12-27T18:11:19.117Z",
            event_time_end="2019-12-27T18:11:19.117Z",
            resource="string",
            entity_id="string",
            event_name="string",
        )
        assert isinstance(resource, SyncPage)


class TestAsyncEvents:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.events.retrieve(
            "string",
        )
        assert isinstance(resource, Event)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.events.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.events.list(
            after_cursor="string",
            per_page=0,
            event_time_start="2019-12-27T18:11:19.117Z",
            event_time_end="2019-12-27T18:11:19.117Z",
            resource="string",
            entity_id="string",
            event_name="string",
        )
        assert isinstance(resource, AsyncPage)
