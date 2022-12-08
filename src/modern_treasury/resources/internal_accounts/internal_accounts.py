# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from ...types import shared_params, internal_account_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .balance_reports import BalanceReports, AsyncBalanceReports
from ...types.internal_account import InternalAccount

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
        name: str,
        party_name: str,
        party_address: internal_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        currency: Literal["USD", "CAD"],
        entity_id: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InternalAccount:
        """
        Args:
          connection_id: The identifier of the financial institution the account belongs to.

          name: The nickname of the account.

          party_name: The legal name of the entity which owns the account.

          party_address: The address associated with the owner or null.

          currency: Either "USD" or "CAD". Internal accounts created at Increase only supports
              "USD".

          entity_id: The identifier of the entity at Increase which owns the account.

          parent_account_id: The parent internal account of this new account.

          counterparty_id: The Counterparty associated to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/api/internal_accounts",
            body={
                "connection_id": connection_id,
                "name": name,
                "party_name": party_name,
                "party_address": party_address,
                "currency": currency,
                "entity_id": entity_id,
                "parent_account_id": parent_account_id,
                "counterparty_id": counterparty_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> InternalAccount:
        return self._get(
            f"/api/internal_accounts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InternalAccount,
        )

    def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InternalAccount:
        """
        Args:
          name: The nickname for the internal account.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          parent_account_id: The parent internal account for this account.

          counterparty_id: The Counterparty associated to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/api/internal_accounts/{id}",
            body={
                "name": name,
                "metadata": metadata,
                "parent_account_id": parent_account_id,
                "counterparty_id": counterparty_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InternalAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        currency: shared_params.Currency | NotGiven = NOT_GIVEN,
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
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        payment_direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[InternalAccount]:
        """
        Args:
          currency: The currency associated with the internal account.

          payment_type: The type of payment that can be made by the internal account.

          payment_direction: The direction of payments that can be made by internal account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/internal_accounts",
            page=SyncPage[InternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "currency": currency,
                    "payment_type": payment_type,
                    "payment_direction": payment_direction,
                },
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
        name: str,
        party_name: str,
        party_address: internal_account_create_params.PartyAddress | NotGiven = NOT_GIVEN,
        currency: Literal["USD", "CAD"],
        entity_id: str | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InternalAccount:
        """
        Args:
          connection_id: The identifier of the financial institution the account belongs to.

          name: The nickname of the account.

          party_name: The legal name of the entity which owns the account.

          party_address: The address associated with the owner or null.

          currency: Either "USD" or "CAD". Internal accounts created at Increase only supports
              "USD".

          entity_id: The identifier of the entity at Increase which owns the account.

          parent_account_id: The parent internal account of this new account.

          counterparty_id: The Counterparty associated to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/api/internal_accounts",
            body={
                "connection_id": connection_id,
                "name": name,
                "party_name": party_name,
                "party_address": party_address,
                "currency": currency,
                "entity_id": entity_id,
                "parent_account_id": parent_account_id,
                "counterparty_id": counterparty_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> InternalAccount:
        return await self._get(
            f"/api/internal_accounts/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InternalAccount,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        parent_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InternalAccount:
        """
        Args:
          name: The nickname for the internal account.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          parent_account_id: The parent internal account for this account.

          counterparty_id: The Counterparty associated to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/api/internal_accounts/{id}",
            body={
                "name": name,
                "metadata": metadata,
                "parent_account_id": parent_account_id,
                "counterparty_id": counterparty_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InternalAccount,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        currency: shared_params.Currency | NotGiven = NOT_GIVEN,
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
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        payment_direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[InternalAccount, AsyncPage[InternalAccount]]:
        """
        Args:
          currency: The currency associated with the internal account.

          payment_type: The type of payment that can be made by the internal account.

          payment_direction: The direction of payments that can be made by internal account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/internal_accounts",
            page=AsyncPage[InternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "currency": currency,
                    "payment_type": payment_type,
                    "payment_direction": payment_direction,
                },
            ),
            model=InternalAccount,
        )
