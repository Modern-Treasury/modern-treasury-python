# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    PaymentRequest,
)
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        payment_request = client.payment_requests.retrieve(
            "id",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.payment_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.payment_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        payment_request = client.payment_requests.update(
            id="id",
            status="approved",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.payment_requests.with_raw_response.update(
            id="id",
            status="approved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.payment_requests.with_streaming_response.update(
            id="id",
            status="approved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_requests.with_raw_response.update(
                id="",
                status="approved",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        payment_request = client.payment_requests.list()
        assert_matches_type(SyncPage[PaymentRequest], payment_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        payment_request = client.payment_requests.list(
            id="id",
            after_cursor="after_cursor",
            created_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            internal_account_id="internal_account_id",
            per_page=0,
            status="approved",
            type="wire",
        )
        assert_matches_type(SyncPage[PaymentRequest], payment_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.payment_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(SyncPage[PaymentRequest], payment_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.payment_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(SyncPage[PaymentRequest], payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel_simulation(self, client: ModernTreasury) -> None:
        payment_request = client.payment_requests.cancel_simulation(
            id="id",
            status="cancelled",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_raw_response_cancel_simulation(self, client: ModernTreasury) -> None:
        response = client.payment_requests.with_raw_response.cancel_simulation(
            id="id",
            status="cancelled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_streaming_response_cancel_simulation(self, client: ModernTreasury) -> None:
        with client.payment_requests.with_streaming_response.cancel_simulation(
            id="id",
            status="cancelled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel_simulation(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_requests.with_raw_response.cancel_simulation(
                id="",
                status="cancelled",
            )

    @parametrize
    def test_method_simulate(self, client: ModernTreasury) -> None:
        payment_request = client.payment_requests.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_method_simulate_with_all_params(self, client: ModernTreasury) -> None:
        payment_request = client.payment_requests.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
            description="description",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_raw_response_simulate(self, client: ModernTreasury) -> None:
        response = client.payment_requests.with_raw_response.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    def test_streaming_response_simulate(self, client: ModernTreasury) -> None:
        with client.payment_requests.with_streaming_response.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        payment_request = await async_client.payment_requests.retrieve(
            "id",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        payment_request = await async_client.payment_requests.update(
            id="id",
            status="approved",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_requests.with_raw_response.update(
            id="id",
            status="approved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_requests.with_streaming_response.update(
            id="id",
            status="approved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_requests.with_raw_response.update(
                id="",
                status="approved",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        payment_request = await async_client.payment_requests.list()
        assert_matches_type(AsyncPage[PaymentRequest], payment_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_request = await async_client.payment_requests.list(
            id="id",
            after_cursor="after_cursor",
            created_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            internal_account_id="internal_account_id",
            per_page=0,
            status="approved",
            type="wire",
        )
        assert_matches_type(AsyncPage[PaymentRequest], payment_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(AsyncPage[PaymentRequest], payment_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(AsyncPage[PaymentRequest], payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel_simulation(self, async_client: AsyncModernTreasury) -> None:
        payment_request = await async_client.payment_requests.cancel_simulation(
            id="id",
            status="cancelled",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_raw_response_cancel_simulation(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_requests.with_raw_response.cancel_simulation(
            id="id",
            status="cancelled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_simulation(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_requests.with_streaming_response.cancel_simulation(
            id="id",
            status="cancelled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel_simulation(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_requests.with_raw_response.cancel_simulation(
                id="",
                status="cancelled",
            )

    @parametrize
    async def test_method_simulate(self, async_client: AsyncModernTreasury) -> None:
        payment_request = await async_client.payment_requests.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_method_simulate_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_request = await async_client.payment_requests.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
            description="description",
        )
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_raw_response_simulate(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_requests.with_raw_response.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_request = response.parse()
        assert_matches_type(PaymentRequest, payment_request, path=["response"])

    @parametrize
    async def test_streaming_response_simulate(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_requests.with_streaming_response.simulate(
            amount=0,
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requesting_account_number="requesting_account_number",
            requesting_party_name="requesting_party_name",
            requesting_routing_number="requesting_routing_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_request = await response.parse()
            assert_matches_type(PaymentRequest, payment_request, path=["response"])

        assert cast(Any, response.is_closed) is True
