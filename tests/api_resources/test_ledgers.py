# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.ledger import Ledger

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
        resource = client.ledgers.create(
            name="string",
        )
        assert isinstance(resource, Ledger)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledgers.create(
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, Ledger)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.ledgers.retrieve(
            "string",
        )
        assert isinstance(resource, Ledger)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.ledgers.update(
            "string",
        )
        assert isinstance(resource, Ledger)

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledgers.update(
            "string",
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, Ledger)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.ledgers.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledgers.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            updated_at={"foo": "2019-12-27T18:11:19.117Z"},
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        resource = client.ledgers.delete(
            "string",
        )
        assert isinstance(resource, Ledger)


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
        resource = await client.ledgers.create(
            name="string",
        )
        assert isinstance(resource, Ledger)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledgers.create(
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, Ledger)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledgers.retrieve(
            "string",
        )
        assert isinstance(resource, Ledger)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledgers.update(
            "string",
        )
        assert isinstance(resource, Ledger)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledgers.update(
            "string",
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, Ledger)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledgers.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledgers.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            updated_at={"foo": "2019-12-27T18:11:19.117Z"},
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledgers.delete(
            "string",
        )
        assert isinstance(resource, Ledger)
