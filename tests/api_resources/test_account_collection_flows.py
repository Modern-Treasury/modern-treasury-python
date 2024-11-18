# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    AccountCollectionFlow,
)
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountCollectionFlows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
            receiving_countries=["USA"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.account_collection_flows.with_raw_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.account_collection_flows.with_streaming_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.retrieve(
            "id",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.account_collection_flows.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.account_collection_flows.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.account_collection_flows.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.update(
            id="id",
            status="cancelled",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.account_collection_flows.with_raw_response.update(
            id="id",
            status="cancelled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.account_collection_flows.with_streaming_response.update(
            id="id",
            status="cancelled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.account_collection_flows.with_raw_response.update(
                id="",
                status="cancelled",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.list()
        assert_matches_type(SyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        account_collection_flow = client.account_collection_flows.list(
            after_cursor="after_cursor",
            client_token="client_token",
            counterparty_id="counterparty_id",
            external_account_id="external_account_id",
            per_page=0,
            status="status",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        account_collection_flow = await async_client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        account_collection_flow = await async_client.account_collection_flows.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
            receiving_countries=["USA"],
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_collection_flows.with_raw_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_collection_flows.with_streaming_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_types=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        account_collection_flow = await async_client.account_collection_flows.retrieve(
            "id",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_collection_flows.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_collection_flows.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.account_collection_flows.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        account_collection_flow = await async_client.account_collection_flows.update(
            id="id",
            status="cancelled",
        )
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_collection_flows.with_raw_response.update(
            id="id",
            status="cancelled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_collection_flows.with_streaming_response.update(
            id="id",
            status="cancelled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AccountCollectionFlow, account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.account_collection_flows.with_raw_response.update(
                id="",
                status="cancelled",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        account_collection_flow = await async_client.account_collection_flows.list()
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        account_collection_flow = await async_client.account_collection_flows.list(
            after_cursor="after_cursor",
            client_token="client_token",
            counterparty_id="counterparty_id",
            external_account_id="external_account_id",
            per_page=0,
            status="status",
        )
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_collection_flows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_collection_flow = response.parse()
        assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_collection_flows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_collection_flow = await response.parse()
            assert_matches_type(AsyncPage[AccountCollectionFlow], account_collection_flow, path=["response"])

        assert cast(Any, response.is_closed) is True
