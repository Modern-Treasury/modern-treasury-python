# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    Counterparty,
    CounterpartyCollectAccountResponse,
)
from modern_treasury._utils import parse_datetime
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestCounterparties:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
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
            verification_status="denied",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.create(
            name="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.retrieve(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
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
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
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
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.delete(
            "string",
        )
        assert counterparty is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
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
            fields=["name", "nameOnAccount", "taxpayerIdentifier"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_raw_response_collect_account(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.collect_account(
            "string",
            direction="credit",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])


class TestAsyncCounterparties:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
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
            verification_status="denied",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.counterparties.with_raw_response.create(
            name="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.retrieve(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.counterparties.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
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
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.counterparties.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
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
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.counterparties.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        counterparty = await client.counterparties.delete(
            "string",
        )
        assert counterparty is None

    @parametrize
    async def test_raw_response_delete(self, client: AsyncModernTreasury) -> None:
        response = await client.counterparties.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
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
            fields=["name", "nameOnAccount", "taxpayerIdentifier"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_collect_account(self, client: AsyncModernTreasury) -> None:
        response = await client.counterparties.with_raw_response.collect_account(
            "string",
            direction="credit",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])
