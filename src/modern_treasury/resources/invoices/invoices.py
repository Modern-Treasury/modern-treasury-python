# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...types import (
    Invoice,
    shared_params,
    invoice_list_params,
    invoice_create_params,
    invoice_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from .line_items import LineItems, AsyncLineItems
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import ModernTreasury, AsyncModernTreasury

__all__ = ["Invoices", "AsyncInvoices"]


class Invoices(SyncAPIResource):
    line_items: LineItems

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.line_items = LineItems(client)

    def create(
        self,
        *,
        counterparty_id: str,
        due_date: Union[str, datetime],
        originating_account_id: str,
        contact_details: List[invoice_create_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_create_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_create_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_create_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: Literal[
            "ach",
            "au_becs",
            "se_bankgirot",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "cross_border",
            "interac",
            "masav",
            "neft",
            "nics",
            "provxchange",
            "rtp",
            "sen",
            "sic",
            "sepa",
            "signet",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        create invoice

        Args:
          counterparty_id: The ID of the counterparty receiving the invoice.

          due_date: A future date by when the invoice needs to be paid.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          invoicer_address: The invoice issuer's business address.

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

          payment_type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `sic`, `signet`, `provexchange`,
              `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

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
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "invoicer_address": invoicer_address,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Invoice:
        """
        get invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        contact_details: List[invoice_update_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_update_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_update_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_update_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: Literal[
            "ach",
            "au_becs",
            "se_bankgirot",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "cross_border",
            "interac",
            "masav",
            "neft",
            "nics",
            "provxchange",
            "rtp",
            "sen",
            "sic",
            "sepa",
            "signet",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          invoicer_address: The invoice issuer's business address.

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

          payment_type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `sic`, `signet`, `provexchange`,
              `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

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
                    "invoicer_address": invoicer_address,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "originating_account_id": originating_account_id,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
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
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Invoice]:
        """
        list invoices

        Args:
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
                        "per_page": per_page,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    line_items: AsyncLineItems

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.line_items = AsyncLineItems(client)

    async def create(
        self,
        *,
        counterparty_id: str,
        due_date: Union[str, datetime],
        originating_account_id: str,
        contact_details: List[invoice_create_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_create_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_create_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_create_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: Literal[
            "ach",
            "au_becs",
            "se_bankgirot",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "cross_border",
            "interac",
            "masav",
            "neft",
            "nics",
            "provxchange",
            "rtp",
            "sen",
            "sic",
            "sepa",
            "signet",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        create invoice

        Args:
          counterparty_id: The ID of the counterparty receiving the invoice.

          due_date: A future date by when the invoice needs to be paid.

          originating_account_id: The ID of the internal account the invoice should be paid to.

          contact_details: The invoicer's contact details displayed at the top of the invoice.

          counterparty_billing_address: The counterparty's billing address.

          counterparty_shipping_address: The counterparty's shipping address where physical goods should be delivered.

          currency: Currency that the invoice is denominated in. Defaults to `USD` if not provided.

          description: A free-form description of the invoice.

          invoicer_address: The invoice issuer's business address.

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

          payment_type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `sic`, `signet`, `provexchange`,
              `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          virtual_account_id: The ID of the virtual account the invoice should be paid to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/invoices",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "due_date": due_date,
                    "originating_account_id": originating_account_id,
                    "contact_details": contact_details,
                    "counterparty_billing_address": counterparty_billing_address,
                    "counterparty_shipping_address": counterparty_shipping_address,
                    "currency": currency,
                    "description": description,
                    "invoicer_address": invoicer_address,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Invoice:
        """
        get invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        contact_details: List[invoice_update_params.ContactDetail] | NotGiven = NOT_GIVEN,
        counterparty_billing_address: Optional[invoice_update_params.CounterpartyBillingAddress] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        counterparty_shipping_address: Optional[invoice_update_params.CounterpartyShippingAddress]
        | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoicer_address: Optional[invoice_update_params.InvoicerAddress] | NotGiven = NOT_GIVEN,
        notification_email_addresses: Optional[List[str]] | NotGiven = NOT_GIVEN,
        notifications_enabled: bool | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        payment_method: Literal["ui", "manual", "automatic"] | NotGiven = NOT_GIVEN,
        payment_type: Literal[
            "ach",
            "au_becs",
            "se_bankgirot",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "cross_border",
            "interac",
            "masav",
            "neft",
            "nics",
            "provxchange",
            "rtp",
            "sen",
            "sic",
            "sepa",
            "signet",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        recipient_email: Optional[str] | NotGiven = NOT_GIVEN,
        recipient_name: Optional[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          invoicer_address: The invoice issuer's business address.

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

          payment_type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `sic`, `signet`, `provexchange`,
              `zengin`.

          receiving_account_id: The receiving account ID. Can be an `external_account`.

          recipient_email: The email of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

          recipient_name: The name of the recipient of the invoice. Leaving this value as null will
              fallback to using the counterparty's name.

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
        return await self._patch(
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
                    "invoicer_address": invoicer_address,
                    "notification_email_addresses": notification_email_addresses,
                    "notifications_enabled": notifications_enabled,
                    "originating_account_id": originating_account_id,
                    "payment_effective_date": payment_effective_date,
                    "payment_method": payment_method,
                    "payment_type": payment_type,
                    "receiving_account_id": receiving_account_id,
                    "recipient_email": recipient_email,
                    "recipient_name": recipient_name,
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
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Invoice, AsyncPage[Invoice]]:
        """
        list invoices

        Args:
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
                        "per_page": per_page,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
