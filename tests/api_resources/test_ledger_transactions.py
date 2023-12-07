# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerTransaction,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLedgerTransactions:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create(
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
            ],
            description="string",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_date=parse_date("2019-12-27"),
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
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.create(
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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.retrieve(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
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
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.list()
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.list(
            id=["string", "string", "string"],
            after_cursor="string",
            effective_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            effective_date={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            external_id="string",
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_account_payout_id="string",
            ledger_id="string",
            ledgerable_id="string",
            ledgerable_type="counterparty",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            per_page=0,
            posted_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            reverses_ledger_transaction_id="string",
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    def test_method_create_reversal(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create_reversal(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_create_reversal_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create_reversal(
            "string",
            description="string",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
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
    def test_raw_response_create_reversal(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.create_reversal(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])


class TestAsyncLedgerTransactions:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.create(
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
            ],
            description="string",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_date=parse_date("2019-12-27"),
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
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_transactions.with_raw_response.create(
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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.retrieve(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_transactions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
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
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
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
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_transactions.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.list()
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.list(
            id=["string", "string", "string"],
            after_cursor="string",
            effective_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            effective_date={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            external_id="string",
            ledger_account_category_id="string",
            ledger_account_id="string",
            ledger_account_payout_id="string",
            ledger_id="string",
            ledgerable_id="string",
            ledgerable_type="counterparty",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            per_page=0,
            posted_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            reverses_ledger_transaction_id="string",
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_transactions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    async def test_method_create_reversal(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.create_reversal(
            "string",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_create_reversal_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_transaction = await client.ledger_transactions.create_reversal(
            "string",
            description="string",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
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
    async def test_raw_response_create_reversal(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_transactions.with_raw_response.create_reversal(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])
