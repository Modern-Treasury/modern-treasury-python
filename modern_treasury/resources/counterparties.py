# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Dict, List, Union, Optional, cast, overload
from typing_extensions import Literal

from ..types import counterparty_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NoneType, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.counterparty import Counterparty
from ..types.counterparty_list_params import CounterpartyListParams
from ..types.counterparty_create_params import CounterpartyCreateParams
from ..types.counterparty_update_params import CounterpartyUpdateParams
from ..types.counterparty_collect_account_params import CounterpartyCollectAccountParams
from ..types.counterparty_collect_account_response import (
    CounterpartyCollectAccountResponse,
)

__all__ = ["Counterparties", "AsyncCounterparties"]


class Counterparties(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        name: Optional[str],
        accounts: List[counterparty_create_params.Accounts] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        accounting: counterparty_create_params.Accounting | NotGiven = NOT_GIVEN,
        ledger_type: Literal["customer", "vendor"] | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Create a new counterparty.

        Args:
          name: A human friendly name for this counterparty.

          accounts: The accounts for this counterparty.

          email: The counterparty's email.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          send_remittance_advice: Send an email to the counterparty whenever an associated payment order is sent
              to the bank.

          ledger_type: An optional type to auto-sync the counterparty to your ledger. Either `customer`
              or `vendor`.

          taxpayer_identifier: Either a valid SSN or EIN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: CounterpartyCreateParams,
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
    ) -> Counterparty:
        """Create a new counterparty."""
        ...

    @required_args(["body"], ["name"])
    def create(
        self,
        body: CounterpartyCreateParams | None = None,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        accounts: List[counterparty_create_params.Accounts] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        accounting: counterparty_create_params.Accounting | NotGiven = NOT_GIVEN,
        ledger_type: Literal["customer", "vendor"] | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Create a new counterparty.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          name: A human friendly name for this counterparty.

          accounts: The accounts for this counterparty.

          email: The counterparty's email.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          send_remittance_advice: Send an email to the counterparty whenever an associated payment order is sent
              to the bank.

          ledger_type: An optional type to auto-sync the counterparty to your ledger. Either `customer`
              or `vendor`.

          taxpayer_identifier: Either a valid SSN or EIN.

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
            # with the standard CounterpartyCreateParams type.
            body = cast(
                Any,
                {
                    "name": name,
                    "accounts": accounts,
                    "email": email,
                    "metadata": metadata,
                    "send_remittance_advice": send_remittance_advice,
                    "accounting": accounting,
                    "ledger_type": ledger_type,
                    "taxpayer_identifier": taxpayer_identifier,
                },
            )

        return self._post(
            "/api/counterparties",
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
            cast_to=Counterparty,
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
    ) -> Counterparty:
        """Get details on a single counterparty."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Counterparty,
        )

    @overload
    def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Updates a given counterparty with new information.

        Args:
          name: A new name for the counterparty. Will only update if passed.

          email: A new email for the counterparty.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          send_remittance_advice: If this is `true`, Modern Treasury will send an email to the counterparty
              whenever an associated payment order is sent to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def update(
        self,
        id: str,
        body: CounterpartyUpdateParams = {},
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
    ) -> Counterparty:
        """Updates a given counterparty with new information."""
        ...

    def update(
        self,
        id: str,
        body: CounterpartyUpdateParams | None = None,
        *,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Updates a given counterparty with new information.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          name: A new name for the counterparty. Will only update if passed.

          email: A new email for the counterparty.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          send_remittance_advice: If this is `true`, Modern Treasury will send an email to the counterparty
              whenever an associated payment order is sent to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

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
            # with the standard CounterpartyUpdateParams type.
            body = cast(
                Any,
                {
                    "name": name,
                    "email": email,
                    "metadata": metadata,
                    "send_remittance_advice": send_remittance_advice,
                    "taxpayer_identifier": taxpayer_identifier,
                },
            )

        return self._patch(
            f"/api/counterparties/{id}",
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
            cast_to=Counterparty,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: str | NotGiven = NOT_GIVEN,
        created_at_upper_bound: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Counterparty]:
        """
        Get a paginated list of all counterparties.

        Args:
          name: Performs a partial string match of the name field. This is also case
              insensitive.

          email: Performs a partial string match of the email field. This is also case
              insensitive.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          created_at_lower_bound: Used to return counterparties created after some datetime.

          created_at_upper_bound: Used to return counterparties created before some datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: CounterpartyListParams = {},
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
    ) -> SyncPage[Counterparty]:
        """Get a paginated list of all counterparties."""
        ...

    def list(
        self,
        query: CounterpartyListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: str | NotGiven = NOT_GIVEN,
        created_at_upper_bound: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Counterparty]:
        """
        Get a paginated list of all counterparties.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          name: Performs a partial string match of the name field. This is also case
              insensitive.

          email: Performs a partial string match of the email field. This is also case
              insensitive.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          created_at_lower_bound: Used to return counterparties created after some datetime.

          created_at_upper_bound: Used to return counterparties created before some datetime.

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
            # with the standard CounterpartyListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "name": name,
                    "email": email,
                    "metadata": metadata,
                    "created_at_lower_bound": created_at_lower_bound,
                    "created_at_upper_bound": created_at_upper_bound,
                },
            )

        return self._get_api_list(
            "/api/counterparties",
            page=SyncPage[Counterparty],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Counterparty,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Deletes a given counterparty."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=NoneType,
        )

    @overload
    def collect_account(
        self,
        id: str,
        *,
        direction: Literal["credit", "debit"],
        send_email: bool | NotGiven = NOT_GIVEN,
        fields: List[
            Literal[
                "name",
                "nameOnAccount",
                "taxpayerIdentifier",
                "accountType",
                "accountNumber",
                "ibanNumber",
                "clabeNumber",
                "walletAddress",
                "panNumber",
                "routingNumber",
                "abaWireRoutingNumber",
                "swiftCode",
                "auBsb",
                "caCpa",
                "cnaps",
                "gbSortCode",
                "inIfsc",
                "myBranchCode",
                "brCodigo",
                "routingNumberType",
                "address",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        custom_redirect: str | NotGiven = NOT_GIVEN,
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
    ) -> CounterpartyCollectAccountResponse:
        """
        Send an email requesting account details.

        Args:
          direction: One of `credit` or `debit`. Use `credit` when you want to pay a counterparty.
              Use `debit` when you need to charge a counterparty. This field helps us send a
              more tailored email to your counterparties."

          send_email: By default, Modern Treasury will send an email to your counterparty that
              includes a link to the form they must fill out. However, if you would like to
              send the counterparty the link, you can set this parameter to `false`. The JSON
              body will include the link to the secure Modern Treasury form.

          fields: The list of fields you want on the form. This field is optional and if it is not
              set, will default to [\"nameOnAccount\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\"]. The full list of options is [\"name\",
              \"nameOnAccount\", \"taxpayerIdentifier\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\", \"ibanNumber\", \"swiftCode\"].

          custom_redirect: The URL you want your customer to visit upon filling out the form. By default,
              they will be sent to a Modern Treasury landing page. This must be a valid HTTPS
              URL if set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def collect_account(
        self,
        id: str,
        body: CounterpartyCollectAccountParams,
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
    ) -> CounterpartyCollectAccountResponse:
        """Send an email requesting account details."""
        ...

    @required_args(["body"], ["direction"])
    def collect_account(
        self,
        id: str,
        body: CounterpartyCollectAccountParams | None = None,
        *,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        fields: List[
            Literal[
                "name",
                "nameOnAccount",
                "taxpayerIdentifier",
                "accountType",
                "accountNumber",
                "ibanNumber",
                "clabeNumber",
                "walletAddress",
                "panNumber",
                "routingNumber",
                "abaWireRoutingNumber",
                "swiftCode",
                "auBsb",
                "caCpa",
                "cnaps",
                "gbSortCode",
                "inIfsc",
                "myBranchCode",
                "brCodigo",
                "routingNumberType",
                "address",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        custom_redirect: str | NotGiven = NOT_GIVEN,
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
    ) -> CounterpartyCollectAccountResponse:
        """
        Send an email requesting account details.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          direction: One of `credit` or `debit`. Use `credit` when you want to pay a counterparty.
              Use `debit` when you need to charge a counterparty. This field helps us send a
              more tailored email to your counterparties."

          send_email: By default, Modern Treasury will send an email to your counterparty that
              includes a link to the form they must fill out. However, if you would like to
              send the counterparty the link, you can set this parameter to `false`. The JSON
              body will include the link to the secure Modern Treasury form.

          fields: The list of fields you want on the form. This field is optional and if it is not
              set, will default to [\"nameOnAccount\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\"]. The full list of options is [\"name\",
              \"nameOnAccount\", \"taxpayerIdentifier\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\", \"ibanNumber\", \"swiftCode\"].

          custom_redirect: The URL you want your customer to visit upon filling out the form. By default,
              they will be sent to a Modern Treasury landing page. This must be a valid HTTPS
              URL if set.

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
            # with the standard CounterpartyCollectAccountParams type.
            body = cast(
                Any,
                {
                    "direction": direction,
                    "send_email": send_email,
                    "fields": fields,
                    "custom_redirect": custom_redirect,
                },
            )

        return self._post(
            f"/api/counterparties/{id}/collect_account",
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
            cast_to=CounterpartyCollectAccountResponse,
        )


class AsyncCounterparties(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        name: Optional[str],
        accounts: List[counterparty_create_params.Accounts] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        accounting: counterparty_create_params.Accounting | NotGiven = NOT_GIVEN,
        ledger_type: Literal["customer", "vendor"] | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Create a new counterparty.

        Args:
          name: A human friendly name for this counterparty.

          accounts: The accounts for this counterparty.

          email: The counterparty's email.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          send_remittance_advice: Send an email to the counterparty whenever an associated payment order is sent
              to the bank.

          ledger_type: An optional type to auto-sync the counterparty to your ledger. Either `customer`
              or `vendor`.

          taxpayer_identifier: Either a valid SSN or EIN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: CounterpartyCreateParams,
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
    ) -> Counterparty:
        """Create a new counterparty."""
        ...

    @required_args(["body"], ["name"])
    async def create(
        self,
        body: CounterpartyCreateParams | None = None,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        accounts: List[counterparty_create_params.Accounts] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        accounting: counterparty_create_params.Accounting | NotGiven = NOT_GIVEN,
        ledger_type: Literal["customer", "vendor"] | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Create a new counterparty.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          name: A human friendly name for this counterparty.

          accounts: The accounts for this counterparty.

          email: The counterparty's email.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          send_remittance_advice: Send an email to the counterparty whenever an associated payment order is sent
              to the bank.

          ledger_type: An optional type to auto-sync the counterparty to your ledger. Either `customer`
              or `vendor`.

          taxpayer_identifier: Either a valid SSN or EIN.

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
            # with the standard CounterpartyCreateParams type.
            body = cast(
                Any,
                {
                    "name": name,
                    "accounts": accounts,
                    "email": email,
                    "metadata": metadata,
                    "send_remittance_advice": send_remittance_advice,
                    "accounting": accounting,
                    "ledger_type": ledger_type,
                    "taxpayer_identifier": taxpayer_identifier,
                },
            )

        return await self._post(
            "/api/counterparties",
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
            cast_to=Counterparty,
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
    ) -> Counterparty:
        """Get details on a single counterparty."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Counterparty,
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Updates a given counterparty with new information.

        Args:
          name: A new name for the counterparty. Will only update if passed.

          email: A new email for the counterparty.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          send_remittance_advice: If this is `true`, Modern Treasury will send an email to the counterparty
              whenever an associated payment order is sent to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        body: CounterpartyUpdateParams = {},
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
    ) -> Counterparty:
        """Updates a given counterparty with new information."""
        ...

    async def update(
        self,
        id: str,
        body: CounterpartyUpdateParams | None = None,
        *,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: bool | NotGiven = NOT_GIVEN,
        taxpayer_identifier: str | NotGiven = NOT_GIVEN,
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
    ) -> Counterparty:
        """
        Updates a given counterparty with new information.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          name: A new name for the counterparty. Will only update if passed.

          email: A new email for the counterparty.

          metadata: Additional data in the form of key-value pairs. Pairs can be removed by passing
              an empty string or `null` as the value.

          send_remittance_advice: If this is `true`, Modern Treasury will send an email to the counterparty
              whenever an associated payment order is sent to the bank.

          taxpayer_identifier: Either a valid SSN or EIN.

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
            # with the standard CounterpartyUpdateParams type.
            body = cast(
                Any,
                {
                    "name": name,
                    "email": email,
                    "metadata": metadata,
                    "send_remittance_advice": send_remittance_advice,
                    "taxpayer_identifier": taxpayer_identifier,
                },
            )

        return await self._patch(
            f"/api/counterparties/{id}",
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
            cast_to=Counterparty,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: str | NotGiven = NOT_GIVEN,
        created_at_upper_bound: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Counterparty, AsyncPage[Counterparty]]:
        """
        Get a paginated list of all counterparties.

        Args:
          name: Performs a partial string match of the name field. This is also case
              insensitive.

          email: Performs a partial string match of the email field. This is also case
              insensitive.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          created_at_lower_bound: Used to return counterparties created after some datetime.

          created_at_upper_bound: Used to return counterparties created before some datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: CounterpartyListParams = {},
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
    ) -> AsyncPaginator[Counterparty, AsyncPage[Counterparty]]:
        """Get a paginated list of all counterparties."""
        ...

    def list(
        self,
        query: CounterpartyListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        created_at_lower_bound: str | NotGiven = NOT_GIVEN,
        created_at_upper_bound: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Counterparty, AsyncPage[Counterparty]]:
        """
        Get a paginated list of all counterparties.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          name: Performs a partial string match of the name field. This is also case
              insensitive.

          email: Performs a partial string match of the email field. This is also case
              insensitive.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          created_at_lower_bound: Used to return counterparties created after some datetime.

          created_at_upper_bound: Used to return counterparties created before some datetime.

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
            # with the standard CounterpartyListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "name": name,
                    "email": email,
                    "metadata": metadata,
                    "created_at_lower_bound": created_at_lower_bound,
                    "created_at_upper_bound": created_at_upper_bound,
                },
            )

        return self._get_api_list(
            "/api/counterparties",
            page=AsyncPage[Counterparty],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Counterparty,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> None:
        """Deletes a given counterparty."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/counterparties/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=NoneType,
        )

    @overload
    async def collect_account(
        self,
        id: str,
        *,
        direction: Literal["credit", "debit"],
        send_email: bool | NotGiven = NOT_GIVEN,
        fields: List[
            Literal[
                "name",
                "nameOnAccount",
                "taxpayerIdentifier",
                "accountType",
                "accountNumber",
                "ibanNumber",
                "clabeNumber",
                "walletAddress",
                "panNumber",
                "routingNumber",
                "abaWireRoutingNumber",
                "swiftCode",
                "auBsb",
                "caCpa",
                "cnaps",
                "gbSortCode",
                "inIfsc",
                "myBranchCode",
                "brCodigo",
                "routingNumberType",
                "address",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        custom_redirect: str | NotGiven = NOT_GIVEN,
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
    ) -> CounterpartyCollectAccountResponse:
        """
        Send an email requesting account details.

        Args:
          direction: One of `credit` or `debit`. Use `credit` when you want to pay a counterparty.
              Use `debit` when you need to charge a counterparty. This field helps us send a
              more tailored email to your counterparties."

          send_email: By default, Modern Treasury will send an email to your counterparty that
              includes a link to the form they must fill out. However, if you would like to
              send the counterparty the link, you can set this parameter to `false`. The JSON
              body will include the link to the secure Modern Treasury form.

          fields: The list of fields you want on the form. This field is optional and if it is not
              set, will default to [\"nameOnAccount\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\"]. The full list of options is [\"name\",
              \"nameOnAccount\", \"taxpayerIdentifier\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\", \"ibanNumber\", \"swiftCode\"].

          custom_redirect: The URL you want your customer to visit upon filling out the form. By default,
              they will be sent to a Modern Treasury landing page. This must be a valid HTTPS
              URL if set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def collect_account(
        self,
        id: str,
        body: CounterpartyCollectAccountParams,
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
    ) -> CounterpartyCollectAccountResponse:
        """Send an email requesting account details."""
        ...

    @required_args(["body"], ["direction"])
    async def collect_account(
        self,
        id: str,
        body: CounterpartyCollectAccountParams | None = None,
        *,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        fields: List[
            Literal[
                "name",
                "nameOnAccount",
                "taxpayerIdentifier",
                "accountType",
                "accountNumber",
                "ibanNumber",
                "clabeNumber",
                "walletAddress",
                "panNumber",
                "routingNumber",
                "abaWireRoutingNumber",
                "swiftCode",
                "auBsb",
                "caCpa",
                "cnaps",
                "gbSortCode",
                "inIfsc",
                "myBranchCode",
                "brCodigo",
                "routingNumberType",
                "address",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        custom_redirect: str | NotGiven = NOT_GIVEN,
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
    ) -> CounterpartyCollectAccountResponse:
        """
        Send an email requesting account details.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          direction: One of `credit` or `debit`. Use `credit` when you want to pay a counterparty.
              Use `debit` when you need to charge a counterparty. This field helps us send a
              more tailored email to your counterparties."

          send_email: By default, Modern Treasury will send an email to your counterparty that
              includes a link to the form they must fill out. However, if you would like to
              send the counterparty the link, you can set this parameter to `false`. The JSON
              body will include the link to the secure Modern Treasury form.

          fields: The list of fields you want on the form. This field is optional and if it is not
              set, will default to [\"nameOnAccount\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\"]. The full list of options is [\"name\",
              \"nameOnAccount\", \"taxpayerIdentifier\", \"accountType\", \"accountNumber\",
              \"routingNumber\", \"address\", \"ibanNumber\", \"swiftCode\"].

          custom_redirect: The URL you want your customer to visit upon filling out the form. By default,
              they will be sent to a Modern Treasury landing page. This must be a valid HTTPS
              URL if set.

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
            # with the standard CounterpartyCollectAccountParams type.
            body = cast(
                Any,
                {
                    "direction": direction,
                    "send_email": send_email,
                    "fields": fields,
                    "custom_redirect": custom_redirect,
                },
            )

        return await self._post(
            f"/api/counterparties/{id}/collect_account",
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
            cast_to=CounterpartyCollectAccountResponse,
        )
