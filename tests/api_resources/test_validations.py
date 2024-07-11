# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import RoutingNumberLookupRequest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_validate_routing_number(self, client: ModernTreasury) -> None:
        validation = client.validations.validate_routing_number(
            routing_number="routing_number",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])

    @parametrize
    def test_raw_response_validate_routing_number(self, client: ModernTreasury) -> None:
        response = client.validations.with_raw_response.validate_routing_number(
            routing_number="routing_number",
            routing_number_type="aba",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = response.parse()
        assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])

    @parametrize
    def test_streaming_response_validate_routing_number(self, client: ModernTreasury) -> None:
        with client.validations.with_streaming_response.validate_routing_number(
            routing_number="routing_number",
            routing_number_type="aba",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = response.parse()
            assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_validate_routing_number(self, async_client: AsyncModernTreasury) -> None:
        validation = await async_client.validations.validate_routing_number(
            routing_number="routing_number",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])

    @parametrize
    async def test_raw_response_validate_routing_number(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.validations.with_raw_response.validate_routing_number(
            routing_number="routing_number",
            routing_number_type="aba",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = response.parse()
        assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])

    @parametrize
    async def test_streaming_response_validate_routing_number(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.validations.with_streaming_response.validate_routing_number(
            routing_number="routing_number",
            routing_number_type="aba",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = await response.parse()
            assert_matches_type(RoutingNumberLookupRequest, validation, path=["response"])

        assert cast(Any, response.is_closed) is True
