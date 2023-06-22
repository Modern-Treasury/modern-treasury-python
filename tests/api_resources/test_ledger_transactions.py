# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerTransaction
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

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
        ledger_transaction = client.ledger_transactions.create(
            effective_date=parse_date("2019-12-27"),
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
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create(
            effective_date=parse_date("2019-12-27"),
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
            ],
            description="string",
            external_id="string",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="counterparty",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.retrieve(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.update(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.update(
            "string",
            description="string",
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.list()
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.list(
            after_cursor="string",
            effective_at={"foo": "string"},
            effective_date={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            external_id="string",
            id={"foo": "string"},
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            per_page=0,
            posted_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])


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
        ledger_transaction = await client.ledger_transactions.create(
            effective_date=parse_date("2019-12-27"),
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
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.create(
            effective_date=parse_date("2019-12-27"),
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
            ],
            description="string",
            external_id="string",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="counterparty",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.retrieve(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.update(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.update(
            "string",
            description="string",
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "lock_version": 0,
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "available_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.list()
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.list(
            after_cursor="string",
            effective_at={"foo": "string"},
            effective_date={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            external_id="string",
            id={"foo": "string"},
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            per_page=0,
            posted_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])
