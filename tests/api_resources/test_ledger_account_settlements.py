# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerAccountSettlement,
)
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerAccountSettlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account_settlement = client.ledger_account_settlements.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_settlement = client.ledger_account_settlements.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_either_direction=True,
            description="description",
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            skip_settlement_ledger_transaction=True,
            status="pending",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_account_settlements.with_raw_response.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_account_settlements.with_streaming_response.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = response.parse()
            assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_settlement = client.ledger_account_settlements.retrieve(
            "id",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_account_settlements.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_account_settlements.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = response.parse()
            assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_settlements.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account_settlement = client.ledger_account_settlements.update(
            id="id",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_settlement = client.ledger_account_settlements.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="posted",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_account_settlements.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_account_settlements.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = response.parse()
            assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_settlements.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account_settlement = client.ledger_account_settlements.list()
        assert_matches_type(SyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_settlement = client.ledger_account_settlements.list(
            id=["string"],
            after_cursor="after_cursor",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_id="ledger_id",
            ledger_transaction_id="ledger_transaction_id",
            metadata={"foo": "string"},
            per_page=0,
            settled_ledger_account_id="settled_ledger_account_id",
            settlement_entry_direction="settlement_entry_direction",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_account_settlements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(SyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_account_settlements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = response.parse()
            assert_matches_type(SyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLedgerAccountSettlements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_settlement = await async_client.ledger_account_settlements.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_settlement = await async_client.ledger_account_settlements.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_either_direction=True,
            description="description",
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            skip_settlement_ledger_transaction=True,
            status="pending",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_settlements.with_raw_response.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_settlements.with_streaming_response.create(
            contra_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            settled_ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = await response.parse()
            assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_settlement = await async_client.ledger_account_settlements.retrieve(
            "id",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_settlements.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_settlements.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = await response.parse()
            assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_settlements.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_settlement = await async_client.ledger_account_settlements.update(
            id="id",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_settlement = await async_client.ledger_account_settlements.update(
            id="id",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="posted",
        )
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_settlements.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_settlements.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = await response.parse()
            assert_matches_type(LedgerAccountSettlement, ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_settlements.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_settlement = await async_client.ledger_account_settlements.list()
        assert_matches_type(AsyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_settlement = await async_client.ledger_account_settlements.list(
            id=["string"],
            after_cursor="after_cursor",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_id="ledger_id",
            ledger_transaction_id="ledger_transaction_id",
            metadata={"foo": "string"},
            per_page=0,
            settled_ledger_account_id="settled_ledger_account_id",
            settlement_entry_direction="settlement_entry_direction",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_settlements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_settlement = response.parse()
        assert_matches_type(AsyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_settlements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_settlement = await response.parse()
            assert_matches_type(AsyncPage[LedgerAccountSettlement], ledger_account_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True
