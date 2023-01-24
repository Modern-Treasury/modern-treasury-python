# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerAccountCategory
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgerAccountCategories:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.create(
            name="string",
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            normal_balance="credit",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.create(
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            currency="string",
            currency_exponent=0,
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            normal_balance="credit",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.retrieve(
            "string",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.update(
            "string",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.update(
            "string",
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            name="string",
            ledger_id="string",
            parent_ledger_account_category_id="string",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.delete(
            "string",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    def test_method_add_ledger_account(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.add_ledger_account(
            "string",
            id="string",
        )
        assert resource is None

    @parametrize
    def test_method_add_nested_category(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.add_nested_category(
            "string",
            id="string",
        )
        assert resource is None

    @parametrize
    def test_method_remove_ledger_account(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.remove_ledger_account(
            "string",
            id="string",
        )
        assert resource is None

    @parametrize
    def test_method_remove_nested_category(self, client: ModernTreasury) -> None:
        resource = client.ledger_account_categories.remove_nested_category(
            "string",
            id="string",
        )
        assert resource is None


class TestAsyncLedgerAccountCategories:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.create(
            name="string",
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            normal_balance="credit",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.create(
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            currency="string",
            currency_exponent=0,
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            normal_balance="credit",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.retrieve(
            "string",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.update(
            "string",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.update(
            "string",
            name="string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.list(
            after_cursor="string",
            per_page=0,
            metadata={"foo": "string"},
            name="string",
            ledger_id="string",
            parent_ledger_account_category_id="string",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.delete(
            "string",
        )
        assert isinstance(resource, LedgerAccountCategory)

    @parametrize
    async def test_method_add_ledger_account(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.add_ledger_account(
            "string",
            id="string",
        )
        assert resource is None

    @parametrize
    async def test_method_add_nested_category(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.add_nested_category(
            "string",
            id="string",
        )
        assert resource is None

    @parametrize
    async def test_method_remove_ledger_account(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.remove_ledger_account(
            "string",
            id="string",
        )
        assert resource is None

    @parametrize
    async def test_method_remove_nested_category(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_account_categories.remove_nested_category(
            "string",
            id="string",
        )
        assert resource is None
