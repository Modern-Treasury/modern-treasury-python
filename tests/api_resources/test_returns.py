# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import ReturnObject
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestReturns:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )
        assert isinstance(resource, ReturnObject)

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="901",
            reason="string",
            date_of_death="2019-12-27",
            additional_information="string",
            returnable_type="incoming_payment_detail",
        )
        assert isinstance(resource, ReturnObject)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.returns.retrieve(
            "string",
        )
        assert isinstance(resource, ReturnObject)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.returns.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.returns.list(
            after_cursor="string",
            per_page=0,
            internal_account_id="string",
            counterparty_id="string",
            returnable_id="string",
            returnable_type="incoming_payment_detail",
        )
        assert isinstance(resource, SyncPage)


class TestAsyncReturns:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )
        assert isinstance(resource, ReturnObject)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="901",
            reason="string",
            date_of_death="2019-12-27",
            additional_information="string",
            returnable_type="incoming_payment_detail",
        )
        assert isinstance(resource, ReturnObject)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.returns.retrieve(
            "string",
        )
        assert isinstance(resource, ReturnObject)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.returns.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.returns.list(
            after_cursor="string",
            per_page=0,
            internal_account_id="string",
            counterparty_id="string",
            returnable_id="string",
            returnable_type="incoming_payment_detail",
        )
        assert isinstance(resource, AsyncPage)
