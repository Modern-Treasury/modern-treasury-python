# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestVersions:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_versions(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.versions.versions(
            "string",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_versions_with_optional_params(self, client: ModernTreasury) -> None:
        resource = client.ledger_transactions.versions.versions(
            "string",
            {
                "after_cursor": "string",
                "per_page": 0,
                "created_at": {"foo": "2019-12-27T18:11:19.117Z"},
                "version": {"foo": 0},
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncVersions:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_versions(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.versions.versions(
            "string",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_versions_with_optional_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.ledger_transactions.versions.versions(
            "string",
            {
                "after_cursor": "string",
                "per_page": 0,
                "created_at": {"foo": "2019-12-27T18:11:19.117Z"},
                "version": {"foo": 0},
            },
        )
        assert isinstance(resource, AsyncPage)
