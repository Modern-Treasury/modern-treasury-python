# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    HoldListResponse,
    HoldCreateResponse,
    HoldUpdateResponse,
    HoldRetrieveResponse,
)
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHolds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        hold = client.holds.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
        )
        assert_matches_type(HoldCreateResponse, hold, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        hold = client.holds.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
            metadata={"foo": "string"},
            reason="reason",
        )
        assert_matches_type(HoldCreateResponse, hold, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.holds.with_raw_response.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldCreateResponse, hold, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.holds.with_streaming_response.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(HoldCreateResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        hold = client.holds.retrieve(
            "id",
        )
        assert_matches_type(HoldRetrieveResponse, hold, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.holds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldRetrieveResponse, hold, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.holds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(HoldRetrieveResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.holds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        hold = client.holds.update(
            id="id",
            status="resolved",
        )
        assert_matches_type(HoldUpdateResponse, hold, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        hold = client.holds.update(
            id="id",
            status="resolved",
            resolution="resolution",
        )
        assert_matches_type(HoldUpdateResponse, hold, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.holds.with_raw_response.update(
            id="id",
            status="resolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldUpdateResponse, hold, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.holds.with_streaming_response.update(
            id="id",
            status="resolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(HoldUpdateResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.holds.with_raw_response.update(
                id="",
                status="resolved",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        hold = client.holds.list()
        assert_matches_type(SyncPage[HoldListResponse], hold, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        hold = client.holds.list(
            after_cursor="after_cursor",
            metadata={"foo": "string"},
            per_page=0,
            status="active",
            target_id="target_id",
            target_type="payment_order",
        )
        assert_matches_type(SyncPage[HoldListResponse], hold, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.holds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(SyncPage[HoldListResponse], hold, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.holds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(SyncPage[HoldListResponse], hold, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHolds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        hold = await async_client.holds.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
        )
        assert_matches_type(HoldCreateResponse, hold, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        hold = await async_client.holds.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
            metadata={"foo": "string"},
            reason="reason",
        )
        assert_matches_type(HoldCreateResponse, hold, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.holds.with_raw_response.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldCreateResponse, hold, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.holds.with_streaming_response.create(
            status="active",
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_type="payment_order",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(HoldCreateResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        hold = await async_client.holds.retrieve(
            "id",
        )
        assert_matches_type(HoldRetrieveResponse, hold, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.holds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldRetrieveResponse, hold, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.holds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(HoldRetrieveResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.holds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        hold = await async_client.holds.update(
            id="id",
            status="resolved",
        )
        assert_matches_type(HoldUpdateResponse, hold, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        hold = await async_client.holds.update(
            id="id",
            status="resolved",
            resolution="resolution",
        )
        assert_matches_type(HoldUpdateResponse, hold, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.holds.with_raw_response.update(
            id="id",
            status="resolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldUpdateResponse, hold, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.holds.with_streaming_response.update(
            id="id",
            status="resolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(HoldUpdateResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.holds.with_raw_response.update(
                id="",
                status="resolved",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        hold = await async_client.holds.list()
        assert_matches_type(AsyncPage[HoldListResponse], hold, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        hold = await async_client.holds.list(
            after_cursor="after_cursor",
            metadata={"foo": "string"},
            per_page=0,
            status="active",
            target_id="target_id",
            target_type="payment_order",
        )
        assert_matches_type(AsyncPage[HoldListResponse], hold, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.holds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(AsyncPage[HoldListResponse], hold, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.holds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(AsyncPage[HoldListResponse], hold, path=["response"])

        assert cast(Any, response.is_closed) is True
