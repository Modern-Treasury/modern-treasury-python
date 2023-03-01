# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Ledger
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgers:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.create(
            name="string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.create(
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.retrieve(
            "string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.update(
            "string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.update(
            "string",
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.list()
        assert_matches_type(SyncPage[Ledger], ledger, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[Ledger], ledger, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger = client.ledgers.delete(
            "string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])


class TestAsyncLedgers:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.create(
            name="string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.create(
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.retrieve(
            "string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.update(
            "string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.update(
            "string",
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(Ledger, ledger, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.list()
        assert_matches_type(AsyncPage[Ledger], ledger, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[Ledger], ledger, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        ledger = await client.ledgers.delete(
            "string",
        )
        assert_matches_type(Ledger, ledger, path=["response"])
