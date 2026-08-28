# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    VirtualAccountSetting,
)
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVirtualAccountSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        virtual_account_setting = client.virtual_account_settings.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        virtual_account_setting = client.virtual_account_settings.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allocation_identifier="allocation_identifier",
            allocation_length=0,
            allocation_range_end="allocation_range_end",
            allocation_range_start="allocation_range_start",
            external_id="external_id",
            generated_allocation_identifier_length=0,
        )
        assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.virtual_account_settings.with_raw_response.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account_setting = response.parse()
        assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.virtual_account_settings.with_streaming_response.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_account_setting = response.parse()
            assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        virtual_account_setting = client.virtual_account_settings.list()
        assert_matches_type(SyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        virtual_account_setting = client.virtual_account_settings.list(
            after_cursor="after_cursor",
            external_id="external_id",
            per_page=0,
        )
        assert_matches_type(SyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.virtual_account_settings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account_setting = response.parse()
        assert_matches_type(SyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.virtual_account_settings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_account_setting = response.parse()
            assert_matches_type(SyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVirtualAccountSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        virtual_account_setting = await async_client.virtual_account_settings.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        virtual_account_setting = await async_client.virtual_account_settings.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allocation_identifier="allocation_identifier",
            allocation_length=0,
            allocation_range_end="allocation_range_end",
            allocation_range_start="allocation_range_start",
            external_id="external_id",
            generated_allocation_identifier_length=0,
        )
        assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.virtual_account_settings.with_raw_response.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account_setting = response.parse()
        assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.virtual_account_settings.with_streaming_response.create(
            allocation_type="allocation_type",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_account_setting = await response.parse()
            assert_matches_type(VirtualAccountSetting, virtual_account_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        virtual_account_setting = await async_client.virtual_account_settings.list()
        assert_matches_type(AsyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        virtual_account_setting = await async_client.virtual_account_settings.list(
            after_cursor="after_cursor",
            external_id="external_id",
            per_page=0,
        )
        assert_matches_type(AsyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.virtual_account_settings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account_setting = response.parse()
        assert_matches_type(AsyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.virtual_account_settings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_account_setting = await response.parse()
            assert_matches_type(AsyncPage[VirtualAccountSetting], virtual_account_setting, path=["response"])

        assert cast(Any, response.is_closed) is True
