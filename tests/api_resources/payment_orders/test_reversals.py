# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.payment_orders.reversal import Reversal

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestReversals:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.payment_orders.reversals.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="duplicate",
        )
        assert isinstance(resource, Reversal)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.payment_orders.reversals.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="duplicate",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_date": "2019-12-27",
                "ledger_entries": [
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
                "external_id": "string",
                "ledgerable_type": "counterparty",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert isinstance(resource, Reversal)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.payment_orders.reversals.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Reversal)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.payment_orders.reversals.list(
            "string",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.payment_orders.reversals.list(
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, SyncPage)


class TestAsyncReversals:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.payment_orders.reversals.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="duplicate",
        )
        assert isinstance(resource, Reversal)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.payment_orders.reversals.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="duplicate",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_date": "2019-12-27",
                "ledger_entries": [
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
                "external_id": "string",
                "ledgerable_type": "counterparty",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert isinstance(resource, Reversal)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.payment_orders.reversals.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Reversal)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.payment_orders.reversals.list(
            "string",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.payment_orders.reversals.list(
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, AsyncPage)
