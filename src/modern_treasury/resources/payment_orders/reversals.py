# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payment_orders import (
    Reversal,
    reversal_list_params,
    reversal_create_params,
)

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
        ledger_transaction: reversal_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Reversal:
        """
        Create a reversal for a payment order.

        Args:
          payment_order_id: The id of the payment order being reversed.

          reason: The reason for the reversal. Must be one of `duplicate`, `incorrect_amount`,
              `incorrect_receiving_account`, `date_earlier_than_intended`,
              `date_later_than_intended`.

          ledger_transaction: Specifies a ledger transaction object that will be created with the reversal. If
              the ledger transaction cannot be created, then the reversal creation will fail.
              The resulting ledger transaction will mirror the status of the reversal.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/api/payment_orders/{payment_order_id}/reversals",
            body=maybe_transform(
                {
                    "reason": reason,
                    "ledger_transaction": ledger_transaction,
                    "metadata": metadata,
                },
                reversal_create_params.ReversalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Reversal:
        """
        Get details on a single reversal of a payment order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/payment_orders/{payment_order_id}/reversals/{reversal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Reversal]:
        """
        Get a list of all reversals of a payment order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=SyncPage[Reversal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                    },
                    reversal_list_params.ReversalListParams,
                ),
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
        ledger_transaction: reversal_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Reversal:
        """
        Create a reversal for a payment order.

        Args:
          payment_order_id: The id of the payment order being reversed.

          reason: The reason for the reversal. Must be one of `duplicate`, `incorrect_amount`,
              `incorrect_receiving_account`, `date_earlier_than_intended`,
              `date_later_than_intended`.

          ledger_transaction: Specifies a ledger transaction object that will be created with the reversal. If
              the ledger transaction cannot be created, then the reversal creation will fail.
              The resulting ledger transaction will mirror the status of the reversal.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/api/payment_orders/{payment_order_id}/reversals",
            body=maybe_transform(
                {
                    "reason": reason,
                    "ledger_transaction": ledger_transaction,
                    "metadata": metadata,
                },
                reversal_create_params.ReversalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Reversal:
        """
        Get details on a single reversal of a payment order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/payment_orders/{payment_order_id}/reversals/{reversal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Reversal, AsyncPage[Reversal]]:
        """
        Get a list of all reversals of a payment order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/api/payment_orders/{payment_order_id}/reversals",
            page=AsyncPage[Reversal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                    },
                    reversal_list_params.ReversalListParams,
                ),
            ),
            model=Reversal,
        )
