# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import InternalAccount
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
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
        internal_account = client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
            counterparty_id="string",
            parent_account_id="string",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            vendor_attributes={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.retrieve(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.update(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.update(
            "string",
            counterparty_id="string",
            metadata={"foo": "string"},
            name="string",
            parent_account_id="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.list()
        assert_matches_type(SyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.list(
            after_cursor="string",
            counterparty_id="string",
            currency="AED",
            metadata={"foo": "string"},
            payment_direction="credit",
            payment_type="ach",
            per_page=0,
        )
        assert_matches_type(SyncPage[InternalAccount], internal_account, path=["response"])


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
        internal_account = await client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
            counterparty_id="string",
            parent_account_id="string",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            vendor_attributes={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.retrieve(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.update(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.update(
            "string",
            counterparty_id="string",
            metadata={"foo": "string"},
            name="string",
            parent_account_id="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.list()
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.list(
            after_cursor="string",
            counterparty_id="string",
            currency="AED",
            metadata={"foo": "string"},
            payment_direction="credit",
            payment_type="ach",
            per_page=0,
        )
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])
