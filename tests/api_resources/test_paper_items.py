# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import PaperItem
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestPaperItems:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        paper_item = client.paper_items.retrieve(
            "string",
        )
        assert_matches_type(PaperItem, paper_item, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        paper_item = client.paper_items.list()
        assert_matches_type(SyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        paper_item = client.paper_items.list(
            after_cursor="string",
            deposit_date_end=parse_date("2019-12-27"),
            deposit_date_start=parse_date("2019-12-27"),
            lockbox_number="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[PaperItem], paper_item, path=["response"])


class TestAsyncPaperItems:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        paper_item = await client.paper_items.retrieve(
            "string",
        )
        assert_matches_type(PaperItem, paper_item, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        paper_item = await client.paper_items.list()
        assert_matches_type(AsyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        paper_item = await client.paper_items.list(
            after_cursor="string",
            deposit_date_end=parse_date("2019-12-27"),
            deposit_date_start=parse_date("2019-12-27"),
            lockbox_number="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[PaperItem], paper_item, path=["response"])
