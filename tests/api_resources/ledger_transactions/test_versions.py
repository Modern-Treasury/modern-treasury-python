# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.ledger_transactions import LedgerTransactionVersion

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
    def test_method_list(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.list(
            "string",
        )
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.list(
            "string",
            after_cursor="string",
            per_page=0,
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            version={"foo": 0},
        )
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    def test_method_versions(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.versions(
            "string",
        )
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    def test_method_versions_with_all_params(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.versions(
            "string",
            after_cursor="string",
            per_page=0,
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            version={"foo": 0},
        )
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])


class TestAsyncVersions:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        version = await client.ledger_transactions.versions.list(
            "string",
        )
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        version = await client.ledger_transactions.versions.list(
            "string",
            after_cursor="string",
            per_page=0,
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            version={"foo": 0},
        )
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    async def test_method_versions(self, client: AsyncModernTreasury) -> None:
        version = await client.ledger_transactions.versions.versions(
            "string",
        )
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    async def test_method_versions_with_all_params(self, client: AsyncModernTreasury) -> None:
        version = await client.ledger_transactions.versions.versions(
            "string",
            after_cursor="string",
            per_page=0,
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            version={"foo": 0},
        )
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])
