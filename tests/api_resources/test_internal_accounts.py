# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    InternalAccount,
    InternalAccountUpdateAccountCapabilityResponse,
)
from modern_treasury._utils import parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternalAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.create(
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.create(
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
            account_capabilities=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "direction": "credit",
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "identifier": "identifier",
                    "live_mode": True,
                    "object": "object",
                    "payment_type": "ach",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            account_type="checking",
            counterparty_id="counterparty_id",
            legal_entity_id="legal_entity_id",
            parent_account_id="parent_account_id",
            party_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
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
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.create(
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.retrieve(
            "id",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.retrieve(
            "id",
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
            id="id",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.update(
            id="id",
            counterparty_id="counterparty_id",
            ledger_account_id="ledger_account_id",
            metadata={"foo": "string"},
            name="name",
            parent_account_id="parent_account_id",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.update(
            id="id",
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
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.list()
        assert_matches_type(SyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            currency="AED",
            legal_entity_id="legal_entity_id",
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

    @parametrize
    def test_method_update_account_capability(self, client: ModernTreasury) -> None:
        internal_account = client.internal_accounts.update_account_capability(
            id="id",
            internal_account_id="internal_account_id",
            identifier="identifier",
        )
        assert_matches_type(InternalAccountUpdateAccountCapabilityResponse, internal_account, path=["response"])

    @parametrize
    def test_raw_response_update_account_capability(self, client: ModernTreasury) -> None:
        response = client.internal_accounts.with_raw_response.update_account_capability(
            id="id",
            internal_account_id="internal_account_id",
            identifier="identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccountUpdateAccountCapabilityResponse, internal_account, path=["response"])

    @parametrize
    def test_streaming_response_update_account_capability(self, client: ModernTreasury) -> None:
        with client.internal_accounts.with_streaming_response.update_account_capability(
            id="id",
            internal_account_id="internal_account_id",
            identifier="identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = response.parse()
            assert_matches_type(InternalAccountUpdateAccountCapabilityResponse, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_account_capability(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            client.internal_accounts.with_raw_response.update_account_capability(
                id="id",
                internal_account_id="",
                identifier="identifier",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.internal_accounts.with_raw_response.update_account_capability(
                id="",
                internal_account_id="internal_account_id",
                identifier="identifier",
            )


class TestAsyncInternalAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.create(
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.create(
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
            account_capabilities=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "direction": "credit",
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "identifier": "identifier",
                    "live_mode": True,
                    "object": "object",
                    "payment_type": "ach",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            account_type="checking",
            counterparty_id="counterparty_id",
            legal_entity_id="legal_entity_id",
            parent_account_id="parent_account_id",
            party_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
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
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.create(
            connection_id="connection_id",
            currency="USD",
            name="name",
            party_name="party_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(InternalAccount, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.retrieve(
            "id",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.retrieve(
            "id",
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
            id="id",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.update(
            id="id",
            counterparty_id="counterparty_id",
            ledger_account_id="ledger_account_id",
            metadata={"foo": "string"},
            name="name",
            parent_account_id="parent_account_id",
        )
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccount, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.update(
            id="id",
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
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.list()
        assert_matches_type(AsyncPage[InternalAccount], internal_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            currency="AED",
            legal_entity_id="legal_entity_id",
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

    @parametrize
    async def test_method_update_account_capability(self, async_client: AsyncModernTreasury) -> None:
        internal_account = await async_client.internal_accounts.update_account_capability(
            id="id",
            internal_account_id="internal_account_id",
            identifier="identifier",
        )
        assert_matches_type(InternalAccountUpdateAccountCapabilityResponse, internal_account, path=["response"])

    @parametrize
    async def test_raw_response_update_account_capability(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.internal_accounts.with_raw_response.update_account_capability(
            id="id",
            internal_account_id="internal_account_id",
            identifier="identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_account = response.parse()
        assert_matches_type(InternalAccountUpdateAccountCapabilityResponse, internal_account, path=["response"])

    @parametrize
    async def test_streaming_response_update_account_capability(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.internal_accounts.with_streaming_response.update_account_capability(
            id="id",
            internal_account_id="internal_account_id",
            identifier="identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_account = await response.parse()
            assert_matches_type(InternalAccountUpdateAccountCapabilityResponse, internal_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_account_capability(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_account_id` but received ''"):
            await async_client.internal_accounts.with_raw_response.update_account_capability(
                id="id",
                internal_account_id="",
                identifier="identifier",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.internal_accounts.with_raw_response.update_account_capability(
                id="",
                internal_account_id="internal_account_id",
                identifier="identifier",
            )
