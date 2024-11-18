# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.payment_orders import Reversal

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReversals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        reversal = client.payment_orders.reversals.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
        )
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        reversal = client.payment_orders.reversals.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
            ledger_transaction={
                "ledger_entries": [
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "available_balance_amount": {"foo": 0},
                        "lock_version": 0,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                    }
                ],
                "description": "description",
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_date": parse_date("2019-12-27"),
                "external_id": "external_id",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "ledgerable_type": "expected_payment",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "status": "archived",
            },
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.payment_orders.reversals.with_raw_response.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reversal = response.parse()
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.payment_orders.reversals.with_streaming_response.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reversal = response.parse()
            assert_matches_type(Reversal, reversal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            client.payment_orders.reversals.with_raw_response.create(
                payment_order_id="",
                reason="duplicate",
            )

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        reversal = client.payment_orders.reversals.retrieve(
            reversal_id="reversal_id",
            payment_order_id="payment_order_id",
        )
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.payment_orders.reversals.with_raw_response.retrieve(
            reversal_id="reversal_id",
            payment_order_id="payment_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reversal = response.parse()
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.payment_orders.reversals.with_streaming_response.retrieve(
            reversal_id="reversal_id",
            payment_order_id="payment_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reversal = response.parse()
            assert_matches_type(Reversal, reversal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            client.payment_orders.reversals.with_raw_response.retrieve(
                reversal_id="reversal_id",
                payment_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reversal_id` but received ''"):
            client.payment_orders.reversals.with_raw_response.retrieve(
                reversal_id="",
                payment_order_id="payment_order_id",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        reversal = client.payment_orders.reversals.list(
            payment_order_id="payment_order_id",
        )
        assert_matches_type(SyncPage[Reversal], reversal, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        reversal = client.payment_orders.reversals.list(
            payment_order_id="payment_order_id",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(SyncPage[Reversal], reversal, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.payment_orders.reversals.with_raw_response.list(
            payment_order_id="payment_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reversal = response.parse()
        assert_matches_type(SyncPage[Reversal], reversal, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.payment_orders.reversals.with_streaming_response.list(
            payment_order_id="payment_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reversal = response.parse()
            assert_matches_type(SyncPage[Reversal], reversal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            client.payment_orders.reversals.with_raw_response.list(
                payment_order_id="",
            )


class TestAsyncReversals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        reversal = await async_client.payment_orders.reversals.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
        )
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        reversal = await async_client.payment_orders.reversals.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
            ledger_transaction={
                "ledger_entries": [
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "available_balance_amount": {"foo": 0},
                        "lock_version": 0,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                    }
                ],
                "description": "description",
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_date": parse_date("2019-12-27"),
                "external_id": "external_id",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "ledgerable_type": "expected_payment",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "status": "archived",
            },
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.reversals.with_raw_response.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reversal = response.parse()
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.reversals.with_streaming_response.create(
            payment_order_id="payment_order_id",
            reason="duplicate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reversal = await response.parse()
            assert_matches_type(Reversal, reversal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            await async_client.payment_orders.reversals.with_raw_response.create(
                payment_order_id="",
                reason="duplicate",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        reversal = await async_client.payment_orders.reversals.retrieve(
            reversal_id="reversal_id",
            payment_order_id="payment_order_id",
        )
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.reversals.with_raw_response.retrieve(
            reversal_id="reversal_id",
            payment_order_id="payment_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reversal = response.parse()
        assert_matches_type(Reversal, reversal, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.reversals.with_streaming_response.retrieve(
            reversal_id="reversal_id",
            payment_order_id="payment_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reversal = await response.parse()
            assert_matches_type(Reversal, reversal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            await async_client.payment_orders.reversals.with_raw_response.retrieve(
                reversal_id="reversal_id",
                payment_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reversal_id` but received ''"):
            await async_client.payment_orders.reversals.with_raw_response.retrieve(
                reversal_id="",
                payment_order_id="payment_order_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        reversal = await async_client.payment_orders.reversals.list(
            payment_order_id="payment_order_id",
        )
        assert_matches_type(AsyncPage[Reversal], reversal, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        reversal = await async_client.payment_orders.reversals.list(
            payment_order_id="payment_order_id",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(AsyncPage[Reversal], reversal, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.reversals.with_raw_response.list(
            payment_order_id="payment_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reversal = response.parse()
        assert_matches_type(AsyncPage[Reversal], reversal, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.reversals.with_streaming_response.list(
            payment_order_id="payment_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reversal = await response.parse()
            assert_matches_type(AsyncPage[Reversal], reversal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            await async_client.payment_orders.reversals.with_raw_response.list(
                payment_order_id="",
            )
