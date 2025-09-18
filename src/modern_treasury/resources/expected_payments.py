# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    ExpectedPaymentType,
    expected_payment_list_params,
    expected_payment_create_params,
    expected_payment_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.currency import Currency
from ..types.expected_payment import ExpectedPayment
from ..types.expected_payment_type import ExpectedPaymentType
from ..types.reconciliation_rule_param import ReconciliationRuleParam
from ..types.shared.transaction_direction import TransactionDirection
from ..types.shared_params.ledger_transaction_create_request import LedgerTransactionCreateRequest

__all__ = ["ExpectedPayments", "AsyncExpectedPayments"]


class ExpectedPayments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExpectedPaymentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return ExpectedPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpectedPaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return ExpectedPaymentsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount_lower_bound: Optional[int] | Omit = omit,
        amount_upper_bound: Optional[int] | Omit = omit,
        counterparty_id: Optional[str] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        date_lower_bound: Union[str, date, None] | Omit = omit,
        date_upper_bound: Union[str, date, None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        direction: Optional[Literal["credit", "debit"]] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        internal_account_id: Optional[str] | Omit = omit,
        ledger_transaction: LedgerTransactionCreateRequest | Omit = omit,
        ledger_transaction_id: str | Omit = omit,
        line_items: Iterable[expected_payment_create_params.LineItem] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reconciliation_filters: Optional[object] | Omit = omit,
        reconciliation_groups: Optional[object] | Omit = omit,
        reconciliation_rule_variables: Optional[Iterable[ReconciliationRuleParam]] | Omit = omit,
        remittance_information: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        type: Optional[ExpectedPaymentType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        create expected payment

        Args:
          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          counterparty_id: The ID of the counterparty you expect for this payment.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          external_id: An optional user-defined 180 character unique identifier.

          internal_account_id: The ID of the Internal Account for the expected payment.

          ledger_transaction: Specifies a ledger transaction object that will be created with the expected
              payment. If the ledger transaction cannot be created, then the expected payment
              creation will fail. The resulting ledger transaction will mirror the status of
              the expected payment.

          ledger_transaction_id: Either ledger_transaction or ledger_transaction_id can be provided. Only a
              pending ledger transaction can be attached upon expected payment creation. Once
              the expected payment is created, the status of the ledger transaction tracks the
              expected payment automatically.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

          reconciliation_rule_variables: An array of reconciliation rule variables for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/expected_payments",
            body=maybe_transform(
                {
                    "amount_lower_bound": amount_lower_bound,
                    "amount_upper_bound": amount_upper_bound,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "date_lower_bound": date_lower_bound,
                    "date_upper_bound": date_upper_bound,
                    "description": description,
                    "direction": direction,
                    "external_id": external_id,
                    "internal_account_id": internal_account_id,
                    "ledger_transaction": ledger_transaction,
                    "ledger_transaction_id": ledger_transaction_id,
                    "line_items": line_items,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
                    "reconciliation_rule_variables": reconciliation_rule_variables,
                    "remittance_information": remittance_information,
                    "statement_descriptor": statement_descriptor,
                    "type": type,
                },
                expected_payment_create_params.ExpectedPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExpectedPayment,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpectedPayment:
        """
        get expected payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/expected_payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpectedPayment,
        )

    def update(
        self,
        id: str,
        *,
        amount_lower_bound: Optional[int] | Omit = omit,
        amount_upper_bound: Optional[int] | Omit = omit,
        counterparty_id: Optional[str] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        date_lower_bound: Union[str, date, None] | Omit = omit,
        date_upper_bound: Union[str, date, None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        direction: Optional[Literal["credit", "debit"]] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        internal_account_id: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reconciliation_filters: Optional[object] | Omit = omit,
        reconciliation_groups: Optional[object] | Omit = omit,
        reconciliation_rule_variables: Optional[Iterable[ReconciliationRuleParam]] | Omit = omit,
        remittance_information: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        status: Optional[Literal["reconciled"]] | Omit = omit,
        type: Optional[ExpectedPaymentType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        update expected payment

        Args:
          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          counterparty_id: The ID of the counterparty you expect for this payment.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          external_id: An optional user-defined 180 character unique identifier.

          internal_account_id: The ID of the Internal Account for the expected payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

          reconciliation_rule_variables: An array of reconciliation rule variables for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          status: The Expected Payment's status can be updated from partially_reconciled to
              reconciled.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/expected_payments/{id}",
            body=maybe_transform(
                {
                    "amount_lower_bound": amount_lower_bound,
                    "amount_upper_bound": amount_upper_bound,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "date_lower_bound": date_lower_bound,
                    "date_upper_bound": date_upper_bound,
                    "description": description,
                    "direction": direction,
                    "external_id": external_id,
                    "internal_account_id": internal_account_id,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
                    "reconciliation_rule_variables": reconciliation_rule_variables,
                    "remittance_information": remittance_information,
                    "statement_descriptor": statement_descriptor,
                    "status": status,
                    "type": type,
                },
                expected_payment_update_params.ExpectedPaymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExpectedPayment,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        counterparty_id: str | Omit = omit,
        created_at_lower_bound: Union[str, datetime] | Omit = omit,
        created_at_upper_bound: Union[str, datetime] | Omit = omit,
        direction: TransactionDirection | Omit = omit,
        external_id: str | Omit = omit,
        internal_account_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["archived", "partially_reconciled", "reconciled", "unreconciled"] | Omit = omit,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "base",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "ethereum",
            "gb_fps",
            "hu_ics",
            "interac",
            "masav",
            "mx_ccen",
            "neft",
            "nics",
            "nz_becs",
            "pl_elixir",
            "polygon",
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
            "solana",
            "wire",
            "zengin",
        ]
        | Omit = omit,
        updated_at_lower_bound: Union[str, datetime] | Omit = omit,
        updated_at_upper_bound: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ExpectedPayment]:
        """
        list expected_payments

        Args:
          counterparty_id: Specify counterparty_id to see expected_payments for a specific account.

          created_at_lower_bound: Used to return expected payments created after some datetime

          created_at_upper_bound: Used to return expected payments created before some datetime

          direction: One of credit, debit

          internal_account_id: Specify internal_account_id to see expected_payments for a specific account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: One of unreconciled, reconciled, or archived.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp,sen,
              sepa, signet, wire

          updated_at_lower_bound: Used to return expected payments updated after some datetime

          updated_at_upper_bound: Used to return expected payments updated before some datetime

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/expected_payments",
            page=SyncPage[ExpectedPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "created_at_lower_bound": created_at_lower_bound,
                        "created_at_upper_bound": created_at_upper_bound,
                        "direction": direction,
                        "external_id": external_id,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                        "updated_at_lower_bound": updated_at_lower_bound,
                        "updated_at_upper_bound": updated_at_upper_bound,
                    },
                    expected_payment_list_params.ExpectedPaymentListParams,
                ),
            ),
            model=ExpectedPayment,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        delete expected payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/expected_payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExpectedPayment,
        )


