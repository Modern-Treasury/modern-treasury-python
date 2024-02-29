# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions, _legacy_response
from ._qs import Querystring
from .types import PingResponse
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
    AsyncTransport,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ModernTreasuryError
from ._base_client import (
    DEFAULT_LIMITS,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    SyncHttpxClientWrapper,
    AsyncHttpxClientWrapper,
    make_request_options,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "ModernTreasury",
    "AsyncModernTreasury",
    "Client",
    "AsyncClient",
]


class ModernTreasury(SyncAPIClient):
    connections: resources.Connections
    counterparties: resources.Counterparties
    events: resources.Events
    expected_payments: resources.ExpectedPayments
    external_accounts: resources.ExternalAccounts
    incoming_payment_details: resources.IncomingPaymentDetails
    invoices: resources.Invoices
    documents: resources.Documents
    account_collection_flows: resources.AccountCollectionFlows
    account_details: resources.AccountDetails
    routing_details: resources.RoutingDetails
    internal_accounts: resources.InternalAccounts
    ledgers: resources.Ledgers
    ledgerable_events: resources.LedgerableEvents
    ledger_account_categories: resources.LedgerAccountCategories
    ledger_accounts: resources.LedgerAccounts
    ledger_account_balance_monitors: resources.LedgerAccountBalanceMonitors
    ledger_account_payouts: resources.LedgerAccountPayouts
    ledger_account_statements: resources.LedgerAccountStatements
    ledger_entries: resources.LedgerEntries
    ledger_event_handlers: resources.LedgerEventHandlers
    ledger_transactions: resources.LedgerTransactions
    line_items: resources.LineItems
    payment_flows: resources.PaymentFlows
    payment_orders: resources.PaymentOrders
    payment_references: resources.PaymentReferences
    returns: resources.Returns
    transactions: resources.Transactions
    validations: resources.Validations
    paper_items: resources.PaperItems
    webhooks: resources.Webhooks
    virtual_accounts: resources.VirtualAccounts
    bulk_requests: resources.BulkRequests
    bulk_results: resources.BulkResults
    ledger_account_settlements: resources.LedgerAccountSettlements
    foreign_exchange_quotes: resources.ForeignExchangeQuotes
    connection_legal_entities: resources.ConnectionLegalEntities
    legal_entities: resources.LegalEntities
    legal_entity_associations: resources.LegalEntityAssociations
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
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Transport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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
        """Construct a new synchronous Modern Treasury client instance.

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
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.connections = resources.Connections(self)
        self.counterparties = resources.Counterparties(self)
        self.events = resources.Events(self)
        self.expected_payments = resources.ExpectedPayments(self)
        self.external_accounts = resources.ExternalAccounts(self)
        self.incoming_payment_details = resources.IncomingPaymentDetails(self)
        self.invoices = resources.Invoices(self)
        self.documents = resources.Documents(self)
        self.account_collection_flows = resources.AccountCollectionFlows(self)
        self.account_details = resources.AccountDetails(self)
        self.routing_details = resources.RoutingDetails(self)
        self.internal_accounts = resources.InternalAccounts(self)
        self.ledgers = resources.Ledgers(self)
        self.ledgerable_events = resources.LedgerableEvents(self)
        self.ledger_account_categories = resources.LedgerAccountCategories(self)
        self.ledger_accounts = resources.LedgerAccounts(self)
        self.ledger_account_balance_monitors = resources.LedgerAccountBalanceMonitors(self)
        self.ledger_account_payouts = resources.LedgerAccountPayouts(self)
        self.ledger_account_statements = resources.LedgerAccountStatements(self)
        self.ledger_entries = resources.LedgerEntries(self)
        self.ledger_event_handlers = resources.LedgerEventHandlers(self)
        self.ledger_transactions = resources.LedgerTransactions(self)
        self.line_items = resources.LineItems(self)
        self.payment_flows = resources.PaymentFlows(self)
        self.payment_orders = resources.PaymentOrders(self)
        self.payment_references = resources.PaymentReferences(self)
        self.returns = resources.Returns(self)
        self.transactions = resources.Transactions(self)
        self.validations = resources.Validations(self)
        self.paper_items = resources.PaperItems(self)
        self.webhooks = resources.Webhooks(self)
        self.virtual_accounts = resources.VirtualAccounts(self)
        self.bulk_requests = resources.BulkRequests(self)
        self.bulk_results = resources.BulkResults(self)
        self.ledger_account_settlements = resources.LedgerAccountSettlements(self)
        self.foreign_exchange_quotes = resources.ForeignExchangeQuotes(self)
        self.connection_legal_entities = resources.ConnectionLegalEntities(self)
        self.legal_entities = resources.LegalEntities(self)
        self.legal_entity_associations = resources.LegalEntityAssociations(self)
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
        connection_pool_limits: httpx.Limits | None = None,
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if not isinstance(self._client, SyncHttpxClientWrapper):
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            api_key=api_key or self.api_key,
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
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
    connections: resources.AsyncConnections
    counterparties: resources.AsyncCounterparties
    events: resources.AsyncEvents
    expected_payments: resources.AsyncExpectedPayments
    external_accounts: resources.AsyncExternalAccounts
    incoming_payment_details: resources.AsyncIncomingPaymentDetails
    invoices: resources.AsyncInvoices
    documents: resources.AsyncDocuments
    account_collection_flows: resources.AsyncAccountCollectionFlows
    account_details: resources.AsyncAccountDetails
    routing_details: resources.AsyncRoutingDetails
    internal_accounts: resources.AsyncInternalAccounts
    ledgers: resources.AsyncLedgers
    ledgerable_events: resources.AsyncLedgerableEvents
    ledger_account_categories: resources.AsyncLedgerAccountCategories
    ledger_accounts: resources.AsyncLedgerAccounts
    ledger_account_balance_monitors: resources.AsyncLedgerAccountBalanceMonitors
    ledger_account_payouts: resources.AsyncLedgerAccountPayouts
    ledger_account_statements: resources.AsyncLedgerAccountStatements
    ledger_entries: resources.AsyncLedgerEntries
    ledger_event_handlers: resources.AsyncLedgerEventHandlers
    ledger_transactions: resources.AsyncLedgerTransactions
    line_items: resources.AsyncLineItems
    payment_flows: resources.AsyncPaymentFlows
    payment_orders: resources.AsyncPaymentOrders
    payment_references: resources.AsyncPaymentReferences
    returns: resources.AsyncReturns
    transactions: resources.AsyncTransactions
    validations: resources.AsyncValidations
    paper_items: resources.AsyncPaperItems
    webhooks: resources.AsyncWebhooks
    virtual_accounts: resources.AsyncVirtualAccounts
    bulk_requests: resources.AsyncBulkRequests
    bulk_results: resources.AsyncBulkResults
    ledger_account_settlements: resources.AsyncLedgerAccountSettlements
    foreign_exchange_quotes: resources.AsyncForeignExchangeQuotes
    connection_legal_entities: resources.AsyncConnectionLegalEntities
    legal_entities: resources.AsyncLegalEntities
    legal_entity_associations: resources.AsyncLegalEntityAssociations
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
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: AsyncTransport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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
        """Construct a new async Modern Treasury client instance.

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
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.connections = resources.AsyncConnections(self)
        self.counterparties = resources.AsyncCounterparties(self)
        self.events = resources.AsyncEvents(self)
        self.expected_payments = resources.AsyncExpectedPayments(self)
        self.external_accounts = resources.AsyncExternalAccounts(self)
        self.incoming_payment_details = resources.AsyncIncomingPaymentDetails(self)
        self.invoices = resources.AsyncInvoices(self)
        self.documents = resources.AsyncDocuments(self)
        self.account_collection_flows = resources.AsyncAccountCollectionFlows(self)
        self.account_details = resources.AsyncAccountDetails(self)
        self.routing_details = resources.AsyncRoutingDetails(self)
        self.internal_accounts = resources.AsyncInternalAccounts(self)
        self.ledgers = resources.AsyncLedgers(self)
        self.ledgerable_events = resources.AsyncLedgerableEvents(self)
        self.ledger_account_categories = resources.AsyncLedgerAccountCategories(self)
        self.ledger_accounts = resources.AsyncLedgerAccounts(self)
        self.ledger_account_balance_monitors = resources.AsyncLedgerAccountBalanceMonitors(self)
        self.ledger_account_payouts = resources.AsyncLedgerAccountPayouts(self)
        self.ledger_account_statements = resources.AsyncLedgerAccountStatements(self)
        self.ledger_entries = resources.AsyncLedgerEntries(self)
        self.ledger_event_handlers = resources.AsyncLedgerEventHandlers(self)
        self.ledger_transactions = resources.AsyncLedgerTransactions(self)
        self.line_items = resources.AsyncLineItems(self)
        self.payment_flows = resources.AsyncPaymentFlows(self)
        self.payment_orders = resources.AsyncPaymentOrders(self)
        self.payment_references = resources.AsyncPaymentReferences(self)
        self.returns = resources.AsyncReturns(self)
        self.transactions = resources.AsyncTransactions(self)
        self.validations = resources.AsyncValidations(self)
        self.paper_items = resources.AsyncPaperItems(self)
        self.webhooks = resources.AsyncWebhooks(self)
        self.virtual_accounts = resources.AsyncVirtualAccounts(self)
        self.bulk_requests = resources.AsyncBulkRequests(self)
        self.bulk_results = resources.AsyncBulkResults(self)
        self.ledger_account_settlements = resources.AsyncLedgerAccountSettlements(self)
        self.foreign_exchange_quotes = resources.AsyncForeignExchangeQuotes(self)
        self.connection_legal_entities = resources.AsyncConnectionLegalEntities(self)
        self.legal_entities = resources.AsyncLegalEntities(self)
        self.legal_entity_associations = resources.AsyncLegalEntityAssociations(self)
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
        connection_pool_limits: httpx.Limits | None = None,
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if not isinstance(self._client, AsyncHttpxClientWrapper):
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            api_key=api_key or self.api_key,
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
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
        self.connections = resources.ConnectionsWithRawResponse(client.connections)
        self.counterparties = resources.CounterpartiesWithRawResponse(client.counterparties)
        self.events = resources.EventsWithRawResponse(client.events)
        self.expected_payments = resources.ExpectedPaymentsWithRawResponse(client.expected_payments)
        self.external_accounts = resources.ExternalAccountsWithRawResponse(client.external_accounts)
        self.incoming_payment_details = resources.IncomingPaymentDetailsWithRawResponse(client.incoming_payment_details)
        self.invoices = resources.InvoicesWithRawResponse(client.invoices)
        self.documents = resources.DocumentsWithRawResponse(client.documents)
        self.account_collection_flows = resources.AccountCollectionFlowsWithRawResponse(client.account_collection_flows)
        self.account_details = resources.AccountDetailsWithRawResponse(client.account_details)
        self.routing_details = resources.RoutingDetailsWithRawResponse(client.routing_details)
        self.internal_accounts = resources.InternalAccountsWithRawResponse(client.internal_accounts)
        self.ledgers = resources.LedgersWithRawResponse(client.ledgers)
        self.ledgerable_events = resources.LedgerableEventsWithRawResponse(client.ledgerable_events)
        self.ledger_account_categories = resources.LedgerAccountCategoriesWithRawResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = resources.LedgerAccountsWithRawResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = resources.LedgerAccountBalanceMonitorsWithRawResponse(
            client.ledger_account_balance_monitors
        )
        self.ledger_account_payouts = resources.LedgerAccountPayoutsWithRawResponse(client.ledger_account_payouts)
        self.ledger_account_statements = resources.LedgerAccountStatementsWithRawResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = resources.LedgerEntriesWithRawResponse(client.ledger_entries)
        self.ledger_event_handlers = resources.LedgerEventHandlersWithRawResponse(client.ledger_event_handlers)
        self.ledger_transactions = resources.LedgerTransactionsWithRawResponse(client.ledger_transactions)
        self.line_items = resources.LineItemsWithRawResponse(client.line_items)
        self.payment_flows = resources.PaymentFlowsWithRawResponse(client.payment_flows)
        self.payment_orders = resources.PaymentOrdersWithRawResponse(client.payment_orders)
        self.payment_references = resources.PaymentReferencesWithRawResponse(client.payment_references)
        self.returns = resources.ReturnsWithRawResponse(client.returns)
        self.transactions = resources.TransactionsWithRawResponse(client.transactions)
        self.validations = resources.ValidationsWithRawResponse(client.validations)
        self.paper_items = resources.PaperItemsWithRawResponse(client.paper_items)
        self.virtual_accounts = resources.VirtualAccountsWithRawResponse(client.virtual_accounts)
        self.bulk_requests = resources.BulkRequestsWithRawResponse(client.bulk_requests)
        self.bulk_results = resources.BulkResultsWithRawResponse(client.bulk_results)
        self.ledger_account_settlements = resources.LedgerAccountSettlementsWithRawResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = resources.ForeignExchangeQuotesWithRawResponse(client.foreign_exchange_quotes)
        self.connection_legal_entities = resources.ConnectionLegalEntitiesWithRawResponse(
            client.connection_legal_entities
        )
        self.legal_entities = resources.LegalEntitiesWithRawResponse(client.legal_entities)
        self.legal_entity_associations = resources.LegalEntityAssociationsWithRawResponse(
            client.legal_entity_associations
        )

        self.ping = _legacy_response.to_raw_response_wrapper(
            client.ping,
        )


