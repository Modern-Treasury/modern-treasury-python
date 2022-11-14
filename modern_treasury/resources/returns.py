# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.return_object import ReturnObject
from ..types.return_list_params import ReturnListParams
from ..types.return_create_params import ReturnCreateParams

__all__ = ["Returns", "AsyncReturns"]


class Returns(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        returnable_id: Optional[str],
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
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        date_of_death: Optional[str] | NotGiven = NOT_GIVEN,
        additional_information: Optional[str] | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """
        Create a return.

        Args:
          returnable_id: The ID of the object being returned or `null`.

          code: The return code. For ACH returns, this is the required ACH return code.

          reason: An optional description of the reason for the return. This is for internal usage
              and will not be transmitted to the bank.”

          date_of_death: If the return code is `R14` or `R15` this is the date the deceased counterparty
              passed away.

          additional_information: Some returns may include additional information from the bank. In these cases,
              this string will be present.

          returnable_type: The type of object being returned. Currently, this may only be
              incoming_payment_detail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: ReturnCreateParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Create a return."""
        ...

    @required_args(["body"], ["returnable_id", "returnable_type"])
    def create(
        self,
        body: ReturnCreateParams | None = None,
        *,
        returnable_id: Optional[str] | NotGiven = NOT_GIVEN,
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
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        date_of_death: Optional[str] | NotGiven = NOT_GIVEN,
        additional_information: Optional[str] | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """
        Create a return.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          returnable_id: The ID of the object being returned or `null`.

          code: The return code. For ACH returns, this is the required ACH return code.

          reason: An optional description of the reason for the return. This is for internal usage
              and will not be transmitted to the bank.”

          date_of_death: If the return code is `R14` or `R15` this is the date the deceased counterparty
              passed away.

          additional_information: Some returns may include additional information from the bank. In these cases,
              this string will be present.

          returnable_type: The type of object being returned. Currently, this may only be
              incoming_payment_detail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ReturnCreateParams type.
            body = cast(
                Any,
                {
                    "returnable_id": returnable_id,
                    "code": code,
                    "reason": reason,
                    "date_of_death": date_of_death,
                    "additional_information": additional_information,
                    "returnable_type": returnable_type,
                },
            )

        return self._post(
            "/api/returns",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Get a single return."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/returns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ReturnObject,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        returnable_id: str | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail", "paper_item", "payment_order", "reversal"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ReturnObject]:
        """
        Get a list of returns.

        Args:
          internal_account_id: Specify `internal_account_id` if you wish to see returns to/from a specific
              account.

          counterparty_id: Specify `counterparty_id` if you wish to see returns that occurred with a
              specific counterparty.

          returnable_id: The ID of a valid returnable. Must be accompanied by `returnable_type`.

          returnable_type: One of `payment_order`, `paper_item`, `reversal`, or `incoming_payment_detail`.
              Must be accompanied by `returnable_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: ReturnListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ReturnObject]:
        """Get a list of returns."""
        ...

    def list(
        self,
        query: ReturnListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        returnable_id: str | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail", "paper_item", "payment_order", "reversal"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ReturnObject]:
        """
        Get a list of returns.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          internal_account_id: Specify `internal_account_id` if you wish to see returns to/from a specific
              account.

          counterparty_id: Specify `counterparty_id` if you wish to see returns that occurred with a
              specific counterparty.

          returnable_id: The ID of a valid returnable. Must be accompanied by `returnable_type`.

          returnable_type: One of `payment_order`, `paper_item`, `reversal`, or `incoming_payment_detail`.
              Must be accompanied by `returnable_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ReturnListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "internal_account_id": internal_account_id,
                    "counterparty_id": counterparty_id,
                    "returnable_id": returnable_id,
                    "returnable_type": returnable_type,
                },
            )

        return self._get_api_list(
            "/api/returns",
            page=SyncPage[ReturnObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=ReturnObject,
        )


class AsyncReturns(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        returnable_id: Optional[str],
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
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        date_of_death: Optional[str] | NotGiven = NOT_GIVEN,
        additional_information: Optional[str] | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """
        Create a return.

        Args:
          returnable_id: The ID of the object being returned or `null`.

          code: The return code. For ACH returns, this is the required ACH return code.

          reason: An optional description of the reason for the return. This is for internal usage
              and will not be transmitted to the bank.”

          date_of_death: If the return code is `R14` or `R15` this is the date the deceased counterparty
              passed away.

          additional_information: Some returns may include additional information from the bank. In these cases,
              this string will be present.

          returnable_type: The type of object being returned. Currently, this may only be
              incoming_payment_detail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: ReturnCreateParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Create a return."""
        ...

    @required_args(["body"], ["returnable_id", "returnable_type"])
    async def create(
        self,
        body: ReturnCreateParams | None = None,
        *,
        returnable_id: Optional[str] | NotGiven = NOT_GIVEN,
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
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        date_of_death: Optional[str] | NotGiven = NOT_GIVEN,
        additional_information: Optional[str] | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """
        Create a return.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          returnable_id: The ID of the object being returned or `null`.

          code: The return code. For ACH returns, this is the required ACH return code.

          reason: An optional description of the reason for the return. This is for internal usage
              and will not be transmitted to the bank.”

          date_of_death: If the return code is `R14` or `R15` this is the date the deceased counterparty
              passed away.

          additional_information: Some returns may include additional information from the bank. In these cases,
              this string will be present.

          returnable_type: The type of object being returned. Currently, this may only be
              incoming_payment_detail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ReturnCreateParams type.
            body = cast(
                Any,
                {
                    "returnable_id": returnable_id,
                    "code": code,
                    "reason": reason,
                    "date_of_death": date_of_death,
                    "additional_information": additional_information,
                    "returnable_type": returnable_type,
                },
            )

        return await self._post(
            "/api/returns",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ReturnObject:
        """Get a single return."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/returns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ReturnObject,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        returnable_id: str | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail", "paper_item", "payment_order", "reversal"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ReturnObject, AsyncPage[ReturnObject]]:
        """
        Get a list of returns.

        Args:
          internal_account_id: Specify `internal_account_id` if you wish to see returns to/from a specific
              account.

          counterparty_id: Specify `counterparty_id` if you wish to see returns that occurred with a
              specific counterparty.

          returnable_id: The ID of a valid returnable. Must be accompanied by `returnable_type`.

          returnable_type: One of `payment_order`, `paper_item`, `reversal`, or `incoming_payment_detail`.
              Must be accompanied by `returnable_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: ReturnListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ReturnObject, AsyncPage[ReturnObject]]:
        """Get a list of returns."""
        ...

    def list(
        self,
        query: ReturnListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        internal_account_id: str | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        returnable_id: str | NotGiven = NOT_GIVEN,
        returnable_type: Literal["incoming_payment_detail", "paper_item", "payment_order", "reversal"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ReturnObject, AsyncPage[ReturnObject]]:
        """
        Get a list of returns.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          internal_account_id: Specify `internal_account_id` if you wish to see returns to/from a specific
              account.

          counterparty_id: Specify `counterparty_id` if you wish to see returns that occurred with a
              specific counterparty.

          returnable_id: The ID of a valid returnable. Must be accompanied by `returnable_type`.

          returnable_type: One of `payment_order`, `paper_item`, `reversal`, or `incoming_payment_detail`.
              Must be accompanied by `returnable_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ReturnListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "internal_account_id": internal_account_id,
                    "counterparty_id": counterparty_id,
                    "returnable_id": returnable_id,
                    "returnable_type": returnable_type,
                },
            )

        return self._get_api_list(
            "/api/returns",
            page=AsyncPage[ReturnObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=ReturnObject,
        )
