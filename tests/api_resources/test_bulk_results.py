# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.bulk_result import BulkResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bulk_results.with_raw_response.retrieve(
                "",
            )

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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        bulk_result = await async_client.bulk_results.retrieve(
            "string",
        )
        assert_matches_type(BulkResult, bulk_result, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.bulk_results.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_result = response.parse()
        assert_matches_type(BulkResult, bulk_result, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.bulk_results.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_result = await response.parse()
            assert_matches_type(BulkResult, bulk_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bulk_results.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        bulk_result = await async_client.bulk_results.list()
        assert_matches_type(AsyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        bulk_result = await async_client.bulk_results.list(
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
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.bulk_results.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_result = response.parse()
        assert_matches_type(AsyncPage[BulkResult], bulk_result, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.bulk_results.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_result = await response.parse()
            assert_matches_type(AsyncPage[BulkResult], bulk_result, path=["response"])

        assert cast(Any, response.is_closed) is True
