# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.internal_account import InternalAccount

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestInternalAccounts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.internal_accounts.create(
            connection_id="string",
            name="string",
            party_name="string",
            currency="USD",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.internal_accounts.create(
            connection_id="string",
            name="string",
            party_name="string",
            currency="USD",
            entity_id="string",
            parent_account_id="string",
            counterparty_id="string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.internal_accounts.retrieve(
            "string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.internal_accounts.update(
            "string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.internal_accounts.update(
            "string",
            name="string",
            metadata={"foo": "string"},
            parent_account_id="string",
            counterparty_id="string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.internal_accounts.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.internal_accounts.list(
            after_cursor="string",
            per_page=0,
            currency="AED",
            payment_type="ach",
            payment_direction="credit",
        )
        assert isinstance(resource, SyncPage)


class TestAsyncInternalAccounts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.internal_accounts.create(
            connection_id="string",
            name="string",
            party_name="string",
            currency="USD",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.internal_accounts.create(
            connection_id="string",
            name="string",
            party_name="string",
            currency="USD",
            entity_id="string",
            parent_account_id="string",
            counterparty_id="string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.internal_accounts.retrieve(
            "string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.internal_accounts.update(
            "string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.internal_accounts.update(
            "string",
            name="string",
            metadata={"foo": "string"},
            parent_account_id="string",
            counterparty_id="string",
        )
        assert isinstance(resource, InternalAccount)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.internal_accounts.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.internal_accounts.list(
            after_cursor="string",
            per_page=0,
            currency="AED",
            payment_type="ach",
            payment_direction="credit",
        )
        assert isinstance(resource, AsyncPage)
