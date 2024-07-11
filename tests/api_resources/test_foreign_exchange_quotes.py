# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    ForeignExchangeQuote,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForeignExchangeQuotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        foreign_exchange_quote = client.foreign_exchange_quotes.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
        )
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        foreign_exchange_quote = client.foreign_exchange_quotes.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
            base_amount=0,
            base_currency="AED",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            target_amount=0,
        )
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.foreign_exchange_quotes.with_raw_response.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        foreign_exchange_quote = response.parse()
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.foreign_exchange_quotes.with_streaming_response.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            foreign_exchange_quote = response.parse()
            assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        foreign_exchange_quote = client.foreign_exchange_quotes.retrieve(
            "id",
        )
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.foreign_exchange_quotes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        foreign_exchange_quote = response.parse()
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.foreign_exchange_quotes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            foreign_exchange_quote = response.parse()
            assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.foreign_exchange_quotes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        foreign_exchange_quote = client.foreign_exchange_quotes.list()
        assert_matches_type(SyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        foreign_exchange_quote = client.foreign_exchange_quotes.list(
            after_cursor="after_cursor",
            base_currency="base_currency",
            effective_at_end=parse_date("2019-12-27"),
            effective_at_start=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            internal_account_id="internal_account_id",
            metadata={"foo": "string"},
            per_page=0,
            target_currency="target_currency",
        )
        assert_matches_type(SyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.foreign_exchange_quotes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        foreign_exchange_quote = response.parse()
        assert_matches_type(SyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.foreign_exchange_quotes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            foreign_exchange_quote = response.parse()
            assert_matches_type(SyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncForeignExchangeQuotes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        foreign_exchange_quote = await async_client.foreign_exchange_quotes.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
        )
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        foreign_exchange_quote = await async_client.foreign_exchange_quotes.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
            base_amount=0,
            base_currency="AED",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            target_amount=0,
        )
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.foreign_exchange_quotes.with_raw_response.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        foreign_exchange_quote = response.parse()
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.foreign_exchange_quotes.with_streaming_response.create(
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_currency="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            foreign_exchange_quote = await response.parse()
            assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        foreign_exchange_quote = await async_client.foreign_exchange_quotes.retrieve(
            "id",
        )
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.foreign_exchange_quotes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        foreign_exchange_quote = response.parse()
        assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.foreign_exchange_quotes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            foreign_exchange_quote = await response.parse()
            assert_matches_type(ForeignExchangeQuote, foreign_exchange_quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.foreign_exchange_quotes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        foreign_exchange_quote = await async_client.foreign_exchange_quotes.list()
        assert_matches_type(AsyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        foreign_exchange_quote = await async_client.foreign_exchange_quotes.list(
            after_cursor="after_cursor",
            base_currency="base_currency",
            effective_at_end=parse_date("2019-12-27"),
            effective_at_start=parse_date("2019-12-27"),
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            internal_account_id="internal_account_id",
            metadata={"foo": "string"},
            per_page=0,
            target_currency="target_currency",
        )
        assert_matches_type(AsyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.foreign_exchange_quotes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        foreign_exchange_quote = response.parse()
        assert_matches_type(AsyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.foreign_exchange_quotes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            foreign_exchange_quote = await response.parse()
            assert_matches_type(AsyncPage[ForeignExchangeQuote], foreign_exchange_quote, path=["response"])

        assert cast(Any, response.is_closed) is True
