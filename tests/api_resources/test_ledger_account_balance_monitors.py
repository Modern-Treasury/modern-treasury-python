# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerAccountBalanceMonitor
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgerAccountBalanceMonitors:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
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
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

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
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_account_balance_monitor = client.ledger_account_balance_monitors.delete(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])


class TestAsyncLedgerAccountBalanceMonitors:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
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
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])

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
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        ledger_account_balance_monitor = await client.ledger_account_balance_monitors.delete(
            "string",
        )
        assert_matches_type(LedgerAccountBalanceMonitor, ledger_account_balance_monitor, path=["response"])