# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import BulkResult
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestBulkResults:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        bulk_result = client.bulk_results.retrieve(
            "string",
        )
        assert_matches_type(BulkResult, bulk_result, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.bulk_results.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_result = response.parse()
        assert_matches_type(BulkResult, bulk_result, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.bulk_results.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_result = response.parse()
            assert_matches_type(BulkResult, bulk_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        bulk_result = client.bulk_results.list()
        assert_matches_type(SyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        bulk_result = client.bulk_results.list(
            after_cursor="string",
            entity_id="string",
            entity_type="payment_order",
            per_page=0,
            request_id="string",
            request_type="bulk_request",
            status="pending",
        )
        assert_matches_type(SyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.bulk_results.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_result = response.parse()
        assert_matches_type(SyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.bulk_results.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_result = response.parse()
            assert_matches_type(SyncPage[BulkResult], bulk_result, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulkResults:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        bulk_result = await client.bulk_results.retrieve(
            "string",
        )
        assert_matches_type(BulkResult, bulk_result, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.bulk_results.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_result = response.parse()
        assert_matches_type(BulkResult, bulk_result, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.bulk_results.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_result = await response.parse()
            assert_matches_type(BulkResult, bulk_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        bulk_result = await client.bulk_results.list()
        assert_matches_type(AsyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        bulk_result = await client.bulk_results.list(
            after_cursor="string",
            entity_id="string",
            entity_type="payment_order",
            per_page=0,
            request_id="string",
            request_type="bulk_request",
            status="pending",
        )
        assert_matches_type(AsyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.bulk_results.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_result = response.parse()
        assert_matches_type(AsyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncModernTreasury) -> None:
        async with client.bulk_results.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_result = await response.parse()
            assert_matches_type(AsyncPage[BulkResult], bulk_result, path=["response"])

        assert cast(Any, response.is_closed) is True
