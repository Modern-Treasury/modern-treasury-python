# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import BulkRequest
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestBulkRequests:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
                        "ledgerable_type": "counterparty",
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
                    "documents": [
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
                        "ledgerable_type": "counterparty",
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
                    "documents": [
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
                        "ledgerable_type": "counterparty",
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
                    "documents": [
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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(SyncPage[BulkRequest], bulk_request, path=["response"])


class TestAsyncBulkRequests:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Multipart documents aren't constructed properly yet")
    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        bulk_request = await client.bulk_requests.create(
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
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        bulk_request = await client.bulk_requests.create(
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
                        "ledgerable_type": "counterparty",
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
                    "documents": [
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
                        "ledgerable_type": "counterparty",
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
                    "documents": [
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
                        "ledgerable_type": "counterparty",
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
                    "documents": [
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
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.bulk_requests.with_raw_response.create(
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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        bulk_request = await client.bulk_requests.retrieve(
            "string",
        )
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.bulk_requests.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(BulkRequest, bulk_request, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        bulk_request = await client.bulk_requests.list()
        assert_matches_type(AsyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        bulk_request = await client.bulk_requests.list(
            action_type="create",
            after_cursor="string",
            metadata={"foo": "string"},
            per_page=0,
            resource_type="payment_order",
            status="pending",
        )
        assert_matches_type(AsyncPage[BulkRequest], bulk_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.bulk_requests.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_request = response.parse()
        assert_matches_type(AsyncPage[BulkRequest], bulk_request, path=["response"])
