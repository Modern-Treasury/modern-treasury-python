# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerAccountBalanceMonitor,
)
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLedgerAccountBalanceMonitors:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
            description="string",
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
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.create(
            alert_condition={
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_account_balance_monitors.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.update(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.update(
            "string",
            description="string",
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
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.list()
        assert_matches_type(SyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.list(
            id=["string", "string", "string"],
            after_cursor="string",
            ledger_account_id="string",
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
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.ledger_account_balance_monitors.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.ledger_account_balance_monitors.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLedgerAccountBalanceMonitors:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.create(
            alert_condition={
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_account_balance_monitors.with_raw_response.create(
            alert_condition={
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_account_balance_monitors.with_streaming_response.create(
            alert_condition={
                "field": "string",
                "operator": "string",
                "value": 0,
            },
            ledger_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_account_balance_monitors.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_account_balance_monitors.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.update(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_account_balance_monitors.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_account_balance_monitors.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.list()
        assert_matches_type(AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.list(
            id=["string", "string", "string"],
            after_cursor="string",
            ledger_account_id="string",
            metadata={"foo": "string"},
            per_page=0,
        )
        assert_matches_type(AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_account_balance_monitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_account_balance_monitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(
                AsyncPage[LedgerAccountBalanceMonitor], ledger_account_balance_monitor, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.delete(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_account_balance_monitors.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_balance_monitor = response.parse()
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_account_balance_monitors.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_balance_monitor = await response.parse()
            assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

        assert cast(Any, response.is_closed) is True
