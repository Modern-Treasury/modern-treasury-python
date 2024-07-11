# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import ReturnObject
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReturns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        return_ = client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        return_ = client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
            additional_information="additional_information",
            code="901",
            date_of_death=parse_date("2019-12-27"),
            reason="reason",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.returns.with_raw_response.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.returns.with_streaming_response.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(ReturnObject, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        return_ = client.returns.retrieve(
            "id",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.returns.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.returns.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(ReturnObject, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.returns.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        return_ = client.returns.list()
        assert_matches_type(SyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        return_ = client.returns.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            internal_account_id="internal_account_id",
            per_page=0,
            returnable_id="returnable_id",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(SyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.returns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(SyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.returns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(SyncPage[ReturnObject], return_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReturns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        return_ = await async_client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        return_ = await async_client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
            additional_information="additional_information",
            code="901",
            date_of_death=parse_date("2019-12-27"),
            reason="reason",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.returns.with_raw_response.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.returns.with_streaming_response.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(ReturnObject, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        return_ = await async_client.returns.retrieve(
            "id",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.returns.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.returns.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(ReturnObject, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.returns.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        return_ = await async_client.returns.list()
        assert_matches_type(AsyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        return_ = await async_client.returns.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            internal_account_id="internal_account_id",
            per_page=0,
            returnable_id="returnable_id",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(AsyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.returns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(AsyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.returns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(AsyncPage[ReturnObject], return_, path=["response"])

        assert cast(Any, response.is_closed) is True
