# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Transaction
from modern_treasury._utils import parse_date
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
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
    def test_method_create(self, client: ModernTreasury) -> None:
        transaction = client.transactions.create(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            direction="string",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vendor_code="string",
            vendor_code_type="string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        transaction = client.transactions.create(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            direction="string",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vendor_code="string",
            vendor_code_type="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            posted=True,
            vendor_description="string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.transactions.with_raw_response.create(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            direction="string",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vendor_code="string",
            vendor_code_type="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        transaction = client.transactions.retrieve(
            "string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.transactions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
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
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.transactions.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
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

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.transactions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(SyncPage[Transaction], transaction, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        transaction = client.transactions.delete(
            "string",
        )
        assert transaction is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.transactions.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None


class TestAsyncTransactions:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.create(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            direction="string",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vendor_code="string",
            vendor_code_type="string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.create(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            direction="string",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vendor_code="string",
            vendor_code_type="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            posted=True,
            vendor_description="string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.transactions.with_raw_response.create(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            direction="string",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vendor_code="string",
            vendor_code_type="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.retrieve(
            "string",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.transactions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
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
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.transactions.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
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

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.transactions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(AsyncPage[Transaction], transaction, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        transaction = await client.transactions.delete(
            "string",
        )
        assert transaction is None

    @parametrize
    async def test_raw_response_delete(self, client: AsyncModernTreasury) -> None:
        response = await client.transactions.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None
