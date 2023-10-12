# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerAccountStatementCreateResponse,
    LedgerAccountStatementRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLedgerAccountStatements:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account_statement = client.ledger_account_statements.create(
            effective_at_lower_bound="string",
            effective_at_upper_bound="string",
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_statement = client.ledger_account_statements.create(
            effective_at_lower_bound="string",
            effective_at_upper_bound="string",
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_statement = client.ledger_account_statements.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])


class TestAsyncLedgerAccountStatements:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_account_statement = await client.ledger_account_statements.create(
            effective_at_lower_bound="string",
            effective_at_upper_bound="string",
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_statement = await client.ledger_account_statements.create(
            effective_at_lower_bound="string",
            effective_at_upper_bound="string",
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account_statement = await client.ledger_account_statements.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])
