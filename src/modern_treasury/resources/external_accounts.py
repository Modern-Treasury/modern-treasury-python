# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    ExternalAccountType,
    external_account_list_params,
    external_account_create_params,
    external_account_update_params,
    external_account_verify_params,
    external_account_complete_verification_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.currency import Currency
from ..types.external_account import ExternalAccount
from ..types.external_account_type import ExternalAccountType
from ..types.shared_params.address_request import AddressRequest
from ..types.external_account_verify_response import ExternalAccountVerifyResponse
from ..types.contact_detail_create_request_param import ContactDetailCreateRequestParam
from ..types.shared_params.ledger_account_create_request import LedgerAccountCreateRequest

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalAccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return ExternalAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalAccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return ExternalAccountsWithStreamingResponse(self)

    def create(
        self,
        *,
        counterparty_id: Optional[str],
        query_external_id: str | NotGiven = NOT_GIVEN,
        account_details: Iterable[external_account_create_params.AccountDetail] | NotGiven = NOT_GIVEN,
        account_type: ExternalAccountType | NotGiven = NOT_GIVEN,
        contact_details: Iterable[ContactDetailCreateRequestParam] | NotGiven = NOT_GIVEN,
        body_external_id: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_account: LedgerAccountCreateRequest | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_address: AddressRequest | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        routing_details: Iterable[external_account_create_params.RoutingDetail] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        create external account

        Args:
          query_external_id: An optional user-defined 180 character unique identifier.

          account_type: Can be `checking`, `savings` or `other`.

          body_external_id: An optional user-defined 180 character unique identifier.

          ledger_account: Specifies a ledger account object that will be created with the external
              account. The resulting ledger account is linked to the external account for
              auto-ledgering Payment objects. See
              https://docs.moderntreasury.com/docs/linking-to-other-modern-treasury-objects
              for more details.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_address: Required if receiving wire payments.

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          party_type: Either `individual` or `business`.

          plaid_processor_token: If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
              you can pass the processor token in this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/external_accounts",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "account_details": account_details,
                    "account_type": account_type,
                    "contact_details": contact_details,
                    "body_external_id": body_external_id,
                    "ledger_account": ledger_account,
                    "metadata": metadata,
                    "name": name,
                    "party_address": party_address,
                    "party_identifier": party_identifier,
                    "party_name": party_name,
                    "party_type": party_type,
                    "plaid_processor_token": plaid_processor_token,
                    "routing_details": routing_details,
                },
                external_account_create_params.ExternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {"query_external_id": query_external_id}, external_account_create_params.ExternalAccountCreateParams
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAccount:
        """
        show external account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/external_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccount,
        )

    def update(
        self,
        id: str,
        *,
        account_type: ExternalAccountType | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_address: AddressRequest | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        update external account

        Args:
          account_type: Can be `checking`, `savings` or `other`.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          party_type: Either `individual` or `business`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/external_accounts/{id}",
            body=maybe_transform(
                {
                    "account_type": account_type,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                    "name": name,
                    "party_address": party_address,
                    "party_name": party_name,
                    "party_type": party_type,
                },
                external_account_update_params.ExternalAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ExternalAccount]:
        """
        list external accounts

        Args:
          external_id: An optional user-defined 180 character unique identifier.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          party_name: Searches the ExternalAccount's party_name AND the Counterparty's party_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/external_accounts",
            page=SyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "external_id": external_id,
                        "metadata": metadata,
                        "party_name": party_name,
                        "per_page": per_page,
                    },
                    external_account_list_params.ExternalAccountListParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        delete external account

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
            f"/api/external_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def complete_verification(
        self,
        id: str,
        *,
        amounts: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        complete verification of external account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/external_accounts/{id}/complete_verification",
            body=maybe_transform(
                {"amounts": amounts},
                external_account_complete_verification_params.ExternalAccountCompleteVerificationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    def verify(
        self,
        id: str,
        *,
        originating_account_id: str,
        payment_type: Literal[
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
        ],
        currency: Currency | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccountVerifyResponse:
        """
        verify external account

        Args:
          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Can be `ach`, `eft`, or `rtp`.

          currency: Defaults to the currency of the originating account.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (payment_type=rtp and fallback_type=ach)

          priority: Either `normal` or `high`. For ACH payments, `high` represents a same-day ACH
              transfer. This will apply to both `payment_type` and `fallback_type`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            ExternalAccountVerifyResponse,
            self._post(
                f"/api/external_accounts/{id}/verify",
                body=maybe_transform(
                    {
                        "originating_account_id": originating_account_id,
                        "payment_type": payment_type,
                        "currency": currency,
                        "fallback_type": fallback_type,
                        "priority": priority,
                    },
                    external_account_verify_params.ExternalAccountVerifyParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, ExternalAccountVerifyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncExternalAccounts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalAccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalAccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncExternalAccountsWithStreamingResponse(self)

    async def create(
        self,
        *,
        counterparty_id: Optional[str],
        query_external_id: str | NotGiven = NOT_GIVEN,
        account_details: Iterable[external_account_create_params.AccountDetail] | NotGiven = NOT_GIVEN,
        account_type: ExternalAccountType | NotGiven = NOT_GIVEN,
        contact_details: Iterable[ContactDetailCreateRequestParam] | NotGiven = NOT_GIVEN,
        body_external_id: Optional[str] | NotGiven = NOT_GIVEN,
        ledger_account: LedgerAccountCreateRequest | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_address: AddressRequest | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        routing_details: Iterable[external_account_create_params.RoutingDetail] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        create external account

        Args:
          query_external_id: An optional user-defined 180 character unique identifier.

          account_type: Can be `checking`, `savings` or `other`.

          body_external_id: An optional user-defined 180 character unique identifier.

          ledger_account: Specifies a ledger account object that will be created with the external
              account. The resulting ledger account is linked to the external account for
              auto-ledgering Payment objects. See
              https://docs.moderntreasury.com/docs/linking-to-other-modern-treasury-objects
              for more details.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_address: Required if receiving wire payments.

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          party_type: Either `individual` or `business`.

          plaid_processor_token: If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
              you can pass the processor token in this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/external_accounts",
            body=await async_maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "account_details": account_details,
                    "account_type": account_type,
                    "contact_details": contact_details,
                    "body_external_id": body_external_id,
                    "ledger_account": ledger_account,
                    "metadata": metadata,
                    "name": name,
                    "party_address": party_address,
                    "party_identifier": party_identifier,
                    "party_name": party_name,
                    "party_type": party_type,
                    "plaid_processor_token": plaid_processor_token,
                    "routing_details": routing_details,
                },
                external_account_create_params.ExternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=await async_maybe_transform(
                    {"query_external_id": query_external_id}, external_account_create_params.ExternalAccountCreateParams
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAccount:
        """
        show external account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/external_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccount,
        )

    async def update(
        self,
        id: str,
        *,
        account_type: ExternalAccountType | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_address: AddressRequest | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        update external account

        Args:
          account_type: Can be `checking`, `savings` or `other`.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          name: A nickname for the external account. This is only for internal usage and won't
              affect any payments

          party_name: If this value isn't provided, it will be inherited from the counterparty's name.

          party_type: Either `individual` or `business`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/external_accounts/{id}",
            body=await async_maybe_transform(
                {
                    "account_type": account_type,
                    "counterparty_id": counterparty_id,
                    "metadata": metadata,
                    "name": name,
                    "party_address": party_address,
                    "party_name": party_name,
                    "party_type": party_type,
                },
                external_account_update_params.ExternalAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        """
        list external accounts

        Args:
          external_id: An optional user-defined 180 character unique identifier.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          party_name: Searches the ExternalAccount's party_name AND the Counterparty's party_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/external_accounts",
            page=AsyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "external_id": external_id,
                        "metadata": metadata,
                        "party_name": party_name,
                        "per_page": per_page,
                    },
                    external_account_list_params.ExternalAccountListParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        delete external account

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
            f"/api/external_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def complete_verification(
        self,
        id: str,
        *,
        amounts: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        complete verification of external account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/external_accounts/{id}/complete_verification",
            body=await async_maybe_transform(
                {"amounts": amounts},
                external_account_complete_verification_params.ExternalAccountCompleteVerificationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    async def verify(
        self,
        id: str,
        *,
        originating_account_id: str,
        payment_type: Literal[
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
        ],
        currency: Currency | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccountVerifyResponse:
        """
        verify external account

        Args:
          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Can be `ach`, `eft`, or `rtp`.

          currency: Defaults to the currency of the originating account.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (payment_type=rtp and fallback_type=ach)

          priority: Either `normal` or `high`. For ACH payments, `high` represents a same-day ACH
              transfer. This will apply to both `payment_type` and `fallback_type`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            ExternalAccountVerifyResponse,
            await self._post(
                f"/api/external_accounts/{id}/verify",
                body=await async_maybe_transform(
                    {
                        "originating_account_id": originating_account_id,
                        "payment_type": payment_type,
                        "currency": currency,
                        "fallback_type": fallback_type,
                        "priority": priority,
                    },
                    external_account_verify_params.ExternalAccountVerifyParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, ExternalAccountVerifyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ExternalAccountsWithRawResponse:
    def __init__(self, external_accounts: ExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            external_accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            external_accounts.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            external_accounts.delete,
        )
        self.complete_verification = _legacy_response.to_raw_response_wrapper(
            external_accounts.complete_verification,
        )
        self.verify = _legacy_response.to_raw_response_wrapper(
            external_accounts.verify,
        )


class AsyncExternalAccountsWithRawResponse:
    def __init__(self, external_accounts: AsyncExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.delete,
        )
        self.complete_verification = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.complete_verification,
        )
        self.verify = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.verify,
        )


class ExternalAccountsWithStreamingResponse:
    def __init__(self, external_accounts: ExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = to_streamed_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            external_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            external_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            external_accounts.delete,
        )
        self.complete_verification = to_streamed_response_wrapper(
            external_accounts.complete_verification,
        )
        self.verify = to_streamed_response_wrapper(
            external_accounts.verify,
        )


class AsyncExternalAccountsWithStreamingResponse:
    def __init__(self, external_accounts: AsyncExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = async_to_streamed_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            external_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            external_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            external_accounts.delete,
        )
        self.complete_verification = async_to_streamed_response_wrapper(
            external_accounts.complete_verification,
        )
        self.verify = async_to_streamed_response_wrapper(
            external_accounts.verify,
        )
