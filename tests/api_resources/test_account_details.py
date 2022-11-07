# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.shared import AccountDetail

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountDetails:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.account_details.create(
            "external_accounts",
            "string",
            account_number="string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.account_details.create(
            "external_accounts",
            "string",
            account_number="string",
            account_number_type="clabe",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.account_details.retrieve(
            "external_accounts",
            "string",
            "string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.account_details.list(
            "external_accounts",
            "string",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.account_details.list(
            "external_accounts",
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        resource = client.account_details.delete(
            "external_accounts",
            "string",
            "string",
        )
        assert resource is None


class TestAsyncAccountDetails:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.create(
            "external_accounts",
            "string",
            account_number="string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.create(
            "external_accounts",
            "string",
            account_number="string",
            account_number_type="clabe",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.retrieve(
            "external_accounts",
            "string",
            "string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.list(
            "external_accounts",
            "string",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.list(
            "external_accounts",
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.delete(
            "external_accounts",
            "string",
            "string",
        )
        assert resource is None
