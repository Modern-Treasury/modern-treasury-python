# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_date
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.internal_accounts import (
    BalanceReport,
)

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
    def test_method_create(self, client: ModernTreasury) -> None:
        balance_report = client.internal_accounts.balance_reports.create(
            "string",
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            as_of_time="string",
            balance_report_type="intraday",
            balances=[
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
            ],
        )
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.balance_reports.with_raw_response.create(
            "string",
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            as_of_time="string",
            balance_report_type="intraday",
            balances=[
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.internal_accounts.balance_reports.with_streaming_response.create(
            "string",
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            as_of_time="string",
            balance_report_type="intraday",
            balances=[
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = response.parse()
            assert_matches_type(BalanceReport, balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.internal_accounts.balance_reports.with_streaming_response.retrieve(
            "string",
            internal_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = response.parse()
            assert_matches_type(BalanceReport, balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(SyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.internal_accounts.balance_reports.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = response.parse()
            assert_matches_type(SyncPage[BalanceReport], balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        balance_report = client.internal_accounts.balance_reports.delete(
            "string",
            internal_account_id="string",
        )
        assert balance_report is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.balance_reports.with_raw_response.delete(
            "string",
            internal_account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert balance_report is None

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.internal_accounts.balance_reports.with_streaming_response.delete(
            "string",
            internal_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = response.parse()
            assert balance_report is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBalanceReports:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        balance_report = await client.internal_accounts.balance_reports.create(
            "string",
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            as_of_time="string",
            balance_report_type="intraday",
            balances=[
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
            ],
        )
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.balance_reports.with_raw_response.create(
            "string",
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            as_of_time="string",
            balance_report_type="intraday",
            balances=[
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.balance_reports.with_streaming_response.create(
            "string",
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            as_of_time="string",
            balance_report_type="intraday",
            balances=[
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
                {
                    "amount": 0,
                    "balance_type": "closing_available",
                    "vendor_code": "string",
                    "vendor_code_type": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = await response.parse()
            assert_matches_type(BalanceReport, balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.balance_reports.with_streaming_response.retrieve(
            "string",
            internal_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = await response.parse()
            assert_matches_type(BalanceReport, balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.balance_reports.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = await response.parse()
            assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        balance_report = await client.internal_accounts.balance_reports.delete(
            "string",
            internal_account_id="string",
        )
        assert balance_report is None

    @parametrize
    async def test_raw_response_delete(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.balance_reports.with_raw_response.delete(
            "string",
            internal_account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert balance_report is None

    @parametrize
    async def test_streaming_response_delete(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.balance_reports.with_streaming_response.delete(
            "string",
            internal_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = await response.parse()
            assert balance_report is None

        assert cast(Any, response.is_closed) is True
