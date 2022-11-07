# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.expected_payment import ExpectedPayment

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestExpectedPayments:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.create(
            amount_upper_bound=0,
            amount_lower_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.create(
            amount_upper_bound=0,
            amount_lower_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            currency="AED",
            date_upper_bound="2019-12-27",
            date_lower_bound="2019-12-27",
            description="string",
            statement_descriptor="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
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
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.retrieve(
            "string",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.update(
            "string",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.update(
            "string",
            amount_upper_bound=0,
            amount_lower_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            currency="AED",
            date_upper_bound="2019-12-27",
            date_lower_bound="2019-12-27",
            description="string",
            statement_descriptor="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.list(
            after_cursor="string",
            per_page=0,
            status="archived",
            internal_account_id="string",
            direction="credit",
            type="ach",
            counterparty_id="string",
            metadata={"foo": "string"},
            created_at_lower_bound="2019-12-27T18:11:19.117Z",
            created_at_upper_bound="2019-12-27T18:11:19.117Z",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        resource = client.expected_payments.delete(
            "string",
        )
        assert isinstance(resource, ExpectedPayment)


class TestAsyncExpectedPayments:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.create(
            amount_upper_bound=0,
            amount_lower_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.create(
            amount_upper_bound=0,
            amount_lower_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            currency="AED",
            date_upper_bound="2019-12-27",
            date_lower_bound="2019-12-27",
            description="string",
            statement_descriptor="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
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
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.retrieve(
            "string",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.update(
            "string",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.update(
            "string",
            amount_upper_bound=0,
            amount_lower_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            currency="AED",
            date_upper_bound="2019-12-27",
            date_lower_bound="2019-12-27",
            description="string",
            statement_descriptor="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remittance_information="string",
        )
        assert isinstance(resource, ExpectedPayment)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.list(
            after_cursor="string",
            per_page=0,
            status="archived",
            internal_account_id="string",
            direction="credit",
            type="ach",
            counterparty_id="string",
            metadata={"foo": "string"},
            created_at_lower_bound="2019-12-27T18:11:19.117Z",
            created_at_upper_bound="2019-12-27T18:11:19.117Z",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        resource = await client.expected_payments.delete(
            "string",
        )
        assert isinstance(resource, ExpectedPayment)
