# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    InternalAccount,
)
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternalAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            legal_entity_id="string",
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
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.internal_accounts.with_raw_response.retrieve(
                "",
            )

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
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.internal_accounts.with_raw_response.update(
                "",
            )

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
            legal_entity_id="string",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.create(
            connection_id="string",
            currency="USD",
            name="string",
            party_name="string",
            counterparty_id="string",
            legal_entity_id="string",
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
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.with_raw_response.create(
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
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.create(
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
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.retrieve(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.internal_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.update(
            "string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.update(
            "string",
            counterparty_id="string",
            ledger_account_id="string",
            metadata={"foo": "string"},
            name="string",
            parent_account_id="string",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.internal_accounts.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.list()
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.list(
            after_cursor="string",
            counterparty_id="string",
            currency="AED",
            legal_entity_id="string",
            metadata={"foo": "string"},
            payment_direction="credit",
            payment_type="ach",
            per_page=0,
        )
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True
