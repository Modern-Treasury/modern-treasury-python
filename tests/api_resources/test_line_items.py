# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LineItem
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLineItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        line_item = client.line_items.retrieve(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.line_items.with_raw_response.retrieve(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.line_items.with_streaming_response.retrieve(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(LineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `itemizable_id` but received ''"):
            client.line_items.with_raw_response.retrieve(
                id="id",
                itemizable_type="expected_payments",
                itemizable_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.line_items.with_raw_response.retrieve(
                id="",
                itemizable_type="expected_payments",
                itemizable_id="itemizable_id",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        line_item = client.line_items.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.line_items.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.line_items.with_raw_response.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.line_items.with_streaming_response.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(LineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `itemizable_id` but received ''"):
            client.line_items.with_raw_response.update(
                id="id",
                itemizable_type="expected_payments",
                itemizable_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.line_items.with_raw_response.update(
                id="",
                itemizable_type="expected_payments",
                itemizable_id="itemizable_id",
            )

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        line_item = client.line_items.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
        )
        assert_matches_type(SyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.line_items.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(SyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.line_items.with_raw_response.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(SyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.line_items.with_streaming_response.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(SyncPage[LineItem], line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_path_params_list(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `itemizable_id` but received ''"):
            client.line_items.with_raw_response.list(
                itemizable_id="",
                itemizable_type="expected_payments",
            )


class TestAsyncLineItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.line_items.retrieve(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.line_items.with_raw_response.retrieve(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.line_items.with_streaming_response.retrieve(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(LineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `itemizable_id` but received ''"):
            await async_client.line_items.with_raw_response.retrieve(
                id="id",
                itemizable_type="expected_payments",
                itemizable_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.line_items.with_raw_response.retrieve(
                id="",
                itemizable_type="expected_payments",
                itemizable_id="itemizable_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.line_items.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.line_items.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.line_items.with_raw_response.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(LineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.line_items.with_streaming_response.update(
            id="id",
            itemizable_type="expected_payments",
            itemizable_id="itemizable_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(LineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `itemizable_id` but received ''"):
            await async_client.line_items.with_raw_response.update(
                id="id",
                itemizable_type="expected_payments",
                itemizable_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.line_items.with_raw_response.update(
                id="",
                itemizable_type="expected_payments",
                itemizable_id="itemizable_id",
            )

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.line_items.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
        )
        assert_matches_type(AsyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.line_items.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(AsyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.line_items.with_raw_response.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(AsyncPage[LineItem], line_item, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.line_items.with_streaming_response.list(
            itemizable_id="itemizable_id",
            itemizable_type="expected_payments",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(AsyncPage[LineItem], line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `itemizable_id` but received ''"):
            await async_client.line_items.with_raw_response.list(
                itemizable_id="",
                itemizable_type="expected_payments",
            )
