# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.transactions import TransactionLineItem

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLineItems:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        line_item = client.transactions.line_items.list(
            "string",
        )
        assert_matches_type(SyncPage[TransactionLineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.transactions.line_items.list(
            "string",
            after_cursor="string",
            per_page=0,
            type="originating",
        )
        assert_matches_type(SyncPage[TransactionLineItem], line_item, path=["response"])


class TestAsyncLineItems:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        line_item = await client.transactions.line_items.list(
            "string",
        )
        assert_matches_type(AsyncPage[TransactionLineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        line_item = await client.transactions.line_items.list(
            "string",
            after_cursor="string",
            per_page=0,
            type="originating",
        )
        assert_matches_type(AsyncPage[TransactionLineItem], line_item, path=["response"])
