# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.ledger_entry import LedgerEntry

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
        resource = client.ledger_entries.retrieve(
            "string",
        )
        assert isinstance(resource, LedgerEntry)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.ledger_entries.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_entries.list(
            after_cursor="string",
            per_page=0,
            ledger_account_id="string",
            ledger_transaction_id="string",
            effective_date={"foo": "2019-12-27"},
            effective_at={"foo": "string"},
            updated_at={"foo": "2019-12-27T18:11:19.117Z"},
            ledger_account_lock_version={"foo": 0},
            ledger_account_category_id="string",
            show_deleted=True,
            direction="credit",
            status="pending",
        )
        assert isinstance(resource, SyncPage)


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
        resource = await client.ledger_entries.retrieve(
            "string",
        )
        assert isinstance(resource, LedgerEntry)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_entries.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_entries.list(
            after_cursor="string",
            per_page=0,
            ledger_account_id="string",
            ledger_transaction_id="string",
            effective_date={"foo": "2019-12-27"},
            effective_at={"foo": "string"},
            updated_at={"foo": "2019-12-27T18:11:19.117Z"},
            ledger_account_lock_version={"foo": 0},
            ledger_account_category_id="string",
            show_deleted=True,
            direction="credit",
            status="pending",
        )
        assert isinstance(resource, AsyncPage)
