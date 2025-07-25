# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import (
    internal_account_list_params,
    internal_account_create_params,
    internal_account_update_params,
    internal_account_update_account_capability_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .balance_reports import (
    BalanceReports,
    AsyncBalanceReports,
    BalanceReportsWithRawResponse,
    AsyncBalanceReportsWithRawResponse,
    BalanceReportsWithStreamingResponse,
    AsyncBalanceReportsWithStreamingResponse,
)
from ...types.shared.currency import Currency
from ...types.internal_account import InternalAccount
from ...types.shared.transaction_direction import TransactionDirection
from ...types.internal_account_update_account_capability_response import InternalAccountUpdateAccountCapabilityResponse

__all__ = ["InternalAccounts", "AsyncInternalAccounts"]


class InternalAccounts(SyncAPIResource):
    @cached_property
    def balance_reports(self) -> BalanceReports:
        return BalanceReports(self._client)

    @cached_property
    def with_raw_response(self) -> InternalAccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return InternalAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InternalAccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return InternalAccountsWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_id: str,
        currency: Literal["USD", "CAD"],
        name: str,
        party_name: str,
        account_capabilities: Iterable[internal_account_create_params.AccountCapability] | NotGiven = NOT_GIVEN,
        account_type: Literal[
            "base_wallet",
            "cash",
            "checking",
            "crypto_wallet",
            "ethereum_wallet",
            "general_ledger",
            "loan",
            "non_resident",
            "other",
            "overdraft",
            "polygon_wallet",
            "savings",
            "solana_wallet",
        ]
        | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        party_address: internal_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        vendor_attributes: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccount:
        """
        create internal account

        Args:
          connection_id: The identifier of the financial institution the account belongs to.

          currency: Either "USD" or "CAD". Internal accounts created at Increase only supports
              "USD".

          name: The nickname of the account.

          party_name: The legal name of the entity which owns the account.

          account_capabilities: An array of AccountCapability objects that list the originating abilities of the
              internal account and any relevant information for them.

          account_type: The account type, used to provision the appropriate account at the financial
              institution.

          counterparty_id: The Counterparty associated to this account.

          legal_entity_id: The LegalEntity associated to this account.

          parent_account_id: The parent internal account of this new account.

          party_address: The address associated with the owner or null.

          vendor_attributes: A hash of vendor specific attributes that will be used when creating the account
              at the vendor specified by the given connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/internal_accounts",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "currency": currency,
                    "name": name,
                    "party_name": party_name,
                    "account_capabilities": account_capabilities,
                    "account_type": account_type,
                    "counterparty_id": counterparty_id,
                    "legal_entity_id": legal_entity_id,
                    "parent_account_id": parent_account_id,
                    "party_address": party_address,
                    "vendor_attributes": vendor_attributes,
                },
                internal_account_create_params.InternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InternalAccount,
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
    ) -> InternalAccount:
        """
        get internal account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/internal_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InternalAccount,
        )

    def update(
        self,
        id: str,
        *,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccount:
        """
        update internal account

        Args:
          counterparty_id: The Counterparty associated to this account.

          ledger_account_id: The Ledger Account associated to this account.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          name: The nickname for the internal account.

          parent_account_id: The parent internal account for this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/internal_accounts/{id}",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "ledger_account_id": ledger_account_id,
                    "metadata": metadata,
                    "name": name,
                    "parent_account_id": parent_account_id,
                },
                internal_account_update_params.InternalAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InternalAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        currency: Currency | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_direction: TransactionDirection | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InternalAccount]:
        """
        list internal accounts

        Args:
          counterparty_id: Only return internal accounts associated with this counterparty.

          currency: Only return internal accounts with this currency.

          legal_entity_id: Only return internal accounts associated with this legal entity.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          payment_direction: Only return internal accounts that can originate payments with this direction.

          payment_type: Only return internal accounts that can make this type of payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/internal_accounts",
            page=SyncPage[InternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "currency": currency,
                        "legal_entity_id": legal_entity_id,
                        "metadata": metadata,
                        "payment_direction": payment_direction,
                        "payment_type": payment_type,
                        "per_page": per_page,
                    },
                    internal_account_list_params.InternalAccountListParams,
                ),
            ),
            model=InternalAccount,
        )

    def update_account_capability(
        self,
        id: str,
        *,
        internal_account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccountUpdateAccountCapabilityResponse:
        """
        update account_capability

        Args:
          identifier: A unique reference assigned by your bank for tracking and recognizing payment
              files. It is important this is formatted exactly how the bank assigned it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/internal_accounts/{internal_account_id}/account_capabilities/{id}",
            body=maybe_transform(
                {"identifier": identifier},
                internal_account_update_account_capability_params.InternalAccountUpdateAccountCapabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InternalAccountUpdateAccountCapabilityResponse,
        )


class AsyncInternalAccounts(AsyncAPIResource):
    @cached_property
    def balance_reports(self) -> AsyncBalanceReports:
        return AsyncBalanceReports(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInternalAccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInternalAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInternalAccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncInternalAccountsWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_id: str,
        currency: Literal["USD", "CAD"],
        name: str,
        party_name: str,
        account_capabilities: Iterable[internal_account_create_params.AccountCapability] | NotGiven = NOT_GIVEN,
        account_type: Literal[
            "base_wallet",
            "cash",
            "checking",
            "crypto_wallet",
            "ethereum_wallet",
            "general_ledger",
            "loan",
            "non_resident",
            "other",
            "overdraft",
            "polygon_wallet",
            "savings",
            "solana_wallet",
        ]
        | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        party_address: internal_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        vendor_attributes: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccount:
        """
        create internal account

        Args:
          connection_id: The identifier of the financial institution the account belongs to.

          currency: Either "USD" or "CAD". Internal accounts created at Increase only supports
              "USD".

          name: The nickname of the account.

          party_name: The legal name of the entity which owns the account.

          account_capabilities: An array of AccountCapability objects that list the originating abilities of the
              internal account and any relevant information for them.

          account_type: The account type, used to provision the appropriate account at the financial
              institution.

          counterparty_id: The Counterparty associated to this account.

          legal_entity_id: The LegalEntity associated to this account.

          parent_account_id: The parent internal account of this new account.

          party_address: The address associated with the owner or null.

          vendor_attributes: A hash of vendor specific attributes that will be used when creating the account
              at the vendor specified by the given connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/internal_accounts",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "currency": currency,
                    "name": name,
                    "party_name": party_name,
                    "account_capabilities": account_capabilities,
                    "account_type": account_type,
                    "counterparty_id": counterparty_id,
                    "legal_entity_id": legal_entity_id,
                    "parent_account_id": parent_account_id,
                    "party_address": party_address,
                    "vendor_attributes": vendor_attributes,
                },
                internal_account_create_params.InternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InternalAccount,
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
    ) -> InternalAccount:
        """
        get internal account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/internal_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InternalAccount,
        )

    async def update(
        self,
        id: str,
        *,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccount:
        """
        update internal account

        Args:
          counterparty_id: The Counterparty associated to this account.

          ledger_account_id: The Ledger Account associated to this account.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          name: The nickname for the internal account.

          parent_account_id: The parent internal account for this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/internal_accounts/{id}",
            body=await async_maybe_transform(
                {
                    "counterparty_id": counterparty_id,
                    "ledger_account_id": ledger_account_id,
                    "metadata": metadata,
                    "name": name,
                    "parent_account_id": parent_account_id,
                },
                internal_account_update_params.InternalAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InternalAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        currency: Currency | NotGiven = NOT_GIVEN,
        legal_entity_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_direction: TransactionDirection | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InternalAccount, AsyncPage[InternalAccount]]:
        """
        list internal accounts

        Args:
          counterparty_id: Only return internal accounts associated with this counterparty.

          currency: Only return internal accounts with this currency.

          legal_entity_id: Only return internal accounts associated with this legal entity.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          payment_direction: Only return internal accounts that can originate payments with this direction.

          payment_type: Only return internal accounts that can make this type of payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/internal_accounts",
            page=AsyncPage[InternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "currency": currency,
                        "legal_entity_id": legal_entity_id,
                        "metadata": metadata,
                        "payment_direction": payment_direction,
                        "payment_type": payment_type,
                        "per_page": per_page,
                    },
                    internal_account_list_params.InternalAccountListParams,
                ),
            ),
            model=InternalAccount,
        )

    async def update_account_capability(
        self,
        id: str,
        *,
        internal_account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccountUpdateAccountCapabilityResponse:
        """
        update account_capability

        Args:
          identifier: A unique reference assigned by your bank for tracking and recognizing payment
              files. It is important this is formatted exactly how the bank assigned it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not internal_account_id:
            raise ValueError(
                f"Expected a non-empty value for `internal_account_id` but received {internal_account_id!r}"
            )
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/internal_accounts/{internal_account_id}/account_capabilities/{id}",
            body=await async_maybe_transform(
                {"identifier": identifier},
                internal_account_update_account_capability_params.InternalAccountUpdateAccountCapabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InternalAccountUpdateAccountCapabilityResponse,
        )


