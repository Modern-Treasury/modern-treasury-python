# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._client import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.invoices import (
    InvoiceLineItem,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestLineItems:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.create(
            "string",
            name="string",
            unit_amount=0,
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.create(
            "string",
            name="string",
            unit_amount=0,
            description="string",
            direction="string",
            quantity=0,
            unit_amount_decimal="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.create(
            "string",
            name="string",
            unit_amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.create(
            "string",
            name="string",
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
                "",
                name="string",
                unit_amount=0,
            )

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.retrieve(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.retrieve(
            "string",
            invoice_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.retrieve(
            "string",
            invoice_id="string",
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
                "string",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.line_items.with_raw_response.retrieve(
                "",
                invoice_id="string",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.update(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.update(
            "string",
            invoice_id="string",
            description="string",
            direction="string",
            name="string",
            quantity=0,
            unit_amount=0,
            unit_amount_decimal="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.update(
            "string",
            invoice_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.update(
            "string",
            invoice_id="string",
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
                "string",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.line_items.with_raw_response.update(
                "",
                invoice_id="string",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.list(
            "string",
        )
        assert_matches_type(SyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.list(
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(SyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.list(
            "string",
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
                "",
            )

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.delete(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.invoices.line_items.with_raw_response.delete(
            "string",
            invoice_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.invoices.line_items.with_streaming_response.delete(
            "string",
            invoice_id="string",
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
                "string",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.line_items.with_raw_response.delete(
                "",
                invoice_id="string",
            )


class TestAsyncLineItems:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.create(
            "string",
            name="string",
            unit_amount=0,
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.create(
            "string",
            name="string",
            unit_amount=0,
            description="string",
            direction="string",
            quantity=0,
            unit_amount_decimal="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncModernTreasury) -> None:
        response = await client.invoices.line_items.with_raw_response.create(
            "string",
            name="string",
            unit_amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncModernTreasury) -> None:
        async with client.invoices.line_items.with_streaming_response.create(
            "string",
            name="string",
            unit_amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await client.invoices.line_items.with_raw_response.create(
                "",
                name="string",
                unit_amount=0,
            )

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.retrieve(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncModernTreasury) -> None:
        response = await client.invoices.line_items.with_raw_response.retrieve(
            "string",
            invoice_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncModernTreasury) -> None:
        async with client.invoices.line_items.with_streaming_response.retrieve(
            "string",
            invoice_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await client.invoices.line_items.with_raw_response.retrieve(
                "string",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.invoices.line_items.with_raw_response.retrieve(
                "",
                invoice_id="string",
            )

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.update(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.update(
            "string",
            invoice_id="string",
            description="string",
            direction="string",
            name="string",
            quantity=0,
            unit_amount=0,
            unit_amount_decimal="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncModernTreasury) -> None:
        response = await client.invoices.line_items.with_raw_response.update(
            "string",
            invoice_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncModernTreasury) -> None:
        async with client.invoices.line_items.with_streaming_response.update(
            "string",
            invoice_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await client.invoices.line_items.with_raw_response.update(
                "string",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.invoices.line_items.with_raw_response.update(
                "",
                invoice_id="string",
            )

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.list(
            "string",
        )
        assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.list(
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncModernTreasury) -> None:
        response = await client.invoices.line_items.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncModernTreasury) -> None:
        async with client.invoices.line_items.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(AsyncPage[InvoiceLineItem], line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await client.invoices.line_items.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.delete(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncModernTreasury) -> None:
        response = await client.invoices.line_items.with_raw_response.delete(
            "string",
            invoice_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line_item = response.parse()
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, client: AsyncModernTreasury) -> None:
        async with client.invoices.line_items.with_streaming_response.delete(
            "string",
            invoice_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line_item = await response.parse()
            assert_matches_type(InvoiceLineItem, line_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await client.invoices.line_items.with_raw_response.delete(
                "string",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.invoices.line_items.with_raw_response.delete(
                "",
                invoice_id="string",
            )
