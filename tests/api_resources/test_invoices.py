# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Invoice
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"
organization_id = "my-organization-ID"


class TestInvoices:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        invoice = client.invoices.create(
            counterparty_id="string",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        invoice = client.invoices.create(
            counterparty_id="string",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="string",
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
            invoicer_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            notification_email_addresses=["string", "string", "string"],
            notifications_enabled=True,
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="string",
            recipient_name="string",
            virtual_account_id="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        invoice = client.invoices.retrieve(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        invoice = client.invoices.update(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        invoice = client.invoices.update(
            "string",
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
            notification_email_addresses=["string", "string", "string"],
            notifications_enabled=True,
            originating_account_id="string",
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="string",
            recipient_name="string",
            status="string",
            virtual_account_id="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        invoice = client.invoices.list()
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        invoice = client.invoices.list(
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_add_payment_order(self, client: ModernTreasury) -> None:
        invoice = client.invoices.add_payment_order(
            "string",
            id="string",
        )
        assert invoice is None


class TestAsyncInvoices:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=True
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, organization_id=organization_id, _strict_response_validation=False
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.create(
            counterparty_id="string",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.create(
            counterparty_id="string",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="string",
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
            invoicer_address={
                "line1": "string",
                "line2": "string",
                "locality": "string",
                "region": "string",
                "postal_code": "string",
                "country": "string",
            },
            notification_email_addresses=["string", "string", "string"],
            notifications_enabled=True,
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="string",
            recipient_name="string",
            virtual_account_id="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.retrieve(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.update(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.update(
            "string",
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
            notification_email_addresses=["string", "string", "string"],
            notifications_enabled=True,
            originating_account_id="string",
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="string",
            recipient_name="string",
            status="string",
            virtual_account_id="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.list()
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.list(
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_add_payment_order(self, client: AsyncModernTreasury) -> None:
        invoice = await client.invoices.add_payment_order(
            "string",
            id="string",
        )
        assert invoice is None
