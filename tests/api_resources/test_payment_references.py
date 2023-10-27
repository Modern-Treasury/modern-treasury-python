# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import PaymentReference
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestPaymentReferences:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        payment_reference = client.payment_references.retrieve(
            "string",
        )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.payment_references.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        payment_reference = client.payment_references.list()
        assert_matches_type(SyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        payment_reference = client.payment_references.list(
            after_cursor="string",
            per_page=0,
            reference_number="string",
            referenceable_id="string",
            referenceable_type="payment_order",
        )
        assert_matches_type(SyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.payment_references.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(SyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    def test_method_retireve(self, client: ModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            payment_reference = client.payment_references.retireve(
                "string",
            )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    def test_raw_response_retireve(self, client: ModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.payment_references.with_raw_response.retireve(
                "string",
            )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])


class TestAsyncPaymentReferences:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        payment_reference = await client.payment_references.retrieve(
            "string",
        )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.payment_references.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        payment_reference = await client.payment_references.list()
        assert_matches_type(AsyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        payment_reference = await client.payment_references.list(
            after_cursor="string",
            per_page=0,
            reference_number="string",
            referenceable_id="string",
            referenceable_type="payment_order",
        )
        assert_matches_type(AsyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.payment_references.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(AsyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    async def test_method_retireve(self, client: AsyncModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            payment_reference = await client.payment_references.retireve(
                "string",
            )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    async def test_raw_response_retireve(self, client: AsyncModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            response = await client.payment_references.with_raw_response.retireve(
                "string",
            )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])
