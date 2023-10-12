# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerAccountCategory
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLedgerAccountCategories:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
            currency_exponent=0,
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.retrieve(
            "string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.update(
            "string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.list()
        assert_matches_type(SyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.list(
            id=["string", "string", "string"],
            after_cursor="string",
            balances={"effective_at": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_account_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            name="string",
            parent_ledger_account_category_id="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.delete(
            "string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_add_ledger_account(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.add_ledger_account(
            "string",
            id="string",
        )
        assert ledger_account_category is None

    @parametrize
    def test_method_add_nested_category(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.add_nested_category(
            "string",
            id="string",
        )
        assert ledger_account_category is None

    @parametrize
    def test_method_remove_ledger_account(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.remove_ledger_account(
            "string",
            id="string",
        )
        assert ledger_account_category is None

    @parametrize
    def test_method_remove_nested_category(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.remove_nested_category(
            "string",
            id="string",
        )
        assert ledger_account_category is None


class TestAsyncLedgerAccountCategories:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
            currency_exponent=0,
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.retrieve(
            "string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.update(
            "string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.list()
        assert_matches_type(AsyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.list(
            id=["string", "string", "string"],
            after_cursor="string",
            balances={"effective_at": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_account_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            name="string",
            parent_ledger_account_category_id="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.delete(
            "string",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_add_ledger_account(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.add_ledger_account(
            "string",
            id="string",
        )
        assert ledger_account_category is None

    @parametrize
    async def test_method_add_nested_category(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.add_nested_category(
            "string",
            id="string",
        )
        assert ledger_account_category is None

    @parametrize
    async def test_method_remove_ledger_account(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.remove_ledger_account(
            "string",
            id="string",
        )
        assert ledger_account_category is None

    @parametrize
    async def test_method_remove_nested_category(self, client: AsyncModernTreasury) -> None:
        ledger_account_category = await client.ledger_account_categories.remove_nested_category(
            "string",
            id="string",
        )
        assert ledger_account_category is None
