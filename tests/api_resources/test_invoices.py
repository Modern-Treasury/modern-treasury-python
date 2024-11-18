# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    Invoice,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        invoice = client.invoices.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        invoice = client.invoices.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
            auto_advance=True,
            contact_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "contact_identifier": "contact_identifier",
                    "contact_identifier_type": "email",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            counterparty_billing_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            counterparty_shipping_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            currency="AED",
            description="description",
            fallback_payment_method="fallback_payment_method",
            ingest_ledger_entries=True,
            invoice_line_items=[
                {
                    "name": "name",
                    "unit_amount": 0,
                    "description": "description",
                    "direction": "direction",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "quantity": 0,
                    "unit_amount_decimal": "unit_amount_decimal",
                }
            ],
            invoicer_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            ledger_account_settlement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            notification_email_addresses=["string"],
            notifications_enabled=True,
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="recipient_email",
            recipient_name="recipient_name",
            remind_after_overdue_days=[0],
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.invoices.with_raw_response.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.invoices.with_streaming_response.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        invoice = client.invoices.retrieve(
            "id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.invoices.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.invoices.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        invoice = client.invoices.update(
            id="id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        invoice = client.invoices.update(
            id="id",
            contact_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "contact_identifier": "contact_identifier",
                    "contact_identifier_type": "email",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            counterparty_billing_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            counterparty_id="counterparty_id",
            counterparty_shipping_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            currency="AED",
            description="description",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_payment_method="fallback_payment_method",
            ingest_ledger_entries=True,
            invoice_line_items=[
                {
                    "name": "name",
                    "unit_amount": 0,
                    "description": "description",
                    "direction": "direction",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "quantity": 0,
                    "unit_amount_decimal": "unit_amount_decimal",
                }
            ],
            invoicer_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            ledger_account_settlement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            notification_email_addresses=["string"],
            notifications_enabled=True,
            originating_account_id="originating_account_id",
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="recipient_email",
            recipient_name="recipient_name",
            remind_after_overdue_days=[0],
            status="status",
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.invoices.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.invoices.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        invoice = client.invoices.list()
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        invoice = client.invoices.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            due_date_end=parse_date("2019-12-27"),
            due_date_start=parse_date("2019-12-27"),
            expected_payment_id="expected_payment_id",
            metadata={"foo": "string"},
            number="number",
            originating_account_id="originating_account_id",
            payment_order_id="payment_order_id",
            per_page=0,
            status="draft",
        )
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_payment_order(self, client: ModernTreasury) -> None:
        invoice = client.invoices.add_payment_order(
            payment_order_id="payment_order_id",
            id="id",
        )
        assert invoice is None

    @parametrize
    def test_raw_response_add_payment_order(self, client: ModernTreasury) -> None:
        response = client.invoices.with_raw_response.add_payment_order(
            payment_order_id="payment_order_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @parametrize
    def test_streaming_response_add_payment_order(self, client: ModernTreasury) -> None:
        with client.invoices.with_streaming_response.add_payment_order(
            payment_order_id="payment_order_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_payment_order(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.add_payment_order(
                payment_order_id="payment_order_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            client.invoices.with_raw_response.add_payment_order(
                payment_order_id="",
                id="id",
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
            auto_advance=True,
            contact_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "contact_identifier": "contact_identifier",
                    "contact_identifier_type": "email",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            counterparty_billing_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            counterparty_shipping_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            currency="AED",
            description="description",
            fallback_payment_method="fallback_payment_method",
            ingest_ledger_entries=True,
            invoice_line_items=[
                {
                    "name": "name",
                    "unit_amount": 0,
                    "description": "description",
                    "direction": "direction",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "quantity": 0,
                    "unit_amount_decimal": "unit_amount_decimal",
                }
            ],
            invoicer_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            ledger_account_settlement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            notification_email_addresses=["string"],
            notifications_enabled=True,
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="recipient_email",
            recipient_name="recipient_name",
            remind_after_overdue_days=[0],
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.with_raw_response.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.with_streaming_response.create(
            counterparty_id="counterparty_id",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            originating_account_id="originating_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.retrieve(
            "id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.update(
            id="id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.update(
            id="id",
            contact_details=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "contact_identifier": "contact_identifier",
                    "contact_identifier_type": "email",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            counterparty_billing_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            counterparty_id="counterparty_id",
            counterparty_shipping_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            currency="AED",
            description="description",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            fallback_payment_method="fallback_payment_method",
            ingest_ledger_entries=True,
            invoice_line_items=[
                {
                    "name": "name",
                    "unit_amount": 0,
                    "description": "description",
                    "direction": "direction",
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "quantity": 0,
                    "unit_amount_decimal": "unit_amount_decimal",
                }
            ],
            invoicer_address={
                "country": "country",
                "line1": "line1",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
                "line2": "line2",
            },
            ledger_account_settlement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            notification_email_addresses=["string"],
            notifications_enabled=True,
            originating_account_id="originating_account_id",
            payment_effective_date=parse_date("2019-12-27"),
            payment_method="ui",
            payment_type="ach",
            receiving_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recipient_email="recipient_email",
            recipient_name="recipient_name",
            remind_after_overdue_days=[0],
            status="status",
            virtual_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.list()
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            due_date_end=parse_date("2019-12-27"),
            due_date_start=parse_date("2019-12-27"),
            expected_payment_id="expected_payment_id",
            metadata={"foo": "string"},
            number="number",
            originating_account_id="originating_account_id",
            payment_order_id="payment_order_id",
            per_page=0,
            status="draft",
        )
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_payment_order(self, async_client: AsyncModernTreasury) -> None:
        invoice = await async_client.invoices.add_payment_order(
            payment_order_id="payment_order_id",
            id="id",
        )
        assert invoice is None

    @parametrize
    async def test_raw_response_add_payment_order(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.invoices.with_raw_response.add_payment_order(
            payment_order_id="payment_order_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @parametrize
    async def test_streaming_response_add_payment_order(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.invoices.with_streaming_response.add_payment_order(
            payment_order_id="payment_order_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_payment_order(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.add_payment_order(
                payment_order_id="payment_order_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_order_id` but received ''"):
            await async_client.invoices.with_raw_response.add_payment_order(
                payment_order_id="",
                id="id",
            )
