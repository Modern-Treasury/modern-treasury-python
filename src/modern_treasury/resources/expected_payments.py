# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..types import (
    ExpectedPayment,
    ExpectedPaymentType,
    shared_params,
    expected_payment_list_params,
    expected_payment_create_params,
    expected_payment_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["ExpectedPayments", "AsyncExpectedPayments"]


class ExpectedPayments(SyncAPIResource):
    def create(
        self,
        *,
        amount_lower_bound: int,
        amount_upper_bound: int,
        direction: Literal["credit", "debit"],
        internal_account_id: str,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        date_lower_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_upper_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        line_items: List[expected_payment_create_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        reconciliation_filters: Optional[object] | NotGiven = NOT_GIVEN,
        reconciliation_groups: Optional[object] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[ExpectedPaymentType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        create expected payment

        Args:
          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          internal_account_id: The ID of the Internal Account for the expected payment.

          counterparty_id: The ID of the counterparty you expect for this payment.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

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
                    "direction": direction,
                    "internal_account_id": internal_account_id,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "date_lower_bound": date_lower_bound,
                    "date_upper_bound": date_upper_bound,
                    "description": description,
                    "line_items": line_items,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ExpectedPayment:
        """
        get expected payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        amount_lower_bound: int | NotGiven = NOT_GIVEN,
        amount_upper_bound: int | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        date_lower_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_upper_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        reconciliation_filters: Optional[object] | NotGiven = NOT_GIVEN,
        reconciliation_groups: Optional[object] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[ExpectedPaymentType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          internal_account_id: The ID of the Internal Account for the expected payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

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
                    "internal_account_id": internal_account_id,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
                    "remittance_information": remittance_information,
                    "statement_descriptor": statement_descriptor,
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
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        created_at_lower_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_upper_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["archived", "partially_reconciled", "reconciled", "unreconciled"] | NotGiven = NOT_GIVEN,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "masav",
            "neft",
            "nics",
            "provxchange",
            "rtp",
            "se_bankgirot",
            "sen",
            "sepa",
            "sic",
            "signet",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def create(
        self,
        *,
        amount_lower_bound: int,
        amount_upper_bound: int,
        direction: Literal["credit", "debit"],
        internal_account_id: str,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        date_lower_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_upper_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        line_items: List[expected_payment_create_params.LineItem] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        reconciliation_filters: Optional[object] | NotGiven = NOT_GIVEN,
        reconciliation_groups: Optional[object] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[ExpectedPaymentType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExpectedPayment:
        """
        create expected payment

        Args:
          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          internal_account_id: The ID of the Internal Account for the expected payment.

          counterparty_id: The ID of the counterparty you expect for this payment.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

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
            body=maybe_transform(
                {
                    "amount_lower_bound": amount_lower_bound,
                    "amount_upper_bound": amount_upper_bound,
                    "direction": direction,
                    "internal_account_id": internal_account_id,
                    "counterparty_id": counterparty_id,
                    "currency": currency,
                    "date_lower_bound": date_lower_bound,
                    "date_upper_bound": date_upper_bound,
                    "description": description,
                    "line_items": line_items,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ExpectedPayment:
        """
        get expected payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        amount_lower_bound: int | NotGiven = NOT_GIVEN,
        amount_upper_bound: int | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        date_lower_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_upper_bound: Union[str, date, None] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        reconciliation_filters: Optional[object] | NotGiven = NOT_GIVEN,
        reconciliation_groups: Optional[object] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[ExpectedPaymentType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          internal_account_id: The ID of the Internal Account for the expected payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          reconciliation_filters: The reconciliation filters you have for this payment.

          reconciliation_groups: The reconciliation groups you have for this payment.

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
        return await self._patch(
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
                    "internal_account_id": internal_account_id,
                    "metadata": metadata,
                    "reconciliation_filters": reconciliation_filters,
                    "reconciliation_groups": reconciliation_groups,
                    "remittance_information": remittance_information,
                    "statement_descriptor": statement_descriptor,
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
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        created_at_lower_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_upper_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["archived", "partially_reconciled", "reconciled", "unreconciled"] | NotGiven = NOT_GIVEN,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "masav",
            "neft",
            "nics",
            "provxchange",
            "rtp",
            "se_bankgirot",
            "sen",
            "sepa",
            "sic",
            "signet",
            "wire",
            "zengin",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
                        "internal_account_id": internal_account_id,
                        "metadata": metadata,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
