# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    ExpectedPayment,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExpectedPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_date": parse_date("2019-12-27"),
                "ledger_entries": [
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "lock_version": 0,
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "available_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "lock_version": 0,
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "available_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "lock_version": 0,
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "available_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                ],
                "external_id": "string",
                "ledgerable_type": "expected_payment",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            ledger_transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            line_items=[
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            reconciliation_rule_variables=[{"foo": "string"}, {"foo": "string"}, {"foo": "string"}],
            remittance_information="string",
            statement_descriptor="string",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.expected_payments.with_raw_response.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.expected_payments.with_streaming_response.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.retrieve(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.expected_payments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.expected_payments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.expected_payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.update(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.update(
            "string",
            amount_lower_bound=0,
            amount_upper_bound=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            reconciliation_rule_variables=[{"foo": "string"}, {"foo": "string"}, {"foo": "string"}],
            remittance_information="string",
            statement_descriptor="string",
            status="reconciled",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.expected_payments.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.expected_payments.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.expected_payments.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.list()
        assert_matches_type(SyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.list(
            after_cursor="string",
            counterparty_id="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="credit",
            internal_account_id="string",
            metadata={"foo": "string"},
            per_page=0,
            status="archived",
            type="ach",
        )
        assert_matches_type(SyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.expected_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(SyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.expected_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = response.parse()
            assert_matches_type(SyncPage[ExpectedPayment], expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.delete(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.expected_payments.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.expected_payments.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.expected_payments.with_raw_response.delete(
                "",
            )


class TestAsyncExpectedPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_date": parse_date("2019-12-27"),
                "ledger_entries": [
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "lock_version": 0,
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "available_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "lock_version": 0,
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "available_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    {
                        "amount": 0,
                        "direction": "credit",
                        "ledger_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "lock_version": 0,
                        "pending_balance_amount": {"foo": 0},
                        "posted_balance_amount": {"foo": 0},
                        "available_balance_amount": {"foo": 0},
                        "show_resulting_ledger_account_balances": True,
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                ],
                "external_id": "string",
                "ledgerable_type": "expected_payment",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            ledger_transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            line_items=[
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            reconciliation_rule_variables=[{"foo": "string"}, {"foo": "string"}, {"foo": "string"}],
            remittance_information="string",
            statement_descriptor="string",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.expected_payments.with_raw_response.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.expected_payments.with_streaming_response.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = await response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.retrieve(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.expected_payments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.expected_payments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = await response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.expected_payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.update(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.update(
            "string",
            amount_lower_bound=0,
            amount_upper_bound=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            reconciliation_rule_variables=[{"foo": "string"}, {"foo": "string"}, {"foo": "string"}],
            remittance_information="string",
            statement_descriptor="string",
            status="reconciled",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.expected_payments.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.expected_payments.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = await response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.expected_payments.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.list()
        assert_matches_type(AsyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.list(
            after_cursor="string",
            counterparty_id="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="credit",
            internal_account_id="string",
            metadata={"foo": "string"},
            per_page=0,
            status="archived",
            type="ach",
        )
        assert_matches_type(AsyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.expected_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(AsyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.expected_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = await response.parse()
            assert_matches_type(AsyncPage[ExpectedPayment], expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        expected_payment = await async_client.expected_payments.delete(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.expected_payments.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expected_payment = response.parse()
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.expected_payments.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expected_payment = await response.parse()
            assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.expected_payments.with_raw_response.delete(
                "",
            )
