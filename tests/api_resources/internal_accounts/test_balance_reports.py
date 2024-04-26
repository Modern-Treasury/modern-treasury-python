# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.internal_accounts import (
    BalanceReport,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalanceReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        balance_report = client.internal_accounts.balance_reports.create(
            "string",
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
    def test_path_params_create(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            client.internal_accounts.balance_reports.with_raw_response.create(
                "",
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
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            client.internal_accounts.balance_reports.with_raw_response.retrieve(
                "string",
                internal_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.internal_accounts.balance_reports.with_raw_response.retrieve(
                "",
                internal_account_id="string",
            )

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
    def test_path_params_list(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            client.internal_accounts.balance_reports.with_raw_response.list(
                "",
            )

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

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            client.internal_accounts.balance_reports.with_raw_response.delete(
                "string",
                internal_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.internal_accounts.balance_reports.with_raw_response.delete(
                "",
                internal_account_id="string",
            )


class TestAsyncBalanceReports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        balance_report = await async_client.internal_accounts.balance_reports.create(
            "string",
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
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.balance_reports.with_raw_response.create(
            "string",
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
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.balance_reports.with_streaming_response.create(
            "string",
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
    async def test_path_params_create(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            await async_client.internal_accounts.balance_reports.with_raw_response.create(
                "",
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

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        balance_report = await async_client.internal_accounts.balance_reports.retrieve(
            "string",
            internal_account_id="string",
        )
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.balance_reports.with_raw_response.retrieve(
            "string",
            internal_account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(BalanceReport, balance_report, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.balance_reports.with_streaming_response.retrieve(
            "string",
            internal_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = await response.parse()
            assert_matches_type(BalanceReport, balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            await async_client.internal_accounts.balance_reports.with_raw_response.retrieve(
                "string",
                internal_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.internal_accounts.balance_reports.with_raw_response.retrieve(
                "",
                internal_account_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        balance_report = await async_client.internal_accounts.balance_reports.list(
            "string",
        )
        assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        balance_report = await async_client.internal_accounts.balance_reports.list(
            "string",
            after_cursor="string",
            as_of_date=parse_date("2019-12-27"),
            balance_report_type="intraday",
            per_page=0,
        )
        assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.balance_reports.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.balance_reports.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = await response.parse()
            assert_matches_type(AsyncPage[BalanceReport], balance_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            await async_client.internal_accounts.balance_reports.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        balance_report = await async_client.internal_accounts.balance_reports.delete(
            "string",
            internal_account_id="string",
        )
        assert balance_report is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.balance_reports.with_raw_response.delete(
            "string",
            internal_account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_report = response.parse()
        assert balance_report is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.balance_reports.with_streaming_response.delete(
            "string",
            internal_account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_report = await response.parse()
            assert balance_report is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            await async_client.internal_accounts.balance_reports.with_raw_response.delete(
                "string",
                internal_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.internal_accounts.balance_reports.with_raw_response.delete(
                "",
                internal_account_id="string",
            )
