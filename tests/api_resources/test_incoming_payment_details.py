# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.incoming_payment_detail import IncomingPaymentDetail

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestIncomingPaymentDetails:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.incoming_payment_details.retrieve(
            "string",
        )
        assert isinstance(resource, IncomingPaymentDetail)

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        resource = client.incoming_payment_details.update(
            "string",
        )
        assert isinstance(resource, IncomingPaymentDetail)

    @parametrize
    def test_method_update_with_optional_params(self, client: ModernTreasury) -> None:
        resource = client.incoming_payment_details.update(
            "string",
            {"metadata": {"foo": "string"}},
        )
        assert isinstance(resource, IncomingPaymentDetail)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.incoming_payment_details.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_optional_params(self, client: ModernTreasury) -> None:
        resource = client.incoming_payment_details.list(
            {
                "after_cursor": "string",
                "per_page": 0,
                "direction": "credit",
                "status": "completed",
                "type": "ach",
                "as_of_date_start": "2019-12-27",
                "as_of_date_end": "2019-12-27",
                "metadata": {"foo": "string"},
                "virtual_account_id": "string",
            },
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_create_async(self, client: ModernTreasury) -> None:
        resource = client.incoming_payment_details.create_async()
        assert resource is None

    @parametrize
    def test_method_create_async_with_optional_params(self, client: ModernTreasury) -> None:
        resource = client.incoming_payment_details.create_async(
            {
                "type": "ach",
                "direction": "credit",
                "amount": 0,
                "currency": "AED",
                "internal_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "virtual_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "as_of_date": "2019-12-27",
            },
        )
        assert resource is None


class TestAsyncIncomingPaymentDetails:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.incoming_payment_details.retrieve(
            "string",
        )
        assert isinstance(resource, IncomingPaymentDetail)

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        resource = await client.incoming_payment_details.update(
            "string",
        )
        assert isinstance(resource, IncomingPaymentDetail)

    @parametrize
    async def test_method_update_with_optional_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.incoming_payment_details.update(
            "string",
            {"metadata": {"foo": "string"}},
        )
        assert isinstance(resource, IncomingPaymentDetail)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.incoming_payment_details.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_optional_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.incoming_payment_details.list(
            {
                "after_cursor": "string",
                "per_page": 0,
                "direction": "credit",
                "status": "completed",
                "type": "ach",
                "as_of_date_start": "2019-12-27",
                "as_of_date_end": "2019-12-27",
                "metadata": {"foo": "string"},
                "virtual_account_id": "string",
            },
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_create_async(self, client: AsyncModernTreasury) -> None:
        resource = await client.incoming_payment_details.create_async()
        assert resource is None

    @parametrize
    async def test_method_create_async_with_optional_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.incoming_payment_details.create_async(
            {
                "type": "ach",
                "direction": "credit",
                "amount": 0,
                "currency": "AED",
                "internal_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "virtual_account_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "as_of_date": "2019-12-27",
            },
        )
        assert resource is None
