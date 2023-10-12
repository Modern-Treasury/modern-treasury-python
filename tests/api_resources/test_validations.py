# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import RoutingNumberLookupRequest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestValidations:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_validate_routing_number(self, client: ModernTreasury) -> None:
        validation = client.validations.validate_routing_number(
            routing_number="string",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])


class TestAsyncValidations:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_validate_routing_number(self, client: AsyncModernTreasury) -> None:
        validation = await client.validations.validate_routing_number(
            routing_number="string",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])
