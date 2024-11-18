# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerAccountBalanceMonitor,
)
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerAccountBalanceMonitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_account_balance_monitors.with_raw_response.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.retrieve(
            "id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_account_balance_monitors.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_balance_monitors.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.update(
            id="id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_account_balance_monitors.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_balance_monitors.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.list()
        assert_matches_type(SyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.list(
            id=["string"],
            after_cursor="after_cursor",
            ledger_account_id="ledger_account_id",
            metadata={"foo": "string"},
            per_page=0,
        )
        assert_matches_type(SyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_account_balance_monitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(SyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(
                SyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.delete(
            "id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.ledger_account_balance_monitors.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_balance_monitors.with_raw_response.delete(
                "",
            )


class TestAsyncLedgerAccountBalanceMonitors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_balance_monitors.with_raw_response.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_balance_monitors.with_streaming_response.create(
            alert_condition={
                "field": "field",
                "operator": "operator",
                "value": 0,
            },
            ledger_account_id="ledger_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.retrieve(
            "id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_balance_monitors.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_balance_monitors.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_balance_monitors.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.update(
            id="id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_balance_monitors.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_balance_monitors.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_balance_monitors.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.list()
        assert_matches_type(AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.list(
            id=["string"],
            after_cursor="after_cursor",
            ledger_account_id="ledger_account_id",
            metadata={"foo": "string"},
            per_page=0,
        )
        assert_matches_type(AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_balance_monitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_balance_monitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(
                AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await async_client.ledger_account_balance_monitors.delete(
            "id",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_balance_monitors.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_balance_monitors.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_balance_monitors.with_raw_response.delete(
                "",
            )
