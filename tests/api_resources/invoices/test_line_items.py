# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.invoices import InvoiceLineItem

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLineItems:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
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
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.retrieve(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

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
            contact_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "contact_identifier": "string",
                    "contact_identifier_type": "email",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "contact_identifier": "string",
                    "contact_identifier_type": "email",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "contact_identifier": "string",
                    "contact_identifier_type": "email",
                },
            ],
            counterparty_billing_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            counterparty_id="string",
            counterparty_shipping_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="AED",
            description="string",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoicer_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            originating_account_id="string",
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

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
    def test_method_delete(self, client: ModernTreasury) -> None:
        line_item = client.invoices.line_items.delete(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])


class TestAsyncLineItems:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
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
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.retrieve(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

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
            contact_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "contact_identifier": "string",
                    "contact_identifier_type": "email",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "contact_identifier": "string",
                    "contact_identifier_type": "email",
                },
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "object": "string",
                    "live_mode": True,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "contact_identifier": "string",
                    "contact_identifier_type": "email",
                },
            ],
            counterparty_billing_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            counterparty_id="string",
            counterparty_shipping_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="AED",
            description="string",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoicer_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            originating_account_id="string",
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])

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
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        line_item = await client.invoices.line_items.delete(
            "string",
            invoice_id="string",
        )
        assert_matches_type(InvoiceLineItem, line_item, path=["response"])
