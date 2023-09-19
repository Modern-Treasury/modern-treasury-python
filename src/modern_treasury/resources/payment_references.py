# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import typing_extensions
from typing import Optional
from typing_extensions import Literal

from ..types import PaymentReference, payment_reference_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["PaymentReferences", "AsyncPaymentReferences"]


class PaymentReferences(SyncAPIResource):
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
    ) -> PaymentReference:
        """
        get payment_reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/payment_references/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentReference,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        reference_number: str | NotGiven = NOT_GIVEN,
        referenceable_id: str | NotGiven = NOT_GIVEN,
        referenceable_type: Literal["payment_order", "return", "reversal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PaymentReference]:
        """
        list payment_references

        Args:
          reference_number: The actual reference number assigned by the bank.

          referenceable_id: The id of the referenceable to search for. Must be accompanied by the
              referenceable_type or will return an error.

          referenceable_type: One of the referenceable types. This must be accompanied by the id of the
              referenceable or will return an error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_references",
            page=SyncPage[PaymentReference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "reference_number": reference_number,
                        "referenceable_id": referenceable_id,
                        "referenceable_type": referenceable_type,
                    },
                    payment_reference_list_params.PaymentReferenceListParams,
                ),
            ),
            model=PaymentReference,
        )

    @typing_extensions.deprecated("use `retrieve` instead")
    def retireve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PaymentReference:
        """
        get payment_reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.retrieve(
            id=id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )


class AsyncPaymentReferences(AsyncAPIResource):
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
    ) -> PaymentReference:
        """
        get payment_reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/payment_references/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentReference,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        reference_number: str | NotGiven = NOT_GIVEN,
        referenceable_id: str | NotGiven = NOT_GIVEN,
        referenceable_type: Literal["payment_order", "return", "reversal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PaymentReference, AsyncPage[PaymentReference]]:
        """
        list payment_references

        Args:
          reference_number: The actual reference number assigned by the bank.

          referenceable_id: The id of the referenceable to search for. Must be accompanied by the
              referenceable_type or will return an error.

          referenceable_type: One of the referenceable types. This must be accompanied by the id of the
              referenceable or will return an error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/payment_references",
            page=AsyncPage[PaymentReference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "reference_number": reference_number,
                        "referenceable_id": referenceable_id,
                        "referenceable_type": referenceable_type,
                    },
                    payment_reference_list_params.PaymentReferenceListParams,
                ),
            ),
            model=PaymentReference,
        )

    @typing_extensions.deprecated("use `retrieve` instead")
    async def retireve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PaymentReference:
        """
        get payment_reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.retrieve(
            id=id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
