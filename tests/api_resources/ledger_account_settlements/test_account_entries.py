# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        account_entry = client.ledger_account_settlements.account_entries.update(
            id="id",
            ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert account_entry is None

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.ledger_account_settlements.account_entries.with_raw_response.update(
            id="id",
            ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_entry = response.parse()
        assert account_entry is None

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.ledger_account_settlements.account_entries.with_streaming_response.update(
            id="id",
            ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_entry = response.parse()
            assert account_entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_settlements.account_entries.with_raw_response.update(
                id="",
                ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        account_entry = client.ledger_account_settlements.account_entries.delete(
            id="id",
            ledger_entry_ids=[{}],
        )
        assert account_entry is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.ledger_account_settlements.account_entries.with_raw_response.delete(
            id="id",
            ledger_entry_ids=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_entry = response.parse()
        assert account_entry is None

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.ledger_account_settlements.account_entries.with_streaming_response.delete(
            id="id",
            ledger_entry_ids=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_entry = response.parse()
            assert account_entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_account_settlements.account_entries.with_raw_response.delete(
                id="",
                ledger_entry_ids=[{}],
            )


class TestAsyncAccountEntries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        account_entry = await async_client.ledger_account_settlements.account_entries.update(
            id="id",
            ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert account_entry is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_settlements.account_entries.with_raw_response.update(
            id="id",
            ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_entry = response.parse()
        assert account_entry is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_settlements.account_entries.with_streaming_response.update(
            id="id",
            ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_entry = await response.parse()
            assert account_entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_settlements.account_entries.with_raw_response.update(
                id="",
                ledger_entry_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        account_entry = await async_client.ledger_account_settlements.account_entries.delete(
            id="id",
            ledger_entry_ids=[{}],
        )
        assert account_entry is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.ledger_account_settlements.account_entries.with_raw_response.delete(
            id="id",
            ledger_entry_ids=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_entry = response.parse()
        assert account_entry is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.ledger_account_settlements.account_entries.with_streaming_response.delete(
            id="id",
            ledger_entry_ids=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_entry = await response.parse()
            assert account_entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_account_settlements.account_entries.with_raw_response.delete(
                id="",
                ledger_entry_ids=[{}],
            )
