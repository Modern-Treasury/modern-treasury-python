# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import (
    PaymentOrderType,
    invoice_list_params,
    invoice_create_params,
    invoice_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .line_items import (
    LineItems,
    AsyncLineItems,
    LineItemsWithRawResponse,
    AsyncLineItemsWithRawResponse,
    LineItemsWithStreamingResponse,
    AsyncLineItemsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.invoice import Invoice
from ...types.shared.currency import Currency
from ...types.payment_order_type import PaymentOrderType

__all__ = ["Invoices", "AsyncInvoices"]


class Invoices(SyncAPIResource):
    @cached_property
    def line_items(self) -> LineItems:
        return LineItems(self._client)

    @cached_property
    def with_raw_response(self) -> InvoicesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return InvoicesWithStreamingResponse(self)

    def create(
        self,
        *,
        counterparty_id: str,
        due_date: Union[str, datetime],
        originating_account_id: str,
        auto_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        contact_details: Iterable[invoice_create_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_create_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_create_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Currency | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        fallback_payment_method: Optional[str] | NotGiven = NOT_GIVEN,
        ingest_ledger_entries: Optional[bool] | NotGiven = NOT_GIVEN,
        invoice_line_items: Optional[Iterable[invoice_create_params.InvoiceLineItem]] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_create_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: PaymentOrderType | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        remind_after_overdue_days: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        create invoice

        Args:
          counterparty_id: The ID of the counterparty receiving the invoice.

          due_date: A future date by when the invoice needs to be paid.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          auto_advance: When true, the invoice will progress to unpaid automatically and cannot be
              edited after entering that state. If the invoice fails to progress to unpaid,
              the errors will be returned and the invoice will not be created.

          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          fallback_payment_method: When payment_method is automatic, the fallback payment method to use when an
              automatic payment fails. One of `manual` or `ui`.

          ingest_ledger_entries: Whether to ingest the ledger_entries to populate the invoice line items. If this
              is false, then a line item must be provided. If this is true, line_items must be
              empty. Ignored if ledger_account_settlement_id is empty.

          invoice_line_items: An array of invoice line items. The API supports a maximum of 50 invoice line
              items per invoice. If a greater number of invoice line items is required, please
              contact support.

          invoicer_address: The invoice issuer's business address.

          ledger_account_settlement_id: The ID of the virtual account the invoice should be paid to.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          notification_email_addresses: Emails in addition to the counterparty email to send invoice status
              notifications to. At least one email is required if notifications are enabled
              and the counterparty doesn't have an email.

          notifications_enabled: If true, the invoice will send email notifications to the invoice recipients
              about invoice status changes.

          payment_effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          payment_method: The method by which the invoice can be paid. `ui` will show the embedded payment
              collection flow. `automatic` will automatically initiate payment based upon the
              account details of the receiving_account id.\nIf the invoice amount is positive,
              the automatically initiated payment order's direction will be debit. If the
              invoice amount is negative, the automatically initiated payment order's
              direction will be credit. One of `manual`, `ui`, or `automatic`.

          payment_type: One of `ach`, `se_bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`,
              `sepa`, `bacs`, `au_becs`, `interac`, `neft`, `nics`,
              `nz_national_clearing_code`, `sic`, `signet`, `provexchange`, `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          remind_after_overdue_days: Number of days after due date when overdue reminder emails will be sent out to
              invoice recipients.

          virtual_account_id: The ID of the virtual account the invoice should be paid to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/invoices",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "due_date": due_date,
                    "originating_account_id": originating_account_id,
                    "auto_advance": auto_advance,
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "fallback_payment_method": fallback_payment_method,
                    "ingest_ledger_entries": ingest_ledger_entries,
                    "invoice_line_items": invoice_line_items,
                    "invoicer_address": invoicer_address,
                    "ledger_account_settlement_id": ledger_account_settlement_id,
                    "metadata": metadata,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
                    "remind_after_overdue_days": remind_after_overdue_days,
                    "virtual_account_id": virtual_account_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invoice:
        """
        get invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def update(
        self,
        id: str,
        *,
        contact_details: Iterable[invoice_update_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_update_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_update_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Currency | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fallback_payment_method: Optional[str] | NotGiven = NOT_GIVEN,
        ingest_ledger_entries: Optional[bool] | NotGiven = NOT_GIVEN,
        invoice_line_items: Optional[Iterable[invoice_update_params.InvoiceLineItem]] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_update_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: PaymentOrderType | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        remind_after_overdue_days: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        update invoice

        Args:
          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_id: The ID of the counterparty receiving the invoice.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          due_date: A future date by when the invoice needs to be paid.

          fallback_payment_method: When payment_method is automatic, the fallback payment method to use when an
              automatic payment fails. One of `manual` or `ui`.

          ingest_ledger_entries: Whether to ingest the ledger_entries to populate the invoice line items. If this
              is false, then a line item must be provided. If this is true, line_items must be
              empty. Ignored if ledger_account_settlement_id is empty.

          invoice_line_items: An array of invoice line items. The API supports a maximum of 50 invoice line
              items per invoice. If a greater number of invoice line items is required, please
              contact support.

          invoicer_address: The invoice issuer's business address.

          ledger_account_settlement_id: The ID of the virtual account the invoice should be paid to.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          notification_email_addresses: Emails in addition to the counterparty email to send invoice status
              notifications to. At least one email is required if notifications are enabled
              and the counterparty doesn't have an email.

          notifications_enabled: If true, the invoice will send email notifications to the invoice recipients
              about invoice status changes.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          payment_effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          payment_method: The method by which the invoice can be paid. `ui` will show the embedded payment
              collection flow. `automatic` will automatically initiate payment based upon the
              account details of the receiving_account id.\nIf the invoice amount is positive,
              the automatically initiated payment order's direction will be debit. If the
              invoice amount is negative, the automatically initiated payment order's
              direction will be credit. One of `manual`, `ui`, or `automatic`.

          payment_type: One of `ach`, `se_bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`,
              `sepa`, `bacs`, `au_becs`, `interac`, `neft`, `nics`,
              `nz_national_clearing_code`, `sic`, `signet`, `provexchange`, `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          remind_after_overdue_days: Number of days after due date when overdue reminder emails will be sent out to
              invoice recipients.

          status: Invoice status must be updated in a `PATCH` request that does not modify any
              other invoice attributes. Valid state transitions are `draft` to `unpaid`,
              `draft` or `unpaid` to `voided`, and `draft` or `unpaid` to `paid`.

          virtual_account_id: The ID of the virtual account the invoice should be paid to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/invoices/{id}",
            body=maybe_transform(
                {
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_id": counterparty_id,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "due_date": due_date,
                    "fallback_payment_method": fallback_payment_method,
                    "ingest_ledger_entries": ingest_ledger_entries,
                    "invoice_line_items": invoice_line_items,
                    "invoicer_address": invoicer_address,
                    "ledger_account_settlement_id": ledger_account_settlement_id,
                    "metadata": metadata,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "originating_account_id": originating_account_id,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
                    "remind_after_overdue_days": remind_after_overdue_days,
                    "status": status,
                    "virtual_account_id": virtual_account_id,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        due_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        due_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        expected_payment_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_order_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["draft", "paid", "partially_paid", "payment_pending", "unpaid", "voided"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Invoice]:
        """
        list invoices

        Args:
          due_date_end: An inclusive upper bound for searching due_date

          due_date_start: An inclusive lower bound for searching due_date

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          number: A unique record number assigned to each invoice that is issued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/invoices",
            page=SyncPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "due_date_end": due_date_end,
                        "due_date_start": due_date_start,
                        "expected_payment_id": expected_payment_id,
                        "metadata": metadata,
                        "number": number,
                        "originating_account_id": originating_account_id,
                        "payment_order_id": payment_order_id,
                        "per_page": per_page,
                        "status": status,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    def add_payment_order(
        self,
        payment_order_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add a payment order to an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not payment_order_id:
            raise ValueError(f"Expected a non-empty value for `payment_order_id` but received {payment_order_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/invoices/{id}/payment_orders/{payment_order_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncInvoices(AsyncAPIResource):
    @cached_property
    def line_items(self) -> AsyncLineItems:
        return AsyncLineItems(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInvoicesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncInvoicesWithStreamingResponse(self)

    async def create(
        self,
        *,
        counterparty_id: str,
        due_date: Union[str, datetime],
        originating_account_id: str,
        auto_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        contact_details: Iterable[invoice_create_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_create_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_create_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Currency | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        fallback_payment_method: Optional[str] | NotGiven = NOT_GIVEN,
        ingest_ledger_entries: Optional[bool] | NotGiven = NOT_GIVEN,
        invoice_line_items: Optional[Iterable[invoice_create_params.InvoiceLineItem]] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_create_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: PaymentOrderType | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        remind_after_overdue_days: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        create invoice

        Args:
          counterparty_id: The ID of the counterparty receiving the invoice.

          due_date: A future date by when the invoice needs to be paid.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          auto_advance: When true, the invoice will progress to unpaid automatically and cannot be
              edited after entering that state. If the invoice fails to progress to unpaid,
              the errors will be returned and the invoice will not be created.

          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          fallback_payment_method: When payment_method is automatic, the fallback payment method to use when an
              automatic payment fails. One of `manual` or `ui`.

          ingest_ledger_entries: Whether to ingest the ledger_entries to populate the invoice line items. If this
              is false, then a line item must be provided. If this is true, line_items must be
              empty. Ignored if ledger_account_settlement_id is empty.

          invoice_line_items: An array of invoice line items. The API supports a maximum of 50 invoice line
              items per invoice. If a greater number of invoice line items is required, please
              contact support.

          invoicer_address: The invoice issuer's business address.

          ledger_account_settlement_id: The ID of the virtual account the invoice should be paid to.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          notification_email_addresses: Emails in addition to the counterparty email to send invoice status
              notifications to. At least one email is required if notifications are enabled
              and the counterparty doesn't have an email.

          notifications_enabled: If true, the invoice will send email notifications to the invoice recipients
              about invoice status changes.

          payment_effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          payment_method: The method by which the invoice can be paid. `ui` will show the embedded payment
              collection flow. `automatic` will automatically initiate payment based upon the
              account details of the receiving_account id.\nIf the invoice amount is positive,
              the automatically initiated payment order's direction will be debit. If the
              invoice amount is negative, the automatically initiated payment order's
              direction will be credit. One of `manual`, `ui`, or `automatic`.

          payment_type: One of `ach`, `se_bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`,
              `sepa`, `bacs`, `au_becs`, `interac`, `neft`, `nics`,
              `nz_national_clearing_code`, `sic`, `signet`, `provexchange`, `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          remind_after_overdue_days: Number of days after due date when overdue reminder emails will be sent out to
              invoice recipients.

          virtual_account_id: The ID of the virtual account the invoice should be paid to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/invoices",
            body=await async_maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "due_date": due_date,
                    "originating_account_id": originating_account_id,
                    "auto_advance": auto_advance,
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "fallback_payment_method": fallback_payment_method,
                    "ingest_ledger_entries": ingest_ledger_entries,
                    "invoice_line_items": invoice_line_items,
                    "invoicer_address": invoicer_address,
                    "ledger_account_settlement_id": ledger_account_settlement_id,
                    "metadata": metadata,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
                    "remind_after_overdue_days": remind_after_overdue_days,
                    "virtual_account_id": virtual_account_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invoice:
        """
        get invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def update(
        self,
        id: str,
        *,
        contact_details: Iterable[invoice_update_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_update_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_update_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Currency | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fallback_payment_method: Optional[str] | NotGiven = NOT_GIVEN,
        ingest_ledger_entries: Optional[bool] | NotGiven = NOT_GIVEN,
        invoice_line_items: Optional[Iterable[invoice_update_params.InvoiceLineItem]] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_update_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        ledger_account_settlement_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: PaymentOrderType | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        remind_after_overdue_days: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        update invoice

        Args:
          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_id: The ID of the counterparty receiving the invoice.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          due_date: A future date by when the invoice needs to be paid.

          fallback_payment_method: When payment_method is automatic, the fallback payment method to use when an
              automatic payment fails. One of `manual` or `ui`.

          ingest_ledger_entries: Whether to ingest the ledger_entries to populate the invoice line items. If this
              is false, then a line item must be provided. If this is true, line_items must be
              empty. Ignored if ledger_account_settlement_id is empty.

          invoice_line_items: An array of invoice line items. The API supports a maximum of 50 invoice line
              items per invoice. If a greater number of invoice line items is required, please
              contact support.

          invoicer_address: The invoice issuer's business address.

          ledger_account_settlement_id: The ID of the virtual account the invoice should be paid to.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          notification_email_addresses: Emails in addition to the counterparty email to send invoice status
              notifications to. At least one email is required if notifications are enabled
              and the counterparty doesn't have an email.

          notifications_enabled: If true, the invoice will send email notifications to the invoice recipients
              about invoice status changes.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          payment_effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          payment_method: The method by which the invoice can be paid. `ui` will show the embedded payment
              collection flow. `automatic` will automatically initiate payment based upon the
              account details of the receiving_account id.\nIf the invoice amount is positive,
              the automatically initiated payment order's direction will be debit. If the
              invoice amount is negative, the automatically initiated payment order's
              direction will be credit. One of `manual`, `ui`, or `automatic`.

          payment_type: One of `ach`, `se_bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`,
              `sepa`, `bacs`, `au_becs`, `interac`, `neft`, `nics`,
              `nz_national_clearing_code`, `sic`, `signet`, `provexchange`, `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          remind_after_overdue_days: Number of days after due date when overdue reminder emails will be sent out to
              invoice recipients.

          status: Invoice status must be updated in a `PATCH` request that does not modify any
              other invoice attributes. Valid state transitions are `draft` to `unpaid`,
              `draft` or `unpaid` to `voided`, and `draft` or `unpaid` to `paid`.

          virtual_account_id: The ID of the virtual account the invoice should be paid to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/invoices/{id}",
            body=await async_maybe_transform(
                {
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_id": counterparty_id,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "due_date": due_date,
                    "fallback_payment_method": fallback_payment_method,
                    "ingest_ledger_entries": ingest_ledger_entries,
                    "invoice_line_items": invoice_line_items,
                    "invoicer_address": invoicer_address,
                    "ledger_account_settlement_id": ledger_account_settlement_id,
                    "metadata": metadata,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "originating_account_id": originating_account_id,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
                    "remind_after_overdue_days": remind_after_overdue_days,
                    "status": status,
                    "virtual_account_id": virtual_account_id,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        due_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        due_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        expected_payment_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_order_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["draft", "paid", "partially_paid", "payment_pending", "unpaid", "voided"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Invoice, AsyncPage[Invoice]]:
        """
        list invoices

        Args:
          due_date_end: An inclusive upper bound for searching due_date

          due_date_start: An inclusive lower bound for searching due_date

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          number: A unique record number assigned to each invoice that is issued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/invoices",
            page=AsyncPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "due_date_end": due_date_end,
                        "due_date_start": due_date_start,
                        "expected_payment_id": expected_payment_id,
                        "metadata": metadata,
                        "number": number,
                        "originating_account_id": originating_account_id,
                        "payment_order_id": payment_order_id,
                        "per_page": per_page,
                        "status": status,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    async def add_payment_order(
        self,
        payment_order_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Add a payment order to an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not payment_order_id:
            raise ValueError(f"Expected a non-empty value for `payment_order_id` but received {payment_order_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/invoices/{id}/payment_orders/{payment_order_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class InvoicesWithRawResponse:
    def __init__(self, invoices: Invoices) -> None:
        self._invoices = invoices

        self.create = _legacy_response.to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            invoices.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            invoices.list,
        )
        self.add_payment_order = _legacy_response.to_raw_response_wrapper(
            invoices.add_payment_order,
        )

    @cached_property
    def line_items(self) -> LineItemsWithRawResponse:
        return LineItemsWithRawResponse(self._invoices.line_items)


class AsyncInvoicesWithRawResponse:
    def __init__(self, invoices: AsyncInvoices) -> None:
        self._invoices = invoices

        self.create = _legacy_response.async_to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            invoices.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            invoices.list,
        )
        self.add_payment_order = _legacy_response.async_to_raw_response_wrapper(
            invoices.add_payment_order,
        )

    @cached_property
    def line_items(self) -> AsyncLineItemsWithRawResponse:
        return AsyncLineItemsWithRawResponse(self._invoices.line_items)


class InvoicesWithStreamingResponse:
    def __init__(self, invoices: Invoices) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.add_payment_order = to_streamed_response_wrapper(
            invoices.add_payment_order,
        )

    @cached_property
    def line_items(self) -> LineItemsWithStreamingResponse:
        return LineItemsWithStreamingResponse(self._invoices.line_items)


class AsyncInvoicesWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoices) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.add_payment_order = async_to_streamed_response_wrapper(
            invoices.add_payment_order,
        )

    @cached_property
    def line_items(self) -> AsyncLineItemsWithStreamingResponse:
        return AsyncLineItemsWithStreamingResponse(self._invoices.line_items)
