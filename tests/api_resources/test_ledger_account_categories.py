# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerAccountCategory,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerAccountCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
            currency_exponent=0,
            description="description",
            ledger_account_category_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.retrieve(
            id="id",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.retrieve(
            id="id",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_categories.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.update(
            id="id",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_categories.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.list()
        assert_matches_type(SyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.list(
            id=["string"],
            after_cursor="after_cursor",
            balances={"effective_at": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="currency",
            ledger_account_id="ledger_account_id",
            ledger_id="ledger_id",
            metadata={"foo": "string"},
            name="name",
            parent_ledger_account_category_id="parent_ledger_account_category_id",
            per_page=0,
        )
        assert_matches_type(SyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(SyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert_matches_type(SyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.delete(
            "id",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_categories.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_add_ledger_account(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.add_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    def test_raw_response_add_ledger_account(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.add_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    def test_streaming_response_add_ledger_account(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.add_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_ledger_account(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_categories.with_raw_response.add_ledger_account(
                ledger_account_id="ledger_account_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ledger_account_id` but received ''"):
            client.ledger_account_categories.with_raw_response.add_ledger_account(
                ledger_account_id="",
                id="id",
            )

    @parametrize
    def test_method_add_nested_category(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.add_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    def test_raw_response_add_nested_category(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.add_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    def test_streaming_response_add_nested_category(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.add_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_nested_category(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_categories.with_raw_response.add_nested_category(
                sub_category_id="sub_category_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_category_id` but received ''"):
            client.ledger_account_categories.with_raw_response.add_nested_category(
                sub_category_id="",
                id="id",
            )

    @parametrize
    def test_method_remove_ledger_account(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.remove_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    def test_raw_response_remove_ledger_account(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.remove_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    def test_streaming_response_remove_ledger_account(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.remove_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_ledger_account(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_categories.with_raw_response.remove_ledger_account(
                ledger_account_id="ledger_account_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ledger_account_id` but received ''"):
            client.ledger_account_categories.with_raw_response.remove_ledger_account(
                ledger_account_id="",
                id="id",
            )

    @parametrize
    def test_method_remove_nested_category(self, client: ModernTreasury) -> None:
        ledger_account_category = client.ledger_account_categories.remove_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    def test_raw_response_remove_nested_category(self, client: ModernTreasury) -> None:
        response = client.ledger_account_categories.with_raw_response.remove_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    def test_streaming_response_remove_nested_category(self, client: ModernTreasury) -> None:
        with client.ledger_account_categories.with_streaming_response.remove_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_nested_category(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_categories.with_raw_response.remove_nested_category(
                sub_category_id="sub_category_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_category_id` but received ''"):
            client.ledger_account_categories.with_raw_response.remove_nested_category(
                sub_category_id="",
                id="id",
            )


class TestAsyncLedgerAccountCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
            currency_exponent=0,
            description="description",
            ledger_account_category_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.create(
            currency="currency",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            normal_balance="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.retrieve(
            id="id",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.retrieve(
            id="id",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.update(
            id="id",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.list()
        assert_matches_type(AsyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.list(
            id=["string"],
            after_cursor="after_cursor",
            balances={"effective_at": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="currency",
            ledger_account_id="ledger_account_id",
            ledger_id="ledger_id",
            metadata={"foo": "string"},
            name="name",
            parent_ledger_account_category_id="parent_ledger_account_category_id",
            per_page=0,
        )
        assert_matches_type(AsyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(AsyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert_matches_type(AsyncPage[LedgerAccountCategory], ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.delete(
            "id",
        )
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert_matches_type(LedgerAccountCategory, ledger_account_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_add_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.add_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    async def test_raw_response_add_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.add_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    async def test_streaming_response_add_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.add_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.add_ledger_account(
                ledger_account_id="ledger_account_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ledger_account_id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.add_ledger_account(
                ledger_account_id="",
                id="id",
            )

    @parametrize
    async def test_method_add_nested_category(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.add_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    async def test_raw_response_add_nested_category(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.add_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    async def test_streaming_response_add_nested_category(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.add_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_nested_category(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.add_nested_category(
                sub_category_id="sub_category_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_category_id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.add_nested_category(
                sub_category_id="",
                id="id",
            )

    @parametrize
    async def test_method_remove_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.remove_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    async def test_raw_response_remove_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.remove_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    async def test_streaming_response_remove_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.remove_ledger_account(
            ledger_account_id="ledger_account_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_ledger_account(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.remove_ledger_account(
                ledger_account_id="ledger_account_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ledger_account_id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.remove_ledger_account(
                ledger_account_id="",
                id="id",
            )

    @parametrize
    async def test_method_remove_nested_category(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_category = await async_client.ledger_account_categories.remove_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )
        assert ledger_account_category is None

    @parametrize
    async def test_raw_response_remove_nested_category(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_categories.with_raw_response.remove_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_category = response.parse()
        assert ledger_account_category is None

    @parametrize
    async def test_streaming_response_remove_nested_category(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_categories.with_streaming_response.remove_nested_category(
            sub_category_id="sub_category_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_category = await response.parse()
            assert ledger_account_category is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_nested_category(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.remove_nested_category(
                sub_category_id="sub_category_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_category_id` but received ''"):
            await async_client.ledger_account_categories.with_raw_response.remove_nested_category(
                sub_category_id="",
                id="id",
            )
