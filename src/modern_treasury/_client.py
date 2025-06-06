# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions, _legacy_response
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ModernTreasuryError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.ping_response import PingResponse

if TYPE_CHECKING:
    from .resources import (
        events,
        ledgers,
        returns,
        invoices,
        webhooks,
        documents,
        line_items,
        connections,
        paper_items,
        validations,
        bulk_results,
        transactions,
        bulk_requests,
        payment_flows,
        counterparties,
        ledger_entries,
        legal_entities,
        payment_orders,
        account_details,
        ledger_accounts,
        payment_actions,
        routing_details,
        virtual_accounts,
        expected_payments,
        external_accounts,
        internal_accounts,
        payment_references,
        ledger_transactions,
        foreign_exchange_quotes,
        account_collection_flows,
        incoming_payment_details,
        connection_legal_entities,
        ledger_account_categories,
        ledger_account_statements,
        legal_entity_associations,
        ledger_account_settlements,
        ledger_account_balance_monitors,
    )
    from .resources.events import Events, AsyncEvents
    from .resources.ledgers import Ledgers, AsyncLedgers
    from .resources.returns import Returns, AsyncReturns
    from .resources.documents import Documents, AsyncDocuments
    from .resources.line_items import LineItems, AsyncLineItems
    from .resources.connections import Connections, AsyncConnections
    from .resources.paper_items import PaperItems, AsyncPaperItems
    from .resources.validations import Validations, AsyncValidations
    from .resources.bulk_results import BulkResults, AsyncBulkResults
    from .resources.bulk_requests import BulkRequests, AsyncBulkRequests
    from .resources.payment_flows import PaymentFlows, AsyncPaymentFlows
    from .resources.counterparties import Counterparties, AsyncCounterparties
    from .resources.ledger_entries import LedgerEntries, AsyncLedgerEntries
    from .resources.legal_entities import LegalEntities, AsyncLegalEntities
    from .resources.account_details import AccountDetails, AsyncAccountDetails
    from .resources.ledger_accounts import LedgerAccounts, AsyncLedgerAccounts
    from .resources.payment_actions import PaymentActions, AsyncPaymentActions
    from .resources.routing_details import RoutingDetails, AsyncRoutingDetails
    from .resources.virtual_accounts import VirtualAccounts, AsyncVirtualAccounts
    from .resources.expected_payments import ExpectedPayments, AsyncExpectedPayments
    from .resources.external_accounts import ExternalAccounts, AsyncExternalAccounts
    from .resources.invoices.invoices import Invoices, AsyncInvoices
    from .resources.payment_references import PaymentReferences, AsyncPaymentReferences
    from .resources.foreign_exchange_quotes import ForeignExchangeQuotes, AsyncForeignExchangeQuotes
    from .resources.account_collection_flows import AccountCollectionFlows, AsyncAccountCollectionFlows
    from .resources.incoming_payment_details import IncomingPaymentDetails, AsyncIncomingPaymentDetails
    from .resources.connection_legal_entities import ConnectionLegalEntities, AsyncConnectionLegalEntities
    from .resources.ledger_account_categories import LedgerAccountCategories, AsyncLedgerAccountCategories
    from .resources.ledger_account_statements import LedgerAccountStatements, AsyncLedgerAccountStatements
    from .resources.legal_entity_associations import LegalEntityAssociations, AsyncLegalEntityAssociations
    from .resources.transactions.transactions import Transactions, AsyncTransactions
    from .resources.payment_orders.payment_orders import PaymentOrders, AsyncPaymentOrders
    from .resources.ledger_account_balance_monitors import (
        LedgerAccountBalanceMonitors,
        AsyncLedgerAccountBalanceMonitors,
    )
    from .resources.internal_accounts.internal_accounts import InternalAccounts, AsyncInternalAccounts
    from .resources.ledger_transactions.ledger_transactions import LedgerTransactions, AsyncLedgerTransactions
    from .resources.ledger_account_settlements.ledger_account_settlements import (
        LedgerAccountSettlements,
        AsyncLedgerAccountSettlements,
    )

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ModernTreasury",
    "AsyncModernTreasury",
    "Client",
    "AsyncClient",
]


