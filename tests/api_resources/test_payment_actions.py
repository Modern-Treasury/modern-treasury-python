# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    PaymentActionListResponse,
    PaymentActionCreateResponse,
    PaymentActionUpdateResponse,
    PaymentActionRetrieveResponse,
)
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        payment_action = client.payment_actions.create(
            type="type",
        )
        assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        payment_action = client.payment_actions.create(
            type="type",
            actionable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actionable_type="actionable_type",
            details={},
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.payment_actions.with_raw_response.create(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.payment_actions.with_streaming_response.create(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = response.parse()
            assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        payment_action = client.payment_actions.retrieve(
            "id",
        )
        assert_matches_type(PaymentActionRetrieveResponse, payment_action, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.payment_actions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(PaymentActionRetrieveResponse, payment_action, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.payment_actions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = response.parse()
            assert_matches_type(PaymentActionRetrieveResponse, payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_actions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        payment_action = client.payment_actions.update(
            id="id",
            status="pending",
        )
        assert_matches_type(PaymentActionUpdateResponse, payment_action, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.payment_actions.with_raw_response.update(
            id="id",
            status="pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(PaymentActionUpdateResponse, payment_action, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.payment_actions.with_streaming_response.update(
            id="id",
            status="pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = response.parse()
            assert_matches_type(PaymentActionUpdateResponse, payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_actions.with_raw_response.update(
                id="",
                status="pending",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        payment_action = client.payment_actions.list()
        assert_matches_type(SyncPage[PaymentActionListResponse], payment_action, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        payment_action = client.payment_actions.list(
            actionable_id="actionable_id",
            actionable_type="actionable_type",
            after_cursor="after_cursor",
            created_at={
                "eq": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            internal_account_id="internal_account_id",
            metadata={"foo": "string"},
            per_page=0,
            status="pending",
            type="stop",
        )
        assert_matches_type(SyncPage[PaymentActionListResponse], payment_action, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.payment_actions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(SyncPage[PaymentActionListResponse], payment_action, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.payment_actions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = response.parse()
            assert_matches_type(SyncPage[PaymentActionListResponse], payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        payment_action = await async_client.payment_actions.create(
            type="type",
        )
        assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_action = await async_client.payment_actions.create(
            type="type",
            actionable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actionable_type="actionable_type",
            details={},
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_actions.with_raw_response.create(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_actions.with_streaming_response.create(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = await response.parse()
            assert_matches_type(PaymentActionCreateResponse, payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        payment_action = await async_client.payment_actions.retrieve(
            "id",
        )
        assert_matches_type(PaymentActionRetrieveResponse, payment_action, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_actions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(PaymentActionRetrieveResponse, payment_action, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_actions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = await response.parse()
            assert_matches_type(PaymentActionRetrieveResponse, payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_actions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        payment_action = await async_client.payment_actions.update(
            id="id",
            status="pending",
        )
        assert_matches_type(PaymentActionUpdateResponse, payment_action, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_actions.with_raw_response.update(
            id="id",
            status="pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(PaymentActionUpdateResponse, payment_action, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_actions.with_streaming_response.update(
            id="id",
            status="pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = await response.parse()
            assert_matches_type(PaymentActionUpdateResponse, payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_actions.with_raw_response.update(
                id="",
                status="pending",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        payment_action = await async_client.payment_actions.list()
        assert_matches_type(AsyncPage[PaymentActionListResponse], payment_action, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_action = await async_client.payment_actions.list(
            actionable_id="actionable_id",
            actionable_type="actionable_type",
            after_cursor="after_cursor",
            created_at={
                "eq": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            internal_account_id="internal_account_id",
            metadata={"foo": "string"},
            per_page=0,
            status="pending",
            type="stop",
        )
        assert_matches_type(AsyncPage[PaymentActionListResponse], payment_action, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_actions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_action = response.parse()
        assert_matches_type(AsyncPage[PaymentActionListResponse], payment_action, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_actions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_action = await response.parse()
            assert_matches_type(AsyncPage[PaymentActionListResponse], payment_action, path=["response"])

        assert cast(Any, response.is_closed) is True
