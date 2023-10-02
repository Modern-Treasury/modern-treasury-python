# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import ReturnObject
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
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
        return_ = client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        return_ = client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
            additional_information="string",
            code="901",
            date_of_death=parse_date("2019-12-27"),
            reason="string",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        return_ = client.returns.retrieve(
            "string",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        return_ = client.returns.list()
        assert_matches_type(SyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        return_ = client.returns.list(
            after_cursor="string",
            counterparty_id="string",
            internal_account_id="string",
            per_page=0,
            returnable_id="string",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(SyncPage[ReturnObject], return_, path=["response"])


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
        return_ = await client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        return_ = await client.returns.create(
            returnable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            returnable_type="incoming_payment_detail",
            additional_information="string",
            code="901",
            date_of_death=parse_date("2019-12-27"),
            reason="string",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        return_ = await client.returns.retrieve(
            "string",
        )
        assert_matches_type(ReturnObject, return_, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        return_ = await client.returns.list()
        assert_matches_type(AsyncPage[ReturnObject], return_, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        return_ = await client.returns.list(
            after_cursor="string",
            counterparty_id="string",
            internal_account_id="string",
            per_page=0,
            returnable_id="string",
            returnable_type="incoming_payment_detail",
        )
        assert_matches_type(AsyncPage[ReturnObject], return_, path=["response"])
