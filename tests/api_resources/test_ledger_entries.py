# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerEntry
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgerEntries:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.list()
        assert_matches_type(SyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_entry = client.ledger_entries.list(
            id={"foo": "string"},
            after_cursor="string",
            as_of_lock_version=0,
            direction="credit",
            effective_at={"foo": "string"},
            effective_date={"foo": parse_date("2019-12-27")},
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_account_lock_version={"foo": 0},
            ledger_account_statement_id="string",
            ledger_transaction_id="string",
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


class TestAsyncLedgerEntries:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_entry = await client.ledger_entries.retrieve(
            "string",
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_entry = await client.ledger_entries.retrieve(
            "string",
            show_balances=True,
        )
        assert_matches_type(LedgerEntry, ledger_entry, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_entry = await client.ledger_entries.list()
        assert_matches_type(AsyncPage[LedgerEntry], ledger_entry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_entry = await client.ledger_entries.list(
            id={"foo": "string"},
            after_cursor="string",
            as_of_lock_version=0,
            direction="credit",
            effective_at={"foo": "string"},
            effective_date={"foo": parse_date("2019-12-27")},
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_account_lock_version={"foo": 0},
            ledger_account_statement_id="string",
            ledger_transaction_id="string",
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
