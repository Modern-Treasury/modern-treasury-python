# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LedgerEventHandlerListResponse,
    LedgerEventHandlerCreateResponse,
    LedgerEventHandlerDeleteResponse,
    LedgerEventHandlerRetrieveResponse,
)
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgerEventHandlers:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "string",
                "effective_at": "string",
                "ledger_entries": [
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            name="string",
        )
        assert_matches_type(LedgerEventHandlerCreateResponse, ledger_event_handler, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "string",
                "effective_at": "string",
                "ledger_entries": [
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            name="string",
            conditions={
                "field": "string",
                "operator": "string",
                "value": "string",
            },
            description="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerEventHandlerCreateResponse, ledger_event_handler, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.retrieve(
            "string",
        )
        assert_matches_type(LedgerEventHandlerRetrieveResponse, ledger_event_handler, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.list()
        assert_matches_type(SyncPage[LedgerEventHandlerListResponse], ledger_event_handler, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.list(
            after_cursor="string",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            metadata={"foo": "string"},
            name="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[LedgerEventHandlerListResponse], ledger_event_handler, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_event_handler = client.ledger_event_handlers.delete(
            "string",
        )
        assert_matches_type(LedgerEventHandlerDeleteResponse, ledger_event_handler, path=["response"])


class TestAsyncLedgerEventHandlers:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_event_handler = await client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "string",
                "effective_at": "string",
                "ledger_entries": [
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            name="string",
        )
        assert_matches_type(LedgerEventHandlerCreateResponse, ledger_event_handler, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_event_handler = await client.ledger_event_handlers.create(
            ledger_transaction_template={
                "description": "string",
                "effective_at": "string",
                "ledger_entries": [
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                    {
                        "amount": "string",
                        "direction": "string",
                        "ledger_account_id": "string",
                    },
                ],
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            name="string",
            conditions={
                "field": "string",
                "operator": "string",
                "value": "string",
            },
            description="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerEventHandlerCreateResponse, ledger_event_handler, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_event_handler = await client.ledger_event_handlers.retrieve(
            "string",
        )
        assert_matches_type(LedgerEventHandlerRetrieveResponse, ledger_event_handler, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_event_handler = await client.ledger_event_handlers.list()
        assert_matches_type(AsyncPage[LedgerEventHandlerListResponse], ledger_event_handler, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_event_handler = await client.ledger_event_handlers.list(
            after_cursor="string",
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            metadata={"foo": "string"},
            name="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[LedgerEventHandlerListResponse], ledger_event_handler, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        ledger_event_handler = await client.ledger_event_handlers.delete(
            "string",
        )
        assert_matches_type(LedgerEventHandlerDeleteResponse, ledger_event_handler, path=["response"])
