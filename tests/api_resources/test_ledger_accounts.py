# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
            currency_exponent=0,
            description="description",
            ledger_account_category_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="counterparty",
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
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
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
            id="id",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.retrieve(
            id="id",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "as_of_lock_version": 0,
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_accounts.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.update(
            id="id",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_accounts.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.list()
        assert_matches_type(SyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.list(
            id=["string"],
            after_cursor="after_cursor",
            available_balance_amount={
                "eq": 0,
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
                "not_eq": 0,
            },
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="currency",
            ledger_account_category_id="ledger_account_category_id",
            ledger_id="ledger_id",
            metadata={"foo": "string"},
            name=["string"],
            pending_balance_amount={
                "eq": 0,
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
                "not_eq": 0,
            },
            per_page=0,
            posted_balance_amount={
                "eq": 0,
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
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
            "id",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.ledger_accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.ledger_accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_accounts.with_raw_response.delete(
                "",
            )


class TestAsyncLedgerAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
            currency_exponent=0,
            description="description",
            ledger_account_category_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="counterparty",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_accounts.with_raw_response.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_accounts.with_streaming_response.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.retrieve(
            id="id",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.retrieve(
            id="id",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "as_of_lock_version": 0,
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_accounts.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_accounts.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_accounts.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.update(
            id="id",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_accounts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_accounts.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.list()
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.list(
            id=["string"],
            after_cursor="after_cursor",
            available_balance_amount={
                "eq": 0,
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
                "not_eq": 0,
            },
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="currency",
            ledger_account_category_id="ledger_account_category_id",
            ledger_id="ledger_id",
            metadata={"foo": "string"},
            name=["string"],
            pending_balance_amount={
                "eq": 0,
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
                "not_eq": 0,
            },
            per_page=0,
            posted_balance_amount={
                "eq": 0,
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
                "not_eq": 0,
            },
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        ledger_account = await async_client.ledger_accounts.delete(
            "id",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccount, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_accounts.with_raw_response.delete(
                "",
            )
