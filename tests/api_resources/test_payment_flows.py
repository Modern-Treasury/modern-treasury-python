# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    PaymentFlow,
)
from modern_treasury._utils import parse_date
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestPaymentFlows:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        payment_flow = client.payment_flows.create(
            amount=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="string",
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        payment_flow = client.payment_flows.create(
            amount=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="string",
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            due_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.payment_flows.with_raw_response.create(
            amount=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="string",
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        payment_flow = client.payment_flows.retrieve(
            "string",
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.payment_flows.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        payment_flow = client.payment_flows.update(
            "string",
            status="cancelled",
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.payment_flows.with_raw_response.update(
            "string",
            status="cancelled",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        payment_flow = client.payment_flows.list()
        assert_matches_type(SyncPage[PaymentFlow], payment_flow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        payment_flow = client.payment_flows.list(
            after_cursor="string",
            client_token="string",
            counterparty_id="string",
            originating_account_id="string",
            payment_order_id="string",
            per_page=0,
            receiving_account_id="string",
            status="string",
        )
        assert_matches_type(SyncPage[PaymentFlow], payment_flow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.payment_flows.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(SyncPage[PaymentFlow], payment_flow, path=["response"])


class TestAsyncPaymentFlows:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        payment_flow = await client.payment_flows.create(
            amount=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="string",
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        payment_flow = await client.payment_flows.create(
            amount=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="string",
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            due_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.payment_flows.with_raw_response.create(
            amount=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="string",
            direction="credit",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        payment_flow = await client.payment_flows.retrieve(
            "string",
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.payment_flows.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        payment_flow = await client.payment_flows.update(
            "string",
            status="cancelled",
        )
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.payment_flows.with_raw_response.update(
            "string",
            status="cancelled",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlow, payment_flow, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        payment_flow = await client.payment_flows.list()
        assert_matches_type(AsyncPage[PaymentFlow], payment_flow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        payment_flow = await client.payment_flows.list(
            after_cursor="string",
            client_token="string",
            counterparty_id="string",
            originating_account_id="string",
            payment_order_id="string",
            per_page=0,
            receiving_account_id="string",
            status="string",
        )
        assert_matches_type(AsyncPage[PaymentFlow], payment_flow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.payment_flows.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(AsyncPage[PaymentFlow], payment_flow, path=["response"])
