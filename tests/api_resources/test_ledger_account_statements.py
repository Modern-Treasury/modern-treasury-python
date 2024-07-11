# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerAccountStatements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            description="description",
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
            "id",
        )
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_account_statements.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_statement = response.parse()
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_account_statements.with_streaming_response.retrieve(
            "id",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_statement = await async_client.ledger_account_statements.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_statement = await async_client.ledger_account_statements.create(
            effective_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            ledger_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccountStatementCreateResponse, ledger_account_statement, path=["response"])

    @pytest.mark.skip(reason="Prism is broken in this case")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_statements.with_raw_response.create(
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
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_statements.with_streaming_response.create(
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
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_account_statement = await async_client.ledger_account_statements.retrieve(
            "id",
        )
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_statements.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account_statement = response.parse()
        assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_statements.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account_statement = await response.parse()
            assert_matches_type(LedgerAccountStatementRetrieveResponse, ledger_account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_statements.with_raw_response.retrieve(
                "",
            )
