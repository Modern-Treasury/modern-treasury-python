# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerableEvent
from modern_treasury._client import ModernTreasury, AsyncModernTreasury

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLedgerableEvents:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.create(
            name="string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.create(
            name="string",
            custom_data={},
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledgerable_events.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledgerable_events.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.retrieve(
            "string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledgerable_events.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledgerable_events.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLedgerableEvents:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledgerable_event = await client.ledgerable_events.create(
            name="string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledgerable_event = await client.ledgerable_events.create(
            name="string",
            custom_data={},
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.ledgerable_events.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.ledgerable_events.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = await response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledgerable_event = await client.ledgerable_events.retrieve(
            "string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.ledgerable_events.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.ledgerable_events.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = await response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True
