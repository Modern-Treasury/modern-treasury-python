# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Transaction
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestTransactions:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        transaction = client.transactions.retrieve(
            "string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        transaction = client.transactions.update(
            "string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        transaction = client.transactions.update(
            "string",
            metadata={"foo": "string"},
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        transaction = client.transactions.list()
        assert_matches_type(SyncPage[Transaction], transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        transaction = client.transactions.list(
            after_cursor="string",
            as_of_date_end=parse_date("2019-12-27"),
            as_of_date_start=parse_date("2019-12-27"),
            counterparty_id="string",
            description="string",
            direction="string",
            internal_account_id="string",
            metadata={"foo": "string"},
            payment_type="string",
            per_page=0,
            posted=True,
            transactable_type="string",
            vendor_id="string",
            virtual_account_id="string",
        )
        assert_matches_type(SyncPage[Transaction], transaction, path=["response"])


class TestAsyncTransactions:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.retrieve(
            "string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.update(
            "string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.update(
            "string",
            metadata={"foo": "string"},
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.list()
        assert_matches_type(AsyncPage[Transaction], transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.list(
            after_cursor="string",
            as_of_date_end=parse_date("2019-12-27"),
            as_of_date_start=parse_date("2019-12-27"),
            counterparty_id="string",
            description="string",
            direction="string",
            internal_account_id="string",
            metadata={"foo": "string"},
            payment_type="string",
            per_page=0,
            posted=True,
            transactable_type="string",
            vendor_id="string",
            virtual_account_id="string",
        )
        assert_matches_type(AsyncPage[Transaction], transaction, path=["response"])
