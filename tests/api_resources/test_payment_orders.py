# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    PaymentOrder,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.shared import AsyncResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            accounting={
                "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            accounting_ledger_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            charge_bearer="shared",
            currency="AED",
            description="description",
            documents=[
                {
                    "documentable_id": "documentable_id",
                    "documentable_type": "cases",
                    "document_type": "document_type",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "documentable_id",
                    "documentable_type": "cases",
                    "document_type": "document_type",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "documentable_id",
                    "documentable_type": "cases",
                    "document_type": "document_type",
                    "file": b"raw file contents",
                },
            ],
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="foreign_exchange_contract",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "description",
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
                "external_id": "external_id",
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
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            nsf_protected=True,
            originating_party_name="originating_party_name",
            priority="high",
            process_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            purpose="purpose",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "line1",
                    "line2": "line2",
                    "locality": "locality",
                    "region": "region",
                    "postal_code": "postal_code",
                    "country": "country",
                },
                "name": "name",
                "account_details": [
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "party_name",
                "party_identifier": "party_identifier",
                "ledger_account": {
                    "name": "name",
                    "description": "description",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "currency",
                    "currency_exponent": 0,
                    "ledger_account_category_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "counterparty",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "plaid_processor_token",
                "contact_details": [
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="remittance_information",
            send_remittance_advice=True,
            statement_descriptor="statement_descriptor",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="ultimate_originating_party_identifier",
            ultimate_originating_party_name="ultimate_originating_party_name",
            ultimate_receiving_party_identifier="ultimate_receiving_party_identifier",
            ultimate_receiving_party_name="ultimate_receiving_party_name",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.payment_orders.with_raw_response.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.payment_orders.with_streaming_response.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = response.parse()
            assert_matches_type(PaymentOrder, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.retrieve(
            "id",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.payment_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.payment_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = response.parse()
            assert_matches_type(PaymentOrder, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.update(
            id="id",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.update(
            id="id",
            accounting={
                "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            accounting_ledger_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            charge_bearer="shared",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            description="description",
            direction="credit",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="foreign_exchange_contract",
            foreign_exchange_indicator="fixed_to_variable",
            line_items=[
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            nsf_protected=True,
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            originating_party_name="originating_party_name",
            priority="high",
            process_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            purpose="purpose",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "line1",
                    "line2": "line2",
                    "locality": "locality",
                    "region": "region",
                    "postal_code": "postal_code",
                    "country": "country",
                },
                "name": "name",
                "account_details": [
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "party_name",
                "party_identifier": "party_identifier",
                "ledger_account": {
                    "name": "name",
                    "description": "description",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "currency",
                    "currency_exponent": 0,
                    "ledger_account_category_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "counterparty",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "plaid_processor_token",
                "contact_details": [
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="remittance_information",
            send_remittance_advice=True,
            statement_descriptor="statement_descriptor",
            status="approved",
            subtype="0C",
            type="ach",
            ultimate_originating_party_identifier="ultimate_originating_party_identifier",
            ultimate_originating_party_name="ultimate_originating_party_name",
            ultimate_receiving_party_identifier="ultimate_receiving_party_identifier",
            ultimate_receiving_party_name="ultimate_receiving_party_name",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.payment_orders.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.payment_orders.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = response.parse()
            assert_matches_type(PaymentOrder, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_orders.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.list()
        assert_matches_type(SyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            created_at_end=parse_date("2019-12-27"),
            created_at_start=parse_date("2019-12-27"),
            direction="credit",
            effective_date_end=parse_date("2019-12-27"),
            effective_date_start=parse_date("2019-12-27"),
            metadata={"foo": "string"},
            originating_account_id="originating_account_id",
            per_page=0,
            priority="high",
            process_after_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            process_after_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            reference_number="reference_number",
            status="approved",
            transaction_id="transaction_id",
            type="ach",
        )
        assert_matches_type(SyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.payment_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(SyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.payment_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = response.parse()
            assert_matches_type(SyncPage[PaymentOrder], payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_async(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(AsyncResponse, payment_order, path=["response"])

    @parametrize
    def test_method_create_async_with_all_params(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            accounting={
                "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            accounting_ledger_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            charge_bearer="shared",
            currency="AED",
            description="description",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="foreign_exchange_contract",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "description",
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
                "external_id": "external_id",
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
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            nsf_protected=True,
            originating_party_name="originating_party_name",
            priority="high",
            process_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            purpose="purpose",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "line1",
                    "line2": "line2",
                    "locality": "locality",
                    "region": "region",
                    "postal_code": "postal_code",
                    "country": "country",
                },
                "name": "name",
                "account_details": [
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "party_name",
                "party_identifier": "party_identifier",
                "ledger_account": {
                    "name": "name",
                    "description": "description",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "currency",
                    "currency_exponent": 0,
                    "ledger_account_category_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "counterparty",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "plaid_processor_token",
                "contact_details": [
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="remittance_information",
            send_remittance_advice=True,
            statement_descriptor="statement_descriptor",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="ultimate_originating_party_identifier",
            ultimate_originating_party_name="ultimate_originating_party_name",
            ultimate_receiving_party_identifier="ultimate_receiving_party_identifier",
            ultimate_receiving_party_name="ultimate_receiving_party_name",
        )
        assert_matches_type(AsyncResponse, payment_order, path=["response"])

    @parametrize
    def test_raw_response_create_async(self, client: ModernTreasury) -> None:
        response = client.payment_orders.with_raw_response.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(AsyncResponse, payment_order, path=["response"])

    @parametrize
    def test_streaming_response_create_async(self, client: ModernTreasury) -> None:
        with client.payment_orders.with_streaming_response.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = response.parse()
            assert_matches_type(AsyncResponse, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            accounting={
                "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            accounting_ledger_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            charge_bearer="shared",
            currency="AED",
            description="description",
            documents=[
                {
                    "documentable_id": "documentable_id",
                    "documentable_type": "cases",
                    "document_type": "document_type",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "documentable_id",
                    "documentable_type": "cases",
                    "document_type": "document_type",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "documentable_id",
                    "documentable_type": "cases",
                    "document_type": "document_type",
                    "file": b"raw file contents",
                },
            ],
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="foreign_exchange_contract",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "description",
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
                "external_id": "external_id",
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
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            nsf_protected=True,
            originating_party_name="originating_party_name",
            priority="high",
            process_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            purpose="purpose",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "line1",
                    "line2": "line2",
                    "locality": "locality",
                    "region": "region",
                    "postal_code": "postal_code",
                    "country": "country",
                },
                "name": "name",
                "account_details": [
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "party_name",
                "party_identifier": "party_identifier",
                "ledger_account": {
                    "name": "name",
                    "description": "description",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "currency",
                    "currency_exponent": 0,
                    "ledger_account_category_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "counterparty",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "plaid_processor_token",
                "contact_details": [
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="remittance_information",
            send_remittance_advice=True,
            statement_descriptor="statement_descriptor",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="ultimate_originating_party_identifier",
            ultimate_originating_party_name="ultimate_originating_party_name",
            ultimate_receiving_party_identifier="ultimate_receiving_party_identifier",
            ultimate_receiving_party_name="ultimate_receiving_party_name",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.with_raw_response.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.with_streaming_response.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = await response.parse()
            assert_matches_type(PaymentOrder, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.retrieve(
            "id",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = await response.parse()
            assert_matches_type(PaymentOrder, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.update(
            id="id",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.update(
            id="id",
            accounting={
                "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            accounting_ledger_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            charge_bearer="shared",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            description="description",
            direction="credit",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="foreign_exchange_contract",
            foreign_exchange_indicator="fixed_to_variable",
            line_items=[
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            nsf_protected=True,
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            originating_party_name="originating_party_name",
            priority="high",
            process_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            purpose="purpose",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "line1",
                    "line2": "line2",
                    "locality": "locality",
                    "region": "region",
                    "postal_code": "postal_code",
                    "country": "country",
                },
                "name": "name",
                "account_details": [
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "party_name",
                "party_identifier": "party_identifier",
                "ledger_account": {
                    "name": "name",
                    "description": "description",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "currency",
                    "currency_exponent": 0,
                    "ledger_account_category_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "counterparty",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "plaid_processor_token",
                "contact_details": [
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="remittance_information",
            send_remittance_advice=True,
            statement_descriptor="statement_descriptor",
            status="approved",
            subtype="0C",
            type="ach",
            ultimate_originating_party_identifier="ultimate_originating_party_identifier",
            ultimate_originating_party_name="ultimate_originating_party_name",
            ultimate_receiving_party_identifier="ultimate_receiving_party_identifier",
            ultimate_receiving_party_name="ultimate_receiving_party_name",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = await response.parse()
            assert_matches_type(PaymentOrder, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_orders.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.list()
        assert_matches_type(AsyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            created_at_end=parse_date("2019-12-27"),
            created_at_start=parse_date("2019-12-27"),
            direction="credit",
            effective_date_end=parse_date("2019-12-27"),
            effective_date_start=parse_date("2019-12-27"),
            metadata={"foo": "string"},
            originating_account_id="originating_account_id",
            per_page=0,
            priority="high",
            process_after_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            process_after_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            reference_number="reference_number",
            status="approved",
            transaction_id="transaction_id",
            type="ach",
        )
        assert_matches_type(AsyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(AsyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = await response.parse()
            assert_matches_type(AsyncPage[PaymentOrder], payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_async(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(AsyncResponse, payment_order, path=["response"])

    @parametrize
    async def test_method_create_async_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_order = await async_client.payment_orders.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            accounting={
                "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            accounting_category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            accounting_ledger_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            charge_bearer="shared",
            currency="AED",
            description="description",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="foreign_exchange_contract",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "description",
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
                "external_id": "external_id",
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
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "description",
                    "accounting_category_id": "accounting_category_id",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            nsf_protected=True,
            originating_party_name="originating_party_name",
            priority="high",
            process_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            purpose="purpose",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "line1",
                    "line2": "line2",
                    "locality": "locality",
                    "region": "region",
                    "postal_code": "postal_code",
                    "country": "country",
                },
                "name": "name",
                "account_details": [
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                    {
                        "account_number": "account_number",
                        "account_number_type": "au_number",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "routing_number",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "party_name",
                "party_identifier": "party_identifier",
                "ledger_account": {
                    "name": "name",
                    "description": "description",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "currency",
                    "currency_exponent": 0,
                    "ledger_account_category_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "counterparty",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "plaid_processor_token",
                "contact_details": [
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "contact_identifier",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="remittance_information",
            send_remittance_advice=True,
            statement_descriptor="statement_descriptor",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="ultimate_originating_party_identifier",
            ultimate_originating_party_name="ultimate_originating_party_name",
            ultimate_receiving_party_identifier="ultimate_receiving_party_identifier",
            ultimate_receiving_party_name="ultimate_receiving_party_name",
        )
        assert_matches_type(AsyncResponse, payment_order, path=["response"])

    @parametrize
    async def test_raw_response_create_async(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_orders.with_raw_response.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_order = response.parse()
        assert_matches_type(AsyncResponse, payment_order, path=["response"])

    @parametrize
    async def test_streaming_response_create_async(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_orders.with_streaming_response.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_order = await response.parse()
            assert_matches_type(AsyncResponse, payment_order, path=["response"])

        assert cast(Any, response.is_closed) is True
