# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerAccountStatementCreateResponse,
    LedgerAccountStatementRetrieveResponse,
)
from modern_treasury._utils import parse_datetime
from modern_treasury._client import ModernTreasury, AsyncModernTreasury

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
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account_statement = client.ledger_account_statements.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_account_statements.with_raw_response.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_statement = response.parse()
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_account_statements.with_streaming_response.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_statement = response.parse()
            assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account_statement = client.ledger_account_statements.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_account_statements.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_statement = response.parse()
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_account_statements.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_statement = response.parse()
            assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_statements.with_raw_response.retrieve(
                "",
            )


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
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account_statement = await client.ledger_account_statements.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_account_statements.with_raw_response.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_statement = response.parse()
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_account_statements.with_streaming_response.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_statement = await response.parse()
            assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account_statement = await client.ledger_account_statements.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.ledger_account_statements.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_statement = response.parse()
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.ledger_account_statements.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_statement = await response.parse()
            assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.ledger_account_statements.with_raw_response.retrieve(
                "",
            )
