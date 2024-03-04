# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import (
    PaymentOrder,
    PaymentOrderType,
    PaymentOrderSubtype,
    payment_order_list_params,
    payment_order_create_params,
    payment_order_update_params,
    payment_order_create_async_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ..._compat import cached_property
from .reversals import (
    Reversals,
    AsyncReversals,
    ReversalsWithRawResponse,
    AsyncReversalsWithRawResponse,
    ReversalsWithStreamingResponse,
    AsyncReversalsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.shared import Currency, AsyncResponse, TransactionDirection

__all__ = ["PaymentOrders", "AsyncPaymentOrders"]


class PaymentOrders(SyncAPIResource):
    @cached_property
    def reversals(self) -> Reversals:
        return Reversals(self._client)

    @cached_property
    def with_raw_response(self) -> PaymentOrdersWithRawResponse:
        return PaymentOrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentOrdersWithStreamingResponse:
        return PaymentOrdersWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        type: PaymentOrderType,
        accounting: payment_order_create_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        documents: Iterable[payment_order_create_params.Document] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        line_items: Iterable[payment_order_create_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        subtype: Optional[PaymentOrderSubtype] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentOrder:
        """
        Create a new Payment Order

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          originating_account_id: The ID of one of your organization's internal accounts.

          type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
              `sic`, `signet`, `provexchange`, `zengin`.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          currency: Defaults to the currency of the originating account.

          description: An optional description for internal use.

          documents: An array of documents to be attached to the payment order. Note that if you
              attach documents, the request's content type must be `multipart/form-data`.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          ledger_transaction_id: Either ledger_transaction or ledger_transaction_id can be provided. Only a
              pending ledger transaction can be attached upon payment order creation. Once the
              payment order is created, the status of the ledger transaction tracks the
              payment order automatically.

          line_items: An array of line items that must sum up to the amount of the payment order.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after: If present, Modern Treasury will not process the payment until after this time.
              If `process_after` is past the cutoff for `effective_date`, `process_after` will
              take precedence and `effective_date` will automatically update to reflect the
              earliest possible sending date after `process_after`. Format is ISO8601
              timestamp.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "amount": amount,
                "direction": direction,
                "originating_account_id": originating_account_id,
                "type": type,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "charge_bearer": charge_bearer,
                "currency": currency,
                "description": description,
                "documents": documents,
                "effective_date": effective_date,
                "expires_at": expires_at,
                "fallback_type": fallback_type,
                "foreign_exchange_contract": foreign_exchange_contract,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "ledger_transaction": ledger_transaction,
                "ledger_transaction_id": ledger_transaction_id,
                "line_items": line_items,
                "metadata": metadata,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "priority": priority,
                "process_after": process_after,
                "purpose": purpose,
                "receiving_account": receiving_account,
                "receiving_account_id": receiving_account_id,
                "remittance_information": remittance_information,
                "send_remittance_advice": send_remittance_advice,
                "statement_descriptor": statement_descriptor,
                "subtype": subtype,
                "transaction_monitoring_enabled": transaction_monitoring_enabled,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["documents", "<array>", "file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/payment_orders",
            body=maybe_transform(body, payment_order_create_params.PaymentOrderCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentOrder,
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
    ) -> PaymentOrder:
        """
        Get details on a single payment order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/payment_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentOrder,
        )

    def update(
        self,
        id: str,
        *,
        accounting: payment_order_update_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        line_items: Iterable[payment_order_update_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_update_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal[
            "approved",
            "cancelled",
            "completed",
            "denied",
            "failed",
            "needs_approval",
            "pending",
            "processing",
            "returned",
            "reversed",
            "sent",
        ]
        | NotGiven = NOT_GIVEN,
        subtype: Optional[PaymentOrderSubtype] | NotGiven = NOT_GIVEN,
        type: PaymentOrderType | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentOrder:
        """
        Update a payment order

        Args:
          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          counterparty_id: Required when receiving_account_id is passed the ID of an external account.

          currency: Defaults to the currency of the originating account.

          description: An optional description for internal use.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          line_items: An array of line items that must sum up to the amount of the payment order.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_account_id: The ID of one of your organization's internal accounts.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after: If present, Modern Treasury will not process the payment until after this time.
              If `process_after` is past the cutoff for `effective_date`, `process_after` will
              take precedence and `effective_date` will automatically update to reflect the
              earliest possible sending date after `process_after`. Format is ISO8601
              timestamp.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          status: To cancel a payment order, use `cancelled`. To redraft a returned payment order,
              use `approved`. To undo approval on a denied or approved payment order, use
              `needs_approval`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
              `sic`, `signet`, `provexchange`, `zengin`.

          ultimate_originating_party_identifier: This represents the identifier by which the person is known to the receiver when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_originating_party_name: This represents the name of the person that the payment is on behalf of when
              using the CIE subtype for ACH payments. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_identifier: This represents the name of the merchant that the payment is being sent to when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_name: This represents the identifier by which the merchant is known to the person
              initiating an ACH payment with CIE subtype. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/payment_orders/{id}",
            body=maybe_transform(
                {
                    "accounting": accounting,
                    "accounting_category_id": accounting_category_id,
                    "accounting_ledger_class_id": accounting_ledger_class_id,
                    "amount": amount,
                    "charge_bearer": charge_bearer,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "description": description,
                    "direction": direction,
                    "effective_date": effective_date,
                    "expires_at": expires_at,
                    "fallback_type": fallback_type,
                    "foreign_exchange_contract": foreign_exchange_contract,
                    "foreign_exchange_indicator": foreign_exchange_indicator,
                    "line_items": line_items,
                    "metadata": metadata,
                    "nsf_protected": nsf_protected,
                    "originating_account_id": originating_account_id,
                    "originating_party_name": originating_party_name,
                    "priority": priority,
                    "process_after": process_after,
                    "purpose": purpose,
                    "receiving_account": receiving_account,
                    "receiving_account_id": receiving_account_id,
                    "remittance_information": remittance_information,
                    "send_remittance_advice": send_remittance_advice,
                    "statement_descriptor": statement_descriptor,
                    "status": status,
                    "subtype": subtype,
                    "type": type,
                    "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                    "ultimate_originating_party_name": ultimate_originating_party_name,
                    "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                    "ultimate_receiving_party_name": ultimate_receiving_party_name,
                },
                payment_order_update_params.PaymentOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentOrder,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        created_at_end: Union[str, date] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, date] | NotGiven = NOT_GIVEN,
        direction: TransactionDirection | NotGiven = NOT_GIVEN,
        effective_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        effective_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        process_after_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        reference_number: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "approved",
            "cancelled",
            "completed",
            "denied",
            "failed",
            "needs_approval",
            "pending",
            "processing",
            "returned",
            "reversed",
            "sent",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "hu_ics",
            "interac",
            "masav",
            "mx_ccen",
            "neft",
            "nics",
            "nz_becs",
            "pl_elixir",
            "provxchange",
            "ro_sent",
            "rtp",
            "se_bankgirot",
            "sen",
            "sepa",
            "sg_giro",
            "sic",
            "signet",
            "sknbi",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PaymentOrder]:
        """
        Get a list of all payment orders

        Args:
          created_at_end: An inclusive upper bound for searching created_at

          created_at_start: An inclusive lower bound for searching created_at

          effective_date_end: An inclusive upper bound for searching effective_date

          effective_date_start: An inclusive lower bound for searching effective_date

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after_end: An inclusive upper bound for searching process_after

          process_after_start: An inclusive lower bound for searching process_after

          reference_number: Query for records with the provided reference number

          transaction_id: The ID of a transaction that the payment order has been reconciled to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_orders",
            page=SyncPage[PaymentOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "direction": direction,
                        "effective_date_end": effective_date_end,
                        "effective_date_start": effective_date_start,
                        "metadata": metadata,
                        "originating_account_id": originating_account_id,
                        "per_page": per_page,
                        "priority": priority,
                        "process_after_end": process_after_end,
                        "process_after_start": process_after_start,
                        "reference_number": reference_number,
                        "status": status,
                        "transaction_id": transaction_id,
                        "type": type,
                    },
                    payment_order_list_params.PaymentOrderListParams,
                ),
            ),
            model=PaymentOrder,
        )

    def create_async(
        self,
        *,
        amount: int,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        type: PaymentOrderType,
        accounting: payment_order_create_async_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_async_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        line_items: Iterable[payment_order_create_async_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_async_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        subtype: Optional[PaymentOrderSubtype] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AsyncResponse:
        """
        Create a new payment order asynchronously

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          originating_account_id: The ID of one of your organization's internal accounts.

          type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
              `sic`, `signet`, `provexchange`, `zengin`.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          currency: Defaults to the currency of the originating account.

          description: An optional description for internal use.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          ledger_transaction_id: Either ledger_transaction or ledger_transaction_id can be provided. Only a
              pending ledger transaction can be attached upon payment order creation. Once the
              payment order is created, the status of the ledger transaction tracks the
              payment order automatically.

          line_items: An array of line items that must sum up to the amount of the payment order.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after: If present, Modern Treasury will not process the payment until after this time.
              If `process_after` is past the cutoff for `effective_date`, `process_after` will
              take precedence and `effective_date` will automatically update to reflect the
              earliest possible sending date after `process_after`. Format is ISO8601
              timestamp.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/payment_orders/create_async",
            body=maybe_transform(
                {
                    "amount": amount,
                    "direction": direction,
                    "originating_account_id": originating_account_id,
                    "type": type,
                    "accounting": accounting,
                    "accounting_category_id": accounting_category_id,
                    "accounting_ledger_class_id": accounting_ledger_class_id,
                    "charge_bearer": charge_bearer,
                    "currency": currency,
                    "description": description,
                    "effective_date": effective_date,
                    "expires_at": expires_at,
                    "fallback_type": fallback_type,
                    "foreign_exchange_contract": foreign_exchange_contract,
                    "foreign_exchange_indicator": foreign_exchange_indicator,
                    "ledger_transaction": ledger_transaction,
                    "ledger_transaction_id": ledger_transaction_id,
                    "line_items": line_items,
                    "metadata": metadata,
                    "nsf_protected": nsf_protected,
                    "originating_party_name": originating_party_name,
                    "priority": priority,
                    "process_after": process_after,
                    "purpose": purpose,
                    "receiving_account": receiving_account,
                    "receiving_account_id": receiving_account_id,
                    "remittance_information": remittance_information,
                    "send_remittance_advice": send_remittance_advice,
                    "statement_descriptor": statement_descriptor,
                    "subtype": subtype,
                    "transaction_monitoring_enabled": transaction_monitoring_enabled,
                    "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                    "ultimate_originating_party_name": ultimate_originating_party_name,
                    "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                    "ultimate_receiving_party_name": ultimate_receiving_party_name,
                },
                payment_order_create_async_params.PaymentOrderCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AsyncResponse,
        )


class AsyncPaymentOrders(AsyncAPIResource):
    @cached_property
    def reversals(self) -> AsyncReversals:
        return AsyncReversals(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPaymentOrdersWithRawResponse:
        return AsyncPaymentOrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentOrdersWithStreamingResponse:
        return AsyncPaymentOrdersWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        type: PaymentOrderType,
        accounting: payment_order_create_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        documents: Iterable[payment_order_create_params.Document] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        line_items: Iterable[payment_order_create_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        subtype: Optional[PaymentOrderSubtype] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentOrder:
        """
        Create a new Payment Order

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          originating_account_id: The ID of one of your organization's internal accounts.

          type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
              `sic`, `signet`, `provexchange`, `zengin`.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          currency: Defaults to the currency of the originating account.

          description: An optional description for internal use.

          documents: An array of documents to be attached to the payment order. Note that if you
              attach documents, the request's content type must be `multipart/form-data`.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          ledger_transaction_id: Either ledger_transaction or ledger_transaction_id can be provided. Only a
              pending ledger transaction can be attached upon payment order creation. Once the
              payment order is created, the status of the ledger transaction tracks the
              payment order automatically.

          line_items: An array of line items that must sum up to the amount of the payment order.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after: If present, Modern Treasury will not process the payment until after this time.
              If `process_after` is past the cutoff for `effective_date`, `process_after` will
              take precedence and `effective_date` will automatically update to reflect the
              earliest possible sending date after `process_after`. Format is ISO8601
              timestamp.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "amount": amount,
                "direction": direction,
                "originating_account_id": originating_account_id,
                "type": type,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "charge_bearer": charge_bearer,
                "currency": currency,
                "description": description,
                "documents": documents,
                "effective_date": effective_date,
                "expires_at": expires_at,
                "fallback_type": fallback_type,
                "foreign_exchange_contract": foreign_exchange_contract,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "ledger_transaction": ledger_transaction,
                "ledger_transaction_id": ledger_transaction_id,
                "line_items": line_items,
                "metadata": metadata,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "priority": priority,
                "process_after": process_after,
                "purpose": purpose,
                "receiving_account": receiving_account,
                "receiving_account_id": receiving_account_id,
                "remittance_information": remittance_information,
                "send_remittance_advice": send_remittance_advice,
                "statement_descriptor": statement_descriptor,
                "subtype": subtype,
                "transaction_monitoring_enabled": transaction_monitoring_enabled,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["documents", "<array>", "file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/payment_orders",
            body=await async_maybe_transform(body, payment_order_create_params.PaymentOrderCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentOrder,
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
    ) -> PaymentOrder:
        """
        Get details on a single payment order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/payment_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentOrder,
        )

    async def update(
        self,
        id: str,
        *,
        accounting: payment_order_update_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        line_items: Iterable[payment_order_update_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_update_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal[
            "approved",
            "cancelled",
            "completed",
            "denied",
            "failed",
            "needs_approval",
            "pending",
            "processing",
            "returned",
            "reversed",
            "sent",
        ]
        | NotGiven = NOT_GIVEN,
        subtype: Optional[PaymentOrderSubtype] | NotGiven = NOT_GIVEN,
        type: PaymentOrderType | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PaymentOrder:
        """
        Update a payment order

        Args:
          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          counterparty_id: Required when receiving_account_id is passed the ID of an external account.

          currency: Defaults to the currency of the originating account.

          description: An optional description for internal use.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          line_items: An array of line items that must sum up to the amount of the payment order.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_account_id: The ID of one of your organization's internal accounts.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after: If present, Modern Treasury will not process the payment until after this time.
              If `process_after` is past the cutoff for `effective_date`, `process_after` will
              take precedence and `effective_date` will automatically update to reflect the
              earliest possible sending date after `process_after`. Format is ISO8601
              timestamp.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          status: To cancel a payment order, use `cancelled`. To redraft a returned payment order,
              use `approved`. To undo approval on a denied or approved payment order, use
              `needs_approval`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
              `sic`, `signet`, `provexchange`, `zengin`.

          ultimate_originating_party_identifier: This represents the identifier by which the person is known to the receiver when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_originating_party_name: This represents the name of the person that the payment is on behalf of when
              using the CIE subtype for ACH payments. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_identifier: This represents the name of the merchant that the payment is being sent to when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_name: This represents the identifier by which the merchant is known to the person
              initiating an ACH payment with CIE subtype. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/payment_orders/{id}",
            body=await async_maybe_transform(
                {
                    "accounting": accounting,
                    "accounting_category_id": accounting_category_id,
                    "accounting_ledger_class_id": accounting_ledger_class_id,
                    "amount": amount,
                    "charge_bearer": charge_bearer,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "description": description,
                    "direction": direction,
                    "effective_date": effective_date,
                    "expires_at": expires_at,
                    "fallback_type": fallback_type,
                    "foreign_exchange_contract": foreign_exchange_contract,
                    "foreign_exchange_indicator": foreign_exchange_indicator,
                    "line_items": line_items,
                    "metadata": metadata,
                    "nsf_protected": nsf_protected,
                    "originating_account_id": originating_account_id,
                    "originating_party_name": originating_party_name,
                    "priority": priority,
                    "process_after": process_after,
                    "purpose": purpose,
                    "receiving_account": receiving_account,
                    "receiving_account_id": receiving_account_id,
                    "remittance_information": remittance_information,
                    "send_remittance_advice": send_remittance_advice,
                    "statement_descriptor": statement_descriptor,
                    "status": status,
                    "subtype": subtype,
                    "type": type,
                    "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                    "ultimate_originating_party_name": ultimate_originating_party_name,
                    "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                    "ultimate_receiving_party_name": ultimate_receiving_party_name,
                },
                payment_order_update_params.PaymentOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentOrder,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        created_at_end: Union[str, date] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, date] | NotGiven = NOT_GIVEN,
        direction: TransactionDirection | NotGiven = NOT_GIVEN,
        effective_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        effective_date_start: Union[str, date] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        process_after_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        reference_number: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "approved",
            "cancelled",
            "completed",
            "denied",
            "failed",
            "needs_approval",
            "pending",
            "processing",
            "returned",
            "reversed",
            "sent",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "hu_ics",
            "interac",
            "masav",
            "mx_ccen",
            "neft",
            "nics",
            "nz_becs",
            "pl_elixir",
            "provxchange",
            "ro_sent",
            "rtp",
            "se_bankgirot",
            "sen",
            "sepa",
            "sg_giro",
            "sic",
            "signet",
            "sknbi",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PaymentOrder, AsyncPage[PaymentOrder]]:
        """
        Get a list of all payment orders

        Args:
          created_at_end: An inclusive upper bound for searching created_at

          created_at_start: An inclusive lower bound for searching created_at

          effective_date_end: An inclusive upper bound for searching effective_date

          effective_date_start: An inclusive lower bound for searching effective_date

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after_end: An inclusive upper bound for searching process_after

          process_after_start: An inclusive lower bound for searching process_after

          reference_number: Query for records with the provided reference number

          transaction_id: The ID of a transaction that the payment order has been reconciled to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_orders",
            page=AsyncPage[PaymentOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "direction": direction,
                        "effective_date_end": effective_date_end,
                        "effective_date_start": effective_date_start,
                        "metadata": metadata,
                        "originating_account_id": originating_account_id,
                        "per_page": per_page,
                        "priority": priority,
                        "process_after_end": process_after_end,
                        "process_after_start": process_after_start,
                        "reference_number": reference_number,
                        "status": status,
                        "transaction_id": transaction_id,
                        "type": type,
                    },
                    payment_order_list_params.PaymentOrderListParams,
                ),
            ),
            model=PaymentOrder,
        )

    async def create_async(
        self,
        *,
        amount: int,
        direction: Literal["credit", "debit"],
        originating_account_id: str,
        type: PaymentOrderType,
        accounting: payment_order_create_async_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_async_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        ledger_transaction_id: str | NotGiven = NOT_GIVEN,
        line_items: Iterable[payment_order_create_async_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        process_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_async_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        subtype: Optional[PaymentOrderSubtype] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AsyncResponse:
        """
        Create a new payment order asynchronously

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          originating_account_id: The ID of one of your organization's internal accounts.

          type: One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
              `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
              `sic`, `signet`, `provexchange`, `zengin`.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          currency: Defaults to the currency of the originating account.

          description: An optional description for internal use.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          ledger_transaction_id: Either ledger_transaction or ledger_transaction_id can be provided. Only a
              pending ledger transaction can be attached upon payment order creation. Once the
              payment order is created, the status of the ledger transaction tracks the
              payment order automatically.

          line_items: An array of line items that must sum up to the amount of the payment order.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          process_after: If present, Modern Treasury will not process the payment until after this time.
              If `process_after` is past the cutoff for `effective_date`, `process_after` will
              take precedence and `effective_date` will automatically update to reflect the
              earliest possible sending date after `process_after`. Format is ISO8601
              timestamp.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/payment_orders/create_async",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "direction": direction,
                    "originating_account_id": originating_account_id,
                    "type": type,
                    "accounting": accounting,
                    "accounting_category_id": accounting_category_id,
                    "accounting_ledger_class_id": accounting_ledger_class_id,
                    "charge_bearer": charge_bearer,
                    "currency": currency,
                    "description": description,
                    "effective_date": effective_date,
                    "expires_at": expires_at,
                    "fallback_type": fallback_type,
                    "foreign_exchange_contract": foreign_exchange_contract,
                    "foreign_exchange_indicator": foreign_exchange_indicator,
                    "ledger_transaction": ledger_transaction,
                    "ledger_transaction_id": ledger_transaction_id,
                    "line_items": line_items,
                    "metadata": metadata,
                    "nsf_protected": nsf_protected,
                    "originating_party_name": originating_party_name,
                    "priority": priority,
                    "process_after": process_after,
                    "purpose": purpose,
                    "receiving_account": receiving_account,
                    "receiving_account_id": receiving_account_id,
                    "remittance_information": remittance_information,
                    "send_remittance_advice": send_remittance_advice,
                    "statement_descriptor": statement_descriptor,
                    "subtype": subtype,
                    "transaction_monitoring_enabled": transaction_monitoring_enabled,
                    "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                    "ultimate_originating_party_name": ultimate_originating_party_name,
                    "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                    "ultimate_receiving_party_name": ultimate_receiving_party_name,
                },
                payment_order_create_async_params.PaymentOrderCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AsyncResponse,
        )


class PaymentOrdersWithRawResponse:
    def __init__(self, payment_orders: PaymentOrders) -> None:
        self._payment_orders = payment_orders

        self.create = _legacy_response.to_raw_response_wrapper(
            payment_orders.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            payment_orders.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            payment_orders.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            payment_orders.list,
        )
        self.create_async = _legacy_response.to_raw_response_wrapper(
            payment_orders.create_async,
        )

    @cached_property
    def reversals(self) -> ReversalsWithRawResponse:
        return ReversalsWithRawResponse(self._payment_orders.reversals)


class AsyncPaymentOrdersWithRawResponse:
    def __init__(self, payment_orders: AsyncPaymentOrders) -> None:
        self._payment_orders = payment_orders

        self.create = _legacy_response.async_to_raw_response_wrapper(
            payment_orders.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            payment_orders.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            payment_orders.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            payment_orders.list,
        )
        self.create_async = _legacy_response.async_to_raw_response_wrapper(
            payment_orders.create_async,
        )

    @cached_property
    def reversals(self) -> AsyncReversalsWithRawResponse:
        return AsyncReversalsWithRawResponse(self._payment_orders.reversals)


class PaymentOrdersWithStreamingResponse:
    def __init__(self, payment_orders: PaymentOrders) -> None:
        self._payment_orders = payment_orders

        self.create = to_streamed_response_wrapper(
            payment_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            payment_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            payment_orders.list,
        )
        self.create_async = to_streamed_response_wrapper(
            payment_orders.create_async,
        )

    @cached_property
    def reversals(self) -> ReversalsWithStreamingResponse:
        return ReversalsWithStreamingResponse(self._payment_orders.reversals)


class AsyncPaymentOrdersWithStreamingResponse:
    def __init__(self, payment_orders: AsyncPaymentOrders) -> None:
        self._payment_orders = payment_orders

        self.create = async_to_streamed_response_wrapper(
            payment_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            payment_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_orders.list,
        )
        self.create_async = async_to_streamed_response_wrapper(
            payment_orders.create_async,
        )

    @cached_property
    def reversals(self) -> AsyncReversalsWithStreamingResponse:
        return AsyncReversalsWithStreamingResponse(self._payment_orders.reversals)
