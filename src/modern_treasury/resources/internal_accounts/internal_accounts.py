# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from ...types import (
    InternalAccount,
    shared_params,
    internal_account_list_params,
    internal_account_create_params,
    internal_account_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .balance_reports import BalanceReports, AsyncBalanceReports

if TYPE_CHECKING:
    from ..._client import ModernTreasury, AsyncModernTreasury

__all__ = ["InternalAccounts", "AsyncInternalAccounts"]


class InternalAccounts(SyncAPIResource):
    balance_reports: BalanceReports

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.balance_reports = BalanceReports(client)

    def create(
        self,
        *,
        connection_id: str,
        currency: Literal["USD", "CAD"],
        name: str,
        party_name: str,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        party_address: internal_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        vendor_attributes: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          counterparty_id: The Counterparty associated to this account.

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
                    "counterparty_id": counterparty_id,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InternalAccount:
        """
        get internal account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccount:
        """
        update internal account

        Args:
          counterparty_id: The Counterparty associated to this account.

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
        return self._patch(
            f"/api/internal_accounts/{id}",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
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
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InternalAccount]:
        """
        list internal accounts

        Args:
          counterparty_id: The counterparty associated with the internal account.

          currency: The currency associated with the internal account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          payment_direction: The direction of payments that can be made by internal account.

          payment_type: The type of payment that can be made by the internal account.

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


class AsyncInternalAccounts(AsyncAPIResource):
    balance_reports: AsyncBalanceReports

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.balance_reports = AsyncBalanceReports(client)

    async def create(
        self,
        *,
        connection_id: str,
        currency: Literal["USD", "CAD"],
        name: str,
        party_name: str,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        party_address: internal_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        vendor_attributes: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          counterparty_id: The Counterparty associated to this account.

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
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "currency": currency,
                    "name": name,
                    "party_name": party_name,
                    "counterparty_id": counterparty_id,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InternalAccount:
        """
        get internal account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InternalAccount:
        """
        update internal account

        Args:
          counterparty_id: The Counterparty associated to this account.

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
        return await self._patch(
            f"/api/internal_accounts/{id}",
            body=maybe_transform(
                {
                    "counterparty_id": counterparty_id,
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
        currency: Optional[shared_params.Currency] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InternalAccount, AsyncPage[InternalAccount]]:
        """
        list internal accounts

        Args:
          counterparty_id: The counterparty associated with the internal account.

          currency: The currency associated with the internal account.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          payment_direction: The direction of payments that can be made by internal account.

          payment_type: The type of payment that can be made by the internal account.

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
