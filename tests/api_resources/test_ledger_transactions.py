# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerTransaction,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "available_balance_amount": {"foo": 0},
                    "lock_version": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                }
            ],
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_date=parse_date("2019-12-27"),
            external_id="external_id",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="expected_payment",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_transactions.with_streaming_response.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.retrieve(
            "id",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_transactions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.update(
            id="id",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.update(
            id="id",
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "available_balance_amount": {"foo": 0},
                    "lock_version": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                }
            ],
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="expected_payment",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_transactions.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_transactions.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.list()
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.list(
            id=["string"],
            after_cursor="after_cursor",
            effective_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            effective_date={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            external_id="external_id",
            ledger_account_category_id="ledger_account_category_id",
            ledger_account_id="ledger_account_id",
            ledger_account_settlement_id="ledger_account_settlement_id",
            ledger_id="ledger_id",
            ledgerable_id="ledgerable_id",
            ledgerable_type="expected_payment",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            partially_posts_ledger_transaction_id="partially_posts_ledger_transaction_id",
            per_page=0,
            posted_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            reverses_ledger_transaction_id="reverses_ledger_transaction_id",
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = response.parse()
            assert_matches_type(SyncPage[LedgerTransaction], ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_partial_post(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_create_partial_post_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                }
            ],
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_create_partial_post(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_streaming_response_create_partial_post(self, client: ModernTreasury) -> None:
        with client.ledger_transactions.with_streaming_response.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_partial_post(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_transactions.with_raw_response.create_partial_post(
                id="",
                posted_ledger_entries=[
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
            )

    @parametrize
    def test_method_create_reversal(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create_reversal(
            id="id",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_method_create_reversal_with_all_params(self, client: ModernTreasury) -> None:
        ledger_transaction = client.ledger_transactions.create_reversal(
            id="id",
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_id="external_id",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="expected_payment",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_raw_response_create_reversal(self, client: ModernTreasury) -> None:
        response = client.ledger_transactions.with_raw_response.create_reversal(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    def test_streaming_response_create_reversal(self, client: ModernTreasury) -> None:
        with client.ledger_transactions.with_streaming_response.create_reversal(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_reversal(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_transactions.with_raw_response.create_reversal(
                id="",
            )


class TestAsyncLedgerTransactions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "available_balance_amount": {"foo": 0},
                    "lock_version": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                }
            ],
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_date=parse_date("2019-12-27"),
            external_id="external_id",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="expected_payment",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_transactions.with_raw_response.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_transactions.with_streaming_response.create(
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = await response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.retrieve(
            "id",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_transactions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_transactions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = await response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.update(
            id="id",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.update(
            id="id",
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "available_balance_amount": {"foo": 0},
                    "lock_version": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "pending_balance_amount": {"foo": 0},
                    "posted_balance_amount": {"foo": 0},
                    "show_resulting_ledger_account_balances": True,
                }
            ],
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="expected_payment",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_transactions.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_transactions.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = await response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_transactions.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.list()
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.list(
            id=["string"],
            after_cursor="after_cursor",
            effective_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            effective_date={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            external_id="external_id",
            ledger_account_category_id="ledger_account_category_id",
            ledger_account_id="ledger_account_id",
            ledger_account_settlement_id="ledger_account_settlement_id",
            ledger_id="ledger_id",
            ledgerable_id="ledgerable_id",
            ledgerable_type="expected_payment",
            metadata={"foo": "string"},
            order_by={
                "created_at": "asc",
                "effective_at": "asc",
            },
            partially_posts_ledger_transaction_id="partially_posts_ledger_transaction_id",
            per_page=0,
            posted_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            reverses_ledger_transaction_id="reverses_ledger_transaction_id",
            status="pending",
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = await response.parse()
            assert_matches_type(AsyncPage[LedgerTransaction], ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_partial_post(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_create_partial_post_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                }
            ],
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_create_partial_post(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_transactions.with_raw_response.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_create_partial_post(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_transactions.with_streaming_response.create_partial_post(
            id="id",
            posted_ledger_entries=[
                {
                    "amount": 0,
                    "direction": "credit",
                    "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = await response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_partial_post(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_transactions.with_raw_response.create_partial_post(
                id="",
                posted_ledger_entries=[
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
            )

    @parametrize
    async def test_method_create_reversal(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.create_reversal(
            id="id",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_method_create_reversal_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_transaction = await async_client.ledger_transactions.create_reversal(
            id="id",
            description="description",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_id="external_id",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="expected_payment",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            status="archived",
        )
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_raw_response_create_reversal(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_transactions.with_raw_response.create_reversal(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_transaction = response.parse()
        assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_create_reversal(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_transactions.with_streaming_response.create_reversal(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_transaction = await response.parse()
            assert_matches_type(LedgerTransaction, ledger_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_reversal(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_transactions.with_raw_response.create_reversal(
                id="",
            )
