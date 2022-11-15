# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payment_orders import reversal_create_params
from ...types.payment_orders.reversal import Reversal

__all__ = ["Reversals", "AsyncReversals"]


class Reversals(SyncAPIResource):
    def create(
        self,
        payment_order_id: str,
        *,
        reason: Literal[
            "duplicate",
            "incorrect_amount",
            "incorrect_receiving_account",
            "date_earlier_than_intended",
            "date_later_than_intended",
        ],
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_transaction: reversal_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Reversal:
        """
        Create a reversal for a payment order.

        Args:
          reason: The reason for the reversal. Must be one of `duplicate`, `incorrect_amount`,
              `incorrect_receiving_account`, `date_earlier_than_intended`,
              `date_later_than_intended`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          ledger_transaction: Specifies a ledger transaction object that will be created with the reversal. If
              the ledger transaction cannot be created, then the reversal creation will fail.
              The resulting ledger transaction will mirror the status of the reversal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/api/payment_orders/{payment_order_id}/reversals",
            body={
                "reason": reason,
                "metadata": metadata,
                "ledger_transaction": ledger_transaction,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Reversal,
        )

    def retrieve(
        self,
        reversal_id: str,
        *,
        payment_order_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Reversal:
        """Get details on a single reversal of a payment order."""
        return self._get(
            f"/api/payment_orders/{payment_order_id}/reversals/{reversal_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Reversal,
        )

    def list(
        self,
        payment_order_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Reversal]:
        """
        Get a list of all reversals of a payment order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=SyncPage[Reversal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=Reversal,
        )


class AsyncReversals(AsyncAPIResource):
    async def create(
        self,
        payment_order_id: str,
        *,
        reason: Literal[
            "duplicate",
            "incorrect_amount",
            "incorrect_receiving_account",
            "date_earlier_than_intended",
            "date_later_than_intended",
        ],
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_transaction: reversal_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Reversal:
        """
        Create a reversal for a payment order.

        Args:
          reason: The reason for the reversal. Must be one of `duplicate`, `incorrect_amount`,
              `incorrect_receiving_account`, `date_earlier_than_intended`,
              `date_later_than_intended`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          ledger_transaction: Specifies a ledger transaction object that will be created with the reversal. If
              the ledger transaction cannot be created, then the reversal creation will fail.
              The resulting ledger transaction will mirror the status of the reversal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/api/payment_orders/{payment_order_id}/reversals",
            body={
                "reason": reason,
                "metadata": metadata,
                "ledger_transaction": ledger_transaction,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Reversal,
        )

    async def retrieve(
        self,
        reversal_id: str,
        *,
        payment_order_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Reversal:
        """Get details on a single reversal of a payment order."""
        return await self._get(
            f"/api/payment_orders/{payment_order_id}/reversals/{reversal_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Reversal,
        )

    def list(
        self,
        payment_order_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Reversal, AsyncPage[Reversal]]:
        """
        Get a list of all reversals of a payment order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=AsyncPage[Reversal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                },
            ),
            model=Reversal,
        )
