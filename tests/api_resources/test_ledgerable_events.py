# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerableEvent

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
            amount=0,
            name="string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.create(
            amount=0,
            name="string",
            currency="string",
            currency_exponent=0,
            custom_data={},
            description="string",
            direction="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.retrieve(
            "string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])


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
            amount=0,
            name="string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledgerable_event = await client.ledgerable_events.create(
            amount=0,
            name="string",
            currency="string",
            currency_exponent=0,
            custom_data={},
            description="string",
            direction="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledgerable_event = await client.ledgerable_events.retrieve(
            "string",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])
