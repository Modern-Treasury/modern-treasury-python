# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import AccountDetail
from modern_treasury.pagination import SyncPage, AsyncPage

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
            "string",
            accounts_type="external_accounts",
            account_number="string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.account_details.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
            account_number_type="clabe",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.account_details.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.account_details.list(
            "string",
            accounts_type="external_accounts",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.account_details.list(
            "string",
            accounts_type="external_accounts",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        resource = client.account_details.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
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
            "string",
            accounts_type="external_accounts",
            account_number="string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
            account_number_type="clabe",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert isinstance(resource, AccountDetail)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.list(
            "string",
            accounts_type="external_accounts",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.list(
            "string",
            accounts_type="external_accounts",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        resource = await client.account_details.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert resource is None
