# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LineItem
from modern_treasury.pagination import SyncPage, AsyncPage

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
        line_item = client.line_items.retrieve(
            "string",
            itemizable_type="expected_payments",
            itemizable_id="string",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        line_item = client.line_items.update(
            "string",
            itemizable_type="expected_payments",
            itemizable_id="string",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.line_items.update(
            "string",
            itemizable_type="expected_payments",
            itemizable_id="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        line_item = client.line_items.list(
            "string",
            itemizable_type="expected_payments",
        )
        assert_matches_type(SyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.line_items.list(
            "string",
            itemizable_type="expected_payments",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[LineItem], line_item, path=["response"])


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
        line_item = await client.line_items.retrieve(
            "string",
            itemizable_type="expected_payments",
            itemizable_id="string",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        line_item = await client.line_items.update(
            "string",
            itemizable_type="expected_payments",
            itemizable_id="string",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        line_item = await client.line_items.update(
            "string",
            itemizable_type="expected_payments",
            itemizable_id="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        line_item = await client.line_items.list(
            "string",
            itemizable_type="expected_payments",
        )
        assert_matches_type(AsyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        line_item = await client.line_items.list(
            "string",
            itemizable_type="expected_payments",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[LineItem], line_item, path=["response"])
