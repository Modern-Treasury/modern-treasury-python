# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.transactions import TransactionLineItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLineItems:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        line_item = client.transactions.line_items.retrieve(
            "string",
        )
        assert_matches_type(TransactionLineItem, line_item, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        line_item = client.transactions.line_items.list()
        assert_matches_type(SyncPage[TransactionLineItem], line_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.transactions.line_items.list(
            id={"foo": "string"},
            after_cursor="string",
            per_page=0,
            transaction_id="string",
            type="originating",
        )
        assert_matches_type(SyncPage[TransactionLineItem], line_item, path=["response"])


class TestAsyncLineItems:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        line_item = await client.transactions.line_items.retrieve(
            "string",
        )
        assert_matches_type(TransactionLineItem, line_item, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        line_item = await client.transactions.line_items.list()
        assert_matches_type(AsyncPage[TransactionLineItem], line_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        line_item = await client.transactions.line_items.list(
            id={"foo": "string"},
            after_cursor="string",
            per_page=0,
            transaction_id="string",
            type="originating",
        )
        assert_matches_type(AsyncPage[TransactionLineItem], line_item, path=["response"])
