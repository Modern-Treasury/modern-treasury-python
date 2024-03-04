# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    Counterparty,
    CounterpartyCollectAccountResponse,
    counterparty_list_params,
    counterparty_create_params,
    counterparty_update_params,
    counterparty_collect_account_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.shared import TransactionDirection

__all__ = ["Counterparties", "AsyncCounterparties"]


class Counterparties(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CounterpartiesWithRawResponse:
        return CounterpartiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CounterpartiesWithStreamingResponse:
        return CounterpartiesWithStreamingResponse(self)

    def create(
        self,
        *,
        name: Optional[str],
        accounting: counterparty_create_params.Accounting | NotGiven = NOT_GIVEN,
        accounts: Iterable[counterparty_create_params.Account] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_type: Literal["customer", "vendor"] | NotGiven = NOT_GIVEN,
        legal_entity: counterparty_create_params.LegalEntity | NotGiven = NOT_GIVEN,
        legal_entity_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
        verification_status: Literal["denied", "needs_approval", "unverified", "verified"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Counterparty:
        """
        Create a new counterparty.

        Args:
          name: A human friendly name for this counterparty.

          accounts: The accounts for this counterparty.

          email: The counterparty's email.

          ledger_type: An optional type to auto-sync the counterparty to your ledger. Either `customer`
              or `vendor`.

          legal_entity_id: The id of the legal entity.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          send_remittance_advice: Send an email to the counterparty whenever an associated payment order is sent
              to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

          verification_status: The verification status of the counterparty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/counterparties",
            body=maybe_transform(
                {
                    "name": name,
                    "accounting": accounting,
                    "accounts": accounts,
                    "email": email,
                    "ledger_type": ledger_type,
                    "legal_entity": legal_entity,
                    "legal_entity_id": legal_entity_id,
                    "metadata": metadata,
                    "send_remittance_advice": send_remittance_advice,
                    "taxpayer_identifier": taxpayer_identifier,
                    "verification_status": verification_status,
                },
                counterparty_create_params.CounterpartyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Counterparty,
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
    ) -> Counterparty:
        """
        Get details on a single counterparty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Counterparty,
        )

    def update(
        self,
        id: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        legal_entity_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Counterparty:
        """
        Updates a given counterparty with new information.

        Args:
          email: A new email for the counterparty.

          legal_entity_id: The id of the legal entity.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          name: A new name for the counterparty. Will only update if passed.

          send_remittance_advice: If this is `true`, Modern Treasury will send an email to the counterparty
              whenever an associated payment order is sent to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/counterparties/{id}",
            body=maybe_transform(
                {
                    "email": email,
                    "legal_entity_id": legal_entity_id,
                    "metadata": metadata,
                    "name": name,
                    "send_remittance_advice": send_remittance_advice,
                    "taxpayer_identifier": taxpayer_identifier,
                },
                counterparty_update_params.CounterpartyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Counterparty,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_upper_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Counterparty]:
        """
        Get a paginated list of all counterparties.

        Args:
          created_at_lower_bound: Used to return counterparties created after some datetime.

          created_at_upper_bound: Used to return counterparties created before some datetime.

          email: Performs a partial string match of the email field. This is also case
              insensitive.

          legal_entity_id: Filters for counterparties with the given legal entity ID.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          name: Performs a partial string match of the name field. This is also case
              insensitive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/counterparties",
            page=SyncPage[Counterparty],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at_lower_bound": created_at_lower_bound,
                        "created_at_upper_bound": created_at_upper_bound,
                        "email": email,
                        "legal_entity_id": legal_entity_id,
                        "metadata": metadata,
                        "name": name,
                        "per_page": per_page,
                    },
                    counterparty_list_params.CounterpartyListParams,
                ),
            ),
            model=Counterparty,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes a given counterparty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def collect_account(
        self,
        id: str,
        *,
        direction: TransactionDirection,
        custom_redirect: str | NotGiven = NOT_GIVEN,
        fields: List[
            Literal[
                "name",
                "nameOnAccount",
                "taxpayerIdentifier",
                "accountType",
                "accountNumber",
                "ibanNumber",
                "clabeNumber",
                "walletAddress",
                "panNumber",
                "routingNumber",
                "abaWireRoutingNumber",
                "swiftCode",
                "auBsb",
                "caCpa",
                "cnaps",
                "gbSortCode",
                "inIfsc",
                "myBranchCode",
                "brCodigo",
                "routingNumberType",
                "address",
                "jp_zengin_code",
                "se_bankgiro_clearing_code",
                "nz_national_clearing_code",
                "hk_interbank_clearing_code",
                "hu_interbank_clearing_code",
                "dk_interbank_clearing_code",
                "id_sknbi_code",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CounterpartyCollectAccountResponse:
        """
        Send an email requesting account details.

        Args:
          direction: One of `credit` or `debit`. Use `credit` when you want to pay a counterparty.
              Use `debit` when you need to charge a counterparty. This field helps us send a
              more tailored email to your counterparties."

          custom_redirect: The URL you want your customer to visit upon filling out the form. By default,
              they will be sent to a Modern Treasury landing page. This must be a valid HTTPS
              URL if set.

          fields: The list of fields you want on the form. This field is optional and if it is not
              set, will default to [\"nameOnAccount\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\"]. The full list of options is [\"name\",
              \"nameOnAccount\", \"taxpayerIdentifier\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\", \"ibanNumber\", \"swiftCode\"].

          send_email: By default, Modern Treasury will send an email to your counterparty that
              includes a link to the form they must fill out. However, if you would like to
              send the counterparty the link, you can set this parameter to `false`. The JSON
              body will include the link to the secure Modern Treasury form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/counterparties/{id}/collect_account",
            body=maybe_transform(
                {
                    "direction": direction,
                    "custom_redirect": custom_redirect,
                    "fields": fields,
                    "send_email": send_email,
                },
                counterparty_collect_account_params.CounterpartyCollectAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CounterpartyCollectAccountResponse,
        )


class AsyncCounterparties(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCounterpartiesWithRawResponse:
        return AsyncCounterpartiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCounterpartiesWithStreamingResponse:
        return AsyncCounterpartiesWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: Optional[str],
        accounting: counterparty_create_params.Accounting | NotGiven = NOT_GIVEN,
        accounts: Iterable[counterparty_create_params.Account] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_type: Literal["customer", "vendor"] | NotGiven = NOT_GIVEN,
        legal_entity: counterparty_create_params.LegalEntity | NotGiven = NOT_GIVEN,
        legal_entity_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
        verification_status: Literal["denied", "needs_approval", "unverified", "verified"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Counterparty:
        """
        Create a new counterparty.

        Args:
          name: A human friendly name for this counterparty.

          accounts: The accounts for this counterparty.

          email: The counterparty's email.

          ledger_type: An optional type to auto-sync the counterparty to your ledger. Either `customer`
              or `vendor`.

          legal_entity_id: The id of the legal entity.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          send_remittance_advice: Send an email to the counterparty whenever an associated payment order is sent
              to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

          verification_status: The verification status of the counterparty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/counterparties",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "accounting": accounting,
                    "accounts": accounts,
                    "email": email,
                    "ledger_type": ledger_type,
                    "legal_entity": legal_entity,
                    "legal_entity_id": legal_entity_id,
                    "metadata": metadata,
                    "send_remittance_advice": send_remittance_advice,
                    "taxpayer_identifier": taxpayer_identifier,
                    "verification_status": verification_status,
                },
                counterparty_create_params.CounterpartyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Counterparty,
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
    ) -> Counterparty:
        """
        Get details on a single counterparty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Counterparty,
        )

    async def update(
        self,
        id: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        legal_entity_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Counterparty:
        """
        Updates a given counterparty with new information.

        Args:
          email: A new email for the counterparty.

          legal_entity_id: The id of the legal entity.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          name: A new name for the counterparty. Will only update if passed.

          send_remittance_advice: If this is `true`, Modern Treasury will send an email to the counterparty
              whenever an associated payment order is sent to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/counterparties/{id}",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "legal_entity_id": legal_entity_id,
                    "metadata": metadata,
                    "name": name,
                    "send_remittance_advice": send_remittance_advice,
                    "taxpayer_identifier": taxpayer_identifier,
                },
                counterparty_update_params.CounterpartyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Counterparty,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_upper_bound: Union[str, datetime] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Counterparty, AsyncPage[Counterparty]]:
        """
        Get a paginated list of all counterparties.

        Args:
          created_at_lower_bound: Used to return counterparties created after some datetime.

          created_at_upper_bound: Used to return counterparties created before some datetime.

          email: Performs a partial string match of the email field. This is also case
              insensitive.

          legal_entity_id: Filters for counterparties with the given legal entity ID.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          name: Performs a partial string match of the name field. This is also case
              insensitive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/counterparties",
            page=AsyncPage[Counterparty],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at_lower_bound": created_at_lower_bound,
                        "created_at_upper_bound": created_at_upper_bound,
                        "email": email,
                        "legal_entity_id": legal_entity_id,
                        "metadata": metadata,
                        "name": name,
                        "per_page": per_page,
                    },
                    counterparty_list_params.CounterpartyListParams,
                ),
            ),
            model=Counterparty,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes a given counterparty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def collect_account(
        self,
        id: str,
        *,
        direction: TransactionDirection,
        custom_redirect: str | NotGiven = NOT_GIVEN,
        fields: List[
            Literal[
                "name",
                "nameOnAccount",
                "taxpayerIdentifier",
                "accountType",
                "accountNumber",
                "ibanNumber",
                "clabeNumber",
                "walletAddress",
                "panNumber",
                "routingNumber",
                "abaWireRoutingNumber",
                "swiftCode",
                "auBsb",
                "caCpa",
                "cnaps",
                "gbSortCode",
                "inIfsc",
                "myBranchCode",
                "brCodigo",
                "routingNumberType",
                "address",
                "jp_zengin_code",
                "se_bankgiro_clearing_code",
                "nz_national_clearing_code",
                "hk_interbank_clearing_code",
                "hu_interbank_clearing_code",
                "dk_interbank_clearing_code",
                "id_sknbi_code",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CounterpartyCollectAccountResponse:
        """
        Send an email requesting account details.

        Args:
          direction: One of `credit` or `debit`. Use `credit` when you want to pay a counterparty.
              Use `debit` when you need to charge a counterparty. This field helps us send a
              more tailored email to your counterparties."

          custom_redirect: The URL you want your customer to visit upon filling out the form. By default,
              they will be sent to a Modern Treasury landing page. This must be a valid HTTPS
              URL if set.

          fields: The list of fields you want on the form. This field is optional and if it is not
              set, will default to [\"nameOnAccount\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\"]. The full list of options is [\"name\",
              \"nameOnAccount\", \"taxpayerIdentifier\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\", \"ibanNumber\", \"swiftCode\"].

          send_email: By default, Modern Treasury will send an email to your counterparty that
              includes a link to the form they must fill out. However, if you would like to
              send the counterparty the link, you can set this parameter to `false`. The JSON
              body will include the link to the secure Modern Treasury form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/counterparties/{id}/collect_account",
            body=await async_maybe_transform(
                {
                    "direction": direction,
                    "custom_redirect": custom_redirect,
                    "fields": fields,
                    "send_email": send_email,
                },
                counterparty_collect_account_params.CounterpartyCollectAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CounterpartyCollectAccountResponse,
        )


class CounterpartiesWithRawResponse:
    def __init__(self, counterparties: Counterparties) -> None:
        self._counterparties = counterparties

        self.create = _legacy_response.to_raw_response_wrapper(
            counterparties.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            counterparties.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            counterparties.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            counterparties.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            counterparties.delete,
        )
        self.collect_account = _legacy_response.to_raw_response_wrapper(
            counterparties.collect_account,
        )


class AsyncCounterpartiesWithRawResponse:
    def __init__(self, counterparties: AsyncCounterparties) -> None:
        self._counterparties = counterparties

        self.create = _legacy_response.async_to_raw_response_wrapper(
            counterparties.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            counterparties.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            counterparties.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            counterparties.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            counterparties.delete,
        )
        self.collect_account = _legacy_response.async_to_raw_response_wrapper(
            counterparties.collect_account,
        )


class CounterpartiesWithStreamingResponse:
    def __init__(self, counterparties: Counterparties) -> None:
        self._counterparties = counterparties

        self.create = to_streamed_response_wrapper(
            counterparties.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            counterparties.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            counterparties.update,
        )
        self.list = to_streamed_response_wrapper(
            counterparties.list,
        )
        self.delete = to_streamed_response_wrapper(
            counterparties.delete,
        )
        self.collect_account = to_streamed_response_wrapper(
            counterparties.collect_account,
        )


class AsyncCounterpartiesWithStreamingResponse:
    def __init__(self, counterparties: AsyncCounterparties) -> None:
        self._counterparties = counterparties

        self.create = async_to_streamed_response_wrapper(
            counterparties.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            counterparties.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            counterparties.update,
        )
        self.list = async_to_streamed_response_wrapper(
            counterparties.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            counterparties.delete,
        )
        self.collect_account = async_to_streamed_response_wrapper(
            counterparties.collect_account,
        )
