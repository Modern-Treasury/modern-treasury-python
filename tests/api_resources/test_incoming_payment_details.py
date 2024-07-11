# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    IncomingPaymentDetail,
)
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.shared import AsyncResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIncomingPaymentDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.retrieve(
            "id",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.incoming_payment_details.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.incoming_payment_details.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = response.parse()
            assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.incoming_payment_details.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.update(
            id="id",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.update(
            id="id",
            metadata={"foo": "string"},
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.incoming_payment_details.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.incoming_payment_details.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = response.parse()
            assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.incoming_payment_details.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.list()
        assert_matches_type(SyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.list(
            after_cursor="after_cursor",
            as_of_date_end=parse_date("2019-12-27"),
            as_of_date_start=parse_date("2019-12-27"),
            direction="credit",
            metadata={"foo": "string"},
            per_page=0,
            status="completed",
            type="ach",
            virtual_account_id="virtual_account_id",
        )
        assert_matches_type(SyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.incoming_payment_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(SyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.incoming_payment_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = response.parse()
            assert_matches_type(SyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_async(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.create_async()
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_create_async_with_all_params(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.create_async(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            currency="AED",
            description="description",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    def test_raw_response_create_async(self, client: ModernTreasury) -> None:
        response = client.incoming_payment_details.with_raw_response.create_async()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    def test_streaming_response_create_async(self, client: ModernTreasury) -> None:
        with client.incoming_payment_details.with_streaming_response.create_async() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = response.parse()
            assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIncomingPaymentDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await async_client.incoming_payment_details.retrieve(
            "id",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.incoming_payment_details.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.incoming_payment_details.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = await response.parse()
            assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.incoming_payment_details.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await async_client.incoming_payment_details.update(
            id="id",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await async_client.incoming_payment_details.update(
            id="id",
            metadata={"foo": "string"},
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.incoming_payment_details.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.incoming_payment_details.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = await response.parse()
            assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.incoming_payment_details.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await async_client.incoming_payment_details.list()
        assert_matches_type(AsyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await async_client.incoming_payment_details.list(
            after_cursor="after_cursor",
            as_of_date_end=parse_date("2019-12-27"),
            as_of_date_start=parse_date("2019-12-27"),
            direction="credit",
            metadata={"foo": "string"},
            per_page=0,
            status="completed",
            type="ach",
            virtual_account_id="virtual_account_id",
        )
        assert_matches_type(AsyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.incoming_payment_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(AsyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.incoming_payment_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = await response.parse()
            assert_matches_type(AsyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_async(self, async_client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await async_client.incoming_payment_details.create_async()
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_create_async_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await async_client.incoming_payment_details.create_async(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            currency="AED",
            description="description",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_raw_response_create_async(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.incoming_payment_details.with_raw_response.create_async()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming_payment_detail = response.parse()
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_streaming_response_create_async(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.incoming_payment_details.with_streaming_response.create_async() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming_payment_detail = await response.parse()
            assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

        assert cast(Any, response.is_closed) is True
