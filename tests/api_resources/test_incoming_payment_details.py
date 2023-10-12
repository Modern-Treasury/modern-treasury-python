# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import IncomingPaymentDetail
from modern_treasury._utils import parse_date
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.shared import AsyncResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestIncomingPaymentDetails:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.retrieve(
            "string",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.update(
            "string",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.update(
            "string",
            metadata={"foo": "string"},
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.list()
        assert_matches_type(SyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.list(
            after_cursor="string",
            as_of_date_end=parse_date("2019-12-27"),
            as_of_date_start=parse_date("2019-12-27"),
            direction="credit",
            metadata={"foo": "string"},
            per_page=0,
            status="completed",
            type="ach",
            virtual_account_id="string",
        )
        assert_matches_type(SyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_create_async(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.create_async()
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    def test_method_create_async_with_all_params(self, client: ModernTreasury) -> None:
        incoming_payment_detail = client.incoming_payment_details.create_async(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            currency="AED",
            description="string",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])


class TestAsyncIncomingPaymentDetails:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await client.incoming_payment_details.retrieve(
            "string",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await client.incoming_payment_details.update(
            "string",
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await client.incoming_payment_details.update(
            "string",
            metadata={"foo": "string"},
        )
        assert_matches_type(IncomingPaymentDetail, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await client.incoming_payment_details.list()
        assert_matches_type(AsyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await client.incoming_payment_details.list(
            after_cursor="string",
            as_of_date_end=parse_date("2019-12-27"),
            as_of_date_start=parse_date("2019-12-27"),
            direction="credit",
            metadata={"foo": "string"},
            per_page=0,
            status="completed",
            type="ach",
            virtual_account_id="string",
        )
        assert_matches_type(AsyncPage[IncomingPaymentDetail], incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_create_async(self, client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await client.incoming_payment_details.create_async()
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])

    @parametrize
    async def test_method_create_async_with_all_params(self, client: AsyncModernTreasury) -> None:
        incoming_payment_detail = await client.incoming_payment_details.create_async(
            amount=0,
            as_of_date=parse_date("2019-12-27"),
            currency="AED",
            description="string",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ach",
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncResponse, incoming_payment_detail, path=["response"])