class AsyncModernTreasuryWithRawResponse:
    def __init__(self, client: AsyncModernTreasury) -> None:
        self.connections = resources.AsyncConnectionsWithRawResponse(client.connections)
        self.counterparties = resources.AsyncCounterpartiesWithRawResponse(client.counterparties)
        self.events = resources.AsyncEventsWithRawResponse(client.events)
        self.expected_payments = resources.AsyncExpectedPaymentsWithRawResponse(client.expected_payments)
        self.external_accounts = resources.AsyncExternalAccountsWithRawResponse(client.external_accounts)
        self.incoming_payment_details = resources.AsyncIncomingPaymentDetailsWithRawResponse(
            client.incoming_payment_details
        )
        self.invoices = resources.AsyncInvoicesWithRawResponse(client.invoices)
        self.documents = resources.AsyncDocumentsWithRawResponse(client.documents)
        self.account_collection_flows = resources.AsyncAccountCollectionFlowsWithRawResponse(
            client.account_collection_flows
        )
        self.account_details = resources.AsyncAccountDetailsWithRawResponse(client.account_details)
        self.routing_details = resources.AsyncRoutingDetailsWithRawResponse(client.routing_details)
        self.internal_accounts = resources.AsyncInternalAccountsWithRawResponse(client.internal_accounts)
        self.ledgers = resources.AsyncLedgersWithRawResponse(client.ledgers)
        self.ledgerable_events = resources.AsyncLedgerableEventsWithRawResponse(client.ledgerable_events)
        self.ledger_account_categories = resources.AsyncLedgerAccountCategoriesWithRawResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = resources.AsyncLedgerAccountsWithRawResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = resources.AsyncLedgerAccountBalanceMonitorsWithRawResponse(
            client.ledger_account_balance_monitors
        )
        self.ledger_account_payouts = resources.AsyncLedgerAccountPayoutsWithRawResponse(client.ledger_account_payouts)
        self.ledger_account_statements = resources.AsyncLedgerAccountStatementsWithRawResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = resources.AsyncLedgerEntriesWithRawResponse(client.ledger_entries)
        self.ledger_event_handlers = resources.AsyncLedgerEventHandlersWithRawResponse(client.ledger_event_handlers)
        self.ledger_transactions = resources.AsyncLedgerTransactionsWithRawResponse(client.ledger_transactions)
        self.line_items = resources.AsyncLineItemsWithRawResponse(client.line_items)
        self.payment_flows = resources.AsyncPaymentFlowsWithRawResponse(client.payment_flows)
        self.payment_orders = resources.AsyncPaymentOrdersWithRawResponse(client.payment_orders)
        self.payment_references = resources.AsyncPaymentReferencesWithRawResponse(client.payment_references)
        self.returns = resources.AsyncReturnsWithRawResponse(client.returns)
        self.transactions = resources.AsyncTransactionsWithRawResponse(client.transactions)
        self.validations = resources.AsyncValidationsWithRawResponse(client.validations)
        self.paper_items = resources.AsyncPaperItemsWithRawResponse(client.paper_items)
        self.virtual_accounts = resources.AsyncVirtualAccountsWithRawResponse(client.virtual_accounts)
        self.bulk_requests = resources.AsyncBulkRequestsWithRawResponse(client.bulk_requests)
        self.bulk_results = resources.AsyncBulkResultsWithRawResponse(client.bulk_results)
        self.ledger_account_settlements = resources.AsyncLedgerAccountSettlementsWithRawResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = resources.AsyncForeignExchangeQuotesWithRawResponse(
            client.foreign_exchange_quotes
        )
        self.connection_legal_entities = resources.AsyncConnectionLegalEntitiesWithRawResponse(
            client.connection_legal_entities
        )
        self.legal_entities = resources.AsyncLegalEntitiesWithRawResponse(client.legal_entities)
        self.legal_entity_associations = resources.AsyncLegalEntityAssociationsWithRawResponse(
            client.legal_entity_associations
        )

        self.ping = _legacy_response.async_to_raw_response_wrapper(
            client.ping,
        )


