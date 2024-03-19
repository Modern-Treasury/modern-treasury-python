# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerEntry,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.retrieve(
            "string",
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.retrieve(
            "string",
            show_balances=True,
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_entries.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_entries.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = response.parse()
            assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_entries.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.update(
            "string",
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.update(
            "string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_entries.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_entries.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = response.parse()
            assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_entries.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.list()
        assert_matches_type(SyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.list(
            id=["string", "string", "string"],
            after_cursor="string",
            as_of_lock_version=0,
            direction="credit",
            effective_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            effective_date={"foo": parse_date("2019-12-27")},
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_account_lock_version={"foo": 0},
            ledger_account_payout_id="string",
            ledger_account_settlement_id="string",
            ledger_account_statement_id="string",
            ledger_transaction_id="string",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            per_page=0,
            show_balances=True,
            show_deleted=True,
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_entries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(SyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_entries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = response.parse()
            assert_matches_type(SyncPage[LedgerEntry], ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLedgerEntries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_entry = await async_client.ledger_entries.retrieve(
            "string",
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_entry = await async_client.ledger_entries.retrieve(
            "string",
            show_balances=True,
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_entries.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_entries.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = await response.parse()
            assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_entries.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        ledger_entry = await async_client.ledger_entries.update(
            "string",
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_entry = await async_client.ledger_entries.update(
            "string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_entries.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_entries.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = await response.parse()
            assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_entries.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        ledger_entry = await async_client.ledger_entries.list()
        assert_matches_type(AsyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_entry = await async_client.ledger_entries.list(
            id=["string", "string", "string"],
            after_cursor="string",
            as_of_lock_version=0,
            direction="credit",
            effective_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            effective_date={"foo": parse_date("2019-12-27")},
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_account_lock_version={"foo": 0},
            ledger_account_payout_id="string",
            ledger_account_settlement_id="string",
            ledger_account_statement_id="string",
            ledger_transaction_id="string",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            per_page=0,
            show_balances=True,
            show_deleted=True,
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_entries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(AsyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_entries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = await response.parse()
            assert_matches_type(AsyncPage[LedgerEntry], ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True
