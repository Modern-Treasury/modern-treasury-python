# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    AccountCollectionFlow,
)
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestAccountCollectionFlows:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
            receiving_countries=["USA", "AUS", "BEL"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.account_collection_flows.with_raw_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.account_collection_flows.with_streaming_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.retrieve(
            "string",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.account_collection_flows.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.account_collection_flows.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.update(
            "string",
            status="cancelled",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.account_collection_flows.with_raw_response.update(
            "string",
            status="cancelled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.account_collection_flows.with_streaming_response.update(
            "string",
            status="cancelled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.list()
        assert_matches_type(SyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.list(
            after_cursor="string",
            client_token="string",
            counterparty_id="string",
            external_account_id="string",
            per_page=0,
            status="string",
        )
        assert_matches_type(SyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.account_collection_flows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(SyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.account_collection_flows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = response.parse()
            assert_matches_type(SyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountCollectionFlows:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
            receiving_countries=["USA", "AUS", "BEL"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.account_collection_flows.with_raw_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.account_collection_flows.with_streaming_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.retrieve(
            "string",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.account_collection_flows.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.account_collection_flows.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.update(
            "string",
            status="cancelled",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.account_collection_flows.with_raw_response.update(
            "string",
            status="cancelled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncModernTreasury) -> None:
        async with client.account_collection_flows.with_streaming_response.update(
            "string",
            status="cancelled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.list()
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        account_collection_flow = await client.account_collection_flows.list(
            after_cursor="string",
            client_token="string",
            counterparty_id="string",
            external_account_id="string",
            per_page=0,
            status="string",
        )
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.account_collection_flows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncModernTreasury) -> None:
        async with client.account_collection_flows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True
