# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Counterparty, CounterpartyCollectAccountResponse
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCounterparties:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.create(
            name="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.create(
            name="string",
            accounting={"type": "customer"},
            accounts=[
                {
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
                {
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
                {
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
            ],
            email="dev@stainlessapi.com",
            ledger_type="customer",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.retrieve(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.update(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.update(
            "string",
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            name="string",
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.list()
        assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.list(
            after_cursor="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            name="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.delete(
            "string",
        )
        assert counterparty is None

    @parametrize
    def test_method_collect_account(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.collect_account(
            "string",
            direction="credit",
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_method_collect_account_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.collect_account(
            "string",
            direction="credit",
            custom_redirect="https://example.com",
            fields=["name", "name", "name"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])


class TestAsyncCounterparties:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.create(
            name="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.create(
            name="string",
            accounting={"type": "customer"},
            accounts=[
                {
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
                {
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
                {
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
            ],
            email="dev@stainlessapi.com",
            ledger_type="customer",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.retrieve(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.update(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.update(
            "string",
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            name="string",
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.list()
        assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.list(
            after_cursor="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            name="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.delete(
            "string",
        )
        assert counterparty is None

    @parametrize
    async def test_method_collect_account(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.collect_account(
            "string",
            direction="credit",
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_method_collect_account_with_all_params(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.collect_account(
            "string",
            direction="credit",
            custom_redirect="https://example.com",
            fields=["name", "name", "name"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])
