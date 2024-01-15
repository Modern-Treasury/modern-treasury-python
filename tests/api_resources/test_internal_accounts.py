# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    InternalAccount,
)
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestInternalAccounts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
            counterparty_id="string",
            parent_account_id="string",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            vendor_attributes={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.with_raw_response.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.retrieve(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.update(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.update(
            "string",
            counterparty_id="string",
            ledger_account_id="string",
            metadata={"foo": "string"},
            name="string",
            parent_account_id="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.list()
        assert_matches_type(SyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.list(
            after_cursor="string",
            counterparty_id="string",
            currency="AED",
            metadata={"foo": "string"},
            payment_direction="credit",
            payment_type="ach",
            per_page=0,
        )
        assert_matches_type(SyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(SyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = response.parse()
            assert_matches_type(SyncPage[InternalAccount], internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInternalAccounts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
            counterparty_id="string",
            parent_account_id="string",
            party_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            vendor_attributes={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.with_raw_response.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.with_streaming_response.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.retrieve(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.update(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.update(
            "string",
            counterparty_id="string",
            ledger_account_id="string",
            metadata={"foo": "string"},
            name="string",
            parent_account_id="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.list()
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        internal_account = await client.internal_accounts.list(
            after_cursor="string",
            counterparty_id="string",
            currency="AED",
            metadata={"foo": "string"},
            payment_direction="credit",
            payment_type="ach",
            per_page=0,
        )
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.internal_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncModernTreasury) -> None:
        async with client.internal_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True
