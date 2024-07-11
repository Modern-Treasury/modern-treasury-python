# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.ledger_transactions import LedgerTransactionVersion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.list()
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.list(
            after_cursor="after_cursor",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_account_statement_id="ledger_account_statement_id",
            ledger_transaction_id="ledger_transaction_id",
            per_page=0,
            version={"foo": 0},
        )
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.versions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_transactions.versions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        version = await async_client.ledger_transactions.versions.list()
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        version = await async_client.ledger_transactions.versions.list(
            after_cursor="after_cursor",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_account_statement_id="ledger_account_statement_id",
            ledger_transaction_id="ledger_transaction_id",
            per_page=0,
            version={"foo": 0},
        )
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_transactions.versions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_transactions.versions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

        assert cast(Any, response.is_closed) is True
