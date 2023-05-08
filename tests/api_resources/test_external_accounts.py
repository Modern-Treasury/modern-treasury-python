# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import ExternalAccount
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestExternalAccounts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.create(
            account_type="cash",
            party_type="business",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            name="string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_details=[
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
            routing_details=[
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
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            party_name="string",
            party_identifier="string",
            ledger_account={
                "name": "string",
                "description": "string",
                "normal_balance": "credit",
                "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "currency": "string",
                "currency_exponent": 0,
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            plaid_processor_token="string",
            contact_details=[
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
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.retrieve(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.update(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.update(
            "string",
            party_type="business",
            account_type="cash",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            party_name="string",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.list()
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.list(
            after_cursor="string",
            per_page=0,
            party_name="string",
            counterparty_id="string",
            metadata={"foo": "string"},
        )
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.delete(
            "string",
        )
        assert external_account is None

    @parametrize
    def test_method_complete_verification(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.complete_verification(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_complete_verification_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.complete_verification(
            "string",
            amounts=[0, 0],
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_verify(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.verify(
            "string",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_verify_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.verify(
            "string",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
            currency="AED",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])


class TestAsyncExternalAccounts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.create(
            account_type="cash",
            party_type="business",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            name="string",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_details=[
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
            routing_details=[
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
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            party_name="string",
            party_identifier="string",
            ledger_account={
                "name": "string",
                "description": "string",
                "normal_balance": "credit",
                "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "currency": "string",
                "currency_exponent": 0,
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            plaid_processor_token="string",
            contact_details=[
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
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.retrieve(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.update(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.update(
            "string",
            party_type="business",
            account_type="cash",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            party_name="string",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.list()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.list(
            after_cursor="string",
            per_page=0,
            party_name="string",
            counterparty_id="string",
            metadata={"foo": "string"},
        )
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.delete(
            "string",
        )
        assert external_account is None

    @parametrize
    async def test_method_complete_verification(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.complete_verification(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_complete_verification_with_all_params(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.complete_verification(
            "string",
            amounts=[0, 0],
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_verify(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.verify(
            "string",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_verify_with_all_params(self, client: AsyncModernTreasury) -> None:
        external_account = await client.external_accounts.verify(
            "string",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
            currency="AED",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])
