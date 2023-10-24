# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerAccountPayout
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLedgerAccountPayouts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account_payout = client.ledger_account_payouts.create(
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_payout = client.ledger_account_payouts.create(
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_either_direction=True,
            description="string",
            effective_at_upper_bound="14:15:22Z",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            skip_payout_ledger_transaction=True,
            status="pending",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_payout = client.ledger_account_payouts.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account_payout = client.ledger_account_payouts.update(
            "string",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_payout = client.ledger_account_payouts.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="posted",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account_payout = client.ledger_account_payouts.list()
        assert_matches_type(SyncPage[LedgerAccountPayout], ledger_account_payout, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_payout = client.ledger_account_payouts.list(
            id=["string", "string", "string"],
            after_cursor="string",
            metadata={"foo": "string"},
            payout_entry_direction="string",
            payout_ledger_account_id="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[LedgerAccountPayout], ledger_account_payout, path=["response"])

    @parametrize
    def test_method_retireve(self, client: ModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            ledger_account_payout = client.ledger_account_payouts.retireve(  # pyright: ignore[reportDeprecated]
                "string",
            )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])


class TestAsyncLedgerAccountPayouts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_account_payout = await client.ledger_account_payouts.create(
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_payout = await client.ledger_account_payouts.create(
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_either_direction=True,
            description="string",
            effective_at_upper_bound="14:15:22Z",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            skip_payout_ledger_transaction=True,
            status="pending",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account_payout = await client.ledger_account_payouts.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        ledger_account_payout = await client.ledger_account_payouts.update(
            "string",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_payout = await client.ledger_account_payouts.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="posted",
        )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_account_payout = await client.ledger_account_payouts.list()
        assert_matches_type(AsyncPage[LedgerAccountPayout], ledger_account_payout, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_payout = await client.ledger_account_payouts.list(
            id=["string", "string", "string"],
            after_cursor="string",
            metadata={"foo": "string"},
            payout_entry_direction="string",
            payout_ledger_account_id="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[LedgerAccountPayout], ledger_account_payout, path=["response"])

    @parametrize
    async def test_method_retireve(self, client: AsyncModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            ledger_account_payout = await client.ledger_account_payouts.retireve(  # pyright: ignore[reportDeprecated]
                "string",
            )
        assert_matches_type(LedgerAccountPayout, ledger_account_payout, path=["response"])
