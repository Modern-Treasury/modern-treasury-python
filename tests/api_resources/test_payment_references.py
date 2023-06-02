# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import PaymentReference
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestPaymentReferences:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
    def test_method_retireve(self, client: ModernTreasury) -> None:
        payment_reference = client.payment_references.retireve(
            "string",
        )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])


class TestAsyncPaymentReferences:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
    async def test_method_retireve(self, client: AsyncModernTreasury) -> None:
        payment_reference = await client.payment_references.retireve(
            "string",
        )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])
