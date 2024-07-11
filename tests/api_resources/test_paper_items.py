# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import PaperItem
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaperItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        paper_item = client.paper_items.retrieve(
            "id",
        )
        assert_matches_type(PaperItem, paper_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.paper_items.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_item = response.parse()
        assert_matches_type(PaperItem, paper_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.paper_items.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper_item = response.parse()
            assert_matches_type(PaperItem, paper_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.paper_items.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        paper_item = client.paper_items.list()
        assert_matches_type(SyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        paper_item = client.paper_items.list(
            after_cursor="after_cursor",
            deposit_date_end=parse_date("2019-12-27"),
            deposit_date_start=parse_date("2019-12-27"),
            lockbox_number="lockbox_number",
            per_page=0,
        )
        assert_matches_type(SyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.paper_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_item = response.parse()
        assert_matches_type(SyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.paper_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper_item = response.parse()
            assert_matches_type(SyncPage[PaperItem], paper_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaperItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        paper_item = await async_client.paper_items.retrieve(
            "id",
        )
        assert_matches_type(PaperItem, paper_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.paper_items.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_item = response.parse()
        assert_matches_type(PaperItem, paper_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.paper_items.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper_item = await response.parse()
            assert_matches_type(PaperItem, paper_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.paper_items.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        paper_item = await async_client.paper_items.list()
        assert_matches_type(AsyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        paper_item = await async_client.paper_items.list(
            after_cursor="after_cursor",
            deposit_date_end=parse_date("2019-12-27"),
            deposit_date_start=parse_date("2019-12-27"),
            lockbox_number="lockbox_number",
            per_page=0,
        )
        assert_matches_type(AsyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.paper_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_item = response.parse()
        assert_matches_type(AsyncPage[PaperItem], paper_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.paper_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper_item = await response.parse()
            assert_matches_type(AsyncPage[PaperItem], paper_item, path=["response"])

        assert cast(Any, response.is_closed) is True
