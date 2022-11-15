# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..types import expected_payment_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.expected_payment import ExpectedPayment

__all__ = ["ExpectedPayments", "AsyncExpectedPayments"]


class ExpectedPayments(SyncAPIResource):
    def create(
        self,
        *,
        amount_upper_bound: int,
        amount_lower_bound: int,
        direction: Literal["credit", "debit"],
        internal_account_id: str,
        type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "cross_border",
                "eft",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_upper_bound: Optional[str] | NotGiven = NOT_GIVEN,
        date_lower_bound: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        line_items: List[expected_payment_create_params.LineItems] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExpectedPayment:
        """
        Args:
          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          internal_account_id: The ID of the Internal Account for the expected payment.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          counterparty_id: The ID of the counterparty you expect for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/api/expected_payments",
            body={
                "amount_upper_bound": amount_upper_bound,
                "amount_lower_bound": amount_lower_bound,
                "direction": direction,
                "internal_account_id": internal_account_id,
                "type": type,
                "currency": currency,
                "date_upper_bound": date_upper_bound,
                "date_lower_bound": date_lower_bound,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "metadata": metadata,
                "counterparty_id": counterparty_id,
                "remittance_information": remittance_information,
                "line_items": line_items,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> ExpectedPayment:
        return self._get(
            f"/api/expected_payments/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExpectedPayment,
        )

    def update(
        self,
        id: str,
        *,
        amount_upper_bound: int | NotGiven = NOT_GIVEN,
        amount_lower_bound: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "cross_border",
                "eft",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_upper_bound: Optional[str] | NotGiven = NOT_GIVEN,
        date_lower_bound: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExpectedPayment:
        """
        Args:
          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          internal_account_id: The ID of the Internal Account for the expected payment.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          counterparty_id: The ID of the counterparty you expect for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/api/expected_payments/{id}",
            body={
                "amount_upper_bound": amount_upper_bound,
                "amount_lower_bound": amount_lower_bound,
                "direction": direction,
                "internal_account_id": internal_account_id,
                "type": type,
                "currency": currency,
                "date_upper_bound": date_upper_bound,
                "date_lower_bound": date_lower_bound,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "metadata": metadata,
                "counterparty_id": counterparty_id,
                "remittance_information": remittance_information,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExpectedPayment,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["archived", "reconciled", "unreconciled"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
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
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: str | NotGiven = NOT_GIVEN,
        created_at_upper_bound: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[ExpectedPayment]:
        """
        Args:
          status: One of unreconciled, reconciled, or archived.

          internal_account_id: Specify internal_account_id to see expected_payments for a specific account.

          direction: One of credit, debit

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp,sen,
              sepa, signet, wire

          counterparty_id: Specify counterparty_id to see expected_payments for a specific account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          created_at_lower_bound: Used to return expected payments created after some datetime

          created_at_upper_bound: Used to return expected payments created before some datetime

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/expected_payments",
            page=SyncPage[ExpectedPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "status": status,
                    "internal_account_id": internal_account_id,
                    "direction": direction,
                    "type": type,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                    "created_at_lower_bound": created_at_lower_bound,
                    "created_at_upper_bound": created_at_upper_bound,
                },
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
    ) -> ExpectedPayment:
        return self._delete(
            f"/api/expected_payments/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExpectedPayment,
        )


class AsyncExpectedPayments(AsyncAPIResource):
    async def create(
        self,
        *,
        amount_upper_bound: int,
        amount_lower_bound: int,
        direction: Literal["credit", "debit"],
        internal_account_id: str,
        type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "cross_border",
                "eft",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_upper_bound: Optional[str] | NotGiven = NOT_GIVEN,
        date_lower_bound: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        line_items: List[expected_payment_create_params.LineItems] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExpectedPayment:
        """
        Args:
          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          internal_account_id: The ID of the Internal Account for the expected payment.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          counterparty_id: The ID of the counterparty you expect for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/api/expected_payments",
            body={
                "amount_upper_bound": amount_upper_bound,
                "amount_lower_bound": amount_lower_bound,
                "direction": direction,
                "internal_account_id": internal_account_id,
                "type": type,
                "currency": currency,
                "date_upper_bound": date_upper_bound,
                "date_lower_bound": date_lower_bound,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "metadata": metadata,
                "counterparty_id": counterparty_id,
                "remittance_information": remittance_information,
                "line_items": line_items,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> ExpectedPayment:
        return await self._get(
            f"/api/expected_payments/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExpectedPayment,
        )

    async def update(
        self,
        id: str,
        *,
        amount_upper_bound: int | NotGiven = NOT_GIVEN,
        amount_lower_bound: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "cross_border",
                "eft",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_upper_bound: Optional[str] | NotGiven = NOT_GIVEN,
        date_lower_bound: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExpectedPayment:
        """
        Args:
          amount_upper_bound: The highest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          amount_lower_bound: The lowest amount this expected payment may be equal to. Value in specified
              currency's smallest unit. e.g. $10 would be represented as 1000.

          direction: One of credit or debit. When you are receiving money, use credit. When you are
              being charged, use debit.

          internal_account_id: The ID of the Internal Account for the expected payment.

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
              sepa, signet, wire.

          currency: Must conform to ISO 4217. Defaults to the currency of the internal account.

          date_upper_bound: The latest date the payment may come in. Format: yyyy-mm-dd

          date_lower_bound: The earliest date the payment may come in. Format: yyyy-mm-dd

          description: An optional description for internal use.

          statement_descriptor: The statement description you expect to see on the transaction. For ACH
              payments, this will be the full line item passed from the bank. For wire
              payments, this will be the OBI field on the wire. For check payments, this will
              be the memo field.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          counterparty_id: The ID of the counterparty you expect for this payment.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/api/expected_payments/{id}",
            body={
                "amount_upper_bound": amount_upper_bound,
                "amount_lower_bound": amount_lower_bound,
                "direction": direction,
                "internal_account_id": internal_account_id,
                "type": type,
                "currency": currency,
                "date_upper_bound": date_upper_bound,
                "date_lower_bound": date_lower_bound,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "metadata": metadata,
                "counterparty_id": counterparty_id,
                "remittance_information": remittance_information,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExpectedPayment,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["archived", "reconciled", "unreconciled"] | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
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
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: str | NotGiven = NOT_GIVEN,
        created_at_upper_bound: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[ExpectedPayment, AsyncPage[ExpectedPayment]]:
        """
        Args:
          status: One of unreconciled, reconciled, or archived.

          internal_account_id: Specify internal_account_id to see expected_payments for a specific account.

          direction: One of credit, debit

          type: One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp,sen,
              sepa, signet, wire

          counterparty_id: Specify counterparty_id to see expected_payments for a specific account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          created_at_lower_bound: Used to return expected payments created after some datetime

          created_at_upper_bound: Used to return expected payments created before some datetime

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/expected_payments",
            page=AsyncPage[ExpectedPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "status": status,
                    "internal_account_id": internal_account_id,
                    "direction": direction,
                    "type": type,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                    "created_at_lower_bound": created_at_lower_bound,
                    "created_at_upper_bound": created_at_upper_bound,
                },
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
    ) -> ExpectedPayment:
        return await self._delete(
            f"/api/expected_payments/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExpectedPayment,
        )