class ModernTreasuryWithStreamedResponse:
    def __init__(self, client: ModernTreasury) -> None:
        self.connections = resources.ConnectionsWithStreamingResponse(client.connections)
        self.counterparties = resources.CounterpartiesWithStreamingResponse(client.counterparties)
        self.events = resources.EventsWithStreamingResponse(client.events)
        self.expected_payments = resources.ExpectedPaymentsWithStreamingResponse(client.expected_payments)
        self.external_accounts = resources.ExternalAccountsWithStreamingResponse(client.external_accounts)
        self.incoming_payment_details = resources.IncomingPaymentDetailsWithStreamingResponse(
            client.incoming_payment_details
        )
        self.invoices = resources.InvoicesWithStreamingResponse(client.invoices)
        self.documents = resources.DocumentsWithStreamingResponse(client.documents)
        self.account_collection_flows = resources.AccountCollectionFlowsWithStreamingResponse(
            client.account_collection_flows
        )
        self.account_details = resources.AccountDetailsWithStreamingResponse(client.account_details)
        self.routing_details = resources.RoutingDetailsWithStreamingResponse(client.routing_details)
        self.internal_accounts = resources.InternalAccountsWithStreamingResponse(client.internal_accounts)
        self.ledgers = resources.LedgersWithStreamingResponse(client.ledgers)
        self.ledgerable_events = resources.LedgerableEventsWithStreamingResponse(client.ledgerable_events)
        self.ledger_account_categories = resources.LedgerAccountCategoriesWithStreamingResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = resources.LedgerAccountsWithStreamingResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = resources.LedgerAccountBalanceMonitorsWithStreamingResponse(
            client.ledger_account_balance_monitors
        )
        self.ledger_account_payouts = resources.LedgerAccountPayoutsWithStreamingResponse(client.ledger_account_payouts)
        self.ledger_account_statements = resources.LedgerAccountStatementsWithStreamingResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = resources.LedgerEntriesWithStreamingResponse(client.ledger_entries)
        self.ledger_event_handlers = resources.LedgerEventHandlersWithStreamingResponse(client.ledger_event_handlers)
        self.ledger_transactions = resources.LedgerTransactionsWithStreamingResponse(client.ledger_transactions)
        self.line_items = resources.LineItemsWithStreamingResponse(client.line_items)
        self.payment_flows = resources.PaymentFlowsWithStreamingResponse(client.payment_flows)
        self.payment_orders = resources.PaymentOrdersWithStreamingResponse(client.payment_orders)
        self.payment_references = resources.PaymentReferencesWithStreamingResponse(client.payment_references)
        self.returns = resources.ReturnsWithStreamingResponse(client.returns)
        self.transactions = resources.TransactionsWithStreamingResponse(client.transactions)
        self.validations = resources.ValidationsWithStreamingResponse(client.validations)
        self.paper_items = resources.PaperItemsWithStreamingResponse(client.paper_items)
        self.virtual_accounts = resources.VirtualAccountsWithStreamingResponse(client.virtual_accounts)
        self.bulk_requests = resources.BulkRequestsWithStreamingResponse(client.bulk_requests)
        self.bulk_results = resources.BulkResultsWithStreamingResponse(client.bulk_results)
        self.ledger_account_settlements = resources.LedgerAccountSettlementsWithStreamingResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = resources.ForeignExchangeQuotesWithStreamingResponse(
            client.foreign_exchange_quotes
        )
        self.connection_legal_entities = resources.ConnectionLegalEntitiesWithStreamingResponse(
            client.connection_legal_entities
        )
        self.legal_entities = resources.LegalEntitiesWithStreamingResponse(client.legal_entities)
        self.legal_entity_associations = resources.LegalEntityAssociationsWithStreamingResponse(
            client.legal_entity_associations
        )

        self.ping = to_streamed_response_wrapper(
            client.ping,
        )


