# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Any, Dict, List, Union, Optional, cast, overload
from typing_extensions import Literal

from ...types import ledger_transaction_create_params, ledger_transaction_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from ..._utils import required_args
from .versions import Versions, AsyncVersions
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ledger_transaction import LedgerTransaction
from ...types.ledger_transaction_list_params import LedgerTransactionListParams
from ...types.ledger_transaction_create_params import LedgerTransactionCreateParams
from ...types.ledger_transaction_update_params import LedgerTransactionUpdateParams

if TYPE_CHECKING:
    from ..._client import ModernTreasury, AsyncModernTreasury

__all__ = ["LedgerTransactions", "AsyncLedgerTransactions"]


class LedgerTransactions(SyncAPIResource):
    versions: Versions

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.versions = Versions(client)

    @overload
    def create(
        self,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_date: str,
        ledger_entries: List[ledger_transaction_create_params.LedgerEntries],
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Create a ledger transaction.

        Args:
          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          effective_date: The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
              purposes.

          ledger_entries: An array of ledger entry objects.

          external_id: A unique string to represent the ledger transaction. Only one pending or posted
              ledger transaction may have this ID in the ledger.

          ledgerable_type: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the type will be populated here, otherwise null. This can be one of
              payment_order, incoming_payment_detail, expected_payment, return, or reversal.

          ledgerable_id: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the id will be populated here, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: LedgerTransactionCreateParams,
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
    ) -> LedgerTransaction:
        """Create a ledger transaction."""
        ...

    @required_args(["body"], ["effective_date", "ledger_entries"])
    def create(
        self,
        body: LedgerTransactionCreateParams | None = None,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        ledger_entries: List[ledger_transaction_create_params.LedgerEntries] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Create a ledger transaction.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          effective_date: The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
              purposes.

          ledger_entries: An array of ledger entry objects.

          external_id: A unique string to represent the ledger transaction. Only one pending or posted
              ledger transaction may have this ID in the ledger.

          ledgerable_type: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the type will be populated here, otherwise null. This can be one of
              payment_order, incoming_payment_detail, expected_payment, return, or reversal.

          ledgerable_id: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the id will be populated here, otherwise null.

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
            # with the standard LedgerTransactionCreateParams type.
            body = cast(
                Any,
                {
                    "description": description,
                    "status": status,
                    "metadata": metadata,
                    "effective_date": effective_date,
                    "ledger_entries": ledger_entries,
                    "external_id": external_id,
                    "ledgerable_type": ledgerable_type,
                    "ledgerable_id": ledgerable_id,
                },
            )

        return self._post(
            "/api/ledger_transactions",
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
            cast_to=LedgerTransaction,
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
    ) -> LedgerTransaction:
        """Get details on a single ledger transaction."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/api/ledger_transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=LedgerTransaction,
        )

    @overload
    def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_entries: List[ledger_transaction_update_params.LedgerEntries] | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Update the details of a ledger transaction.

        Args:
          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          ledger_entries: An array of ledger entry objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def update(
        self,
        id: str,
        body: LedgerTransactionUpdateParams = {},
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
    ) -> LedgerTransaction:
        """Update the details of a ledger transaction."""
        ...

    def update(
        self,
        id: str,
        body: LedgerTransactionUpdateParams | None = None,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_entries: List[ledger_transaction_update_params.LedgerEntries] | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Update the details of a ledger transaction.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          ledger_entries: An array of ledger entry objects.

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
            # with the standard LedgerTransactionUpdateParams type.
            body = cast(
                Any,
                {
                    "description": description,
                    "status": status,
                    "metadata": metadata,
                    "ledger_entries": ledger_entries,
                },
            )

        return self._patch(
            f"/api/ledger_transactions/{id}",
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
            cast_to=LedgerTransaction,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, str] | NotGiven = NOT_GIVEN,
        posted_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LedgerTransaction]:
        """
        Get a list of ledger transactions.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          effective_date: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by
              effective date. For example, for all dates after Jan 1 2000, use
              effective_date%5Bgt%5D=2000-01-01.

          posted_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              posted_at%5Bgt%5D=2000-01-01T12:00:00Z.

          updated_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: LedgerTransactionListParams = {},
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
    ) -> SyncPage[LedgerTransaction]:
        """Get a list of ledger transactions."""
        ...

    def list(
        self,
        query: LedgerTransactionListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, str] | NotGiven = NOT_GIVEN,
        posted_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[LedgerTransaction]:
        """
        Get a list of ledger transactions.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          effective_date: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by
              effective date. For example, for all dates after Jan 1 2000, use
              effective_date%5Bgt%5D=2000-01-01.

          posted_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              posted_at%5Bgt%5D=2000-01-01T12:00:00Z.

          updated_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

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
            # with the standard LedgerTransactionListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "metadata": metadata,
                    "ledger_id": ledger_id,
                    "ledger_account_id": ledger_account_id,
                    "effective_date": effective_date,
                    "posted_at": posted_at,
                    "updated_at": updated_at,
                    "status": status,
                    "external_id": external_id,
                    "ledger_account_category_id": ledger_account_category_id,
                },
            )

        return self._get_api_list(
            "/api/ledger_transactions",
            page=SyncPage[LedgerTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=LedgerTransaction,
        )


class AsyncLedgerTransactions(AsyncAPIResource):
    versions: AsyncVersions

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.versions = AsyncVersions(client)

    @overload
    async def create(
        self,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_date: str,
        ledger_entries: List[ledger_transaction_create_params.LedgerEntries],
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Create a ledger transaction.

        Args:
          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          effective_date: The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
              purposes.

          ledger_entries: An array of ledger entry objects.

          external_id: A unique string to represent the ledger transaction. Only one pending or posted
              ledger transaction may have this ID in the ledger.

          ledgerable_type: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the type will be populated here, otherwise null. This can be one of
              payment_order, incoming_payment_detail, expected_payment, return, or reversal.

          ledgerable_id: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the id will be populated here, otherwise null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: LedgerTransactionCreateParams,
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
    ) -> LedgerTransaction:
        """Create a ledger transaction."""
        ...

    @required_args(["body"], ["effective_date", "ledger_entries"])
    async def create(
        self,
        body: LedgerTransactionCreateParams | None = None,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        ledger_entries: List[ledger_transaction_create_params.LedgerEntries] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledgerable_type: Literal[
            "counterparty",
            "expected_payment",
            "incoming_payment_detail",
            "internal_account",
            "line_item",
            "paper_item",
            "payment_order",
            "payment_order_attempt",
            "return",
            "reversal",
        ]
        | NotGiven = NOT_GIVEN,
        ledgerable_id: str | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Create a ledger transaction.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          effective_date: The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
              purposes.

          ledger_entries: An array of ledger entry objects.

          external_id: A unique string to represent the ledger transaction. Only one pending or posted
              ledger transaction may have this ID in the ledger.

          ledgerable_type: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the type will be populated here, otherwise null. This can be one of
              payment_order, incoming_payment_detail, expected_payment, return, or reversal.

          ledgerable_id: If the ledger transaction can be reconciled to another object in Modern
              Treasury, the id will be populated here, otherwise null.

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
            # with the standard LedgerTransactionCreateParams type.
            body = cast(
                Any,
                {
                    "description": description,
                    "status": status,
                    "metadata": metadata,
                    "effective_date": effective_date,
                    "ledger_entries": ledger_entries,
                    "external_id": external_id,
                    "ledgerable_type": ledgerable_type,
                    "ledgerable_id": ledgerable_id,
                },
            )

        return await self._post(
            "/api/ledger_transactions",
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
            cast_to=LedgerTransaction,
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
    ) -> LedgerTransaction:
        """Get details on a single ledger transaction."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/api/ledger_transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=LedgerTransaction,
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_entries: List[ledger_transaction_update_params.LedgerEntries] | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Update the details of a ledger transaction.

        Args:
          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          ledger_entries: An array of ledger entry objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        body: LedgerTransactionUpdateParams = {},
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
    ) -> LedgerTransaction:
        """Update the details of a ledger transaction."""
        ...

    async def update(
        self,
        id: str,
        body: LedgerTransactionUpdateParams | None = None,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["archived", "pending", "posted"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_entries: List[ledger_transaction_update_params.LedgerEntries] | NotGiven = NOT_GIVEN,
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
    ) -> LedgerTransaction:
        """
        Update the details of a ledger transaction.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          description: An optional description for internal use.

          status: To post a ledger transaction at creation, use `posted`.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          ledger_entries: An array of ledger entry objects.

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
            # with the standard LedgerTransactionUpdateParams type.
            body = cast(
                Any,
                {
                    "description": description,
                    "status": status,
                    "metadata": metadata,
                    "ledger_entries": ledger_entries,
                },
            )

        return await self._patch(
            f"/api/ledger_transactions/{id}",
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
            cast_to=LedgerTransaction,
        )

    @overload
    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, str] | NotGiven = NOT_GIVEN,
        posted_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerTransaction, AsyncPage[LedgerTransaction]]:
        """
        Get a list of ledger transactions.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          effective_date: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by
              effective date. For example, for all dates after Jan 1 2000, use
              effective_date%5Bgt%5D=2000-01-01.

          posted_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              posted_at%5Bgt%5D=2000-01-01T12:00:00Z.

          updated_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: LedgerTransactionListParams = {},
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
    ) -> AsyncPaginator[LedgerTransaction, AsyncPage[LedgerTransaction]]:
        """Get a list of ledger transactions."""
        ...

    def list(
        self,
        query: LedgerTransactionListParams | None = None,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        ledger_id: str | NotGiven = NOT_GIVEN,
        ledger_account_id: str | NotGiven = NOT_GIVEN,
        effective_date: Dict[str, str] | NotGiven = NOT_GIVEN,
        posted_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        updated_at: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "posted", "archived"] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ledger_account_category_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[LedgerTransaction, AsyncPage[LedgerTransaction]]:
        """
        Get a list of ledger transactions.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          effective_date: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by
              effective date. For example, for all dates after Jan 1 2000, use
              effective_date%5Bgt%5D=2000-01-01.

          posted_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              posted_at%5Bgt%5D=2000-01-01T12:00:00Z.

          updated_at: Use "gt" (>), "gte" (>=), "lt" (<), "lte" (<=), or "eq" (=) to filter by the
              posted at timestamp. For example, for all times after Jan 1 2000 12:00 UTC, use
              updated_at%5Bgt%5D=2000-01-01T12:00:00Z.

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
            # with the standard LedgerTransactionListParams type.
            query = cast(
                Any,
                {
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "metadata": metadata,
                    "ledger_id": ledger_id,
                    "ledger_account_id": ledger_account_id,
                    "effective_date": effective_date,
                    "posted_at": posted_at,
                    "updated_at": updated_at,
                    "status": status,
                    "external_id": external_id,
                    "ledger_account_category_id": ledger_account_category_id,
                },
            )

        return self._get_api_list(
            "/api/ledger_transactions",
            page=AsyncPage[LedgerTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=LedgerTransaction,
        )