class ModernTreasury(SyncAPIClient):
    # client options
    api_key: str
    organization_id: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ModernTreasury client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MODERN_TREASURY_API_KEY`
        - `organization_id` from `MODERN_TREASURY_ORGANIZATION_ID`
        - `webhook_key` from `MODERN_TREASURY_WEBHOOK_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("MODERN_TREASURY_API_KEY")
        if api_key is None:
            raise ModernTreasuryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MODERN_TREASURY_API_KEY environment variable"
            )
        self.api_key = api_key

        if organization_id is None:
            organization_id = os.environ.get("MODERN_TREASURY_ORGANIZATION_ID")
        if organization_id is None:
            raise ModernTreasuryError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )
        self.organization_id = organization_id

        if webhook_key is None:
            webhook_key = os.environ.get("MODERN_TREASURY_WEBHOOK_KEY")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("MODERN_TREASURY_BASE_URL")
        if base_url is None:
            base_url = f"https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def connections(self) -> Connections:
        from .resources.connections import Connections

        return Connections(self)

    @cached_property
    def counterparties(self) -> Counterparties:
        from .resources.counterparties import Counterparties

        return Counterparties(self)

    @cached_property
    def events(self) -> Events:
        from .resources.events import Events

        return Events(self)

    @cached_property
    def webhooks(self) -> webhooks.Webhooks:
        from .resources.webhooks import Webhooks

        return Webhooks(self)

    @cached_property
    def expected_payments(self) -> ExpectedPayments:
        from .resources.expected_payments import ExpectedPayments

        return ExpectedPayments(self)

    @cached_property
    def external_accounts(self) -> ExternalAccounts:
        from .resources.external_accounts import ExternalAccounts

        return ExternalAccounts(self)

    @cached_property
    def incoming_payment_details(self) -> IncomingPaymentDetails:
        from .resources.incoming_payment_details import IncomingPaymentDetails

        return IncomingPaymentDetails(self)

    @cached_property
    def invoices(self) -> Invoices:
        from .resources.invoices import Invoices

        return Invoices(self)

    @cached_property
    def documents(self) -> Documents:
        from .resources.documents import Documents

        return Documents(self)

    @cached_property
    def account_collection_flows(self) -> AccountCollectionFlows:
        from .resources.account_collection_flows import AccountCollectionFlows

        return AccountCollectionFlows(self)

    @cached_property
    def account_details(self) -> AccountDetails:
        from .resources.account_details import AccountDetails

        return AccountDetails(self)

    @cached_property
    def routing_details(self) -> RoutingDetails:
        from .resources.routing_details import RoutingDetails

        return RoutingDetails(self)

    @cached_property
    def internal_accounts(self) -> InternalAccounts:
        from .resources.internal_accounts import InternalAccounts

        return InternalAccounts(self)

    @cached_property
    def ledgers(self) -> Ledgers:
        from .resources.ledgers import Ledgers

        return Ledgers(self)

    @cached_property
    def ledger_account_categories(self) -> LedgerAccountCategories:
        from .resources.ledger_account_categories import LedgerAccountCategories

        return LedgerAccountCategories(self)

    @cached_property
    def ledger_accounts(self) -> LedgerAccounts:
        from .resources.ledger_accounts import LedgerAccounts

        return LedgerAccounts(self)

    @cached_property
    def ledger_account_balance_monitors(self) -> LedgerAccountBalanceMonitors:
        from .resources.ledger_account_balance_monitors import LedgerAccountBalanceMonitors

        return LedgerAccountBalanceMonitors(self)

    @cached_property
    def ledger_account_statements(self) -> LedgerAccountStatements:
        from .resources.ledger_account_statements import LedgerAccountStatements

        return LedgerAccountStatements(self)

    @cached_property
    def ledger_entries(self) -> LedgerEntries:
        from .resources.ledger_entries import LedgerEntries

        return LedgerEntries(self)

    @cached_property
    def ledger_transactions(self) -> LedgerTransactions:
        from .resources.ledger_transactions import LedgerTransactions

        return LedgerTransactions(self)

    @cached_property
    def line_items(self) -> LineItems:
        from .resources.line_items import LineItems

        return LineItems(self)

    @cached_property
    def payment_flows(self) -> PaymentFlows:
        from .resources.payment_flows import PaymentFlows

        return PaymentFlows(self)

    @cached_property
    def payment_orders(self) -> PaymentOrders:
        from .resources.payment_orders import PaymentOrders

        return PaymentOrders(self)

    @cached_property
    def payment_references(self) -> PaymentReferences:
        from .resources.payment_references import PaymentReferences

        return PaymentReferences(self)

    @cached_property
    def returns(self) -> Returns:
        from .resources.returns import Returns

        return Returns(self)

    @cached_property
    def transactions(self) -> Transactions:
        from .resources.transactions import Transactions

        return Transactions(self)

    @cached_property
    def validations(self) -> Validations:
        from .resources.validations import Validations

        return Validations(self)

    @cached_property
    def paper_items(self) -> PaperItems:
        from .resources.paper_items import PaperItems

        return PaperItems(self)

    @cached_property
    def virtual_accounts(self) -> VirtualAccounts:
        from .resources.virtual_accounts import VirtualAccounts

        return VirtualAccounts(self)

    @cached_property
    def bulk_requests(self) -> BulkRequests:
        from .resources.bulk_requests import BulkRequests

        return BulkRequests(self)

    @cached_property
    def bulk_results(self) -> BulkResults:
        from .resources.bulk_results import BulkResults

        return BulkResults(self)

    @cached_property
    def ledger_account_settlements(self) -> LedgerAccountSettlements:
        from .resources.ledger_account_settlements import LedgerAccountSettlements

        return LedgerAccountSettlements(self)

    @cached_property
    def foreign_exchange_quotes(self) -> ForeignExchangeQuotes:
        from .resources.foreign_exchange_quotes import ForeignExchangeQuotes

        return ForeignExchangeQuotes(self)

    @cached_property
    def connection_legal_entities(self) -> ConnectionLegalEntities:
        from .resources.connection_legal_entities import ConnectionLegalEntities

        return ConnectionLegalEntities(self)

    @cached_property
    def legal_entities(self) -> LegalEntities:
        from .resources.legal_entities import LegalEntities

        return LegalEntities(self)

    @cached_property
    def legal_entity_associations(self) -> LegalEntityAssociations:
        from .resources.legal_entity_associations import LegalEntityAssociations

        return LegalEntityAssociations(self)

    @cached_property
    def payment_actions(self) -> PaymentActions:
        from .resources.payment_actions import PaymentActions

        return PaymentActions(self)

    @cached_property
    def with_raw_response(self) -> ModernTreasuryWithRawResponse:
        return ModernTreasuryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModernTreasuryWithStreamedResponse:
        return ModernTreasuryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PingResponse:
        """
        A test endpoint often used to confirm credentials and headers are being passed
        in correctly.
        """
        return self.get(
            "/api/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PingResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncModernTreasury(AsyncAPIClient):
    # client options
    api_key: str
    organization_id: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncModernTreasury client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MODERN_TREASURY_API_KEY`
        - `organization_id` from `MODERN_TREASURY_ORGANIZATION_ID`
        - `webhook_key` from `MODERN_TREASURY_WEBHOOK_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("MODERN_TREASURY_API_KEY")
        if api_key is None:
            raise ModernTreasuryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MODERN_TREASURY_API_KEY environment variable"
            )
        self.api_key = api_key

        if organization_id is None:
            organization_id = os.environ.get("MODERN_TREASURY_ORGANIZATION_ID")
        if organization_id is None:
            raise ModernTreasuryError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )
        self.organization_id = organization_id

        if webhook_key is None:
            webhook_key = os.environ.get("MODERN_TREASURY_WEBHOOK_KEY")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("MODERN_TREASURY_BASE_URL")
        if base_url is None:
            base_url = f"https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def connections(self) -> AsyncConnections:
        from .resources.connections import AsyncConnections

        return AsyncConnections(self)

    @cached_property
    def counterparties(self) -> AsyncCounterparties:
        from .resources.counterparties import AsyncCounterparties

        return AsyncCounterparties(self)

    @cached_property
    def events(self) -> AsyncEvents:
        from .resources.events import AsyncEvents

        return AsyncEvents(self)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooks:
        from .resources.webhooks import AsyncWebhooks

        return AsyncWebhooks(self)

    @cached_property
    def expected_payments(self) -> AsyncExpectedPayments:
        from .resources.expected_payments import AsyncExpectedPayments

        return AsyncExpectedPayments(self)

    @cached_property
    def external_accounts(self) -> AsyncExternalAccounts:
        from .resources.external_accounts import AsyncExternalAccounts

        return AsyncExternalAccounts(self)

    @cached_property
    def incoming_payment_details(self) -> AsyncIncomingPaymentDetails:
        from .resources.incoming_payment_details import AsyncIncomingPaymentDetails

        return AsyncIncomingPaymentDetails(self)

    @cached_property
    def invoices(self) -> AsyncInvoices:
        from .resources.invoices import AsyncInvoices

        return AsyncInvoices(self)

    @cached_property
    def documents(self) -> AsyncDocuments:
        from .resources.documents import AsyncDocuments

        return AsyncDocuments(self)

    @cached_property
    def account_collection_flows(self) -> AsyncAccountCollectionFlows:
        from .resources.account_collection_flows import AsyncAccountCollectionFlows

        return AsyncAccountCollectionFlows(self)

    @cached_property
    def account_details(self) -> AsyncAccountDetails:
        from .resources.account_details import AsyncAccountDetails

        return AsyncAccountDetails(self)

    @cached_property
    def routing_details(self) -> AsyncRoutingDetails:
        from .resources.routing_details import AsyncRoutingDetails

        return AsyncRoutingDetails(self)

    @cached_property
    def internal_accounts(self) -> AsyncInternalAccounts:
        from .resources.internal_accounts import AsyncInternalAccounts

        return AsyncInternalAccounts(self)

    @cached_property
    def ledgers(self) -> AsyncLedgers:
        from .resources.ledgers import AsyncLedgers

        return AsyncLedgers(self)

    @cached_property
    def ledger_account_categories(self) -> AsyncLedgerAccountCategories:
        from .resources.ledger_account_categories import AsyncLedgerAccountCategories

        return AsyncLedgerAccountCategories(self)

    @cached_property
    def ledger_accounts(self) -> AsyncLedgerAccounts:
        from .resources.ledger_accounts import AsyncLedgerAccounts

        return AsyncLedgerAccounts(self)

    @cached_property
    def ledger_account_balance_monitors(self) -> AsyncLedgerAccountBalanceMonitors:
        from .resources.ledger_account_balance_monitors import AsyncLedgerAccountBalanceMonitors

        return AsyncLedgerAccountBalanceMonitors(self)

    @cached_property
    def ledger_account_statements(self) -> AsyncLedgerAccountStatements:
        from .resources.ledger_account_statements import AsyncLedgerAccountStatements

        return AsyncLedgerAccountStatements(self)

    @cached_property
    def ledger_entries(self) -> AsyncLedgerEntries:
        from .resources.ledger_entries import AsyncLedgerEntries

        return AsyncLedgerEntries(self)

    @cached_property
    def ledger_transactions(self) -> AsyncLedgerTransactions:
        from .resources.ledger_transactions import AsyncLedgerTransactions

        return AsyncLedgerTransactions(self)

    @cached_property
    def line_items(self) -> AsyncLineItems:
        from .resources.line_items import AsyncLineItems

        return AsyncLineItems(self)

    @cached_property
    def payment_flows(self) -> AsyncPaymentFlows:
        from .resources.payment_flows import AsyncPaymentFlows

        return AsyncPaymentFlows(self)

    @cached_property
    def payment_orders(self) -> AsyncPaymentOrders:
        from .resources.payment_orders import AsyncPaymentOrders

        return AsyncPaymentOrders(self)

    @cached_property
    def payment_references(self) -> AsyncPaymentReferences:
        from .resources.payment_references import AsyncPaymentReferences

        return AsyncPaymentReferences(self)

    @cached_property
    def returns(self) -> AsyncReturns:
        from .resources.returns import AsyncReturns

        return AsyncReturns(self)

    @cached_property
    def transactions(self) -> AsyncTransactions:
        from .resources.transactions import AsyncTransactions

        return AsyncTransactions(self)

    @cached_property
    def validations(self) -> AsyncValidations:
        from .resources.validations import AsyncValidations

        return AsyncValidations(self)

    @cached_property
    def paper_items(self) -> AsyncPaperItems:
        from .resources.paper_items import AsyncPaperItems

        return AsyncPaperItems(self)

    @cached_property
    def virtual_accounts(self) -> AsyncVirtualAccounts:
        from .resources.virtual_accounts import AsyncVirtualAccounts

        return AsyncVirtualAccounts(self)

    @cached_property
    def bulk_requests(self) -> AsyncBulkRequests:
        from .resources.bulk_requests import AsyncBulkRequests

        return AsyncBulkRequests(self)

    @cached_property
    def bulk_results(self) -> AsyncBulkResults:
        from .resources.bulk_results import AsyncBulkResults

        return AsyncBulkResults(self)

    @cached_property
    def ledger_account_settlements(self) -> AsyncLedgerAccountSettlements:
        from .resources.ledger_account_settlements import AsyncLedgerAccountSettlements

        return AsyncLedgerAccountSettlements(self)

    @cached_property
    def foreign_exchange_quotes(self) -> AsyncForeignExchangeQuotes:
        from .resources.foreign_exchange_quotes import AsyncForeignExchangeQuotes

        return AsyncForeignExchangeQuotes(self)

    @cached_property
    def connection_legal_entities(self) -> AsyncConnectionLegalEntities:
        from .resources.connection_legal_entities import AsyncConnectionLegalEntities

        return AsyncConnectionLegalEntities(self)

    @cached_property
    def legal_entities(self) -> AsyncLegalEntities:
        from .resources.legal_entities import AsyncLegalEntities

        return AsyncLegalEntities(self)

    @cached_property
    def legal_entity_associations(self) -> AsyncLegalEntityAssociations:
        from .resources.legal_entity_associations import AsyncLegalEntityAssociations

        return AsyncLegalEntityAssociations(self)

    @cached_property
    def payment_actions(self) -> AsyncPaymentActions:
        from .resources.payment_actions import AsyncPaymentActions

        return AsyncPaymentActions(self)

    @cached_property
    def with_raw_response(self) -> AsyncModernTreasuryWithRawResponse:
        return AsyncModernTreasuryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModernTreasuryWithStreamedResponse:
        return AsyncModernTreasuryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PingResponse:
        """
        A test endpoint often used to confirm credentials and headers are being passed
        in correctly.
        """
        return await self.get(
            "/api/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PingResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ModernTreasuryWithRawResponse:
    _client: ModernTreasury

    def __init__(self, client: ModernTreasury) -> None:
        self._client = client

        self.ping = _legacy_response.to_raw_response_wrapper(
            client.ping,
        )

    @cached_property
    def connections(self) -> connections.ConnectionsWithRawResponse:
        from .resources.connections import ConnectionsWithRawResponse

        return ConnectionsWithRawResponse(self._client.connections)

    @cached_property
    def counterparties(self) -> counterparties.CounterpartiesWithRawResponse:
        from .resources.counterparties import CounterpartiesWithRawResponse

        return CounterpartiesWithRawResponse(self._client.counterparties)

    @cached_property
    def events(self) -> events.EventsWithRawResponse:
        from .resources.events import EventsWithRawResponse

        return EventsWithRawResponse(self._client.events)

    @cached_property
    def expected_payments(self) -> expected_payments.ExpectedPaymentsWithRawResponse:
        from .resources.expected_payments import ExpectedPaymentsWithRawResponse

        return ExpectedPaymentsWithRawResponse(self._client.expected_payments)

    @cached_property
    def external_accounts(self) -> external_accounts.ExternalAccountsWithRawResponse:
        from .resources.external_accounts import ExternalAccountsWithRawResponse

        return ExternalAccountsWithRawResponse(self._client.external_accounts)

    @cached_property
    def incoming_payment_details(self) -> incoming_payment_details.IncomingPaymentDetailsWithRawResponse:
        from .resources.incoming_payment_details import IncomingPaymentDetailsWithRawResponse

        return IncomingPaymentDetailsWithRawResponse(self._client.incoming_payment_details)

    @cached_property
    def invoices(self) -> invoices.InvoicesWithRawResponse:
        from .resources.invoices import InvoicesWithRawResponse

        return InvoicesWithRawResponse(self._client.invoices)

    @cached_property
    def documents(self) -> documents.DocumentsWithRawResponse:
        from .resources.documents import DocumentsWithRawResponse

        return DocumentsWithRawResponse(self._client.documents)

    @cached_property
    def account_collection_flows(self) -> account_collection_flows.AccountCollectionFlowsWithRawResponse:
        from .resources.account_collection_flows import AccountCollectionFlowsWithRawResponse

        return AccountCollectionFlowsWithRawResponse(self._client.account_collection_flows)

    @cached_property
    def account_details(self) -> account_details.AccountDetailsWithRawResponse:
        from .resources.account_details import AccountDetailsWithRawResponse

        return AccountDetailsWithRawResponse(self._client.account_details)

    @cached_property
    def routing_details(self) -> routing_details.RoutingDetailsWithRawResponse:
        from .resources.routing_details import RoutingDetailsWithRawResponse

        return RoutingDetailsWithRawResponse(self._client.routing_details)

    @cached_property
    def internal_accounts(self) -> internal_accounts.InternalAccountsWithRawResponse:
        from .resources.internal_accounts import InternalAccountsWithRawResponse

        return InternalAccountsWithRawResponse(self._client.internal_accounts)

    @cached_property
    def ledgers(self) -> ledgers.LedgersWithRawResponse:
        from .resources.ledgers import LedgersWithRawResponse

        return LedgersWithRawResponse(self._client.ledgers)

    @cached_property
    def ledger_account_categories(self) -> ledger_account_categories.LedgerAccountCategoriesWithRawResponse:
        from .resources.ledger_account_categories import LedgerAccountCategoriesWithRawResponse

        return LedgerAccountCategoriesWithRawResponse(self._client.ledger_account_categories)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsWithRawResponse:
        from .resources.ledger_accounts import LedgerAccountsWithRawResponse

        return LedgerAccountsWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def ledger_account_balance_monitors(
        self,
    ) -> ledger_account_balance_monitors.LedgerAccountBalanceMonitorsWithRawResponse:
        from .resources.ledger_account_balance_monitors import LedgerAccountBalanceMonitorsWithRawResponse

        return LedgerAccountBalanceMonitorsWithRawResponse(self._client.ledger_account_balance_monitors)

    @cached_property
    def ledger_account_statements(self) -> ledger_account_statements.LedgerAccountStatementsWithRawResponse:
        from .resources.ledger_account_statements import LedgerAccountStatementsWithRawResponse

        return LedgerAccountStatementsWithRawResponse(self._client.ledger_account_statements)

    @cached_property
    def ledger_entries(self) -> ledger_entries.LedgerEntriesWithRawResponse:
        from .resources.ledger_entries import LedgerEntriesWithRawResponse

        return LedgerEntriesWithRawResponse(self._client.ledger_entries)

    @cached_property
    def ledger_transactions(self) -> ledger_transactions.LedgerTransactionsWithRawResponse:
        from .resources.ledger_transactions import LedgerTransactionsWithRawResponse

        return LedgerTransactionsWithRawResponse(self._client.ledger_transactions)

    @cached_property
    def line_items(self) -> line_items.LineItemsWithRawResponse:
        from .resources.line_items import LineItemsWithRawResponse

        return LineItemsWithRawResponse(self._client.line_items)

    @cached_property
    def payment_flows(self) -> payment_flows.PaymentFlowsWithRawResponse:
        from .resources.payment_flows import PaymentFlowsWithRawResponse

        return PaymentFlowsWithRawResponse(self._client.payment_flows)

    @cached_property
    def payment_orders(self) -> payment_orders.PaymentOrdersWithRawResponse:
        from .resources.payment_orders import PaymentOrdersWithRawResponse

        return PaymentOrdersWithRawResponse(self._client.payment_orders)

    @cached_property
    def payment_references(self) -> payment_references.PaymentReferencesWithRawResponse:
        from .resources.payment_references import PaymentReferencesWithRawResponse

        return PaymentReferencesWithRawResponse(self._client.payment_references)

    @cached_property
    def returns(self) -> returns.ReturnsWithRawResponse:
        from .resources.returns import ReturnsWithRawResponse

        return ReturnsWithRawResponse(self._client.returns)

    @cached_property
    def transactions(self) -> transactions.TransactionsWithRawResponse:
        from .resources.transactions import TransactionsWithRawResponse

        return TransactionsWithRawResponse(self._client.transactions)

    @cached_property
    def validations(self) -> validations.ValidationsWithRawResponse:
        from .resources.validations import ValidationsWithRawResponse

        return ValidationsWithRawResponse(self._client.validations)

    @cached_property
    def paper_items(self) -> paper_items.PaperItemsWithRawResponse:
        from .resources.paper_items import PaperItemsWithRawResponse

        return PaperItemsWithRawResponse(self._client.paper_items)

    @cached_property
    def virtual_accounts(self) -> virtual_accounts.VirtualAccountsWithRawResponse:
        from .resources.virtual_accounts import VirtualAccountsWithRawResponse

        return VirtualAccountsWithRawResponse(self._client.virtual_accounts)

    @cached_property
    def bulk_requests(self) -> bulk_requests.BulkRequestsWithRawResponse:
        from .resources.bulk_requests import BulkRequestsWithRawResponse

        return BulkRequestsWithRawResponse(self._client.bulk_requests)

    @cached_property
    def bulk_results(self) -> bulk_results.BulkResultsWithRawResponse:
        from .resources.bulk_results import BulkResultsWithRawResponse

        return BulkResultsWithRawResponse(self._client.bulk_results)

    @cached_property
    def ledger_account_settlements(self) -> ledger_account_settlements.LedgerAccountSettlementsWithRawResponse:
        from .resources.ledger_account_settlements import LedgerAccountSettlementsWithRawResponse

        return LedgerAccountSettlementsWithRawResponse(self._client.ledger_account_settlements)

    @cached_property
    def foreign_exchange_quotes(self) -> foreign_exchange_quotes.ForeignExchangeQuotesWithRawResponse:
        from .resources.foreign_exchange_quotes import ForeignExchangeQuotesWithRawResponse

        return ForeignExchangeQuotesWithRawResponse(self._client.foreign_exchange_quotes)

    @cached_property
    def connection_legal_entities(self) -> connection_legal_entities.ConnectionLegalEntitiesWithRawResponse:
        from .resources.connection_legal_entities import ConnectionLegalEntitiesWithRawResponse

        return ConnectionLegalEntitiesWithRawResponse(self._client.connection_legal_entities)

    @cached_property
    def legal_entities(self) -> legal_entities.LegalEntitiesWithRawResponse:
        from .resources.legal_entities import LegalEntitiesWithRawResponse

        return LegalEntitiesWithRawResponse(self._client.legal_entities)

    @cached_property
    def legal_entity_associations(self) -> legal_entity_associations.LegalEntityAssociationsWithRawResponse:
        from .resources.legal_entity_associations import LegalEntityAssociationsWithRawResponse

        return LegalEntityAssociationsWithRawResponse(self._client.legal_entity_associations)

    @cached_property
    def payment_actions(self) -> payment_actions.PaymentActionsWithRawResponse:
        from .resources.payment_actions import PaymentActionsWithRawResponse

        return PaymentActionsWithRawResponse(self._client.payment_actions)


class AsyncModernTreasuryWithRawResponse:
    _client: AsyncModernTreasury

    def __init__(self, client: AsyncModernTreasury) -> None:
        self._client = client

        self.ping = _legacy_response.async_to_raw_response_wrapper(
            client.ping,
        )

    @cached_property
    def connections(self) -> connections.AsyncConnectionsWithRawResponse:
        from .resources.connections import AsyncConnectionsWithRawResponse

        return AsyncConnectionsWithRawResponse(self._client.connections)

    @cached_property
    def counterparties(self) -> counterparties.AsyncCounterpartiesWithRawResponse:
        from .resources.counterparties import AsyncCounterpartiesWithRawResponse

        return AsyncCounterpartiesWithRawResponse(self._client.counterparties)

    @cached_property
    def events(self) -> events.AsyncEventsWithRawResponse:
        from .resources.events import AsyncEventsWithRawResponse

        return AsyncEventsWithRawResponse(self._client.events)

    @cached_property
    def expected_payments(self) -> expected_payments.AsyncExpectedPaymentsWithRawResponse:
        from .resources.expected_payments import AsyncExpectedPaymentsWithRawResponse

        return AsyncExpectedPaymentsWithRawResponse(self._client.expected_payments)

    @cached_property
    def external_accounts(self) -> external_accounts.AsyncExternalAccountsWithRawResponse:
        from .resources.external_accounts import AsyncExternalAccountsWithRawResponse

        return AsyncExternalAccountsWithRawResponse(self._client.external_accounts)

    @cached_property
    def incoming_payment_details(self) -> incoming_payment_details.AsyncIncomingPaymentDetailsWithRawResponse:
        from .resources.incoming_payment_details import AsyncIncomingPaymentDetailsWithRawResponse

        return AsyncIncomingPaymentDetailsWithRawResponse(self._client.incoming_payment_details)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesWithRawResponse:
        from .resources.invoices import AsyncInvoicesWithRawResponse

        return AsyncInvoicesWithRawResponse(self._client.invoices)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsWithRawResponse:
        from .resources.documents import AsyncDocumentsWithRawResponse

        return AsyncDocumentsWithRawResponse(self._client.documents)

    @cached_property
    def account_collection_flows(self) -> account_collection_flows.AsyncAccountCollectionFlowsWithRawResponse:
        from .resources.account_collection_flows import AsyncAccountCollectionFlowsWithRawResponse

        return AsyncAccountCollectionFlowsWithRawResponse(self._client.account_collection_flows)

    @cached_property
    def account_details(self) -> account_details.AsyncAccountDetailsWithRawResponse:
        from .resources.account_details import AsyncAccountDetailsWithRawResponse

        return AsyncAccountDetailsWithRawResponse(self._client.account_details)

    @cached_property
    def routing_details(self) -> routing_details.AsyncRoutingDetailsWithRawResponse:
        from .resources.routing_details import AsyncRoutingDetailsWithRawResponse

        return AsyncRoutingDetailsWithRawResponse(self._client.routing_details)

    @cached_property
    def internal_accounts(self) -> internal_accounts.AsyncInternalAccountsWithRawResponse:
        from .resources.internal_accounts import AsyncInternalAccountsWithRawResponse

        return AsyncInternalAccountsWithRawResponse(self._client.internal_accounts)

    @cached_property
    def ledgers(self) -> ledgers.AsyncLedgersWithRawResponse:
        from .resources.ledgers import AsyncLedgersWithRawResponse

        return AsyncLedgersWithRawResponse(self._client.ledgers)

    @cached_property
    def ledger_account_categories(self) -> ledger_account_categories.AsyncLedgerAccountCategoriesWithRawResponse:
        from .resources.ledger_account_categories import AsyncLedgerAccountCategoriesWithRawResponse

        return AsyncLedgerAccountCategoriesWithRawResponse(self._client.ledger_account_categories)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsWithRawResponse:
        from .resources.ledger_accounts import AsyncLedgerAccountsWithRawResponse

        return AsyncLedgerAccountsWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def ledger_account_balance_monitors(
        self,
    ) -> ledger_account_balance_monitors.AsyncLedgerAccountBalanceMonitorsWithRawResponse:
        from .resources.ledger_account_balance_monitors import AsyncLedgerAccountBalanceMonitorsWithRawResponse

        return AsyncLedgerAccountBalanceMonitorsWithRawResponse(self._client.ledger_account_balance_monitors)

    @cached_property
    def ledger_account_statements(self) -> ledger_account_statements.AsyncLedgerAccountStatementsWithRawResponse:
        from .resources.ledger_account_statements import AsyncLedgerAccountStatementsWithRawResponse

        return AsyncLedgerAccountStatementsWithRawResponse(self._client.ledger_account_statements)

    @cached_property
    def ledger_entries(self) -> ledger_entries.AsyncLedgerEntriesWithRawResponse:
        from .resources.ledger_entries import AsyncLedgerEntriesWithRawResponse

        return AsyncLedgerEntriesWithRawResponse(self._client.ledger_entries)

    @cached_property
    def ledger_transactions(self) -> ledger_transactions.AsyncLedgerTransactionsWithRawResponse:
        from .resources.ledger_transactions import AsyncLedgerTransactionsWithRawResponse

        return AsyncLedgerTransactionsWithRawResponse(self._client.ledger_transactions)

    @cached_property
    def line_items(self) -> line_items.AsyncLineItemsWithRawResponse:
        from .resources.line_items import AsyncLineItemsWithRawResponse

        return AsyncLineItemsWithRawResponse(self._client.line_items)

    @cached_property
    def payment_flows(self) -> payment_flows.AsyncPaymentFlowsWithRawResponse:
        from .resources.payment_flows import AsyncPaymentFlowsWithRawResponse

        return AsyncPaymentFlowsWithRawResponse(self._client.payment_flows)

    @cached_property
    def payment_orders(self) -> payment_orders.AsyncPaymentOrdersWithRawResponse:
        from .resources.payment_orders import AsyncPaymentOrdersWithRawResponse

        return AsyncPaymentOrdersWithRawResponse(self._client.payment_orders)

    @cached_property
    def payment_references(self) -> payment_references.AsyncPaymentReferencesWithRawResponse:
        from .resources.payment_references import AsyncPaymentReferencesWithRawResponse

        return AsyncPaymentReferencesWithRawResponse(self._client.payment_references)

    @cached_property
    def returns(self) -> returns.AsyncReturnsWithRawResponse:
        from .resources.returns import AsyncReturnsWithRawResponse

        return AsyncReturnsWithRawResponse(self._client.returns)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsWithRawResponse:
        from .resources.transactions import AsyncTransactionsWithRawResponse

        return AsyncTransactionsWithRawResponse(self._client.transactions)

    @cached_property
    def validations(self) -> validations.AsyncValidationsWithRawResponse:
        from .resources.validations import AsyncValidationsWithRawResponse

        return AsyncValidationsWithRawResponse(self._client.validations)

    @cached_property
    def paper_items(self) -> paper_items.AsyncPaperItemsWithRawResponse:
        from .resources.paper_items import AsyncPaperItemsWithRawResponse

        return AsyncPaperItemsWithRawResponse(self._client.paper_items)

    @cached_property
    def virtual_accounts(self) -> virtual_accounts.AsyncVirtualAccountsWithRawResponse:
        from .resources.virtual_accounts import AsyncVirtualAccountsWithRawResponse

        return AsyncVirtualAccountsWithRawResponse(self._client.virtual_accounts)

    @cached_property
    def bulk_requests(self) -> bulk_requests.AsyncBulkRequestsWithRawResponse:
        from .resources.bulk_requests import AsyncBulkRequestsWithRawResponse

        return AsyncBulkRequestsWithRawResponse(self._client.bulk_requests)

    @cached_property
    def bulk_results(self) -> bulk_results.AsyncBulkResultsWithRawResponse:
        from .resources.bulk_results import AsyncBulkResultsWithRawResponse

        return AsyncBulkResultsWithRawResponse(self._client.bulk_results)

    @cached_property
    def ledger_account_settlements(self) -> ledger_account_settlements.AsyncLedgerAccountSettlementsWithRawResponse:
        from .resources.ledger_account_settlements import AsyncLedgerAccountSettlementsWithRawResponse

        return AsyncLedgerAccountSettlementsWithRawResponse(self._client.ledger_account_settlements)

    @cached_property
    def foreign_exchange_quotes(self) -> foreign_exchange_quotes.AsyncForeignExchangeQuotesWithRawResponse:
        from .resources.foreign_exchange_quotes import AsyncForeignExchangeQuotesWithRawResponse

        return AsyncForeignExchangeQuotesWithRawResponse(self._client.foreign_exchange_quotes)

    @cached_property
    def connection_legal_entities(self) -> connection_legal_entities.AsyncConnectionLegalEntitiesWithRawResponse:
        from .resources.connection_legal_entities import AsyncConnectionLegalEntitiesWithRawResponse

        return AsyncConnectionLegalEntitiesWithRawResponse(self._client.connection_legal_entities)

    @cached_property
    def legal_entities(self) -> legal_entities.AsyncLegalEntitiesWithRawResponse:
        from .resources.legal_entities import AsyncLegalEntitiesWithRawResponse

        return AsyncLegalEntitiesWithRawResponse(self._client.legal_entities)

    @cached_property
    def legal_entity_associations(self) -> legal_entity_associations.AsyncLegalEntityAssociationsWithRawResponse:
        from .resources.legal_entity_associations import AsyncLegalEntityAssociationsWithRawResponse

        return AsyncLegalEntityAssociationsWithRawResponse(self._client.legal_entity_associations)

    @cached_property
    def payment_actions(self) -> payment_actions.AsyncPaymentActionsWithRawResponse:
        from .resources.payment_actions import AsyncPaymentActionsWithRawResponse

        return AsyncPaymentActionsWithRawResponse(self._client.payment_actions)


class ModernTreasuryWithStreamedResponse:
    _client: ModernTreasury

    def __init__(self, client: ModernTreasury) -> None:
        self._client = client

        self.ping = to_streamed_response_wrapper(
            client.ping,
        )

    @cached_property
    def connections(self) -> connections.ConnectionsWithStreamingResponse:
        from .resources.connections import ConnectionsWithStreamingResponse

        return ConnectionsWithStreamingResponse(self._client.connections)

    @cached_property
    def counterparties(self) -> counterparties.CounterpartiesWithStreamingResponse:
        from .resources.counterparties import CounterpartiesWithStreamingResponse

        return CounterpartiesWithStreamingResponse(self._client.counterparties)

    @cached_property
    def events(self) -> events.EventsWithStreamingResponse:
        from .resources.events import EventsWithStreamingResponse

        return EventsWithStreamingResponse(self._client.events)

    @cached_property
    def expected_payments(self) -> expected_payments.ExpectedPaymentsWithStreamingResponse:
        from .resources.expected_payments import ExpectedPaymentsWithStreamingResponse

        return ExpectedPaymentsWithStreamingResponse(self._client.expected_payments)

    @cached_property
    def external_accounts(self) -> external_accounts.ExternalAccountsWithStreamingResponse:
        from .resources.external_accounts import ExternalAccountsWithStreamingResponse

        return ExternalAccountsWithStreamingResponse(self._client.external_accounts)

    @cached_property
    def incoming_payment_details(self) -> incoming_payment_details.IncomingPaymentDetailsWithStreamingResponse:
        from .resources.incoming_payment_details import IncomingPaymentDetailsWithStreamingResponse

        return IncomingPaymentDetailsWithStreamingResponse(self._client.incoming_payment_details)

    @cached_property
    def invoices(self) -> invoices.InvoicesWithStreamingResponse:
        from .resources.invoices import InvoicesWithStreamingResponse

        return InvoicesWithStreamingResponse(self._client.invoices)

    @cached_property
    def documents(self) -> documents.DocumentsWithStreamingResponse:
        from .resources.documents import DocumentsWithStreamingResponse

        return DocumentsWithStreamingResponse(self._client.documents)

    @cached_property
    def account_collection_flows(self) -> account_collection_flows.AccountCollectionFlowsWithStreamingResponse:
        from .resources.account_collection_flows import AccountCollectionFlowsWithStreamingResponse

        return AccountCollectionFlowsWithStreamingResponse(self._client.account_collection_flows)

    @cached_property
    def account_details(self) -> account_details.AccountDetailsWithStreamingResponse:
        from .resources.account_details import AccountDetailsWithStreamingResponse

        return AccountDetailsWithStreamingResponse(self._client.account_details)

    @cached_property
    def routing_details(self) -> routing_details.RoutingDetailsWithStreamingResponse:
        from .resources.routing_details import RoutingDetailsWithStreamingResponse

        return RoutingDetailsWithStreamingResponse(self._client.routing_details)

    @cached_property
    def internal_accounts(self) -> internal_accounts.InternalAccountsWithStreamingResponse:
        from .resources.internal_accounts import InternalAccountsWithStreamingResponse

        return InternalAccountsWithStreamingResponse(self._client.internal_accounts)

    @cached_property
    def ledgers(self) -> ledgers.LedgersWithStreamingResponse:
        from .resources.ledgers import LedgersWithStreamingResponse

        return LedgersWithStreamingResponse(self._client.ledgers)

    @cached_property
    def ledger_account_categories(self) -> ledger_account_categories.LedgerAccountCategoriesWithStreamingResponse:
        from .resources.ledger_account_categories import LedgerAccountCategoriesWithStreamingResponse

        return LedgerAccountCategoriesWithStreamingResponse(self._client.ledger_account_categories)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsWithStreamingResponse:
        from .resources.ledger_accounts import LedgerAccountsWithStreamingResponse

        return LedgerAccountsWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def ledger_account_balance_monitors(
        self,
    ) -> ledger_account_balance_monitors.LedgerAccountBalanceMonitorsWithStreamingResponse:
        from .resources.ledger_account_balance_monitors import LedgerAccountBalanceMonitorsWithStreamingResponse

        return LedgerAccountBalanceMonitorsWithStreamingResponse(self._client.ledger_account_balance_monitors)

    @cached_property
    def ledger_account_statements(self) -> ledger_account_statements.LedgerAccountStatementsWithStreamingResponse:
        from .resources.ledger_account_statements import LedgerAccountStatementsWithStreamingResponse

        return LedgerAccountStatementsWithStreamingResponse(self._client.ledger_account_statements)

    @cached_property
    def ledger_entries(self) -> ledger_entries.LedgerEntriesWithStreamingResponse:
        from .resources.ledger_entries import LedgerEntriesWithStreamingResponse

        return LedgerEntriesWithStreamingResponse(self._client.ledger_entries)

    @cached_property
    def ledger_transactions(self) -> ledger_transactions.LedgerTransactionsWithStreamingResponse:
        from .resources.ledger_transactions import LedgerTransactionsWithStreamingResponse

        return LedgerTransactionsWithStreamingResponse(self._client.ledger_transactions)

    @cached_property
    def line_items(self) -> line_items.LineItemsWithStreamingResponse:
        from .resources.line_items import LineItemsWithStreamingResponse

        return LineItemsWithStreamingResponse(self._client.line_items)

    @cached_property
    def payment_flows(self) -> payment_flows.PaymentFlowsWithStreamingResponse:
        from .resources.payment_flows import PaymentFlowsWithStreamingResponse

        return PaymentFlowsWithStreamingResponse(self._client.payment_flows)

    @cached_property
    def payment_orders(self) -> payment_orders.PaymentOrdersWithStreamingResponse:
        from .resources.payment_orders import PaymentOrdersWithStreamingResponse

        return PaymentOrdersWithStreamingResponse(self._client.payment_orders)

    @cached_property
    def payment_references(self) -> payment_references.PaymentReferencesWithStreamingResponse:
        from .resources.payment_references import PaymentReferencesWithStreamingResponse

        return PaymentReferencesWithStreamingResponse(self._client.payment_references)

    @cached_property
    def returns(self) -> returns.ReturnsWithStreamingResponse:
        from .resources.returns import ReturnsWithStreamingResponse

        return ReturnsWithStreamingResponse(self._client.returns)

    @cached_property
    def transactions(self) -> transactions.TransactionsWithStreamingResponse:
        from .resources.transactions import TransactionsWithStreamingResponse

        return TransactionsWithStreamingResponse(self._client.transactions)

    @cached_property
    def validations(self) -> validations.ValidationsWithStreamingResponse:
        from .resources.validations import ValidationsWithStreamingResponse

        return ValidationsWithStreamingResponse(self._client.validations)

    @cached_property
    def paper_items(self) -> paper_items.PaperItemsWithStreamingResponse:
        from .resources.paper_items import PaperItemsWithStreamingResponse

        return PaperItemsWithStreamingResponse(self._client.paper_items)

    @cached_property
    def virtual_accounts(self) -> virtual_accounts.VirtualAccountsWithStreamingResponse:
        from .resources.virtual_accounts import VirtualAccountsWithStreamingResponse

        return VirtualAccountsWithStreamingResponse(self._client.virtual_accounts)

    @cached_property
    def bulk_requests(self) -> bulk_requests.BulkRequestsWithStreamingResponse:
        from .resources.bulk_requests import BulkRequestsWithStreamingResponse

        return BulkRequestsWithStreamingResponse(self._client.bulk_requests)

    @cached_property
    def bulk_results(self) -> bulk_results.BulkResultsWithStreamingResponse:
        from .resources.bulk_results import BulkResultsWithStreamingResponse

        return BulkResultsWithStreamingResponse(self._client.bulk_results)

    @cached_property
    def ledger_account_settlements(self) -> ledger_account_settlements.LedgerAccountSettlementsWithStreamingResponse:
        from .resources.ledger_account_settlements import LedgerAccountSettlementsWithStreamingResponse

        return LedgerAccountSettlementsWithStreamingResponse(self._client.ledger_account_settlements)

    @cached_property
    def foreign_exchange_quotes(self) -> foreign_exchange_quotes.ForeignExchangeQuotesWithStreamingResponse:
        from .resources.foreign_exchange_quotes import ForeignExchangeQuotesWithStreamingResponse

        return ForeignExchangeQuotesWithStreamingResponse(self._client.foreign_exchange_quotes)

    @cached_property
    def connection_legal_entities(self) -> connection_legal_entities.ConnectionLegalEntitiesWithStreamingResponse:
        from .resources.connection_legal_entities import ConnectionLegalEntitiesWithStreamingResponse

        return ConnectionLegalEntitiesWithStreamingResponse(self._client.connection_legal_entities)

    @cached_property
    def legal_entities(self) -> legal_entities.LegalEntitiesWithStreamingResponse:
        from .resources.legal_entities import LegalEntitiesWithStreamingResponse

        return LegalEntitiesWithStreamingResponse(self._client.legal_entities)

    @cached_property
    def legal_entity_associations(self) -> legal_entity_associations.LegalEntityAssociationsWithStreamingResponse:
        from .resources.legal_entity_associations import LegalEntityAssociationsWithStreamingResponse

        return LegalEntityAssociationsWithStreamingResponse(self._client.legal_entity_associations)

    @cached_property
    def payment_actions(self) -> payment_actions.PaymentActionsWithStreamingResponse:
        from .resources.payment_actions import PaymentActionsWithStreamingResponse

        return PaymentActionsWithStreamingResponse(self._client.payment_actions)


class AsyncModernTreasuryWithStreamedResponse:
    _client: AsyncModernTreasury

    def __init__(self, client: AsyncModernTreasury) -> None:
        self._client = client

        self.ping = async_to_streamed_response_wrapper(
            client.ping,
        )

    @cached_property
    def connections(self) -> connections.AsyncConnectionsWithStreamingResponse:
        from .resources.connections import AsyncConnectionsWithStreamingResponse

        return AsyncConnectionsWithStreamingResponse(self._client.connections)

    @cached_property
    def counterparties(self) -> counterparties.AsyncCounterpartiesWithStreamingResponse:
        from .resources.counterparties import AsyncCounterpartiesWithStreamingResponse

        return AsyncCounterpartiesWithStreamingResponse(self._client.counterparties)

    @cached_property
    def events(self) -> events.AsyncEventsWithStreamingResponse:
        from .resources.events import AsyncEventsWithStreamingResponse

        return AsyncEventsWithStreamingResponse(self._client.events)

    @cached_property
    def expected_payments(self) -> expected_payments.AsyncExpectedPaymentsWithStreamingResponse:
        from .resources.expected_payments import AsyncExpectedPaymentsWithStreamingResponse

        return AsyncExpectedPaymentsWithStreamingResponse(self._client.expected_payments)

    @cached_property
    def external_accounts(self) -> external_accounts.AsyncExternalAccountsWithStreamingResponse:
        from .resources.external_accounts import AsyncExternalAccountsWithStreamingResponse

        return AsyncExternalAccountsWithStreamingResponse(self._client.external_accounts)

    @cached_property
    def incoming_payment_details(self) -> incoming_payment_details.AsyncIncomingPaymentDetailsWithStreamingResponse:
        from .resources.incoming_payment_details import AsyncIncomingPaymentDetailsWithStreamingResponse

        return AsyncIncomingPaymentDetailsWithStreamingResponse(self._client.incoming_payment_details)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesWithStreamingResponse:
        from .resources.invoices import AsyncInvoicesWithStreamingResponse

        return AsyncInvoicesWithStreamingResponse(self._client.invoices)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsWithStreamingResponse:
        from .resources.documents import AsyncDocumentsWithStreamingResponse

        return AsyncDocumentsWithStreamingResponse(self._client.documents)

    @cached_property
    def account_collection_flows(self) -> account_collection_flows.AsyncAccountCollectionFlowsWithStreamingResponse:
        from .resources.account_collection_flows import AsyncAccountCollectionFlowsWithStreamingResponse

        return AsyncAccountCollectionFlowsWithStreamingResponse(self._client.account_collection_flows)

    @cached_property
    def account_details(self) -> account_details.AsyncAccountDetailsWithStreamingResponse:
        from .resources.account_details import AsyncAccountDetailsWithStreamingResponse

        return AsyncAccountDetailsWithStreamingResponse(self._client.account_details)

    @cached_property
    def routing_details(self) -> routing_details.AsyncRoutingDetailsWithStreamingResponse:
        from .resources.routing_details import AsyncRoutingDetailsWithStreamingResponse

        return AsyncRoutingDetailsWithStreamingResponse(self._client.routing_details)

    @cached_property
    def internal_accounts(self) -> internal_accounts.AsyncInternalAccountsWithStreamingResponse:
        from .resources.internal_accounts import AsyncInternalAccountsWithStreamingResponse

        return AsyncInternalAccountsWithStreamingResponse(self._client.internal_accounts)

    @cached_property
    def ledgers(self) -> ledgers.AsyncLedgersWithStreamingResponse:
        from .resources.ledgers import AsyncLedgersWithStreamingResponse

        return AsyncLedgersWithStreamingResponse(self._client.ledgers)

    @cached_property
    def ledger_account_categories(self) -> ledger_account_categories.AsyncLedgerAccountCategoriesWithStreamingResponse:
        from .resources.ledger_account_categories import AsyncLedgerAccountCategoriesWithStreamingResponse

        return AsyncLedgerAccountCategoriesWithStreamingResponse(self._client.ledger_account_categories)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsWithStreamingResponse:
        from .resources.ledger_accounts import AsyncLedgerAccountsWithStreamingResponse

        return AsyncLedgerAccountsWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def ledger_account_balance_monitors(
        self,
    ) -> ledger_account_balance_monitors.AsyncLedgerAccountBalanceMonitorsWithStreamingResponse:
        from .resources.ledger_account_balance_monitors import AsyncLedgerAccountBalanceMonitorsWithStreamingResponse

        return AsyncLedgerAccountBalanceMonitorsWithStreamingResponse(self._client.ledger_account_balance_monitors)

    @cached_property
    def ledger_account_statements(self) -> ledger_account_statements.AsyncLedgerAccountStatementsWithStreamingResponse:
        from .resources.ledger_account_statements import AsyncLedgerAccountStatementsWithStreamingResponse

        return AsyncLedgerAccountStatementsWithStreamingResponse(self._client.ledger_account_statements)

    @cached_property
    def ledger_entries(self) -> ledger_entries.AsyncLedgerEntriesWithStreamingResponse:
        from .resources.ledger_entries import AsyncLedgerEntriesWithStreamingResponse

        return AsyncLedgerEntriesWithStreamingResponse(self._client.ledger_entries)

    @cached_property
    def ledger_transactions(self) -> ledger_transactions.AsyncLedgerTransactionsWithStreamingResponse:
        from .resources.ledger_transactions import AsyncLedgerTransactionsWithStreamingResponse

        return AsyncLedgerTransactionsWithStreamingResponse(self._client.ledger_transactions)

    @cached_property
    def line_items(self) -> line_items.AsyncLineItemsWithStreamingResponse:
        from .resources.line_items import AsyncLineItemsWithStreamingResponse

        return AsyncLineItemsWithStreamingResponse(self._client.line_items)

    @cached_property
    def payment_flows(self) -> payment_flows.AsyncPaymentFlowsWithStreamingResponse:
        from .resources.payment_flows import AsyncPaymentFlowsWithStreamingResponse

        return AsyncPaymentFlowsWithStreamingResponse(self._client.payment_flows)

    @cached_property
    def payment_orders(self) -> payment_orders.AsyncPaymentOrdersWithStreamingResponse:
        from .resources.payment_orders import AsyncPaymentOrdersWithStreamingResponse

        return AsyncPaymentOrdersWithStreamingResponse(self._client.payment_orders)

    @cached_property
    def payment_references(self) -> payment_references.AsyncPaymentReferencesWithStreamingResponse:
        from .resources.payment_references import AsyncPaymentReferencesWithStreamingResponse

        return AsyncPaymentReferencesWithStreamingResponse(self._client.payment_references)

    @cached_property
    def returns(self) -> returns.AsyncReturnsWithStreamingResponse:
        from .resources.returns import AsyncReturnsWithStreamingResponse

        return AsyncReturnsWithStreamingResponse(self._client.returns)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsWithStreamingResponse:
        from .resources.transactions import AsyncTransactionsWithStreamingResponse

        return AsyncTransactionsWithStreamingResponse(self._client.transactions)

    @cached_property
    def validations(self) -> validations.AsyncValidationsWithStreamingResponse:
        from .resources.validations import AsyncValidationsWithStreamingResponse

        return AsyncValidationsWithStreamingResponse(self._client.validations)

    @cached_property
    def paper_items(self) -> paper_items.AsyncPaperItemsWithStreamingResponse:
        from .resources.paper_items import AsyncPaperItemsWithStreamingResponse

        return AsyncPaperItemsWithStreamingResponse(self._client.paper_items)

    @cached_property
    def virtual_accounts(self) -> virtual_accounts.AsyncVirtualAccountsWithStreamingResponse:
        from .resources.virtual_accounts import AsyncVirtualAccountsWithStreamingResponse

        return AsyncVirtualAccountsWithStreamingResponse(self._client.virtual_accounts)

    @cached_property
    def bulk_requests(self) -> bulk_requests.AsyncBulkRequestsWithStreamingResponse:
        from .resources.bulk_requests import AsyncBulkRequestsWithStreamingResponse

        return AsyncBulkRequestsWithStreamingResponse(self._client.bulk_requests)

    @cached_property
    def bulk_results(self) -> bulk_results.AsyncBulkResultsWithStreamingResponse:
        from .resources.bulk_results import AsyncBulkResultsWithStreamingResponse

        return AsyncBulkResultsWithStreamingResponse(self._client.bulk_results)

    @cached_property
    def ledger_account_settlements(
        self,
    ) -> ledger_account_settlements.AsyncLedgerAccountSettlementsWithStreamingResponse:
        from .resources.ledger_account_settlements import AsyncLedgerAccountSettlementsWithStreamingResponse

        return AsyncLedgerAccountSettlementsWithStreamingResponse(self._client.ledger_account_settlements)

    @cached_property
    def foreign_exchange_quotes(self) -> foreign_exchange_quotes.AsyncForeignExchangeQuotesWithStreamingResponse:
        from .resources.foreign_exchange_quotes import AsyncForeignExchangeQuotesWithStreamingResponse

        return AsyncForeignExchangeQuotesWithStreamingResponse(self._client.foreign_exchange_quotes)

    @cached_property
    def connection_legal_entities(self) -> connection_legal_entities.AsyncConnectionLegalEntitiesWithStreamingResponse:
        from .resources.connection_legal_entities import AsyncConnectionLegalEntitiesWithStreamingResponse

        return AsyncConnectionLegalEntitiesWithStreamingResponse(self._client.connection_legal_entities)

    @cached_property
    def legal_entities(self) -> legal_entities.AsyncLegalEntitiesWithStreamingResponse:
        from .resources.legal_entities import AsyncLegalEntitiesWithStreamingResponse

        return AsyncLegalEntitiesWithStreamingResponse(self._client.legal_entities)

    @cached_property
    def legal_entity_associations(self) -> legal_entity_associations.AsyncLegalEntityAssociationsWithStreamingResponse:
        from .resources.legal_entity_associations import AsyncLegalEntityAssociationsWithStreamingResponse

        return AsyncLegalEntityAssociationsWithStreamingResponse(self._client.legal_entity_associations)

    @cached_property
    def payment_actions(self) -> payment_actions.AsyncPaymentActionsWithStreamingResponse:
        from .resources.payment_actions import AsyncPaymentActionsWithStreamingResponse

        return AsyncPaymentActionsWithStreamingResponse(self._client.payment_actions)


Client = ModernTreasury

AsyncClient = AsyncModernTreasury
