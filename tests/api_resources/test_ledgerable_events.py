# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerableEvent

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerableEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.create(
            name="name",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.create(
            name="name",
            custom_data={},
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledgerable_events.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledgerable_events.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledgerable_event = client.ledgerable_events.retrieve(
            "id",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledgerable_events.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledgerable_events.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledgerable_events.with_raw_response.retrieve(
                "",
            )


class TestAsyncLedgerableEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledgerable_event = await async_client.ledgerable_events.create(
            name="name",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledgerable_event = await async_client.ledgerable_events.create(
            name="name",
            custom_data={},
            description="description",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledgerable_events.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledgerable_events.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = await response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledgerable_event = await async_client.ledgerable_events.retrieve(
            "id",
        )
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledgerable_events.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledgerable_event = response.parse()
        assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledgerable_events.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledgerable_event = await response.parse()
            assert_matches_type(LedgerableEvent, ledgerable_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledgerable_events.with_raw_response.retrieve(
                "",
            )
