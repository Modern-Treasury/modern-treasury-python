# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import BulkRequest
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        bulk_request = client.bulk_requests.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        bulk_request = client.bulk_requests.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "subtype": "0C",
                    "amount": 0,
                    "direction": "credit",
                    "priority": "high",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "receiving_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting": {
                        "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "accounting_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting_ledger_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "AED",
                    "effective_date": parse_date("2019-12-27"),
                    "description": "string",
                    "statement_descriptor": "string",
                    "remittance_information": "string",
                    "process_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "purpose": "string",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "charge_bearer": "shared",
                    "foreign_exchange_indicator": "fixed_to_variable",
                    "foreign_exchange_contract": "string",
                    "nsf_protected": True,
                    "originating_party_name": "string",
                    "ultimate_originating_party_name": "string",
                    "ultimate_originating_party_identifier": "string",
                    "ultimate_receiving_party_name": "string",
                    "ultimate_receiving_party_identifier": "string",
                    "send_remittance_advice": True,
                    "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fallback_type": "ach",
                    "receiving_account": {
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
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
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
                    "ledger_transaction": {
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
                    "ledger_transaction_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "line_items": [
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
                    "transaction_monitoring_enabled": True,
                },
                {
                    "type": "ach",
                    "subtype": "0C",
                    "amount": 0,
                    "direction": "credit",
                    "priority": "high",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "receiving_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting": {
                        "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "accounting_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting_ledger_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "AED",
                    "effective_date": parse_date("2019-12-27"),
                    "description": "string",
                    "statement_descriptor": "string",
                    "remittance_information": "string",
                    "process_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "purpose": "string",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "charge_bearer": "shared",
                    "foreign_exchange_indicator": "fixed_to_variable",
                    "foreign_exchange_contract": "string",
                    "nsf_protected": True,
                    "originating_party_name": "string",
                    "ultimate_originating_party_name": "string",
                    "ultimate_originating_party_identifier": "string",
                    "ultimate_receiving_party_name": "string",
                    "ultimate_receiving_party_identifier": "string",
                    "send_remittance_advice": True,
                    "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fallback_type": "ach",
                    "receiving_account": {
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
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
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
                    "ledger_transaction": {
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
                    "ledger_transaction_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "line_items": [
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
                    "transaction_monitoring_enabled": True,
                },
                {
                    "type": "ach",
                    "subtype": "0C",
                    "amount": 0,
                    "direction": "credit",
                    "priority": "high",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "receiving_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting": {
                        "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "accounting_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting_ledger_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "AED",
                    "effective_date": parse_date("2019-12-27"),
                    "description": "string",
                    "statement_descriptor": "string",
                    "remittance_information": "string",
                    "process_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "purpose": "string",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "charge_bearer": "shared",
                    "foreign_exchange_indicator": "fixed_to_variable",
                    "foreign_exchange_contract": "string",
                    "nsf_protected": True,
                    "originating_party_name": "string",
                    "ultimate_originating_party_name": "string",
                    "ultimate_originating_party_identifier": "string",
                    "ultimate_receiving_party_name": "string",
                    "ultimate_receiving_party_identifier": "string",
                    "send_remittance_advice": True,
                    "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fallback_type": "ach",
                    "receiving_account": {
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
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
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
                    "ledger_transaction": {
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
                    "ledger_transaction_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "line_items": [
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
                    "transaction_monitoring_enabled": True,
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.bulk_requests.with_raw_response.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.bulk_requests.with_streaming_response.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_request = response.parse()
            assert_matches_type(BulkRequest, bulk_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        bulk_request = client.bulk_requests.retrieve(
            "string",
        )
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.bulk_requests.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.bulk_requests.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_request = response.parse()
            assert_matches_type(BulkRequest, bulk_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bulk_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        bulk_request = client.bulk_requests.list()
        assert_matches_type(SyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        bulk_request = client.bulk_requests.list(
            action_type="create",
            after_cursor="string",
            metadata={"foo": "string"},
            per_page=0,
            resource_type="payment_order",
            status="pending",
        )
        assert_matches_type(SyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.bulk_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(SyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.bulk_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_request = response.parse()
            assert_matches_type(SyncPage[BulkRequest], bulk_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulkRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        bulk_request = await async_client.bulk_requests.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        bulk_request = await async_client.bulk_requests.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "subtype": "0C",
                    "amount": 0,
                    "direction": "credit",
                    "priority": "high",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "receiving_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting": {
                        "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "accounting_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting_ledger_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "AED",
                    "effective_date": parse_date("2019-12-27"),
                    "description": "string",
                    "statement_descriptor": "string",
                    "remittance_information": "string",
                    "process_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "purpose": "string",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "charge_bearer": "shared",
                    "foreign_exchange_indicator": "fixed_to_variable",
                    "foreign_exchange_contract": "string",
                    "nsf_protected": True,
                    "originating_party_name": "string",
                    "ultimate_originating_party_name": "string",
                    "ultimate_originating_party_identifier": "string",
                    "ultimate_receiving_party_name": "string",
                    "ultimate_receiving_party_identifier": "string",
                    "send_remittance_advice": True,
                    "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fallback_type": "ach",
                    "receiving_account": {
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
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
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
                    "ledger_transaction": {
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
                    "ledger_transaction_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "line_items": [
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
                    "transaction_monitoring_enabled": True,
                },
                {
                    "type": "ach",
                    "subtype": "0C",
                    "amount": 0,
                    "direction": "credit",
                    "priority": "high",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "receiving_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting": {
                        "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "accounting_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting_ledger_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "AED",
                    "effective_date": parse_date("2019-12-27"),
                    "description": "string",
                    "statement_descriptor": "string",
                    "remittance_information": "string",
                    "process_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "purpose": "string",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "charge_bearer": "shared",
                    "foreign_exchange_indicator": "fixed_to_variable",
                    "foreign_exchange_contract": "string",
                    "nsf_protected": True,
                    "originating_party_name": "string",
                    "ultimate_originating_party_name": "string",
                    "ultimate_originating_party_identifier": "string",
                    "ultimate_receiving_party_name": "string",
                    "ultimate_receiving_party_identifier": "string",
                    "send_remittance_advice": True,
                    "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fallback_type": "ach",
                    "receiving_account": {
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
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
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
                    "ledger_transaction": {
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
                    "ledger_transaction_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "line_items": [
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
                    "transaction_monitoring_enabled": True,
                },
                {
                    "type": "ach",
                    "subtype": "0C",
                    "amount": 0,
                    "direction": "credit",
                    "priority": "high",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "receiving_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting": {
                        "account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "accounting_category_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "accounting_ledger_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "currency": "AED",
                    "effective_date": parse_date("2019-12-27"),
                    "description": "string",
                    "statement_descriptor": "string",
                    "remittance_information": "string",
                    "process_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "purpose": "string",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "charge_bearer": "shared",
                    "foreign_exchange_indicator": "fixed_to_variable",
                    "foreign_exchange_contract": "string",
                    "nsf_protected": True,
                    "originating_party_name": "string",
                    "ultimate_originating_party_name": "string",
                    "ultimate_originating_party_identifier": "string",
                    "ultimate_receiving_party_name": "string",
                    "ultimate_receiving_party_identifier": "string",
                    "send_remittance_advice": True,
                    "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fallback_type": "ach",
                    "receiving_account": {
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
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
                            },
                            {
                                "account_number": "string",
                                "account_number_type": "au_number",
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
                    "ledger_transaction": {
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
                    "ledger_transaction_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "line_items": [
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
                    "transaction_monitoring_enabled": True,
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.bulk_requests.with_raw_response.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.bulk_requests.with_streaming_response.create(
            action_type="create",
            resource_type="payment_order",
            resources=[
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "type": "ach",
                    "amount": 0,
                    "direction": "credit",
                    "originating_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_request = await response.parse()
            assert_matches_type(BulkRequest, bulk_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        bulk_request = await async_client.bulk_requests.retrieve(
            "string",
        )
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.bulk_requests.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.bulk_requests.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_request = await response.parse()
            assert_matches_type(BulkRequest, bulk_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bulk_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        bulk_request = await async_client.bulk_requests.list()
        assert_matches_type(AsyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        bulk_request = await async_client.bulk_requests.list(
            action_type="create",
            after_cursor="string",
            metadata={"foo": "string"},
            per_page=0,
            resource_type="payment_order",
            status="pending",
        )
        assert_matches_type(AsyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.bulk_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(AsyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.bulk_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_request = await response.parse()
            assert_matches_type(AsyncPage[BulkRequest], bulk_request, path=["response"])

        assert cast(Any, response.is_closed) is True
