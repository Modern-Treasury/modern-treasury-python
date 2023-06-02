# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Event
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

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
        event = client.events.retrieve(
            "string",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        event = client.events.list()
        assert_matches_type(SyncPage[Event], event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        event = client.events.list(
            after_cursor="string",
            entity_id="string",
            event_name="string",
            event_time_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_time_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            per_page=0,
            resource="string",
        )
        assert_matches_type(SyncPage[Event], event, path=["response"])


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
        event = await client.events.retrieve(
            "string",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        event = await client.events.list()
        assert_matches_type(AsyncPage[Event], event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        event = await client.events.list(
            after_cursor="string",
            entity_id="string",
            event_name="string",
            event_time_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_time_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            per_page=0,
            resource="string",
        )
        assert_matches_type(AsyncPage[Event], event, path=["response"])
