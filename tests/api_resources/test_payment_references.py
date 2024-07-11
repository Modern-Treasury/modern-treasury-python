# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import PaymentReference
from modern_treasury.pagination import SyncPage, AsyncPage

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        payment_reference = client.payment_references.retrieve(
            "id",
        )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.payment_references.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.payment_references.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_reference = response.parse()
            assert_matches_type(PaymentReference, payment_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_references.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        payment_reference = client.payment_references.list()
        assert_matches_type(SyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        payment_reference = client.payment_references.list(
            after_cursor="after_cursor",
            per_page=0,
            reference_number="reference_number",
            referenceable_id="referenceable_id",
            referenceable_type="payment_order",
        )
        assert_matches_type(SyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.payment_references.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(SyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.payment_references.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_reference = response.parse()
            assert_matches_type(SyncPage[PaymentReference], payment_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retireve(self, client: ModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            payment_reference = client.payment_references.retireve(
                "id",
            )

        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    def test_raw_response_retireve(self, client: ModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.payment_references.with_raw_response.retireve(
                "id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    def test_streaming_response_retireve(self, client: ModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            with client.payment_references.with_streaming_response.retireve(
                "id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                payment_reference = response.parse()
                assert_matches_type(PaymentReference, payment_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retireve(self, client: ModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.payment_references.with_raw_response.retireve(
                    "",
                )


class TestAsyncPaymentReferences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        payment_reference = await async_client.payment_references.retrieve(
            "id",
        )
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_references.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_references.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_reference = await response.parse()
            assert_matches_type(PaymentReference, payment_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_references.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        payment_reference = await async_client.payment_references.list()
        assert_matches_type(AsyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        payment_reference = await async_client.payment_references.list(
            after_cursor="after_cursor",
            per_page=0,
            reference_number="reference_number",
            referenceable_id="referenceable_id",
            referenceable_type="payment_order",
        )
        assert_matches_type(AsyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.payment_references.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(AsyncPage[PaymentReference], payment_reference, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.payment_references.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_reference = await response.parse()
            assert_matches_type(AsyncPage[PaymentReference], payment_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retireve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            payment_reference = await async_client.payment_references.retireve(
                "id",
            )

        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    async def test_raw_response_retireve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.payment_references.with_raw_response.retireve(
                "id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_reference = response.parse()
        assert_matches_type(PaymentReference, payment_reference, path=["response"])

    @parametrize
    async def test_streaming_response_retireve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.payment_references.with_streaming_response.retireve(
                "id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                payment_reference = await response.parse()
                assert_matches_type(PaymentReference, payment_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retireve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.payment_references.with_raw_response.retireve(
                    "",
                )
