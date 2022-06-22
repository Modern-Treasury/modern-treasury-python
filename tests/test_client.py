# File generated from our OpenAPI spec by Stainless.

import os

import httpx

from modern_treasury import ModernTreasury, AsyncModernTreasury

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestModernTreasury:
    client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )

    def test_raw_response(self) -> None:
        response = self.client.get("/api/counterparties", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)


class TestAsyncModernTreasury:
    client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )

    async def test_raw_response(self) -> None:
        response = await self.client.get("/api/counterparties", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)
