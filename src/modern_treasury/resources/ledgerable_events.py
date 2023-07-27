# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional

from ..types import LedgerableEvent, ledgerable_event_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["LedgerableEvents", "AsyncLedgerableEvents"]


class LedgerableEvents(SyncAPIResource):
    def create(
        self,
        *,
        amount: int,
        name: str,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        custom_data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerableEvent:
        """
        Translation missing:
        en.openapi.descriptions.ledger.operations.create_ledgerable_event

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          name: Name of the ledgerable event.

          currency: An ISO 4217 conformed currency or a custom currency.

          currency_exponent: Must be included if currency is a custom currency. The currency_exponent cannot
              exceed 30.

          custom_data: Additionally data to be used by the Ledger Event Handler.

          description: Description of the ledgerable event.

          direction: One of `credit`, `debit`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/ledgerable_events",
            body=maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "currency": currency,
                    "currency_exponent": currency_exponent,
                    "custom_data": custom_data,
                    "description": description,
                    "direction": direction,
                    "metadata": metadata,
                },
                ledgerable_event_create_params.LedgerableEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerableEvent,
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
    ) -> LedgerableEvent:
        """
        Get details on a single ledgerable event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/ledgerable_events/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerableEvent,
        )


class AsyncLedgerableEvents(AsyncAPIResource):
    async def create(
        self,
        *,
        amount: int,
        name: str,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        currency_exponent: Optional[int] | NotGiven = NOT_GIVEN,
        custom_data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        direction: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LedgerableEvent:
        """
        Translation missing:
        en.openapi.descriptions.ledger.operations.create_ledgerable_event

        Args:
          amount: Value in specified currency's smallest unit. e.g. $10 would be represented
              as 1000.

          name: Name of the ledgerable event.

          currency: An ISO 4217 conformed currency or a custom currency.

          currency_exponent: Must be included if currency is a custom currency. The currency_exponent cannot
              exceed 30.

          custom_data: Additionally data to be used by the Ledger Event Handler.

          description: Description of the ledgerable event.

          direction: One of `credit`, `debit`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/ledgerable_events",
            body=maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "currency": currency,
                    "currency_exponent": currency_exponent,
                    "custom_data": custom_data,
                    "description": description,
                    "direction": direction,
                    "metadata": metadata,
                },
                ledgerable_event_create_params.LedgerableEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LedgerableEvent,
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
    ) -> LedgerableEvent:
        """
        Get details on a single ledgerable event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/ledgerable_events/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerableEvent,
        )
