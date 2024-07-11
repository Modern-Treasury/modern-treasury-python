# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.invoices import (
    InvoiceLineItem,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLineItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
            description="description",
            direction="direction",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            quantity=0,
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.line_items.with_raw_response.create(
                invoice_id="",
                name="name",
                unit_amount=0,
            )

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.retrieve(
            id="id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.retrieve(
            id="id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.retrieve(
            id="id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.line_items.with_raw_response.retrieve(
                id="id",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.line_items.with_raw_response.retrieve(
                id="",
                invoice_id="invoice_id",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.update(
            id="id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.update(
            id="id",
            invoice_id="invoice_id",
            description="description",
            direction="direction",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
            quantity=0,
            unit_amount=0,
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.update(
            id="id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.update(
            id="id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.line_items.with_raw_response.update(
                id="id",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.line_items.with_raw_response.update(
                id="",
                invoice_id="invoice_id",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.list(
            invoice_id="invoice_id",
        )
        assert_matches_type(SyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.list(
            invoice_id="invoice_id",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(SyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.list(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(SyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.list(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(SyncPage[InvoiceLineItem], line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.line_items.with_raw_response.list(
                invoice_id="",
            )

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.delete(
            id="id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.delete(
            id="id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.delete(
            id="id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.line_items.with_raw_response.delete(
                id="id",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.line_items.with_raw_response.delete(
                id="",
                invoice_id="invoice_id",
            )


class TestAsyncLineItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
            description="description",
            direction="direction",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            quantity=0,
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.line_items.with_raw_response.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.line_items.with_streaming_response.create(
            invoice_id="invoice_id",
            name="name",
            unit_amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.create(
                invoice_id="",
                name="name",
                unit_amount=0,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.retrieve(
            id="id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.line_items.with_raw_response.retrieve(
            id="id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.line_items.with_streaming_response.retrieve(
            id="id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.retrieve(
                id="id",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.retrieve(
                id="",
                invoice_id="invoice_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.update(
            id="id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.update(
            id="id",
            invoice_id="invoice_id",
            description="description",
            direction="direction",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
            quantity=0,
            unit_amount=0,
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.line_items.with_raw_response.update(
            id="id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.line_items.with_streaming_response.update(
            id="id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.update(
                id="id",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.update(
                id="",
                invoice_id="invoice_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.list(
            invoice_id="invoice_id",
        )
        assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.list(
            invoice_id="invoice_id",
            after_cursor="after_cursor",
            per_page=0,
        )
        assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.line_items.with_raw_response.list(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.line_items.with_streaming_response.list(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.list(
                invoice_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        line_item = await async_client.invoices.line_items.delete(
            id="id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.line_items.with_raw_response.delete(
            id="id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.line_items.with_streaming_response.delete(
            id="id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.delete(
                id="id",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.line_items.with_raw_response.delete(
                id="",
                invoice_id="invoice_id",
            )
