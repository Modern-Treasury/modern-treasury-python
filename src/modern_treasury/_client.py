# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import base64
import asyncio
from typing import Union, Mapping, Optional

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from .types import PingResponse
from ._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ModernTreasuryError
from ._base_client import (
    DEFAULT_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
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

    # client options
    api_key: str
    organization_id: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
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
        api_key = api_key or os.environ.get("MODERN_TREASURY_API_KEY", None)
        if not api_key:
            raise ModernTreasuryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MODERN_TREASURY_API_KEY environment variable"
            )
        self.api_key = api_key

        organization_id_envvar = os.environ.get("MODERN_TREASURY_ORGANIZATION_ID", None)
        organization_id = organization_id or organization_id_envvar or None
        if organization_id is None:
            raise ValueError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )
        self.organization_id = organization_id

        webhook_key_envvar = os.environ.get("MODERN_TREASURY_WEBHOOK_KEY", None)
        self.webhook_key = webhook_key or webhook_key_envvar or None

        if base_url is None:
            base_url = f"https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
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

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    def copy(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> ModernTreasury:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
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

        # TODO: share the same httpx client between instances
        return self.__class__(
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or str(self.base_url),
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        self.close()

    def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

    # client options
    api_key: str
    organization_id: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
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
        api_key = api_key or os.environ.get("MODERN_TREASURY_API_KEY", None)
        if not api_key:
            raise ModernTreasuryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MODERN_TREASURY_API_KEY environment variable"
            )
        self.api_key = api_key

        organization_id_envvar = os.environ.get("MODERN_TREASURY_ORGANIZATION_ID", None)
        organization_id = organization_id or organization_id_envvar or None
        if organization_id is None:
            raise ValueError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )
        self.organization_id = organization_id

        webhook_key_envvar = os.environ.get("MODERN_TREASURY_WEBHOOK_KEY", None)
        self.webhook_key = webhook_key or webhook_key_envvar or None

        if base_url is None:
            base_url = f"https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
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

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    def copy(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> AsyncModernTreasury:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
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

        # TODO: share the same httpx client between instances
        return self.__class__(
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or str(self.base_url),
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        try:
            asyncio.get_running_loop().create_task(self.close())
        except Exception:
            pass

    async def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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


Client = ModernTreasury

AsyncClient = AsyncModernTreasury