class AsyncExpectedPayments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExpectedPaymentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpectedPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpectedPaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncExpectedPaymentsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount_lower_bound: Optional[int] | Omit = omit,
        amount_upper_bound: Optional[int] | Omit = omit,
        counterparty_id: Optional[str] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        date_lower_bound: Union[str, date, None] | Omit = omit,
        date_upper_bound: Union[str, date, None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        direction: Optional[Literal["credit", "debit"]] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        internal_account_id: Optional[str] | Omit = omit,
        ledger_transaction: LedgerTransactionCreateRequest | Omit = omit,
        ledger_transaction_id: str | Omit = omit,
        line_items: Iterable[expected_payment_create_params.LineItem] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reconciliation_filters: Optional[object] | Omit = omit,
        reconciliation_groups: Optional[object] | Omit = omit,
        reconciliation_rule_variables: Optional[Iterable[ReconciliationRuleParam]] | Omit = omit,
        remittance_information: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        type: Optional[ExpectedPaymentType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        create expected payment

        Args:
          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          counterparty_id: The ID of the counterparty you expect for this payment.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          external_id: An optional user-defined 180 character unique identifier.

          internal_account_id: The ID of the Internal Account for the expected payment.

          ledger_transaction: Specifies a ledger transaction object that will be created with the expected
              payment. If the ledger transaction cannot be created, then the expected payment
              creation will fail. The resulting ledger transaction will mirror the status of
              the expected payment.

          ledger_transaction_id: Either ledger_transaction or ledger_transaction_id can be provided. Only a
              pending ledger transaction can be attached upon expected payment creation. Once
              the expected payment is created, the status of the ledger transaction tracks the
              expected payment automatically.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

          reconciliation_rule_variables: An array of reconciliation rule variables for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/expected_payments",
            body=await async_maybe_transform(
                {
                    "amount_lower_bound": amount_lower_bound,
                    "amount_upper_bound": amount_upper_bound,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "date_lower_bound": date_lower_bound,
                    "date_upper_bound": date_upper_bound,
                    "description": description,
                    "direction": direction,
                    "external_id": external_id,
                    "internal_account_id": internal_account_id,
                    "ledger_transaction": ledger_transaction,
                    "ledger_transaction_id": ledger_transaction_id,
                    "line_items": line_items,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
                    "reconciliation_rule_variables": reconciliation_rule_variables,
                    "remittance_information": remittance_information,
                    "statement_descriptor": statement_descriptor,
                    "type": type,
                },
                expected_payment_create_params.ExpectedPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExpectedPayment,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpectedPayment:
        """
        get expected payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/expected_payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpectedPayment,
        )

    async def update(
        self,
        id: str,
        *,
        amount_lower_bound: Optional[int] | Omit = omit,
        amount_upper_bound: Optional[int] | Omit = omit,
        counterparty_id: Optional[str] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        date_lower_bound: Union[str, date, None] | Omit = omit,
        date_upper_bound: Union[str, date, None] | Omit = omit,
        description: Optional[str] | Omit = omit,
        direction: Optional[Literal["credit", "debit"]] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        internal_account_id: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reconciliation_filters: Optional[object] | Omit = omit,
        reconciliation_groups: Optional[object] | Omit = omit,
        reconciliation_rule_variables: Optional[Iterable[ReconciliationRuleParam]] | Omit = omit,
        remittance_information: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        status: Optional[Literal["reconciled"]] | Omit = omit,
        type: Optional[ExpectedPaymentType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        update expected payment

        Args:
          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          counterparty_id: The ID of the counterparty you expect for this payment.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          external_id: An optional user-defined 180 character unique identifier.

          internal_account_id: The ID of the Internal Account for the expected payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

          reconciliation_rule_variables: An array of reconciliation rule variables for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          status: The Expected Payment's status can be updated from partially_reconciled to
              reconciled.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/expected_payments/{id}",
            body=await async_maybe_transform(
                {
                    "amount_lower_bound": amount_lower_bound,
                    "amount_upper_bound": amount_upper_bound,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "date_lower_bound": date_lower_bound,
                    "date_upper_bound": date_upper_bound,
                    "description": description,
                    "direction": direction,
                    "external_id": external_id,
                    "internal_account_id": internal_account_id,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
                    "reconciliation_rule_variables": reconciliation_rule_variables,
                    "remittance_information": remittance_information,
                    "statement_descriptor": statement_descriptor,
                    "status": status,
                    "type": type,
                },
                expected_payment_update_params.ExpectedPaymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExpectedPayment,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        counterparty_id: str | Omit = omit,
        created_at_lower_bound: Union[str, datetime] | Omit = omit,
        created_at_upper_bound: Union[str, datetime] | Omit = omit,
        direction: TransactionDirection | Omit = omit,
        external_id: str | Omit = omit,
        internal_account_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["archived", "partially_reconciled", "reconciled", "unreconciled"] | Omit = omit,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "base",
            "book",
            "card",
            "chats",
            "check",
            "cross_border",
            "dk_nets",
            "eft",
            "ethereum",
            "gb_fps",
            "hu_ics",
            "interac",
            "masav",
            "mx_ccen",
            "neft",
            "nics",
            "nz_becs",
            "pl_elixir",
            "polygon",
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
            "solana",
            "wire",
            "zengin",
        ]
        | Omit = omit,
        updated_at_lower_bound: Union[str, datetime] | Omit = omit,
        updated_at_upper_bound: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExpectedPayment, AsyncPage[ExpectedPayment]]:
        """
        list expected_payments

        Args:
          counterparty_id: Specify counterparty_id to see expected_payments for a specific account.

          created_at_lower_bound: Used to return expected payments created after some datetime

          created_at_upper_bound: Used to return expected payments created before some datetime

          direction: One of credit, debit

          internal_account_id: Specify internal_account_id to see expected_payments for a specific account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          status: One of unreconciled, reconciled, or archived.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp,sen,
              sepa, signet, wire

          updated_at_lower_bound: Used to return expected payments updated after some datetime

          updated_at_upper_bound: Used to return expected payments updated before some datetime

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/expected_payments",
            page=AsyncPage[ExpectedPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "created_at_lower_bound": created_at_lower_bound,
                        "created_at_upper_bound": created_at_upper_bound,
                        "direction": direction,
                        "external_id": external_id,
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                        "updated_at_lower_bound": updated_at_lower_bound,
                        "updated_at_upper_bound": updated_at_upper_bound,
                    },
                    expected_payment_list_params.ExpectedPaymentListParams,
                ),
            ),
            model=ExpectedPayment,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        delete expected payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/expected_payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExpectedPayment,
        )


