# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..types import (
    ExternalAccount,
    ExternalAccountType,
    shared_params,
    external_account_list_params,
    external_account_create_params,
    external_account_update_params,
    external_account_verify_params,
    external_account_complete_verification_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
    def create(
        self,
        *,
        counterparty_id: Optional[str],
        account_details: List[external_account_create_params.AccountDetail] | NotGiven = NOT_GIVEN,
        account_type: ExternalAccountType | NotGiven = NOT_GIVEN,
        contact_details: List[external_account_create_params.ContactDetail] | NotGiven = NOT_GIVEN,
        ledger_account: external_account_create_params.LedgerAccount | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_address: external_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        routing_details: List[external_account_create_params.RoutingDetail] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        create external account

        Args:
          account_type: Can be `checking`, `savings` or `other`.

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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAccount:
        """
        show external account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        party_address: external_account_update_params.PartyAddress | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ExternalAccount]:
        """
        list external accounts

        Args:
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        amounts: List[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        ],
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        verify external account

        Args:
          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Both ach and eft are supported payment types.

          currency: Defaults to the currency of the originating account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/api/external_accounts/{id}/verify",
            body=maybe_transform(
                {
                    "originating_account_id": originating_account_id,
                    "payment_type": payment_type,
                    "currency": currency,
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
            cast_to=ExternalAccount,
        )


class AsyncExternalAccounts(AsyncAPIResource):
    async def create(
        self,
        *,
        counterparty_id: Optional[str],
        account_details: List[external_account_create_params.AccountDetail] | NotGiven = NOT_GIVEN,
        account_type: ExternalAccountType | NotGiven = NOT_GIVEN,
        contact_details: List[external_account_create_params.ContactDetail] | NotGiven = NOT_GIVEN,
        ledger_account: external_account_create_params.LedgerAccount | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        party_address: external_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        party_identifier: str | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        plaid_processor_token: str | NotGiven = NOT_GIVEN,
        routing_details: List[external_account_create_params.RoutingDetail] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        create external account

        Args:
          account_type: Can be `checking`, `savings` or `other`.

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
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "account_details": account_details,
                    "account_type": account_type,
                    "contact_details": contact_details,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAccount:
        """
        show external account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        party_address: external_account_update_params.PartyAddress | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        party_type: Optional[Literal["business", "individual"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        return await self._patch(
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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        party_name: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        """
        list external accounts

        Args:
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        amounts: List[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        return await self._post(
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
        ],
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        verify external account

        Args:
          originating_account_id: The ID of the internal account where the micro-deposits originate from. Both
              credit and debit capabilities must be enabled.

          payment_type: Both ach and eft are supported payment types.

          currency: Defaults to the currency of the originating account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/api/external_accounts/{id}/verify",
            body=maybe_transform(
                {
                    "originating_account_id": originating_account_id,
                    "payment_type": payment_type,
                    "currency": currency,
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
            cast_to=ExternalAccount,
        )
