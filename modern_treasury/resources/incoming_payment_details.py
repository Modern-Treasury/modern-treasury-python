# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Dict, Union, Optional, cast, overload
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.incoming_payment_detail import IncomingPaymentDetail
from ..types.incoming_payment_detail_list_params import IncomingPaymentDetailListParams
from ..types.incoming_payment_detail_update_params import (
    IncomingPaymentDetailUpdateParams,
)
from ..types.incoming_payment_detail_create_async_params import (
    IncomingPaymentDetailCreateAsyncParams,
)

__all__ = ["IncomingPaymentDetails", "AsyncIncomingPaymentDetails"]


class IncomingPaymentDetails(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Get an existing Incoming Payment Detail."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/incoming_payment_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=IncomingPaymentDetail,
        )

    @overload
    def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """
        Update an existing Incoming Payment Detail.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def update(
        self,
        id: str,
        body: IncomingPaymentDetailUpdateParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Update an existing Incoming Payment Detail."""
        ...

    def update(
        self,
        id: str,
        body: IncomingPaymentDetailUpdateParams | None = None,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """
        Update an existing Incoming Payment Detail.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard IncomingPaymentDetailUpdateParams type.
            body = cast(Any, {"metadata": metadata})

        return self._patch(
            f"/api/incoming_payment_details/{id}",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=IncomingPaymentDetail,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        status: Literal["completed", "pending", "returned"] | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        as_of_date_start: str | NotGiven = NOT_GIVEN,
        as_of_date_end: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[IncomingPaymentDetail]:
        """
        Get a list of Incoming Payment Details.

        Args:
          direction: One of `credit` or `debit`.

          status: The current status of the incoming payment order. One of `pending`, `completed`,
              or `returned`.

          type: One of: `ach`, `wire`, `check`, `rtp`, `sepa`, `signet`.

          as_of_date_start: Filters incoming payment details with an as_of_date starting on or after the
              specified date (YYYY-MM-DD).

          as_of_date_end: Filters incoming payment details with an as_of_date starting on or before the
              specified date (YYYY-MM-DD).

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          virtual_account_id: If the incoming payment detail is in a virtual account, the ID of the Virtual
              Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: IncomingPaymentDetailListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[IncomingPaymentDetail]:
        """Get a list of Incoming Payment Details."""
        ...

    def list(
        self,
        query: IncomingPaymentDetailListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        status: Literal["completed", "pending", "returned"] | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        as_of_date_start: str | NotGiven = NOT_GIVEN,
        as_of_date_end: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[IncomingPaymentDetail]:
        """
        Get a list of Incoming Payment Details.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          direction: One of `credit` or `debit`.

          status: The current status of the incoming payment order. One of `pending`, `completed`,
              or `returned`.

          type: One of: `ach`, `wire`, `check`, `rtp`, `sepa`, `signet`.

          as_of_date_start: Filters incoming payment details with an as_of_date starting on or after the
              specified date (YYYY-MM-DD).

          as_of_date_end: Filters incoming payment details with an as_of_date starting on or before the
              specified date (YYYY-MM-DD).

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          virtual_account_id: If the incoming payment detail is in a virtual account, the ID of the Virtual
              Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard IncomingPaymentDetailListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "direction": direction,
                    "status": status,
                    "type": type,
                    "as_of_date_start": as_of_date_start,
                    "as_of_date_end": as_of_date_end,
                    "metadata": metadata,
                    "virtual_account_id": virtual_account_id,
                },
            )

        return self._get_api_list(
            "/api/incoming_payment_details",
            page=SyncPage[IncomingPaymentDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=IncomingPaymentDetail,
        )

    @overload
    def create_async(
        self,
        *,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
        internal_account_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """
        Simulate Incoming Payment Detail

        Args:
          type: One of `ach`, `wire`, `check`.

          direction: One of `credit`, `debit`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          currency: Defaults to the currency of the originating account.

          internal_account_id: The ID of one of your internal accounts.

          virtual_account_id: An optional parameter to associate the incoming payment detail to a virtual
              account.

          as_of_date: Defaults to today.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create_async(
        self,
        body: IncomingPaymentDetailCreateAsyncParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Simulate Incoming Payment Detail"""
        ...

    def create_async(
        self,
        body: IncomingPaymentDetailCreateAsyncParams | None = None,
        *,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
        internal_account_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """
        Simulate Incoming Payment Detail

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          type: One of `ach`, `wire`, `check`.

          direction: One of `credit`, `debit`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          currency: Defaults to the currency of the originating account.

          internal_account_id: The ID of one of your internal accounts.

          virtual_account_id: An optional parameter to associate the incoming payment detail to a virtual
              account.

          as_of_date: Defaults to today.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard IncomingPaymentDetailCreateAsyncParams type.
            body = cast(
                Any,
                {
                    "type": type,
                    "direction": direction,
                    "amount": amount,
                    "currency": currency,
                    "internal_account_id": internal_account_id,
                    "virtual_account_id": virtual_account_id,
                    "as_of_date": as_of_date,
                },
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/simulations/incoming_payment_details/create_async",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=NoneType,
        )


class AsyncIncomingPaymentDetails(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Get an existing Incoming Payment Detail."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/incoming_payment_details/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=IncomingPaymentDetail,
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """
        Update an existing Incoming Payment Detail.

        Args:
          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        body: IncomingPaymentDetailUpdateParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """Update an existing Incoming Payment Detail."""
        ...

    async def update(
        self,
        id: str,
        body: IncomingPaymentDetailUpdateParams | None = None,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> IncomingPaymentDetail:
        """
        Update an existing Incoming Payment Detail.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard IncomingPaymentDetailUpdateParams type.
            body = cast(Any, {"metadata": metadata})

        return await self._patch(
            f"/api/incoming_payment_details/{id}",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=IncomingPaymentDetail,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        status: Literal["completed", "pending", "returned"] | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        as_of_date_start: str | NotGiven = NOT_GIVEN,
        as_of_date_end: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[IncomingPaymentDetail, AsyncPage[IncomingPaymentDetail]]:
        """
        Get a list of Incoming Payment Details.

        Args:
          direction: One of `credit` or `debit`.

          status: The current status of the incoming payment order. One of `pending`, `completed`,
              or `returned`.

          type: One of: `ach`, `wire`, `check`, `rtp`, `sepa`, `signet`.

          as_of_date_start: Filters incoming payment details with an as_of_date starting on or after the
              specified date (YYYY-MM-DD).

          as_of_date_end: Filters incoming payment details with an as_of_date starting on or before the
              specified date (YYYY-MM-DD).

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          virtual_account_id: If the incoming payment detail is in a virtual account, the ID of the Virtual
              Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: IncomingPaymentDetailListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[IncomingPaymentDetail, AsyncPage[IncomingPaymentDetail]]:
        """Get a list of Incoming Payment Details."""
        ...

    def list(
        self,
        query: IncomingPaymentDetailListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        status: Literal["completed", "pending", "returned"] | NotGiven = NOT_GIVEN,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        as_of_date_start: str | NotGiven = NOT_GIVEN,
        as_of_date_end: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        virtual_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[IncomingPaymentDetail, AsyncPage[IncomingPaymentDetail]]:
        """
        Get a list of Incoming Payment Details.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          direction: One of `credit` or `debit`.

          status: The current status of the incoming payment order. One of `pending`, `completed`,
              or `returned`.

          type: One of: `ach`, `wire`, `check`, `rtp`, `sepa`, `signet`.

          as_of_date_start: Filters incoming payment details with an as_of_date starting on or after the
              specified date (YYYY-MM-DD).

          as_of_date_end: Filters incoming payment details with an as_of_date starting on or before the
              specified date (YYYY-MM-DD).

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          virtual_account_id: If the incoming payment detail is in a virtual account, the ID of the Virtual
              Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard IncomingPaymentDetailListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "direction": direction,
                    "status": status,
                    "type": type,
                    "as_of_date_start": as_of_date_start,
                    "as_of_date_end": as_of_date_end,
                    "metadata": metadata,
                    "virtual_account_id": virtual_account_id,
                },
            )

        return self._get_api_list(
            "/api/incoming_payment_details",
            page=AsyncPage[IncomingPaymentDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=IncomingPaymentDetail,
        )

    @overload
    async def create_async(
        self,
        *,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
        internal_account_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """
        Simulate Incoming Payment Detail

        Args:
          type: One of `ach`, `wire`, `check`.

          direction: One of `credit`, `debit`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          currency: Defaults to the currency of the originating account.

          internal_account_id: The ID of one of your internal accounts.

          virtual_account_id: An optional parameter to associate the incoming payment detail to a virtual
              account.

          as_of_date: Defaults to today.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create_async(
        self,
        body: IncomingPaymentDetailCreateAsyncParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Simulate Incoming Payment Detail"""
        ...

    async def create_async(
        self,
        body: IncomingPaymentDetailCreateAsyncParams | None = None,
        *,
        type: Literal["ach", "book", "check", "eft", "interac", "rtp", "sepa", "signet", "wire"] | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
        internal_account_id: str | NotGiven = NOT_GIVEN,
        virtual_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """
        Simulate Incoming Payment Detail

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          type: One of `ach`, `wire`, `check`.

          direction: One of `credit`, `debit`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          currency: Defaults to the currency of the originating account.

          internal_account_id: The ID of one of your internal accounts.

          virtual_account_id: An optional parameter to associate the incoming payment detail to a virtual
              account.

          as_of_date: Defaults to today.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard IncomingPaymentDetailCreateAsyncParams type.
            body = cast(
                Any,
                {
                    "type": type,
                    "direction": direction,
                    "amount": amount,
                    "currency": currency,
                    "internal_account_id": internal_account_id,
                    "virtual_account_id": virtual_account_id,
                    "as_of_date": as_of_date,
                },
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/simulations/incoming_payment_details/create_async",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=NoneType,
        )
