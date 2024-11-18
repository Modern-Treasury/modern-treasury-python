# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerEventHandler,
)
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerEventHandlers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
            conditions={
                "field": "ledgerable_event.name",
                "operator": "equals",
                "value": "credit_card_swipe",
            },
            description="description",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            variables={
                "credit_account": {
                    "query": {
                        "field": "name",
                        "operator": "equals",
                        "value": "my_credit_account",
                    },
                    "type": "ledger_account",
                }
            },
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.ledger_event_handlers.with_raw_response.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.ledger_event_handlers.with_streaming_response.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = response.parse()
            assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.retrieve(
            "id",
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.ledger_event_handlers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.ledger_event_handlers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = response.parse()
            assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_event_handlers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.list()
        assert_matches_type(SyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.list(
            after_cursor="after_cursor",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            metadata={"foo": "string"},
            name="name",
            per_page=0,
        )
        assert_matches_type(SyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.ledger_event_handlers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(SyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.ledger_event_handlers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = response.parse()
            assert_matches_type(SyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.delete(
            "id",
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.ledger_event_handlers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.ledger_event_handlers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = response.parse()
            assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_event_handlers.with_raw_response.delete(
                "",
            )


class TestAsyncLedgerEventHandlers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        ledger_event_handler = await async_client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_event_handler = await async_client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
            conditions={
                "field": "ledgerable_event.name",
                "operator": "equals",
                "value": "credit_card_swipe",
            },
            description="description",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            variables={
                "credit_account": {
                    "query": {
                        "field": "name",
                        "operator": "equals",
                        "value": "my_credit_account",
                    },
                    "type": "ledger_account",
                }
            },
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_event_handlers.with_raw_response.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_event_handlers.with_streaming_response.create(
            ledger_transaction_template={
                "description": "My Ledger Transaction Template Description",
                "effective_at": "{{ledgerable_event.custom_data.effective_at}}",
                "ledger_entries": [
                    {
                        "amount": "amount",
                        "direction": "direction",
                        "ledger_account_id": "ledger_account_id",
                    }
                ],
                "status": "posted",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = await response.parse()
            assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        ledger_event_handler = await async_client.ledger_event_handlers.retrieve(
            "id",
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_event_handlers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_event_handlers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = await response.parse()
            assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_event_handlers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        ledger_event_handler = await async_client.ledger_event_handlers.list()
        assert_matches_type(AsyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        ledger_event_handler = await async_client.ledger_event_handlers.list(
            after_cursor="after_cursor",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            metadata={"foo": "string"},
            name="name",
            per_page=0,
        )
        assert_matches_type(AsyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_event_handlers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(AsyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_event_handlers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = await response.parse()
            assert_matches_type(AsyncPage[LedgerEventHandler], ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        ledger_event_handler = await async_client.ledger_event_handlers.delete(
            "id",
        )
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_event_handlers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_event_handler = response.parse()
        assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_event_handlers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_event_handler = await response.parse()
            assert_matches_type(LedgerEventHandler, ledger_event_handler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_event_handlers.with_raw_response.delete(
                "",
            )
