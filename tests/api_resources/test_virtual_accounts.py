# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    VirtualAccount,
)
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestVirtualAccounts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            account_details=[
                {
                    "account_number": "string",
                    "account_number_type": "clabe",
                },
                {
                    "account_number": "string",
                    "account_number_type": "clabe",
                },
                {
                    "account_number": "string",
                    "account_number_type": "clabe",
                },
            ],
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={"foo": "string"},
            routing_details=[
                {
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                },
                {
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                },
                {
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                },
            ],
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.virtual_accounts.with_raw_response.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.retrieve(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.virtual_accounts.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.update(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.update(
            "string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.virtual_accounts.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.list()
        assert_matches_type(SyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.list(
            after_cursor="string",
            counterparty_id="string",
            internal_account_id="string",
            metadata={"foo": "string"},
            per_page=0,
        )
        assert_matches_type(SyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.virtual_accounts.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(SyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.delete(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.virtual_accounts.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])


class TestAsyncVirtualAccounts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            account_details=[
                {
                    "account_number": "string",
                    "account_number_type": "clabe",
                },
                {
                    "account_number": "string",
                    "account_number_type": "clabe",
                },
                {
                    "account_number": "string",
                    "account_number_type": "clabe",
                },
            ],
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={"foo": "string"},
            routing_details=[
                {
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                },
                {
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                },
                {
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                },
            ],
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.virtual_accounts.with_raw_response.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.retrieve(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.virtual_accounts.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.update(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.update(
            "string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.virtual_accounts.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.list()
        assert_matches_type(AsyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.list(
            after_cursor="string",
            counterparty_id="string",
            internal_account_id="string",
            metadata={"foo": "string"},
            per_page=0,
        )
        assert_matches_type(AsyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.virtual_accounts.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(AsyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.delete(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncModernTreasury) -> None:
        response = await client.virtual_accounts.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_account = response.parse()
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])