class InternalAccountsWithRawResponse:
    def __init__(self, internal_accounts: InternalAccounts) -> None:
        self._internal_accounts = internal_accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            internal_accounts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            internal_accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            internal_accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            internal_accounts.list,
        )
        self.update_account_capability = _legacy_response.to_raw_response_wrapper(
            internal_accounts.update_account_capability,
        )

    @cached_property
    def balance_reports(self) -> BalanceReportsWithRawResponse:
        return BalanceReportsWithRawResponse(self._internal_accounts.balance_reports)


class AsyncInternalAccountsWithRawResponse:
    def __init__(self, internal_accounts: AsyncInternalAccounts) -> None:
        self._internal_accounts = internal_accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            internal_accounts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            internal_accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            internal_accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            internal_accounts.list,
        )
        self.update_account_capability = _legacy_response.async_to_raw_response_wrapper(
            internal_accounts.update_account_capability,
        )

    @cached_property
    def balance_reports(self) -> AsyncBalanceReportsWithRawResponse:
        return AsyncBalanceReportsWithRawResponse(self._internal_accounts.balance_reports)


class InternalAccountsWithStreamingResponse:
    def __init__(self, internal_accounts: InternalAccounts) -> None:
        self._internal_accounts = internal_accounts

        self.create = to_streamed_response_wrapper(
            internal_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            internal_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            internal_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            internal_accounts.list,
        )
        self.update_account_capability = to_streamed_response_wrapper(
            internal_accounts.update_account_capability,
        )

    @cached_property
    def balance_reports(self) -> BalanceReportsWithStreamingResponse:
        return BalanceReportsWithStreamingResponse(self._internal_accounts.balance_reports)


class AsyncInternalAccountsWithStreamingResponse:
    def __init__(self, internal_accounts: AsyncInternalAccounts) -> None:
        self._internal_accounts = internal_accounts

        self.create = async_to_streamed_response_wrapper(
            internal_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            internal_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            internal_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            internal_accounts.list,
        )
        self.update_account_capability = async_to_streamed_response_wrapper(
            internal_accounts.update_account_capability,
        )

    @cached_property
    def balance_reports(self) -> AsyncBalanceReportsWithStreamingResponse:
        return AsyncBalanceReportsWithStreamingResponse(self._internal_accounts.balance_reports)
