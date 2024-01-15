# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerAccount,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLedgerAccounts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
            currency_exponent=0,
            description="string",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="external_account",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.retrieve(
            "string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "as_of_lock_version": 0,
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.update(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.list()
        assert_matches_type(SyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.list(
            id=["string", "string", "string"],
            after_cursor="string",
            available_balance_amount={
                "gt": 0,
                "lt": 0,
                "gte": 0,
                "lte": 0,
                "eq": 0,
                "not_eq": 0,
            },
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="string",
            ledger_account_category_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            name="string",
            pending_balance_amount={
                "gt": 0,
                "lt": 0,
                "gte": 0,
                "lte": 0,
                "eq": 0,
                "not_eq": 0,
            },
            per_page=0,
            posted_balance_amount={
                "gt": 0,
                "lt": 0,
                "gte": 0,
                "lte": 0,
                "eq": 0,
                "not_eq": 0,
            },
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(SyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(SyncPage[LedgerAccount], ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.delete(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLedgerAccounts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
            currency_exponent=0,
            description="string",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="external_account",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_accounts.with_raw_response.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_accounts.with_streaming_response.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.retrieve(
            "string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "as_of_lock_version": 0,
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.update(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.list()
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.list(
            id=["string", "string", "string"],
            after_cursor="string",
            available_balance_amount={
                "gt": 0,
                "lt": 0,
                "gte": 0,
                "lte": 0,
                "eq": 0,
                "not_eq": 0,
            },
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="string",
            ledger_account_category_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            name="string",
            pending_balance_amount={
                "gt": 0,
                "lt": 0,
                "gte": 0,
                "lte": 0,
                "eq": 0,
                "not_eq": 0,
            },
            per_page=0,
            posted_balance_amount={
                "gt": 0,
                "lt": 0,
                "gte": 0,
                "lte": 0,
                "eq": 0,
                "not_eq": 0,
            },
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.delete(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_accounts.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_accounts.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True
