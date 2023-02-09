# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerAccountPayout
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgerAccountPayouts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_payouts.create(
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_payouts.create(
            description="string",
            status="pending",
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_at_upper_bound="14:15:22Z",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_payouts.update(
            "string",
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_payouts.update(
            "string",
            description="string",
            status="posted",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_payouts.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_payouts.list(
            after_cursor="string",
            per_page=0,
            payout_ledger_account_id="string",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_retireve(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_payouts.retireve(
            "string",
        )
        assert isinstance(resource, LedgerAccountPayout)


class TestAsyncLedgerAccountPayouts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_payouts.create(
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_payouts.create(
            description="string",
            status="pending",
            payout_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            funding_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_at_upper_bound="14:15:22Z",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_payouts.update(
            "string",
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_payouts.update(
            "string",
            description="string",
            status="posted",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, LedgerAccountPayout)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_payouts.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_payouts.list(
            after_cursor="string",
            per_page=0,
            payout_ledger_account_id="string",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_retireve(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_payouts.retireve(
            "string",
        )
        assert isinstance(resource, LedgerAccountPayout)
