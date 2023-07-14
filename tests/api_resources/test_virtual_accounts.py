# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import VirtualAccount
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestVirtualAccounts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
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
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "account_number": "string",
                    "account_number_type": "clabe",
                    "account_number_safe": "string",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "account_number": "string",
                    "account_number_type": "clabe",
                    "account_number_safe": "string",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "account_number": "string",
                    "account_number_type": "clabe",
                    "account_number_safe": "string",
                },
            ],
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={"foo": "string"},
            routing_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                    "bank_name": "string",
                    "bank_address": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "object": "string",
                        "live_mode": True,
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                    "bank_name": "string",
                    "bank_address": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "object": "string",
                        "live_mode": True,
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                    "bank_name": "string",
                    "bank_address": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "object": "string",
                        "live_mode": True,
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                },
            ],
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.retrieve(
            "string",
        )
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
    def test_method_list(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.list()
        assert_matches_type(SyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.list(
            after_cursor="string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            per_page=0,
        )
        assert_matches_type(SyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        virtual_account = client.virtual_accounts.delete(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])


class TestAsyncVirtualAccounts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
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
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "account_number": "string",
                    "account_number_type": "clabe",
                    "account_number_safe": "string",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "account_number": "string",
                    "account_number_type": "clabe",
                    "account_number_safe": "string",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "account_number": "string",
                    "account_number_type": "clabe",
                    "account_number_safe": "string",
                },
            ],
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debit_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={"foo": "string"},
            routing_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                    "bank_name": "string",
                    "bank_address": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "object": "string",
                        "live_mode": True,
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                    "bank_name": "string",
                    "bank_address": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "object": "string",
                        "live_mode": True,
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "routing_number": "string",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                    "bank_name": "string",
                    "bank_address": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "object": "string",
                        "live_mode": True,
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                },
            ],
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.retrieve(
            "string",
        )
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
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.list()
        assert_matches_type(AsyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.list(
            after_cursor="string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            per_page=0,
        )
        assert_matches_type(AsyncPage[VirtualAccount], virtual_account, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        virtual_account = await client.virtual_accounts.delete(
            "string",
        )
        assert_matches_type(VirtualAccount, virtual_account, path=["response"])
