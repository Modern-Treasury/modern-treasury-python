# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import date
from typing_extensions import Literal

from ..types import ReturnObject, return_list_params, return_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import ModernTreasury, AsyncModernTreasury

__all__ = ["Returns", "AsyncReturns"]


class Returns(SyncAPIResource):
    with_raw_response: ReturnsWithRawResponse

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = ReturnsWithRawResponse(self)

    def create(
        self,
        *,
        returnable_id: Optional[str],
        returnable_type: Literal["incoming_payment_detail"],
        additional_information: Optional[str] | NotGiven = NOT_GIVEN,
        code: Optional[
            Literal[
                "901",
                "902",
                "903",
                "904",
                "905",
                "907",
                "908",
                "909",
                "910",
                "911",
                "912",
                "914",
                "R01",
                "R02",
                "R03",
                "R04",
                "R05",
                "R06",
                "R07",
                "R08",
                "R09",
                "R10",
                "R11",
                "R12",
                "R14",
                "R15",
                "R16",
                "R17",
                "R20",
                "R21",
                "R22",
                "R23",
                "R24",
                "R29",
                "R31",
                "R33",
                "R37",
                "R38",
                "R39",
                "R51",
                "R52",
                "R53",
                "currencycloud",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_of_death: Union[str, date, None] | NotGiven = NOT_GIVEN,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ReturnObject:
        """
        Create a return.

        Args:
          returnable_id: The ID of the object being returned or `null`.

          returnable_type: The type of object being returned. Currently, this may only be
              incoming_payment_detail.

          additional_information: Some returns may include additional information from the bank. In these cases,
              this string will be present.

          code: The return code. For ACH returns, this is the required ACH return code.

          date_of_death: If the return code is `R14` or `R15` this is the date the deceased counterparty
              passed away.

          reason: An optional description of the reason for the return. This is for internal usage
              and will not be transmitted to the bank.”

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/returns",
            body=maybe_transform(
                {
                    "returnable_id": returnable_id,
                    "returnable_type": returnable_type,
                    "additional_information": additional_information,
                    "code": code,
                    "date_of_death": date_of_death,
                    "reason": reason,
                },
                return_create_params.ReturnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ReturnObject,
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
    ) -> ReturnObject:
        """
        Get a single return.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/returns/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnObject,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        returnable_id: str | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail", "paper_item", "payment_order", "return", "reversal"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ReturnObject]:
        """
        Get a list of returns.

        Args:
          counterparty_id: Specify `counterparty_id` if you wish to see returns that occurred with a
              specific counterparty.

          internal_account_id: Specify `internal_account_id` if you wish to see returns to/from a specific
              account.

          returnable_id: The ID of a valid returnable. Must be accompanied by `returnable_type`.

          returnable_type: One of `payment_order`, `paper_item`, `reversal`, or `incoming_payment_detail`.
              Must be accompanied by `returnable_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/returns",
            page=SyncPage[ReturnObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "internal_account_id": internal_account_id,
                        "per_page": per_page,
                        "returnable_id": returnable_id,
                        "returnable_type": returnable_type,
                    },
                    return_list_params.ReturnListParams,
                ),
            ),
            model=ReturnObject,
        )


class AsyncReturns(AsyncAPIResource):
    with_raw_response: AsyncReturnsWithRawResponse

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncReturnsWithRawResponse(self)

    async def create(
        self,
        *,
        returnable_id: Optional[str],
        returnable_type: Literal["incoming_payment_detail"],
        additional_information: Optional[str] | NotGiven = NOT_GIVEN,
        code: Optional[
            Literal[
                "901",
                "902",
                "903",
                "904",
                "905",
                "907",
                "908",
                "909",
                "910",
                "911",
                "912",
                "914",
                "R01",
                "R02",
                "R03",
                "R04",
                "R05",
                "R06",
                "R07",
                "R08",
                "R09",
                "R10",
                "R11",
                "R12",
                "R14",
                "R15",
                "R16",
                "R17",
                "R20",
                "R21",
                "R22",
                "R23",
                "R24",
                "R29",
                "R31",
                "R33",
                "R37",
                "R38",
                "R39",
                "R51",
                "R52",
                "R53",
                "currencycloud",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_of_death: Union[str, date, None] | NotGiven = NOT_GIVEN,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ReturnObject:
        """
        Create a return.

        Args:
          returnable_id: The ID of the object being returned or `null`.

          returnable_type: The type of object being returned. Currently, this may only be
              incoming_payment_detail.

          additional_information: Some returns may include additional information from the bank. In these cases,
              this string will be present.

          code: The return code. For ACH returns, this is the required ACH return code.

          date_of_death: If the return code is `R14` or `R15` this is the date the deceased counterparty
              passed away.

          reason: An optional description of the reason for the return. This is for internal usage
              and will not be transmitted to the bank.”

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/returns",
            body=maybe_transform(
                {
                    "returnable_id": returnable_id,
                    "returnable_type": returnable_type,
                    "additional_information": additional_information,
                    "code": code,
                    "date_of_death": date_of_death,
                    "reason": reason,
                },
                return_create_params.ReturnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ReturnObject,
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
    ) -> ReturnObject:
        """
        Get a single return.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/returns/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnObject,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        returnable_id: str | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail", "paper_item", "payment_order", "return", "reversal"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ReturnObject, AsyncPage[ReturnObject]]:
        """
        Get a list of returns.

        Args:
          counterparty_id: Specify `counterparty_id` if you wish to see returns that occurred with a
              specific counterparty.

          internal_account_id: Specify `internal_account_id` if you wish to see returns to/from a specific
              account.

          returnable_id: The ID of a valid returnable. Must be accompanied by `returnable_type`.

          returnable_type: One of `payment_order`, `paper_item`, `reversal`, or `incoming_payment_detail`.
              Must be accompanied by `returnable_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/returns",
            page=AsyncPage[ReturnObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "counterparty_id": counterparty_id,
                        "internal_account_id": internal_account_id,
                        "per_page": per_page,
                        "returnable_id": returnable_id,
                        "returnable_type": returnable_type,
                    },
                    return_list_params.ReturnListParams,
                ),
            ),
            model=ReturnObject,
        )


class ReturnsWithRawResponse:
    def __init__(self, returns: Returns) -> None:
        self.create = to_raw_response_wrapper(
            returns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            returns.retrieve,
        )
        self.list = to_raw_response_wrapper(
            returns.list,
        )


class AsyncReturnsWithRawResponse:
    def __init__(self, returns: AsyncReturns) -> None:
        self.create = async_to_raw_response_wrapper(
            returns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            returns.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            returns.list,
        )
