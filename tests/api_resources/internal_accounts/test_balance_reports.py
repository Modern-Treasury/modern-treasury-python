# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_date
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.internal_accounts import BalanceReport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestBalanceReports:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        balance_report = client.internal_accounts.balance_reports.retrieve(
            "string",
            internal_account_id="string",
        )
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.balance_reports.with_raw_response.retrieve(
            "string",
            internal_account_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        balance_report = client.internal_accounts.balance_reports.list(
            "string",
        )
        assert_matches_type(SyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        balance_report = client.internal_accounts.balance_reports.list(
            "string",
            after_cursor="string",
            as_of_date=parse_date("2019-12-27"),
            balance_report_type="intraday",
            per_page=0,
        )
        assert_matches_type(SyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.balance_reports.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(SyncPage[BalanceReport], balance_report, path=["response"])


class TestAsyncBalanceReports:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        balance_report = await client.internal_accounts.balance_reports.retrieve(
            "string",
            internal_account_id="string",
        )
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.balance_reports.with_raw_response.retrieve(
            "string",
            internal_account_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        balance_report = await client.internal_accounts.balance_reports.list(
            "string",
        )
        assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        balance_report = await client.internal_accounts.balance_reports.list(
            "string",
            after_cursor="string",
            as_of_date=parse_date("2019-12-27"),
            balance_report_type="intraday",
            per_page=0,
        )
        assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.balance_reports.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])
