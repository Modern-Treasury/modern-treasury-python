# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import RoutingDetail
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutingDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
            payment_type="ach",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.routing_details.with_raw_response.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.routing_details.with_streaming_response.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = response.parse()
            assert_matches_type(RoutingDetail, routing_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.routing_details.with_raw_response.create(
                account_id="",
                accounts_type="external_accounts",
                routing_number="routing_number",
                routing_number_type="aba",
            )

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.retrieve(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.routing_details.with_raw_response.retrieve(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.routing_details.with_streaming_response.retrieve(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = response.parse()
            assert_matches_type(RoutingDetail, routing_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.routing_details.with_raw_response.retrieve(
                id="id",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routing_details.with_raw_response.retrieve(
                id="",
                accounts_type="external_accounts",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.list(
            account_id="account_id",
            accounts_type="external_accounts",
        )
        assert_matches_type(SyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.list(
            account_id="account_id",
            accounts_type="external_accounts",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(SyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.routing_details.with_raw_response.list(
            account_id="account_id",
            accounts_type="external_accounts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert_matches_type(SyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.routing_details.with_streaming_response.list(
            account_id="account_id",
            accounts_type="external_accounts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = response.parse()
            assert_matches_type(SyncPage[RoutingDetail], routing_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.routing_details.with_raw_response.list(
                account_id="",
                accounts_type="external_accounts",
            )

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.delete(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )
        assert routing_detail is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.routing_details.with_raw_response.delete(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert routing_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.routing_details.with_streaming_response.delete(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = response.parse()
            assert routing_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.routing_details.with_raw_response.delete(
                id="id",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routing_details.with_raw_response.delete(
                id="",
                accounts_type="external_accounts",
                account_id="account_id",
            )


class TestAsyncRoutingDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        routing_detail = await async_client.routing_details.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        routing_detail = await async_client.routing_details.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
            payment_type="ach",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.routing_details.with_raw_response.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.routing_details.with_streaming_response.create(
            account_id="account_id",
            accounts_type="external_accounts",
            routing_number="routing_number",
            routing_number_type="aba",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = await response.parse()
            assert_matches_type(RoutingDetail, routing_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.routing_details.with_raw_response.create(
                account_id="",
                accounts_type="external_accounts",
                routing_number="routing_number",
                routing_number_type="aba",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        routing_detail = await async_client.routing_details.retrieve(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.routing_details.with_raw_response.retrieve(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.routing_details.with_streaming_response.retrieve(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = await response.parse()
            assert_matches_type(RoutingDetail, routing_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.routing_details.with_raw_response.retrieve(
                id="id",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routing_details.with_raw_response.retrieve(
                id="",
                accounts_type="external_accounts",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        routing_detail = await async_client.routing_details.list(
            account_id="account_id",
            accounts_type="external_accounts",
        )
        assert_matches_type(AsyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        routing_detail = await async_client.routing_details.list(
            account_id="account_id",
            accounts_type="external_accounts",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(AsyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.routing_details.with_raw_response.list(
            account_id="account_id",
            accounts_type="external_accounts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert_matches_type(AsyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.routing_details.with_streaming_response.list(
            account_id="account_id",
            accounts_type="external_accounts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = await response.parse()
            assert_matches_type(AsyncPage[RoutingDetail], routing_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.routing_details.with_raw_response.list(
                account_id="",
                accounts_type="external_accounts",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        routing_detail = await async_client.routing_details.delete(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )
        assert routing_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.routing_details.with_raw_response.delete(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_detail = response.parse()
        assert routing_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.routing_details.with_streaming_response.delete(
            id="id",
            accounts_type="external_accounts",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_detail = await response.parse()
            assert routing_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.routing_details.with_raw_response.delete(
                id="id",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routing_details.with_raw_response.delete(
                id="",
                accounts_type="external_accounts",
                account_id="account_id",
            )
