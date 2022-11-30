# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.ledger_transaction import LedgerTransaction

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgerTransactions:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.create(
            effective_date="2019-12-27",
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.create(
            description="string",
            status="archived",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            effective_date="2019-12-27",
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
            ],
            external_id="string",
            ledgerable_type="counterparty",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.retrieve(
            "string",
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.update(
            "string",
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.update(
            "string",
            description="string",
            status="archived",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
            ],
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            ledger_id="string",
            ledger_account_id="string",
            effective_at={"foo": "string"},
            effective_date={"foo": "2019-12-27T18:11:19.117Z"},
            posted_at={"foo": "2019-12-27T18:11:19.117Z"},
            updated_at={"foo": "2019-12-27T18:11:19.117Z"},
            status="pending",
            external_id="string",
            ledger_account_category_id="string",
        )
        assert isinstance(resource, SyncPage)


class TestAsyncLedgerTransactions:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.create(
            effective_date="2019-12-27",
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.create(
            description="string",
            status="archived",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            effective_date="2019-12-27",
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
            ],
            external_id="string",
            ledgerable_type="counterparty",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.retrieve(
            "string",
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.update(
            "string",
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.update(
            "string",
            description="string",
            status="archived",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                },
            ],
        )
        assert isinstance(resource, LedgerTransaction)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            ledger_id="string",
            ledger_account_id="string",
            effective_at={"foo": "string"},
            effective_date={"foo": "2019-12-27T18:11:19.117Z"},
            posted_at={"foo": "2019-12-27T18:11:19.117Z"},
            updated_at={"foo": "2019-12-27T18:11:19.117Z"},
            status="pending",
            external_id="string",
            ledger_account_category_id="string",
        )
        assert isinstance(resource, AsyncPage)
