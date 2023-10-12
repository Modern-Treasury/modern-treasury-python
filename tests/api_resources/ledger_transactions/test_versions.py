# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.ledger_transactions import LedgerTransactionVersion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestVersions:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.list()
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        version = client.ledger_transactions.versions.list(
            after_cursor="string",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_account_statement_id="string",
            ledger_transaction_id="string",
            per_page=0,
            version={"foo": 0},
        )
        assert_matches_type(SyncPage[LedgerTransactionVersion], version, path=["response"])


class TestAsyncVersions:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        version = await client.ledger_transactions.versions.list()
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        version = await client.ledger_transactions.versions.list(
            after_cursor="string",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            ledger_account_statement_id="string",
            ledger_transaction_id="string",
            per_page=0,
            version={"foo": 0},
        )
        assert_matches_type(AsyncPage[LedgerTransactionVersion], version, path=["response"])
