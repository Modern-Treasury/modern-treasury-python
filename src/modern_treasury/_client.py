# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
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
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .resources import (
    events,
    ledgers,
    returns,
    webhooks,
    documents,
    line_items,
    connections,
    paper_items,
    validations,
    bulk_results,
    bulk_requests,
    payment_flows,
    counterparties,
    ledger_entries,
    legal_entities,
    account_details,
    ledger_accounts,
    routing_details,
    virtual_accounts,
    expected_payments,
    external_accounts,
    ledgerable_events,
    payment_references,
    ledger_event_handlers,
    foreign_exchange_quotes,
    account_collection_flows,
    incoming_payment_details,
    connection_legal_entities,
    ledger_account_categories,
    ledger_account_statements,
    legal_entity_associations,
    ledger_account_balance_monitors,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ModernTreasuryError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.invoices import invoices
from .types.ping_response import PingResponse
from .resources.transactions import transactions
from .resources.payment_orders import payment_orders
from .resources.internal_accounts import internal_accounts
from .resources.ledger_transactions import ledger_transactions
from .resources.ledger_account_settlements import ledger_account_settlements

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
    connections: connections.Connections
    counterparties: counterparties.Counterparties
    events: events.Events
    expected_payments: expected_payments.ExpectedPayments
    external_accounts: external_accounts.ExternalAccounts
    incoming_payment_details: incoming_payment_details.IncomingPaymentDetails
    invoices: invoices.Invoices
    documents: documents.Documents
    account_collection_flows: account_collection_flows.AccountCollectionFlows
    account_details: account_details.AccountDetails
    routing_details: routing_details.RoutingDetails
    internal_accounts: internal_accounts.InternalAccounts
    ledgers: ledgers.Ledgers
    ledgerable_events: ledgerable_events.LedgerableEvents
    ledger_account_categories: ledger_account_categories.LedgerAccountCategories
    ledger_accounts: ledger_accounts.LedgerAccounts
    ledger_account_balance_monitors: ledger_account_balance_monitors.LedgerAccountBalanceMonitors
    ledger_account_statements: ledger_account_statements.LedgerAccountStatements
    ledger_entries: ledger_entries.LedgerEntries
    ledger_event_handlers: ledger_event_handlers.LedgerEventHandlers
    ledger_transactions: ledger_transactions.LedgerTransactions
    line_items: line_items.LineItems
    payment_flows: payment_flows.PaymentFlows
    payment_orders: payment_orders.PaymentOrders
    payment_references: payment_references.PaymentReferences
    returns: returns.Returns
    transactions: transactions.Transactions
    validations: validations.Validations
    paper_items: paper_items.PaperItems
    webhooks: webhooks.Webhooks
    virtual_accounts: virtual_accounts.VirtualAccounts
    bulk_requests: bulk_requests.BulkRequests
    bulk_results: bulk_results.BulkResults
    ledger_account_settlements: ledger_account_settlements.LedgerAccountSettlements
    foreign_exchange_quotes: foreign_exchange_quotes.ForeignExchangeQuotes
    connection_legal_entities: connection_legal_entities.ConnectionLegalEntities
    legal_entities: legal_entities.LegalEntities
    legal_entity_associations: legal_entity_associations.LegalEntityAssociations
    with_raw_response: ModernTreasuryWithRawResponse
    with_streaming_response: ModernTreasuryWithStreamedResponse

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

        self.connections = connections.Connections(self)
        self.counterparties = counterparties.Counterparties(self)
        self.events = events.Events(self)
        self.expected_payments = expected_payments.ExpectedPayments(self)
        self.external_accounts = external_accounts.ExternalAccounts(self)
        self.incoming_payment_details = incoming_payment_details.IncomingPaymentDetails(self)
        self.invoices = invoices.Invoices(self)
        self.documents = documents.Documents(self)
        self.account_collection_flows = account_collection_flows.AccountCollectionFlows(self)
        self.account_details = account_details.AccountDetails(self)
        self.routing_details = routing_details.RoutingDetails(self)
        self.internal_accounts = internal_accounts.InternalAccounts(self)
        self.ledgers = ledgers.Ledgers(self)
        self.ledgerable_events = ledgerable_events.LedgerableEvents(self)
        self.ledger_account_categories = ledger_account_categories.LedgerAccountCategories(self)
        self.ledger_accounts = ledger_accounts.LedgerAccounts(self)
        self.ledger_account_balance_monitors = ledger_account_balance_monitors.LedgerAccountBalanceMonitors(self)
        self.ledger_account_statements = ledger_account_statements.LedgerAccountStatements(self)
        self.ledger_entries = ledger_entries.LedgerEntries(self)
        self.ledger_event_handlers = ledger_event_handlers.LedgerEventHandlers(self)
        self.ledger_transactions = ledger_transactions.LedgerTransactions(self)
        self.line_items = line_items.LineItems(self)
        self.payment_flows = payment_flows.PaymentFlows(self)
        self.payment_orders = payment_orders.PaymentOrders(self)
        self.payment_references = payment_references.PaymentReferences(self)
        self.returns = returns.Returns(self)
        self.transactions = transactions.Transactions(self)
        self.validations = validations.Validations(self)
        self.paper_items = paper_items.PaperItems(self)
        self.webhooks = webhooks.Webhooks(self)
        self.virtual_accounts = virtual_accounts.VirtualAccounts(self)
        self.bulk_requests = bulk_requests.BulkRequests(self)
        self.bulk_results = bulk_results.BulkResults(self)
        self.ledger_account_settlements = ledger_account_settlements.LedgerAccountSettlements(self)
        self.foreign_exchange_quotes = foreign_exchange_quotes.ForeignExchangeQuotes(self)
        self.connection_legal_entities = connection_legal_entities.ConnectionLegalEntities(self)
        self.legal_entities = legal_entities.LegalEntities(self)
        self.legal_entity_associations = legal_entity_associations.LegalEntityAssociations(self)
        self.with_raw_response = ModernTreasuryWithRawResponse(self)
        self.with_streaming_response = ModernTreasuryWithStreamedResponse(self)

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
    connections: connections.AsyncConnections
    counterparties: counterparties.AsyncCounterparties
    events: events.AsyncEvents
    expected_payments: expected_payments.AsyncExpectedPayments
    external_accounts: external_accounts.AsyncExternalAccounts
    incoming_payment_details: incoming_payment_details.AsyncIncomingPaymentDetails
    invoices: invoices.AsyncInvoices
    documents: documents.AsyncDocuments
    account_collection_flows: account_collection_flows.AsyncAccountCollectionFlows
    account_details: account_details.AsyncAccountDetails
    routing_details: routing_details.AsyncRoutingDetails
    internal_accounts: internal_accounts.AsyncInternalAccounts
    ledgers: ledgers.AsyncLedgers
    ledgerable_events: ledgerable_events.AsyncLedgerableEvents
    ledger_account_categories: ledger_account_categories.AsyncLedgerAccountCategories
    ledger_accounts: ledger_accounts.AsyncLedgerAccounts
    ledger_account_balance_monitors: ledger_account_balance_monitors.AsyncLedgerAccountBalanceMonitors
    ledger_account_statements: ledger_account_statements.AsyncLedgerAccountStatements
    ledger_entries: ledger_entries.AsyncLedgerEntries
    ledger_event_handlers: ledger_event_handlers.AsyncLedgerEventHandlers
    ledger_transactions: ledger_transactions.AsyncLedgerTransactions
    line_items: line_items.AsyncLineItems
    payment_flows: payment_flows.AsyncPaymentFlows
    payment_orders: payment_orders.AsyncPaymentOrders
    payment_references: payment_references.AsyncPaymentReferences
    returns: returns.AsyncReturns
    transactions: transactions.AsyncTransactions
    validations: validations.AsyncValidations
    paper_items: paper_items.AsyncPaperItems
    webhooks: webhooks.AsyncWebhooks
    virtual_accounts: virtual_accounts.AsyncVirtualAccounts
    bulk_requests: bulk_requests.AsyncBulkRequests
    bulk_results: bulk_results.AsyncBulkResults
    ledger_account_settlements: ledger_account_settlements.AsyncLedgerAccountSettlements
    foreign_exchange_quotes: foreign_exchange_quotes.AsyncForeignExchangeQuotes
    connection_legal_entities: connection_legal_entities.AsyncConnectionLegalEntities
    legal_entities: legal_entities.AsyncLegalEntities
    legal_entity_associations: legal_entity_associations.AsyncLegalEntityAssociations
    with_raw_response: AsyncModernTreasuryWithRawResponse
    with_streaming_response: AsyncModernTreasuryWithStreamedResponse

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

        self.connections = connections.AsyncConnections(self)
        self.counterparties = counterparties.AsyncCounterparties(self)
        self.events = events.AsyncEvents(self)
        self.expected_payments = expected_payments.AsyncExpectedPayments(self)
        self.external_accounts = external_accounts.AsyncExternalAccounts(self)
        self.incoming_payment_details = incoming_payment_details.AsyncIncomingPaymentDetails(self)
        self.invoices = invoices.AsyncInvoices(self)
        self.documents = documents.AsyncDocuments(self)
        self.account_collection_flows = account_collection_flows.AsyncAccountCollectionFlows(self)
        self.account_details = account_details.AsyncAccountDetails(self)
        self.routing_details = routing_details.AsyncRoutingDetails(self)
        self.internal_accounts = internal_accounts.AsyncInternalAccounts(self)
        self.ledgers = ledgers.AsyncLedgers(self)
        self.ledgerable_events = ledgerable_events.AsyncLedgerableEvents(self)
        self.ledger_account_categories = ledger_account_categories.AsyncLedgerAccountCategories(self)
        self.ledger_accounts = ledger_accounts.AsyncLedgerAccounts(self)
        self.ledger_account_balance_monitors = ledger_account_balance_monitors.AsyncLedgerAccountBalanceMonitors(self)
        self.ledger_account_statements = ledger_account_statements.AsyncLedgerAccountStatements(self)
        self.ledger_entries = ledger_entries.AsyncLedgerEntries(self)
        self.ledger_event_handlers = ledger_event_handlers.AsyncLedgerEventHandlers(self)
        self.ledger_transactions = ledger_transactions.AsyncLedgerTransactions(self)
        self.line_items = line_items.AsyncLineItems(self)
        self.payment_flows = payment_flows.AsyncPaymentFlows(self)
        self.payment_orders = payment_orders.AsyncPaymentOrders(self)
        self.payment_references = payment_references.AsyncPaymentReferences(self)
        self.returns = returns.AsyncReturns(self)
        self.transactions = transactions.AsyncTransactions(self)
        self.validations = validations.AsyncValidations(self)
        self.paper_items = paper_items.AsyncPaperItems(self)
        self.webhooks = webhooks.AsyncWebhooks(self)
        self.virtual_accounts = virtual_accounts.AsyncVirtualAccounts(self)
        self.bulk_requests = bulk_requests.AsyncBulkRequests(self)
        self.bulk_results = bulk_results.AsyncBulkResults(self)
        self.ledger_account_settlements = ledger_account_settlements.AsyncLedgerAccountSettlements(self)
        self.foreign_exchange_quotes = foreign_exchange_quotes.AsyncForeignExchangeQuotes(self)
        self.connection_legal_entities = connection_legal_entities.AsyncConnectionLegalEntities(self)
        self.legal_entities = legal_entities.AsyncLegalEntities(self)
        self.legal_entity_associations = legal_entity_associations.AsyncLegalEntityAssociations(self)
        self.with_raw_response = AsyncModernTreasuryWithRawResponse(self)
        self.with_streaming_response = AsyncModernTreasuryWithStreamedResponse(self)

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
    def __init__(self, client: ModernTreasury) -> None:
        self.connections = connections.ConnectionsWithRawResponse(client.connections)
        self.counterparties = counterparties.CounterpartiesWithRawResponse(client.counterparties)
        self.events = events.EventsWithRawResponse(client.events)
        self.expected_payments = expected_payments.ExpectedPaymentsWithRawResponse(client.expected_payments)
        self.external_accounts = external_accounts.ExternalAccountsWithRawResponse(client.external_accounts)
        self.incoming_payment_details = incoming_payment_details.IncomingPaymentDetailsWithRawResponse(
            client.incoming_payment_details
        )
        self.invoices = invoices.InvoicesWithRawResponse(client.invoices)
        self.documents = documents.DocumentsWithRawResponse(client.documents)
        self.account_collection_flows = account_collection_flows.AccountCollectionFlowsWithRawResponse(
            client.account_collection_flows
        )
        self.account_details = account_details.AccountDetailsWithRawResponse(client.account_details)
        self.routing_details = routing_details.RoutingDetailsWithRawResponse(client.routing_details)
        self.internal_accounts = internal_accounts.InternalAccountsWithRawResponse(client.internal_accounts)
        self.ledgers = ledgers.LedgersWithRawResponse(client.ledgers)
        self.ledgerable_events = ledgerable_events.LedgerableEventsWithRawResponse(client.ledgerable_events)
        self.ledger_account_categories = ledger_account_categories.LedgerAccountCategoriesWithRawResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = ledger_accounts.LedgerAccountsWithRawResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = (
            ledger_account_balance_monitors.LedgerAccountBalanceMonitorsWithRawResponse(
                client.ledger_account_balance_monitors
            )
        )
        self.ledger_account_statements = ledger_account_statements.LedgerAccountStatementsWithRawResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = ledger_entries.LedgerEntriesWithRawResponse(client.ledger_entries)
        self.ledger_event_handlers = ledger_event_handlers.LedgerEventHandlersWithRawResponse(
            client.ledger_event_handlers
        )
        self.ledger_transactions = ledger_transactions.LedgerTransactionsWithRawResponse(client.ledger_transactions)
        self.line_items = line_items.LineItemsWithRawResponse(client.line_items)
        self.payment_flows = payment_flows.PaymentFlowsWithRawResponse(client.payment_flows)
        self.payment_orders = payment_orders.PaymentOrdersWithRawResponse(client.payment_orders)
        self.payment_references = payment_references.PaymentReferencesWithRawResponse(client.payment_references)
        self.returns = returns.ReturnsWithRawResponse(client.returns)
        self.transactions = transactions.TransactionsWithRawResponse(client.transactions)
        self.validations = validations.ValidationsWithRawResponse(client.validations)
        self.paper_items = paper_items.PaperItemsWithRawResponse(client.paper_items)
        self.virtual_accounts = virtual_accounts.VirtualAccountsWithRawResponse(client.virtual_accounts)
        self.bulk_requests = bulk_requests.BulkRequestsWithRawResponse(client.bulk_requests)
        self.bulk_results = bulk_results.BulkResultsWithRawResponse(client.bulk_results)
        self.ledger_account_settlements = ledger_account_settlements.LedgerAccountSettlementsWithRawResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = foreign_exchange_quotes.ForeignExchangeQuotesWithRawResponse(
            client.foreign_exchange_quotes
        )
        self.connection_legal_entities = connection_legal_entities.ConnectionLegalEntitiesWithRawResponse(
            client.connection_legal_entities
        )
        self.legal_entities = legal_entities.LegalEntitiesWithRawResponse(client.legal_entities)
        self.legal_entity_associations = legal_entity_associations.LegalEntityAssociationsWithRawResponse(
            client.legal_entity_associations
        )

        self.ping = _legacy_response.to_raw_response_wrapper(
            client.ping,
        )


class AsyncModernTreasuryWithRawResponse:
    def __init__(self, client: AsyncModernTreasury) -> None:
        self.connections = connections.AsyncConnectionsWithRawResponse(client.connections)
        self.counterparties = counterparties.AsyncCounterpartiesWithRawResponse(client.counterparties)
        self.events = events.AsyncEventsWithRawResponse(client.events)
        self.expected_payments = expected_payments.AsyncExpectedPaymentsWithRawResponse(client.expected_payments)
        self.external_accounts = external_accounts.AsyncExternalAccountsWithRawResponse(client.external_accounts)
        self.incoming_payment_details = incoming_payment_details.AsyncIncomingPaymentDetailsWithRawResponse(
            client.incoming_payment_details
        )
        self.invoices = invoices.AsyncInvoicesWithRawResponse(client.invoices)
        self.documents = documents.AsyncDocumentsWithRawResponse(client.documents)
        self.account_collection_flows = account_collection_flows.AsyncAccountCollectionFlowsWithRawResponse(
            client.account_collection_flows
        )
        self.account_details = account_details.AsyncAccountDetailsWithRawResponse(client.account_details)
        self.routing_details = routing_details.AsyncRoutingDetailsWithRawResponse(client.routing_details)
        self.internal_accounts = internal_accounts.AsyncInternalAccountsWithRawResponse(client.internal_accounts)
        self.ledgers = ledgers.AsyncLedgersWithRawResponse(client.ledgers)
        self.ledgerable_events = ledgerable_events.AsyncLedgerableEventsWithRawResponse(client.ledgerable_events)
        self.ledger_account_categories = ledger_account_categories.AsyncLedgerAccountCategoriesWithRawResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = ledger_accounts.AsyncLedgerAccountsWithRawResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = (
            ledger_account_balance_monitors.AsyncLedgerAccountBalanceMonitorsWithRawResponse(
                client.ledger_account_balance_monitors
            )
        )
        self.ledger_account_statements = ledger_account_statements.AsyncLedgerAccountStatementsWithRawResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = ledger_entries.AsyncLedgerEntriesWithRawResponse(client.ledger_entries)
        self.ledger_event_handlers = ledger_event_handlers.AsyncLedgerEventHandlersWithRawResponse(
            client.ledger_event_handlers
        )
        self.ledger_transactions = ledger_transactions.AsyncLedgerTransactionsWithRawResponse(
            client.ledger_transactions
        )
        self.line_items = line_items.AsyncLineItemsWithRawResponse(client.line_items)
        self.payment_flows = payment_flows.AsyncPaymentFlowsWithRawResponse(client.payment_flows)
        self.payment_orders = payment_orders.AsyncPaymentOrdersWithRawResponse(client.payment_orders)
        self.payment_references = payment_references.AsyncPaymentReferencesWithRawResponse(client.payment_references)
        self.returns = returns.AsyncReturnsWithRawResponse(client.returns)
        self.transactions = transactions.AsyncTransactionsWithRawResponse(client.transactions)
        self.validations = validations.AsyncValidationsWithRawResponse(client.validations)
        self.paper_items = paper_items.AsyncPaperItemsWithRawResponse(client.paper_items)
        self.virtual_accounts = virtual_accounts.AsyncVirtualAccountsWithRawResponse(client.virtual_accounts)
        self.bulk_requests = bulk_requests.AsyncBulkRequestsWithRawResponse(client.bulk_requests)
        self.bulk_results = bulk_results.AsyncBulkResultsWithRawResponse(client.bulk_results)
        self.ledger_account_settlements = ledger_account_settlements.AsyncLedgerAccountSettlementsWithRawResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = foreign_exchange_quotes.AsyncForeignExchangeQuotesWithRawResponse(
            client.foreign_exchange_quotes
        )
        self.connection_legal_entities = connection_legal_entities.AsyncConnectionLegalEntitiesWithRawResponse(
            client.connection_legal_entities
        )
        self.legal_entities = legal_entities.AsyncLegalEntitiesWithRawResponse(client.legal_entities)
        self.legal_entity_associations = legal_entity_associations.AsyncLegalEntityAssociationsWithRawResponse(
            client.legal_entity_associations
        )

        self.ping = _legacy_response.async_to_raw_response_wrapper(
            client.ping,
        )


class ModernTreasuryWithStreamedResponse:
    def __init__(self, client: ModernTreasury) -> None:
        self.connections = connections.ConnectionsWithStreamingResponse(client.connections)
        self.counterparties = counterparties.CounterpartiesWithStreamingResponse(client.counterparties)
        self.events = events.EventsWithStreamingResponse(client.events)
        self.expected_payments = expected_payments.ExpectedPaymentsWithStreamingResponse(client.expected_payments)
        self.external_accounts = external_accounts.ExternalAccountsWithStreamingResponse(client.external_accounts)
        self.incoming_payment_details = incoming_payment_details.IncomingPaymentDetailsWithStreamingResponse(
            client.incoming_payment_details
        )
        self.invoices = invoices.InvoicesWithStreamingResponse(client.invoices)
        self.documents = documents.DocumentsWithStreamingResponse(client.documents)
        self.account_collection_flows = account_collection_flows.AccountCollectionFlowsWithStreamingResponse(
            client.account_collection_flows
        )
        self.account_details = account_details.AccountDetailsWithStreamingResponse(client.account_details)
        self.routing_details = routing_details.RoutingDetailsWithStreamingResponse(client.routing_details)
        self.internal_accounts = internal_accounts.InternalAccountsWithStreamingResponse(client.internal_accounts)
        self.ledgers = ledgers.LedgersWithStreamingResponse(client.ledgers)
        self.ledgerable_events = ledgerable_events.LedgerableEventsWithStreamingResponse(client.ledgerable_events)
        self.ledger_account_categories = ledger_account_categories.LedgerAccountCategoriesWithStreamingResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = ledger_accounts.LedgerAccountsWithStreamingResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = (
            ledger_account_balance_monitors.LedgerAccountBalanceMonitorsWithStreamingResponse(
                client.ledger_account_balance_monitors
            )
        )
        self.ledger_account_statements = ledger_account_statements.LedgerAccountStatementsWithStreamingResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = ledger_entries.LedgerEntriesWithStreamingResponse(client.ledger_entries)
        self.ledger_event_handlers = ledger_event_handlers.LedgerEventHandlersWithStreamingResponse(
            client.ledger_event_handlers
        )
        self.ledger_transactions = ledger_transactions.LedgerTransactionsWithStreamingResponse(
            client.ledger_transactions
        )
        self.line_items = line_items.LineItemsWithStreamingResponse(client.line_items)
        self.payment_flows = payment_flows.PaymentFlowsWithStreamingResponse(client.payment_flows)
        self.payment_orders = payment_orders.PaymentOrdersWithStreamingResponse(client.payment_orders)
        self.payment_references = payment_references.PaymentReferencesWithStreamingResponse(client.payment_references)
        self.returns = returns.ReturnsWithStreamingResponse(client.returns)
        self.transactions = transactions.TransactionsWithStreamingResponse(client.transactions)
        self.validations = validations.ValidationsWithStreamingResponse(client.validations)
        self.paper_items = paper_items.PaperItemsWithStreamingResponse(client.paper_items)
        self.virtual_accounts = virtual_accounts.VirtualAccountsWithStreamingResponse(client.virtual_accounts)
        self.bulk_requests = bulk_requests.BulkRequestsWithStreamingResponse(client.bulk_requests)
        self.bulk_results = bulk_results.BulkResultsWithStreamingResponse(client.bulk_results)
        self.ledger_account_settlements = ledger_account_settlements.LedgerAccountSettlementsWithStreamingResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = foreign_exchange_quotes.ForeignExchangeQuotesWithStreamingResponse(
            client.foreign_exchange_quotes
        )
        self.connection_legal_entities = connection_legal_entities.ConnectionLegalEntitiesWithStreamingResponse(
            client.connection_legal_entities
        )
        self.legal_entities = legal_entities.LegalEntitiesWithStreamingResponse(client.legal_entities)
        self.legal_entity_associations = legal_entity_associations.LegalEntityAssociationsWithStreamingResponse(
            client.legal_entity_associations
        )

        self.ping = to_streamed_response_wrapper(
            client.ping,
        )


class AsyncModernTreasuryWithStreamedResponse:
    def __init__(self, client: AsyncModernTreasury) -> None:
        self.connections = connections.AsyncConnectionsWithStreamingResponse(client.connections)
        self.counterparties = counterparties.AsyncCounterpartiesWithStreamingResponse(client.counterparties)
        self.events = events.AsyncEventsWithStreamingResponse(client.events)
        self.expected_payments = expected_payments.AsyncExpectedPaymentsWithStreamingResponse(client.expected_payments)
        self.external_accounts = external_accounts.AsyncExternalAccountsWithStreamingResponse(client.external_accounts)
        self.incoming_payment_details = incoming_payment_details.AsyncIncomingPaymentDetailsWithStreamingResponse(
            client.incoming_payment_details
        )
        self.invoices = invoices.AsyncInvoicesWithStreamingResponse(client.invoices)
        self.documents = documents.AsyncDocumentsWithStreamingResponse(client.documents)
        self.account_collection_flows = account_collection_flows.AsyncAccountCollectionFlowsWithStreamingResponse(
            client.account_collection_flows
        )
        self.account_details = account_details.AsyncAccountDetailsWithStreamingResponse(client.account_details)
        self.routing_details = routing_details.AsyncRoutingDetailsWithStreamingResponse(client.routing_details)
        self.internal_accounts = internal_accounts.AsyncInternalAccountsWithStreamingResponse(client.internal_accounts)
        self.ledgers = ledgers.AsyncLedgersWithStreamingResponse(client.ledgers)
        self.ledgerable_events = ledgerable_events.AsyncLedgerableEventsWithStreamingResponse(client.ledgerable_events)
        self.ledger_account_categories = ledger_account_categories.AsyncLedgerAccountCategoriesWithStreamingResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = ledger_accounts.AsyncLedgerAccountsWithStreamingResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = (
            ledger_account_balance_monitors.AsyncLedgerAccountBalanceMonitorsWithStreamingResponse(
                client.ledger_account_balance_monitors
            )
        )
        self.ledger_account_statements = ledger_account_statements.AsyncLedgerAccountStatementsWithStreamingResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = ledger_entries.AsyncLedgerEntriesWithStreamingResponse(client.ledger_entries)
        self.ledger_event_handlers = ledger_event_handlers.AsyncLedgerEventHandlersWithStreamingResponse(
            client.ledger_event_handlers
        )
        self.ledger_transactions = ledger_transactions.AsyncLedgerTransactionsWithStreamingResponse(
            client.ledger_transactions
        )
        self.line_items = line_items.AsyncLineItemsWithStreamingResponse(client.line_items)
        self.payment_flows = payment_flows.AsyncPaymentFlowsWithStreamingResponse(client.payment_flows)
        self.payment_orders = payment_orders.AsyncPaymentOrdersWithStreamingResponse(client.payment_orders)
        self.payment_references = payment_references.AsyncPaymentReferencesWithStreamingResponse(
            client.payment_references
        )
        self.returns = returns.AsyncReturnsWithStreamingResponse(client.returns)
        self.transactions = transactions.AsyncTransactionsWithStreamingResponse(client.transactions)
        self.validations = validations.AsyncValidationsWithStreamingResponse(client.validations)
        self.paper_items = paper_items.AsyncPaperItemsWithStreamingResponse(client.paper_items)
        self.virtual_accounts = virtual_accounts.AsyncVirtualAccountsWithStreamingResponse(client.virtual_accounts)
        self.bulk_requests = bulk_requests.AsyncBulkRequestsWithStreamingResponse(client.bulk_requests)
        self.bulk_results = bulk_results.AsyncBulkResultsWithStreamingResponse(client.bulk_results)
        self.ledger_account_settlements = ledger_account_settlements.AsyncLedgerAccountSettlementsWithStreamingResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = foreign_exchange_quotes.AsyncForeignExchangeQuotesWithStreamingResponse(
            client.foreign_exchange_quotes
        )
        self.connection_legal_entities = connection_legal_entities.AsyncConnectionLegalEntitiesWithStreamingResponse(
            client.connection_legal_entities
        )
        self.legal_entities = legal_entities.AsyncLegalEntitiesWithStreamingResponse(client.legal_entities)
        self.legal_entity_associations = legal_entity_associations.AsyncLegalEntityAssociationsWithStreamingResponse(
            client.legal_entity_associations
        )

        self.ping = async_to_streamed_response_wrapper(
            client.ping,
        )


Client = ModernTreasury

AsyncClient = AsyncModernTreasury