class ExpectedPaymentsWithRawResponse:
    def __init__(self, expected_payments: ExpectedPayments) -> None:
        self._expected_payments = expected_payments

        self.create = _legacy_response.to_raw_response_wrapper(
            expected_payments.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            expected_payments.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            expected_payments.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            expected_payments.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            expected_payments.delete,
        )


class AsyncExpectedPaymentsWithRawResponse:
    def __init__(self, expected_payments: AsyncExpectedPayments) -> None:
        self._expected_payments = expected_payments

        self.create = _legacy_response.async_to_raw_response_wrapper(
            expected_payments.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            expected_payments.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            expected_payments.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            expected_payments.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            expected_payments.delete,
        )


class ExpectedPaymentsWithStreamingResponse:
    def __init__(self, expected_payments: ExpectedPayments) -> None:
        self._expected_payments = expected_payments

        self.create = to_streamed_response_wrapper(
            expected_payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            expected_payments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            expected_payments.update,
        )
        self.list = to_streamed_response_wrapper(
            expected_payments.list,
        )
        self.delete = to_streamed_response_wrapper(
            expected_payments.delete,
        )


class AsyncExpectedPaymentsWithStreamingResponse:
    def __init__(self, expected_payments: AsyncExpectedPayments) -> None:
        self._expected_payments = expected_payments

        self.create = async_to_streamed_response_wrapper(
            expected_payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            expected_payments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            expected_payments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            expected_payments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            expected_payments.delete,
        )
