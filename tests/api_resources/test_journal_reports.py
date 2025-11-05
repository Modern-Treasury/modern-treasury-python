# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJournalReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        journal_report = client.journal_reports.retrieve(
            "id",
        )
        assert journal_report is None

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.journal_reports.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_report = response.parse()
        assert journal_report is None

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.journal_reports.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_report = response.parse()
            assert journal_report is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.journal_reports.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        journal_report = client.journal_reports.update(
            id="id",
        )
        assert journal_report is None

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        journal_report = client.journal_reports.update(
            id="id",
            metadata={},
            status="status",
        )
        assert journal_report is None

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.journal_reports.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_report = response.parse()
        assert journal_report is None

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.journal_reports.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_report = response.parse()
            assert journal_report is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.journal_reports.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        journal_report = client.journal_reports.list()
        assert journal_report is None

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.journal_reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_report = response.parse()
        assert journal_report is None

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.journal_reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_report = response.parse()
            assert journal_report is None

        assert cast(Any, response.is_closed) is True


class TestAsyncJournalReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        journal_report = await async_client.journal_reports.retrieve(
            "id",
        )
        assert journal_report is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.journal_reports.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_report = response.parse()
        assert journal_report is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.journal_reports.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_report = await response.parse()
            assert journal_report is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.journal_reports.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        journal_report = await async_client.journal_reports.update(
            id="id",
        )
        assert journal_report is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        journal_report = await async_client.journal_reports.update(
            id="id",
            metadata={},
            status="status",
        )
        assert journal_report is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.journal_reports.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_report = response.parse()
        assert journal_report is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.journal_reports.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_report = await response.parse()
            assert journal_report is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.journal_reports.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        journal_report = await async_client.journal_reports.list()
        assert journal_report is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.journal_reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_report = response.parse()
        assert journal_report is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.journal_reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_report = await response.parse()
            assert journal_report is None

        assert cast(Any, response.is_closed) is True