class AsyncModernTreasuryWithStreamedResponse:
    def __init__(self, client: AsyncModernTreasury) -> None:
        self.connections = resources.AsyncConnectionsWithStreamingResponse(client.connections)
        self.counterparties = resources.AsyncCounterpartiesWithStreamingResponse(client.counterparties)
        self.events = resources.AsyncEventsWithStreamingResponse(client.events)
        self.expected_payments = resources.AsyncExpectedPaymentsWithStreamingResponse(client.expected_payments)
        self.external_accounts = resources.AsyncExternalAccountsWithStreamingResponse(client.external_accounts)
        self.incoming_payment_details = resources.AsyncIncomingPaymentDetailsWithStreamingResponse(
            client.incoming_payment_details
        )
        self.invoices = resources.AsyncInvoicesWithStreamingResponse(client.invoices)
        self.documents = resources.AsyncDocumentsWithStreamingResponse(client.documents)
        self.account_collection_flows = resources.AsyncAccountCollectionFlowsWithStreamingResponse(
            client.account_collection_flows
        )
        self.account_details = resources.AsyncAccountDetailsWithStreamingResponse(client.account_details)
        self.routing_details = resources.AsyncRoutingDetailsWithStreamingResponse(client.routing_details)
        self.internal_accounts = resources.AsyncInternalAccountsWithStreamingResponse(client.internal_accounts)
        self.ledgers = resources.AsyncLedgersWithStreamingResponse(client.ledgers)
        self.ledgerable_events = resources.AsyncLedgerableEventsWithStreamingResponse(client.ledgerable_events)
        self.ledger_account_categories = resources.AsyncLedgerAccountCategoriesWithStreamingResponse(
            client.ledger_account_categories
        )
        self.ledger_accounts = resources.AsyncLedgerAccountsWithStreamingResponse(client.ledger_accounts)
        self.ledger_account_balance_monitors = resources.AsyncLedgerAccountBalanceMonitorsWithStreamingResponse(
            client.ledger_account_balance_monitors
        )
        self.ledger_account_payouts = resources.AsyncLedgerAccountPayoutsWithStreamingResponse(
            client.ledger_account_payouts
        )
        self.ledger_account_statements = resources.AsyncLedgerAccountStatementsWithStreamingResponse(
            client.ledger_account_statements
        )
        self.ledger_entries = resources.AsyncLedgerEntriesWithStreamingResponse(client.ledger_entries)
        self.ledger_event_handlers = resources.AsyncLedgerEventHandlersWithStreamingResponse(
            client.ledger_event_handlers
        )
        self.ledger_transactions = resources.AsyncLedgerTransactionsWithStreamingResponse(client.ledger_transactions)
        self.line_items = resources.AsyncLineItemsWithStreamingResponse(client.line_items)
        self.payment_flows = resources.AsyncPaymentFlowsWithStreamingResponse(client.payment_flows)
        self.payment_orders = resources.AsyncPaymentOrdersWithStreamingResponse(client.payment_orders)
        self.payment_references = resources.AsyncPaymentReferencesWithStreamingResponse(client.payment_references)
        self.returns = resources.AsyncReturnsWithStreamingResponse(client.returns)
        self.transactions = resources.AsyncTransactionsWithStreamingResponse(client.transactions)
        self.validations = resources.AsyncValidationsWithStreamingResponse(client.validations)
        self.paper_items = resources.AsyncPaperItemsWithStreamingResponse(client.paper_items)
        self.virtual_accounts = resources.AsyncVirtualAccountsWithStreamingResponse(client.virtual_accounts)
        self.bulk_requests = resources.AsyncBulkRequestsWithStreamingResponse(client.bulk_requests)
        self.bulk_results = resources.AsyncBulkResultsWithStreamingResponse(client.bulk_results)
        self.ledger_account_settlements = resources.AsyncLedgerAccountSettlementsWithStreamingResponse(
            client.ledger_account_settlements
        )
        self.foreign_exchange_quotes = resources.AsyncForeignExchangeQuotesWithStreamingResponse(
            client.foreign_exchange_quotes
        )
        self.connection_legal_entities = resources.AsyncConnectionLegalEntitiesWithStreamingResponse(
            client.connection_legal_entities
        )
        self.legal_entities = resources.AsyncLegalEntitiesWithStreamingResponse(client.legal_entities)
        self.legal_entity_associations = resources.AsyncLegalEntityAssociationsWithStreamingResponse(
            client.legal_entity_associations
        )

        self.ping = async_to_streamed_response_wrapper(
            client.ping,
        )


Client = ModernTreasury

AsyncClient = AsyncModernTreasury
