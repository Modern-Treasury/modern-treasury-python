# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import AccountCollectionFlow
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountCollectionFlows:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.retrieve(
            "string",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.update(
            "string",
            status="cancelled",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.list()
        assert_matches_type(SyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.list(
            after_cursor="string",
            client_token="string",
            counterparty_id="string",
            external_account_id="string",
            per_page=0,
            status="string",
        )
        assert_matches_type(SyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])


class TestAsyncAccountCollectionFlows:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.retrieve(
            "string",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.update(
            "string",
            status="cancelled",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.list()
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.list(
            after_cursor="string",
            client_token="string",
            counterparty_id="string",
            external_account_id="string",
            per_page=0,
            status="string",
        )
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])
