# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.counterparty import Counterparty
from modern_treasury.types.counterparty_collect_account_response import (
    CounterpartyCollectAccountResponse,
)

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
        resource = client.counterparties.create(
            name="string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.counterparties.create(
            name="string",
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
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            accounting={"type": "customer"},
            ledger_type="customer",
            taxpayer_identifier="string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.counterparties.retrieve(
            "string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.counterparties.update(
            "string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.counterparties.update(
            "string",
            name="string",
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.counterparties.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.counterparties.list(
            after_cursor="string",
            per_page=0,
            name="string",
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            created_at_lower_bound="2019-12-27T18:11:19.117Z",
            created_at_upper_bound="2019-12-27T18:11:19.117Z",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        resource = client.counterparties.delete(
            "string",
        )
        assert resource is None

    @parametrize
    def test_method_collect_account(self, client: ModernTreasury) -> None:
        resource = client.counterparties.collect_account(
            "string",
            direction="credit",
        )
        assert isinstance(resource, CounterpartyCollectAccountResponse)

    @parametrize
    def test_method_collect_account_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.counterparties.collect_account(
            "string",
            direction="credit",
            send_email=True,
            fields=["name", "name", "name"],
            custom_redirect="https://example.com",
        )
        assert isinstance(resource, CounterpartyCollectAccountResponse)


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
        resource = await client.counterparties.create(
            name="string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.create(
            name="string",
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
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            accounting={"type": "customer"},
            ledger_type="customer",
            taxpayer_identifier="string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.retrieve(
            "string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.update(
            "string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.update(
            "string",
            name="string",
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert isinstance(resource, Counterparty)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.list(
            after_cursor="string",
            per_page=0,
            name="string",
            email="dev@stainlessapi.com",
            metadata={"foo": "string"},
            created_at_lower_bound="2019-12-27T18:11:19.117Z",
            created_at_upper_bound="2019-12-27T18:11:19.117Z",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.delete(
            "string",
        )
        assert resource is None

    @parametrize
    async def test_method_collect_account(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.collect_account(
            "string",
            direction="credit",
        )
        assert isinstance(resource, CounterpartyCollectAccountResponse)

    @parametrize
    async def test_method_collect_account_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.counterparties.collect_account(
            "string",
            direction="credit",
            send_email=True,
            fields=["name", "name", "name"],
            custom_redirect="https://example.com",
        )
        assert isinstance(resource, CounterpartyCollectAccountResponse)
