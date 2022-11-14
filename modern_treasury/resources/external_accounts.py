# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Dict, List, Union, Optional, cast, overload
from typing_extensions import Literal

from ..types import external_account_create_params, external_account_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NoneType, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.external_account import ExternalAccount
from ..types.external_account_list_params import ExternalAccountListParams
from ..types.external_account_create_params import ExternalAccountCreateParams
from ..types.external_account_update_params import ExternalAccountUpdateParams
from ..types.external_account_verify_params import ExternalAccountVerifyParams
from ..types.external_account_complete_verification_params import (
    ExternalAccountCompleteVerificationParams,
)

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        party_address: external_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str],
        account_details: List[external_account_create_params.AccountDetails] | NotGiven = NOT_GIVEN,
        routing_details: List[external_account_create_params.RoutingDetails] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        contact_details: List[external_account_create_params.ContactDetails] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          account_type: Can be `checking`, `savings` or `other`.

          party_type: Either `individual` or `business`.

          party_address: Required if receiving wire payments.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          plaid_processor_token: If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
              you can pass the processor token in this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: ExternalAccountCreateParams,
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
    ) -> ExternalAccount:
        ...

    @required_args(["body"], ["counterparty_id"])
    def create(
        self,
        body: ExternalAccountCreateParams | None = None,
        *,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        party_address: external_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        account_details: List[external_account_create_params.AccountDetails] | NotGiven = NOT_GIVEN,
        routing_details: List[external_account_create_params.RoutingDetails] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        contact_details: List[external_account_create_params.ContactDetails] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_type: Can be `checking`, `savings` or `other`.

          party_type: Either `individual` or `business`.

          party_address: Required if receiving wire payments.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          plaid_processor_token: If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
              you can pass the processor token in this field.

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
            # with the standard ExternalAccountCreateParams type.
            body = cast(
                Any,
                {
                    "account_type": account_type,
                    "party_type": party_type,
                    "party_address": party_address,
                    "name": name,
                    "counterparty_id": counterparty_id,
                    "account_details": account_details,
                    "routing_details": routing_details,
                    "metadata": metadata,
                    "party_name": party_name,
                    "party_identifier": party_identifier,
                    "plaid_processor_token": plaid_processor_token,
                    "contact_details": contact_details,
                },
            )

        return self._post(
            "/api/external_accounts",
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
            cast_to=ExternalAccount,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/external_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ExternalAccount,
        )

    @overload
    def update(
        self,
        id: str,
        *,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_address: external_account_update_params.PartyAddress | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          party_type: Either `individual` or `business`.

          account_type: Can be `checking`, `savings` or `other`.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

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
        body: ExternalAccountUpdateParams = {},
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
    ) -> ExternalAccount:
        ...

    def update(
        self,
        id: str,
        body: ExternalAccountUpdateParams | None = None,
        *,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_address: external_account_update_params.PartyAddress | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          party_type: Either `individual` or `business`.

          account_type: Can be `checking`, `savings` or `other`.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

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
            # with the standard ExternalAccountUpdateParams type.
            body = cast(
                Any,
                {
                    "party_type": party_type,
                    "account_type": account_type,
                    "counterparty_id": counterparty_id,
                    "name": name,
                    "party_name": party_name,
                    "party_address": party_address,
                    "metadata": metadata,
                },
            )

        return self._patch(
            f"/api/external_accounts/{id}",
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
            cast_to=ExternalAccount,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncPage[ExternalAccount]:
        """
        Args:
          party_name: Searches the ExternalAccount's party_name AND the Counterparty's party_name

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: ExternalAccountListParams = {},
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
    ) -> SyncPage[ExternalAccount]:
        ...

    def list(
        self,
        query: ExternalAccountListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncPage[ExternalAccount]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          party_name: Searches the ExternalAccount's party_name AND the Counterparty's party_name

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

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
            # with the standard ExternalAccountListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "party_name": party_name,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                },
            )

        return self._get_api_list(
            "/api/external_accounts",
            page=SyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=ExternalAccount,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/external_accounts/{id}",
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

    @overload
    def complete_verification(
        self,
        id: str,
        *,
        amounts: List[int] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def complete_verification(
        self,
        id: str,
        body: ExternalAccountCompleteVerificationParams = {},
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
    ) -> ExternalAccount:
        ...

    def complete_verification(
        self,
        id: str,
        body: ExternalAccountCompleteVerificationParams | None = None,
        *,
        amounts: List[int] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard ExternalAccountCompleteVerificationParams type.
            body = cast(Any, {"amounts": amounts})

        return self._post(
            f"/api/external_accounts/{id}/complete_verification",
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
            cast_to=ExternalAccount,
        )

    @overload
    def verify(
        self,
        id: str,
        *,
        originating_account_id: str,
        payment_type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "global_pay",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ],
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
    ) -> ExternalAccount:
        """
        Args:
          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Both ach and eft are supported payment types.

          currency: Defaults to the currency of the originating account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def verify(
        self,
        id: str,
        body: ExternalAccountVerifyParams,
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
    ) -> ExternalAccount:
        ...

    @required_args(["body"], ["originating_account_id", "payment_type"])
    def verify(
        self,
        id: str,
        body: ExternalAccountVerifyParams | None = None,
        *,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "global_pay",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Both ach and eft are supported payment types.

          currency: Defaults to the currency of the originating account.

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
            # with the standard ExternalAccountVerifyParams type.
            body = cast(
                Any,
                {
                    "originating_account_id": originating_account_id,
                    "payment_type": payment_type,
                    "currency": currency,
                },
            )

        return self._post(
            f"/api/external_accounts/{id}/verify",
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
            cast_to=ExternalAccount,
        )


class AsyncExternalAccounts(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        party_address: external_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str],
        account_details: List[external_account_create_params.AccountDetails] | NotGiven = NOT_GIVEN,
        routing_details: List[external_account_create_params.RoutingDetails] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        contact_details: List[external_account_create_params.ContactDetails] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          account_type: Can be `checking`, `savings` or `other`.

          party_type: Either `individual` or `business`.

          party_address: Required if receiving wire payments.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          plaid_processor_token: If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
              you can pass the processor token in this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: ExternalAccountCreateParams,
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
    ) -> ExternalAccount:
        ...

    @required_args(["body"], ["counterparty_id"])
    async def create(
        self,
        body: ExternalAccountCreateParams | None = None,
        *,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        party_address: external_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        account_details: List[external_account_create_params.AccountDetails] | NotGiven = NOT_GIVEN,
        routing_details: List[external_account_create_params.RoutingDetails] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        contact_details: List[external_account_create_params.ContactDetails] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_type: Can be `checking`, `savings` or `other`.

          party_type: Either `individual` or `business`.

          party_address: Required if receiving wire payments.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          plaid_processor_token: If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
              you can pass the processor token in this field.

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
            # with the standard ExternalAccountCreateParams type.
            body = cast(
                Any,
                {
                    "account_type": account_type,
                    "party_type": party_type,
                    "party_address": party_address,
                    "name": name,
                    "counterparty_id": counterparty_id,
                    "account_details": account_details,
                    "routing_details": routing_details,
                    "metadata": metadata,
                    "party_name": party_name,
                    "party_identifier": party_identifier,
                    "plaid_processor_token": plaid_processor_token,
                    "contact_details": contact_details,
                },
            )

        return await self._post(
            "/api/external_accounts",
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
            cast_to=ExternalAccount,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/external_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ExternalAccount,
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_address: external_account_update_params.PartyAddress | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          party_type: Either `individual` or `business`.

          account_type: Can be `checking`, `savings` or `other`.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

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
        body: ExternalAccountUpdateParams = {},
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
    ) -> ExternalAccount:
        ...

    async def update(
        self,
        id: str,
        body: ExternalAccountUpdateParams | None = None,
        *,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        account_type: Literal["checking", "other", "savings"] | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_address: external_account_update_params.PartyAddress | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          party_type: Either `individual` or `business`.

          account_type: Can be `checking`, `savings` or `other`.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

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
            # with the standard ExternalAccountUpdateParams type.
            body = cast(
                Any,
                {
                    "party_type": party_type,
                    "account_type": account_type,
                    "counterparty_id": counterparty_id,
                    "name": name,
                    "party_name": party_name,
                    "party_address": party_address,
                    "metadata": metadata,
                },
            )

        return await self._patch(
            f"/api/external_accounts/{id}",
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
            cast_to=ExternalAccount,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        """
        Args:
          party_name: Searches the ExternalAccount's party_name AND the Counterparty's party_name

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: ExternalAccountListParams = {},
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
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        ...

    def list(
        self,
        query: ExternalAccountListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          party_name: Searches the ExternalAccount's party_name AND the Counterparty's party_name

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

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
            # with the standard ExternalAccountListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "party_name": party_name,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                },
            )

        return self._get_api_list(
            "/api/external_accounts",
            page=AsyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=ExternalAccount,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/external_accounts/{id}",
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

    @overload
    async def complete_verification(
        self,
        id: str,
        *,
        amounts: List[int] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def complete_verification(
        self,
        id: str,
        body: ExternalAccountCompleteVerificationParams = {},
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
    ) -> ExternalAccount:
        ...

    async def complete_verification(
        self,
        id: str,
        body: ExternalAccountCompleteVerificationParams | None = None,
        *,
        amounts: List[int] | NotGiven = NOT_GIVEN,
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard ExternalAccountCompleteVerificationParams type.
            body = cast(Any, {"amounts": amounts})

        return await self._post(
            f"/api/external_accounts/{id}/complete_verification",
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
            cast_to=ExternalAccount,
        )

    @overload
    async def verify(
        self,
        id: str,
        *,
        originating_account_id: str,
        payment_type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "global_pay",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ],
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
    ) -> ExternalAccount:
        """
        Args:
          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Both ach and eft are supported payment types.

          currency: Defaults to the currency of the originating account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def verify(
        self,
        id: str,
        body: ExternalAccountVerifyParams,
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
    ) -> ExternalAccount:
        ...

    @required_args(["body"], ["originating_account_id", "payment_type"])
    async def verify(
        self,
        id: str,
        body: ExternalAccountVerifyParams | None = None,
        *,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        payment_type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "eft",
            "global_pay",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
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
    ) -> ExternalAccount:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Both ach and eft are supported payment types.

          currency: Defaults to the currency of the originating account.

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
            # with the standard ExternalAccountVerifyParams type.
            body = cast(
                Any,
                {
                    "originating_account_id": originating_account_id,
                    "payment_type": payment_type,
                    "currency": currency,
                },
            )

        return await self._post(
            f"/api/external_accounts/{id}/verify",
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
            cast_to=ExternalAccount,
        )
