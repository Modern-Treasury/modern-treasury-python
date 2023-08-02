# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import PaymentOrder, shared
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestPaymentOrders:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
            description="string",
            documents=[
                {
                    "documentable_id": "string",
                    "documentable_type": "cases",
                    "document_type": "string",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "string",
                    "documentable_type": "cases",
                    "document_type": "string",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "string",
                    "documentable_type": "cases",
                    "document_type": "string",
                    "file": b"raw file contents",
                },
            ],
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="string",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_at": parse_date("2019-12-27"),
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
                "ledgerable_type": "counterparty",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
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
            nsf_protected=True,
            originating_party_name="string",
            priority="high",
            purpose="string",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "string",
                    "line2": "string",
                    "locality": "string",
                    "region": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "name": "string",
                "account_details": [
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "string",
                "party_identifier": "string",
                "ledger_account": {
                    "name": "string",
                    "description": "string",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "string",
                    "currency_exponent": 0,
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "external_account",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "string",
                "contact_details": [
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
            send_remittance_advice=True,
            statement_descriptor="string",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="string",
            ultimate_originating_party_name="string",
            ultimate_receiving_party_identifier="string",
            ultimate_receiving_party_name="string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.retrieve(
            "string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.update(
            "string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.update(
            "string",
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
            description="string",
            direction="credit",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="string",
            foreign_exchange_indicator="fixed_to_variable",
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
            nsf_protected=True,
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            originating_party_name="string",
            priority="high",
            purpose="string",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "string",
                    "line2": "string",
                    "locality": "string",
                    "region": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "name": "string",
                "account_details": [
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "string",
                "party_identifier": "string",
                "ledger_account": {
                    "name": "string",
                    "description": "string",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "string",
                    "currency_exponent": 0,
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "external_account",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "string",
                "contact_details": [
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
            send_remittance_advice=True,
            statement_descriptor="string",
            status="approved",
            subtype="0C",
            type="ach",
            ultimate_originating_party_identifier="string",
            ultimate_originating_party_name="string",
            ultimate_receiving_party_identifier="string",
            ultimate_receiving_party_name="string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.list()
        assert_matches_type(SyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.list(
            after_cursor="string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="credit",
            effective_date_end=parse_date("2019-12-27"),
            effective_date_start=parse_date("2019-12-27"),
            metadata={"foo": "string"},
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            per_page=0,
            priority="high",
            reference_number="string",
            status="approved",
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(SyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    def test_method_create_async(self, client: ModernTreasury) -> None:
        payment_order = client.payment_orders.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(shared.AsyncResponse, payment_order, path=["response"])

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
            description="string",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="string",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_at": parse_date("2019-12-27"),
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
                "ledgerable_type": "counterparty",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
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
            nsf_protected=True,
            originating_party_name="string",
            priority="high",
            purpose="string",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "string",
                    "line2": "string",
                    "locality": "string",
                    "region": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "name": "string",
                "account_details": [
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "string",
                "party_identifier": "string",
                "ledger_account": {
                    "name": "string",
                    "description": "string",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "string",
                    "currency_exponent": 0,
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "external_account",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "string",
                "contact_details": [
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
            send_remittance_advice=True,
            statement_descriptor="string",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="string",
            ultimate_originating_party_name="string",
            ultimate_receiving_party_identifier="string",
            ultimate_receiving_party_name="string",
        )
        assert_matches_type(shared.AsyncResponse, payment_order, path=["response"])


class TestAsyncPaymentOrders:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.create(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @pytest.mark.skip(reason="Multiple values for nested arrays aren't supported yet")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.create(
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
            description="string",
            documents=[
                {
                    "documentable_id": "string",
                    "documentable_type": "cases",
                    "document_type": "string",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "string",
                    "documentable_type": "cases",
                    "document_type": "string",
                    "file": b"raw file contents",
                },
                {
                    "documentable_id": "string",
                    "documentable_type": "cases",
                    "document_type": "string",
                    "file": b"raw file contents",
                },
            ],
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="string",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_at": parse_date("2019-12-27"),
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
                "ledgerable_type": "counterparty",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
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
            nsf_protected=True,
            originating_party_name="string",
            priority="high",
            purpose="string",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "string",
                    "line2": "string",
                    "locality": "string",
                    "region": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "name": "string",
                "account_details": [
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "string",
                "party_identifier": "string",
                "ledger_account": {
                    "name": "string",
                    "description": "string",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "string",
                    "currency_exponent": 0,
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "external_account",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "string",
                "contact_details": [
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
            send_remittance_advice=True,
            statement_descriptor="string",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="string",
            ultimate_originating_party_name="string",
            ultimate_receiving_party_identifier="string",
            ultimate_receiving_party_name="string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.retrieve(
            "string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.update(
            "string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.update(
            "string",
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
            description="string",
            direction="credit",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="string",
            foreign_exchange_indicator="fixed_to_variable",
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
            nsf_protected=True,
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            originating_party_name="string",
            priority="high",
            purpose="string",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "string",
                    "line2": "string",
                    "locality": "string",
                    "region": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "name": "string",
                "account_details": [
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "string",
                "party_identifier": "string",
                "ledger_account": {
                    "name": "string",
                    "description": "string",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "string",
                    "currency_exponent": 0,
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "external_account",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "string",
                "contact_details": [
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
            send_remittance_advice=True,
            statement_descriptor="string",
            status="approved",
            subtype="0C",
            type="ach",
            ultimate_originating_party_identifier="string",
            ultimate_originating_party_name="string",
            ultimate_receiving_party_identifier="string",
            ultimate_receiving_party_name="string",
        )
        assert_matches_type(PaymentOrder, payment_order, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.list()
        assert_matches_type(AsyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.list(
            after_cursor="string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="credit",
            effective_date_end=parse_date("2019-12-27"),
            effective_date_start=parse_date("2019-12-27"),
            metadata={"foo": "string"},
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            per_page=0,
            priority="high",
            reference_number="string",
            status="approved",
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(AsyncPage[PaymentOrder], payment_order, path=["response"])

    @parametrize
    async def test_method_create_async(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.create_async(
            amount=0,
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
        )
        assert_matches_type(shared.AsyncResponse, payment_order, path=["response"])

    @parametrize
    async def test_method_create_async_with_all_params(self, client: AsyncModernTreasury) -> None:
        payment_order = await client.payment_orders.create_async(
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
            description="string",
            effective_date=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_type="ach",
            foreign_exchange_contract="string",
            foreign_exchange_indicator="fixed_to_variable",
            ledger_transaction={
                "description": "string",
                "status": "archived",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "effective_at": parse_date("2019-12-27"),
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
                "ledgerable_type": "counterparty",
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
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
            nsf_protected=True,
            originating_party_name="string",
            priority="high",
            purpose="string",
            receiving_account={
                "account_type": "cash",
                "party_type": "business",
                "party_address": {
                    "line1": "string",
                    "line2": "string",
                    "locality": "string",
                    "region": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "name": "string",
                "account_details": [
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                    {
                        "account_number": "string",
                        "account_number_type": "iban",
                    },
                ],
                "routing_details": [
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                    {
                        "routing_number": "string",
                        "routing_number_type": "aba",
                        "payment_type": "ach",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "party_name": "string",
                "party_identifier": "string",
                "ledger_account": {
                    "name": "string",
                    "description": "string",
                    "normal_balance": "credit",
                    "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "string",
                    "currency_exponent": 0,
                    "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "ledgerable_type": "external_account",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                },
                "plaid_processor_token": "string",
                "contact_details": [
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                    {
                        "contact_identifier": "string",
                        "contact_identifier_type": "email",
                    },
                ],
            },
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
            send_remittance_advice=True,
            statement_descriptor="string",
            subtype="0C",
            transaction_monitoring_enabled=True,
            ultimate_originating_party_identifier="string",
            ultimate_originating_party_name="string",
            ultimate_receiving_party_identifier="string",
            ultimate_receiving_party_name="string",
        )
        assert_matches_type(shared.AsyncResponse, payment_order, path=["response"])
